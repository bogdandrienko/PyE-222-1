class Events:
    @staticmethod
    def get_events_monitoring_drainage() -> str:
        return """
SELECT MAX(TIME)                                                                              maxtime,
       MIN(TIME)                                                                              mintime,
       MAX(FUEL2_VALUE)                                                                       maxfuel,
       MIN(FUEL2_VALUE)                                                                       minfuel,
       MAX(FUEL2_VALUE) - MIN(FUEL2_VALUE)                                                    diffuel,
       ROUND(( MAX(FUEL2_VALUE) - MIN(FUEL2_VALUE) ) / ( ( MAX(TIME) - MIN(TIME) ) * 24 ), 3) difval
FROM   kgp.UMPMESINEXECUTE_GALILEO 
WHERE  CONTROL_ID = 507 
       AND FUEL2_VALUE NOT IN( 65535, 0, 14807 ) 
       AND ( TIME BETWEEN SYSDATE - ( 1 / 24 / 60 * :param_time_diff ) AND SYSDATE ) 
ORDER  BY TIME DESC 
"""

    @staticmethod
    def get_events_monitoring_dumptrucks() -> str:
        return """
SELECT VEHID,
       TIME,
       X,
       Y,
       WEIGHT,
       FUEL,
       SPEED
FROM   EVENTSTATEARCHIVE
WHERE  MESCOUNTER IN (SELECT MAX(MESCOUNTER)
                      FROM   EVENTSTATEARCHIVE
                      WHERE  TIME BETWEEN ( SYSDATE - ( 1 / 24 / 60 * 500 ) ) AND SYSDATE
                      GROUP  BY VEHID)
ORDER  BY VEHID
"""


class Speed:
    @staticmethod
    def get_speed_monitoring_dumptrucks_for_now():
        return """
WITH prms 
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE)) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE))   SDATETO
         FROM   DUAL) 
SELECT q.VEHID, 
       TRIM(d.FAMNAME) 
       || ' ' 
       || TRIM(d.FIRSTNAME) 
       || ' ' 
       || TRIM(d.SECNAME)                                     fio, 
       q.SHOVID, 
       ROUND(NVL(q.AVSPEED, -1), 2)                           avgloadspeed, 
       ROUND(NVL(q.AVSPEED_EMPTY, -1), 2)                     avgemptyspeed, 
       ROUND(NVL(( q.AVSPEED + q.AVSPEED_EMPTY ) / 2, -1), 2) avspeed, 
       ROUND(q.WEIGHT, 2)                                     WEIGHT, 
       ROUND(q.LENGTH, 2)                                     LENGTH_FULL, 
       ROUND(q.UNLOADLENGTH, 2)                               UNLOADLENGTH_EMPT, 
       ROUND(q.LENGTH + q.UNLOADLENGTH, 2)                    LENGTH_ALL 
FROM   (SELECT s.VEHID, 
               s.VEHCODE, 
               s.SHOVID, 
               s.WORKTYPE, 
               s.WEIGHT, 
               s.LENGTH, 
               s.UNLOADLENGTH, 
               s.TIMELOAD, 
               s.TIMELOAD_NEXT, 
               s.AVSPEED, 
               s.TASKDATE, 
               s.SHIFT, 
               TRIP, 
               SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED) AVSPEED_EMPTY
        FROM   (SELECT VEHID, 
                       VEHCODE, 
                       SHOVID, 
                       WORKTYPE, 
                       WEIGHT, 
                       LENGTH, 
                       UNLOADLENGTH, 
                       TIMELOAD, 
                       TIMEUNLOAD, 
                       NVL(LEAD(TIMELOAD) 
                             over ( 
                               PARTITION BY VEHCODE 
                               ORDER BY TIMELOAD), PRMS.SDATETO) TIMELOAD_NEXT, 
                       AVSPEED, 
                       GETCURSHIFTDATE(0, TIMELOAD)              taskdate, 
                       GETCURSHIFTNUM(0, TIMELOAD)               shift, 
                       1                                         trip 
                FROM   VEHTRIPS 
                       inner join prms 
                               ON TIMELOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                                  AND TIMEUNLOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                WHERE  SHOVID NOT LIKE '%Неопр.%' AND AVSPEED > 5 AND AVSPEED < 70
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' ) 
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) ) 
                ORDER  BY VEHID, 
                          TIMELOAD) s 
               left join SIMPLETRANSITIONS st 
                      ON st.VEHCODE = s.VEHCODE 
                         AND st.AVGSPEED > 5 AND st.AVGSPEED < 70
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT ) 
                         AND st.MOVELENGTH > 0 
        GROUP  BY s.VEHID, 
                  s.VEHCODE, 
                  s.WORKTYPE, 
                  s.WEIGHT, 
                  s.LENGTH, 
                  s.UNLOADLENGTH, 
                  s.SHOVID, 
                  s.TIMELOAD, 
                  s.TIMELOAD_NEXT, 
                  s.AVSPEED, 
                  s.TASKDATE, 
                  s.SHIFT, 
                  s.TRIP)q 
       left join SHIFTTASKS stk 
              ON stk.TASKDATE = q.TASKDATE 
                 AND stk.SHIFT = q.SHIFT 
                 AND stk.VEHID = q.VEHID 
       left join DRIVERS d 
              ON stk.TABELNUM = d.TABELNUM 
ORDER  BY TIMELOAD 
"""

    @staticmethod
    def get_speed_monitoring_dumptrucks_for_select_date():
        return """
WITH prms 
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)   SDATETO
         FROM   DUAL) 
SELECT q.VEHID, 
       TRIM(d.FAMNAME) 
       || ' ' 
       || TRIM(d.FIRSTNAME) 
       || ' ' 
       || TRIM(d.SECNAME)                                     fio, 
       q.SHOVID, 
       ROUND(NVL(q.AVSPEED, -1), 2)                           avgloadspeed, 
       ROUND(NVL(q.AVSPEED_EMPTY, -1), 2)                     avgemptyspeed, 
       ROUND(NVL(( q.AVSPEED + q.AVSPEED_EMPTY ) / 2, -1), 2) avspeed, 
       ROUND(q.WEIGHT, 2)                                     WEIGHT, 
       ROUND(q.LENGTH, 2)                                     LENGTH_FULL, 
       ROUND(q.UNLOADLENGTH, 2)                               UNLOADLENGTH_EMPT, 
       ROUND(q.LENGTH + q.UNLOADLENGTH, 2)                    LENGTH_ALL 
FROM   (SELECT s.VEHID, 
               s.VEHCODE, 
               s.SHOVID, 
               s.WORKTYPE, 
               s.WEIGHT, 
               s.LENGTH, 
               s.UNLOADLENGTH, 
               s.TIMELOAD, 
               s.TIMELOAD_NEXT, 
               s.AVSPEED, 
               s.TASKDATE, 
               s.SHIFT, 
               TRIP, 
               SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED) AVSPEED_EMPTY
        FROM   (SELECT VEHID, 
                       VEHCODE, 
                       SHOVID, 
                       WORKTYPE, 
                       WEIGHT, 
                       LENGTH, 
                       UNLOADLENGTH, 
                       TIMELOAD, 
                       TIMEUNLOAD, 
                       NVL(LEAD(TIMELOAD) 
                             over ( 
                               PARTITION BY VEHCODE 
                               ORDER BY TIMELOAD), PRMS.SDATETO) TIMELOAD_NEXT, 
                       AVSPEED, 
                       GETCURSHIFTDATE(0, TIMELOAD)              taskdate, 
                       GETCURSHIFTNUM(0, TIMELOAD)               shift, 
                       1                                         trip 
                FROM   VEHTRIPS 
                       inner join prms 
                               ON TIMELOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                                  AND TIMEUNLOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                WHERE  SHOVID NOT LIKE '%Неопр.%' 
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' ) 
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) ) 
                ORDER  BY VEHID, 
                          TIMELOAD) s 
               left join SIMPLETRANSITIONS st 
                      ON st.VEHCODE = s.VEHCODE 
                         AND st.AVGSPEED > 5 
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT ) 
                         AND st.MOVELENGTH > 0 
        GROUP  BY s.VEHID, 
                  s.VEHCODE, 
                  s.WORKTYPE, 
                  s.WEIGHT, 
                  s.LENGTH, 
                  s.UNLOADLENGTH, 
                  s.SHOVID, 
                  s.TIMELOAD, 
                  s.TIMELOAD_NEXT, 
                  s.AVSPEED, 
                  s.TASKDATE, 
                  s.SHIFT, 
                  s.TRIP)q 
       left join SHIFTTASKS stk 
              ON stk.TASKDATE = q.TASKDATE 
                 AND stk.SHIFT = q.SHIFT 
                 AND stk.VEHID = q.VEHID 
       left join DRIVERS d 
              ON stk.TABELNUM = d.TABELNUM 
ORDER  BY TIMELOAD 
"""

    @staticmethod
    def get_speed_monitoring_dumptrucks_comments():
        return """
SELECT description, author from dumptrucks_speed_report where veh_id = :veh_id and
taskdate = :taskdate and  shift = :shift
"""

    @staticmethod
    def get_speed_monitoring_all_dumptrucks_comments():
        return """
SELECT veh_id, description, author from dumptrucks_speed_report where taskdate = :taskdate and  shift = :shift
"""

    @staticmethod
    def post_speed_send_comment_dumptrucks_get_id():
        return """
SELECT id FROM dumptrucks_speed_report 
WHERE veh_id = :veh_id and taskdate = :taskdate and shift = :shift
"""

    @staticmethod
    def post_speed_send_comment_dumptrucks_insert():
        return """
INSERT INTO dumptrucks_speed_report (veh_id, description, taskdate, shift, author, updated)
VALUES (:veh_id, :description, :taskdate, :shift, :author, :updated)
"""

    @staticmethod
    def post_speed_send_comment_dumptrucks_update():
        return """
UPDATE dumptrucks_speed_report
SET veh_id = :veh_id, description = :description, taskdate = :taskdate, shift = :shift, author = :author, updated = :updated
WHERE veh_id = :veh_id and taskdate = :taskdate and shift = :shift
"""


class Pto:
    @staticmethod
    def get_pto_monitoring_norm_trips() -> str:
        return """
SELECT tripcounter,
       vehid,
       shovid,
       unloadid,
       worktype,
       timeload,
       timeunload,
       movetime,
       weight,
       nvl(bucketcount, -1) bucketcount,
       avspeed,
       length,
       unloadlength,
       loadheight,
       unloadheight
FROM   vehtrips vt
WHERE  vt.timeunload BETWEEN getpredefinedtimefrom('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE)) AND getpredefinedtimeto('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE))
and length > :param_min_length and avspeed > 0
ORDER  BY vehid ASC, timeload ASC 
"""

    @staticmethod
    def get_pto_report_asd_errors() -> str:
        return """
SELECT *
FROM   (SELECT '4. Не начали смену на айпане после ее факт. начала' AS ErrType,
               'Самосвал '
               || e.VEHID
               || ' - '
               || TO_CHAR(TIME, 'HH24'
                                || CHR(58)
                                || 'MI'
                                || CHR(58)
                                || 'SS')                                                                  AS Description,
               VEHID                                                                                      TEHID,
               'Самосвал'                                                                         TYPETECH
        FROM   EVENTSTATEARCHIVE e
        WHERE  TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) + 1.0 / ( 24.0 * 60 ) AND GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) + 40.0 / ( 24.0 * 60 )
               AND EVENTTYPE = 11
        UNION
        SELECT '4. Не начали смену на айпане после ее факт. начала' AS ErrType,
               'Экскаватор '
               || e.SHOVID
               || ' - '
               || TO_CHAR(TIME, 'HH24'
                                || CHR(58)
                                || 'MI'
                                || CHR(58)
                                || 'SS')                                                                  AS Description,
               e.SHOVID                                                                                   TEHID,
               'Экскаватор'                                                                     TYPETECH
        FROM   SHOVEVENTSTATEARCHIVE e
        WHERE  TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) + 1.0 / ( 24.0 * 60 ) AND GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) + 40.0 / ( 24.0 * 60 )
               AND EVENTTYPE = 11
        UNION
        SELECT '5. Техника, работающая без нажатия начала/завершения смены' AS ErrType,
               'Самосвал '
               || VEHID
               || CASE
                    WHEN MESTYPE = 11 THEN ' не нажата кнопка начала'
                    ELSE ' не нажата кнопка завершения'
                  END                                                                                                       AS Description,
               VEHID                                                                                                        TEHID,
               'Самосвал'                                                                                           TYPETECH
        FROM   (SELECT SHIFTTASKS.VEHID,
                       MESTYPE
                FROM   SHIFTTASKS,
                       (SELECT 11 AS MesType
                        FROM   DUAL
                        UNION
                        SELECT 14 AS MesType
                        FROM   DUAL)
                WHERE  SHIFTTASKS.TASKDATE = :param_date
                       AND SHIFTTASKS.SHIFT = :param_shift
                MINUS
                SELECT e.VEHID,
                       EVENTTYPE
                FROM   EVENTSTATEARCHIVE e
                WHERE  TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) - 40.0 / ( 24.0 * 60 ) AND GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) + 40.0 / ( 24.0 * 60 )
                       AND EVENTTYPE IN ( 11 )
                MINUS
                SELECT e.VEHID,
                       EVENTTYPE
                FROM   EVENTSTATEARCHIVE e
                WHERE  TIME BETWEEN GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) - 40.0 / ( 24.0 * 60 ) AND GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) + 40.0 / ( 24.0 * 60 )
                       AND EVENTTYPE IN ( 14 ))
        UNION
        SELECT '5. Техника, работающая без нажатия начала/завершения смены' AS ErrType,
               'Экскаватор '
               || VEHID
               || CASE
                    WHEN MESTYPE = 11 THEN ' не нажата кнопка начала'
                    ELSE ' не нажата кнопка завершения'
                  END                                                                                                       AS Description,
               VEHID                                                                                                        TEHID,
               'Экскаватор'                                                                                       TYPETECH
        FROM   (SELECT SHOVSHIFTTASKS.SHOVID AS VehID,
                       MESTYPE
                FROM   SHOVSHIFTTASKS,
                       (SELECT 11 AS MesType
                        FROM   DUAL
                        UNION
                        SELECT 14 AS MesType
                        FROM   DUAL)
                WHERE  SHOVSHIFTTASKS.TASKDATE = :param_date
                       AND SHOVSHIFTTASKS.SHIFT = :param_shift
                MINUS
                SELECT e.SHOVID,
                       EVENTTYPE
                FROM   SHOVEVENTSTATEARCHIVE e
                WHERE  TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) - 40.0 / ( 24.0 * 60 ) AND GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) + 40.0 / ( 24.0 * 60 )
                       AND EVENTTYPE IN ( 11 )
                MINUS
                SELECT e.SHOVID,
                       EVENTTYPE
                FROM   SHOVEVENTSTATEARCHIVE e
                WHERE  TIME BETWEEN GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) - 40.0 / ( 24.0 * 60 ) AND GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) + 40.0 / ( 24.0 * 60 )
                       AND EVENTTYPE IN ( 14 )))
WHERE  ( :param_target = 'Все'
          OR :param_target = TYPETECH
          OR ( :param_target = 'Только 001 и 003'
               AND ( TEHID = '001'
                      OR TEHID = '003' ) ) ) 
"""

    @staticmethod
    def get_pto_report_sticking() -> str:
        return """
WITH b
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)   SDATETO
         FROM   DUAL)
SELECT dt.TASKDATE                  TASKDATE,
       dt.TASKSHIFT                 TASKSHIFT,
       dt.VEHID,
       NVL(selq.SUM_TRIPS, 0)       sum_trips,
       NVL(selq.AVWEIGHT_EMPTY, 0)  AVG_WEIGHT,
       NVL(selq.SUMWEIGHT_EMPTY, 0) SUM_WEIGHT,
       NVL(selq.SUM_WEIGHT_ALL, 0) SUM_WEIGHT_ALL
FROM   (SELECT TO_CHAR(:param_date, 'dd.mm.yyyy') TASKDATE,
               :param_shift                       TASKSHIFT,
               VEHID
        FROM   DUMPTRUCKS d
        WHERE  d.COLUMNNUM = 1) dt
       left join (SELECT selres.VEHID,
                         ROUND(SUM(selres.SUMWEIGHT_EMPTY), 0) SUMWEIGHT_EMPTY,
                         ROUND(AVG(selres.AVWEIGHT_EMPTY), 0)  AVWEIGHT_EMPTY,
                         SUM(selres.SUM_TRIPS)                 sum_trips,
                         SUM(selres.SUM_WEIGHT_ALL) SUM_WEIGHT_ALL
                  FROM   (SELECT res.VEHID,
                                 res.SUMWEIGHT_EMPTY,
                                 res.AVWEIGHT_EMPTY,
                                 res.SUM_TRIPS,
                                 res.SUM_WEIGHT_ALL
                          FROM   (SELECT q.VEHID,
                                         SUM(WEIGHT) SUM_WEIGHT_ALL,
                                         SUM(q.AVWEIGHT_EMPTY) SUMWEIGHT_EMPTY,
                                         AVG(q.AVWEIGHT_EMPTY) AVWEIGHT_EMPTY,
                                         SUM(TRIP)             sum_trips
                                  FROM   (SELECT s.*,
                                                 ROUND(( s.TIMELOAD_NEXT - s.TIMEUNLOAD ) * 24, 2)                    DIFF,
                                                 ROUND((SELECT AVG(WEIGHT)
                                                        FROM   dispatcher.EVENTSTATEARCHIVE
                                                        WHERE  VEHID = s.VEHID AND SPEED > :param_min_speed
                                                               AND WEIGHT between :param_min_weight and :param_max_weight                                                                
                                                               AND TIME BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT), 0) AVWEIGHT_EMPTY,
                                                 1                                                                    trip
                                          FROM   (SELECT VEHID,
                                                         SHOVID,
                                                         TIMELOAD,
                                                         TIMEUNLOAD,
                                                         NVL(LEAD(TIMELOAD)
                                                               over (
                                                                 PARTITION BY VEHID
                                                                 ORDER BY TIMELOAD), B.SDATETO) TIMELOAD_NEXT,
                                                         WEIGHT
                                                  FROM   VEHTRIPS
                                                         inner join b
                                                                 ON TIMELOAD BETWEEN B.SDATEFROM AND B.SDATETO
                                                                    AND TIMEUNLOAD BETWEEN B.SDATEFROM AND B.SDATETO
                                                  WHERE  EXTRACT(year FROM SYSDATE) >= EXTRACT(year FROM TIMELOAD)
                                                         AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' )
                                                               AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' )
                                                               AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' )
                                                               AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' )
                                                               AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' )
                                                               AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' )
                                                               AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                                                               AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' )
                                                               AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) )
                                                  ORDER  BY LENGTH(VEHID),
                                                            VEHID,
                                                            TIMELOAD) s) q
                                  GROUP  BY q.VEHID)res)selres
                  GROUP  BY selres.VEHID)selq
              ON selq.VEHID = dt.VEHID
ORDER  BY dt.VEHID 
"""

    @staticmethod
    def get_pto_monitoring_oper_stoppages() -> str:
        return """
WITH b 
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE)) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE))   SDATETO
         FROM   DUAL) 
SELECT STOPCOUNTER                               AS ID, 
       VEHID                                     AS VehID, 
       TIMESTOP, 
       NVL(TIMEGO, SYSDATE)                      AS TimeGo, 
       ROUND(( NVL(TIMEGO, SYSDATE) - TIMESTOP ) * 24 * 60, 1) AS TimeDiff, 
       NVL(IDLESTOPTYPE, -1)                     AS TypeID, 
       NVL(NOTE, ' ')                                      AS Description, 
       PLANNED 
FROM   IDLESTOPPAGES 
       inner join b 
               ON 1 = 1 
WHERE  TIMESTOP BETWEEN B.SDATEFROM AND B.SDATETO 
       AND NVL(TIMEGO, SYSDATE) BETWEEN B.SDATEFROM AND B.SDATETO 
       AND ( NVL(IDLESTOPTYPE, -1) IN ( '-1', '68' ) ) 
       AND ( ( NVL(TIMEGO, SYSDATE) - TIMESTOP ) >= 1 / 24 / 60 ) 
ORDER  BY TIMESTOP DESC 
"""

    @staticmethod
    def get_pto_report_time_wait_to_load() -> str:
        return """
SELECT d.VEHID                                       tech_key,
       psc.POLY_STOP_CAT_NAME                        category,
       s.TIMESTOP                                    TIMESTOP,
       s.TIMEGO                                      TIMEGO,
       ROUND(( s.TIMEGO - s.TIMESTOP ) * 24 * 60, 1) TIME_minutes
FROM   dispatcher.SHIFTSTOPPAGES s
       inner join dispatcher.DUMPTRUCKS d
               ON d.VEHID = s.VEHID
                  AND d.COLUMNNUM = 1
       inner join dispatcher.POLY_USER_STOPPAGES_DUMP ps
               ON ps.POLY_STOP_BINDINGS_ID = 86
                  AND ( ps.CODE = s.IDLESTOPTYPE
                        AND ps.POLY_STOP_CAT_ID IS NOT NULL )
       inner join dispatcher.POLY_STOP_CATEGORIES psc
               ON psc.POLY_STOP_CAT_ID = ps.POLY_STOP_CAT_ID
WHERE  s.SHIFTDATE = :param_date
       AND s.SHIFTNUM = :param_shift
       AND ROUND(( s.TIMEGO - s.TIMESTOP ) * 24 * 60, 1) >= :param_target
       AND NVL(s.IDLESTOPTYPE, 0) NOT IN( 0, 1, 67 )
       AND psc.POLY_STOP_CAT_NAME = 'Ожидание погрузки/самосвала'
ORDER  BY TIMESTOP,
          TIMEGO
"""

    @staticmethod
    def get_pto_report_time_wait_to_load_avg() -> str:
        return """
WITH queryq1
     AS (SELECT SUM_IDLES_MINUTE,
                TRIPS_WITH_IDLES,
                1 val
         FROM   (SELECT SUM(TIME_MINUTES) SUM_IDLES_MINUTE,
                        SUM(TRIP)         TRIPS_WITH_IDLES
                 FROM   (SELECT d.VEHID                                       tech_key,
                                psc.POLY_STOP_CAT_NAME                        category,
                                s.TIMESTOP                                    TIMESTOP,
                                s.TIMEGO                                      TIMEGO,
                                ROUND(( s.TIMEGO - s.TIMESTOP ) * 24 * 60, 1) TIME_minutes,
                                1                                             trip
                         FROM   dispatcher.SHIFTSTOPPAGES s
                                inner join dispatcher.DUMPTRUCKS d
                                        ON d.VEHID = s.VEHID
                                           AND d.COLUMNNUM = 1
                                inner join dispatcher.POLY_USER_STOPPAGES_DUMP ps
                                        ON ps.POLY_STOP_BINDINGS_ID = 86
                                           AND ( ps.CODE = s.IDLESTOPTYPE
                                                 AND ps.POLY_STOP_CAT_ID IS NOT NULL )
                                inner join dispatcher.POLY_STOP_CATEGORIES psc
                                        ON psc.POLY_STOP_CAT_ID = ps.POLY_STOP_CAT_ID
                         WHERE  s.SHIFTDATE = :param_date
                                AND s.SHIFTNUM = :param_shift
                                AND ROUND(( s.TIMEGO - s.TIMESTOP ) * 24 * 60, 1) >= :param_target
                                AND NVL(s.IDLESTOPTYPE, 0) NOT IN( 0, 1, 67 )
                                AND psc.POLY_STOP_CAT_NAME = 'Ожидание погрузки/самосвала'
                         ORDER  BY TIMESTOP,
                                   TIMEGO))),
     queryq2
     AS (SELECT SUM(TRIPNUMBERMANUAL) all_trips,
                1                     val
         FROM   SHIFTREPORTSADV sra
         WHERE  sra.TASKDATE = :param_date
                AND sra.SHIFT = :param_shift)
SELECT SUM_IDLES_MINUTE,
       TRIPS_WITH_IDLES,
       ALL_TRIPS,
       round(SUM_IDLES_MINUTE / ALL_TRIPS, 1)  AVG_WAIT_ALL,
       round(SUM_IDLES_MINUTE / TRIPS_WITH_IDLES, 1)  AVG_WAIT
FROM   DUAL
       left join queryq1
              ON QUERYQ1.VAL = 1
       left join queryq2
              ON QUERYQ1.VAL = QUERYQ2.VAL 
"""


class Stoppages:
    @staticmethod
    def get_stoppages_report_aux_dvs() -> str:
        return """
SELECT 
    TIME,
    SPEED,
    FUEL,
    AUXID TECH
FROM   AUXEVENTARCHIVE t1
WHERE  t1.AUXID = :param_select_tech_id
    AND ( 
    TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) 
    AND GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) 
    )
ORDER  BY TIME DESC
"""

    @staticmethod
    def get_stoppages_report_veh_dvs_old() -> str:
        return """
SELECT 
    TIME,
    SPEED,
    FUEL,
    VEHID TECH
FROM   EVENTSTATEARCHIVE t1
WHERE  t1.VEHID = :param_select_tech_id
    AND ( 
    TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) 
    AND GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) 
    )
ORDER  BY TIME DESC
"""

    @staticmethod
    def get_stoppages_report_veh_dvs_new() -> str:
        return """
SELECT 
    VEHID,
    TIME,
    SPEED,
    MOTOHOURS
FROM   EVENTSTATEARCHIVE t1
WHERE  TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) 
                AND GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) 
                --and vehid = 141
ORDER  BY TIME DESC
    """

    @staticmethod
    def get_stoppages_report_veh_operators() -> str:
        return """
SELECT stk.VEHID,
       TRIM(d.FAMNAME)
       || ' '
       || TRIM(d.FIRSTNAME)
       || ' '
       || TRIM(d.SECNAME) FIO_VEHID
FROM   SHIFTTASKS stk
       inner join DRIVERS d
               ON stk.TABELNUM = d.TABELNUM
WHERE  stk.TASKDATE = :param_date
       AND stk.SHIFT = :param_shift
ORDER  BY VEHID 
"""

    @staticmethod
    def get_empty_peregon_report_dumptrucks_new() -> str:
        return """
SELECT VEHID,
       TIME,
       X
FROM   EVENTSTATEARCHIVE 
WHERE TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) AND 
                    GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)
AND (X > 80000 and X < 90000) AND (Y > 80000 AND Y < 90000)
ORDER BY TIME ASC 
"""

    @staticmethod
    def get_empty_peregon_report_dumptrucks() -> str:
        return """
SELECT VEHID,
       TIME,
       X,
       Y
FROM   EVENTSTATEARCHIVE 
WHERE TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) AND 
                    GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) 
AND (X > :param_min_x AND X < :param_max_x) AND (Y > :param_min_y AND Y < :param_max_y)
ORDER BY TIME ASC 
"""

    @staticmethod
    def get_empty_peregon_report_dumptrucks_old() -> str:
        return """
SELECT VEHID,
       TIME,
       X,
       Y
FROM   EVENTSTATEARCHIVE 
WHERE TIME BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) AND 
                    GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) 
AND X > 0 AND Y > 0
--AND VEHID = '142'
ORDER BY TIME ASC 
"""

    @staticmethod
    def get_all_peregons_report_dumptrucks() -> str:
        return """
WITH prms
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)       SDATETO
         FROM   DUAL)
SELECT VEHID, TIMEGO, TIMESTOP, AVGSPEED
FROM   SIMPLETRANSITIONS st
       inner join prms
               ON ( st.TIMEGO BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO )
                  AND ( st.TIMESTOP BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO )
--WHERE  st.VEHID = '142' 
/*
09:00-09:20
10:26-10:30
10:54-11:04
*/
"""

    @staticmethod
    def get_empty_dvs_work() -> str:
        return """
SELECT * -- 29/08/2023 13:00:00 - 29/08/2023 14:00:00
FROM   (SELECT VEHID,
                --MAX(MOTOHOURS) MAX_MOTOHOURS,
                --MIN(MOTOHOURS) MIN_MOTOHOURS,
               ( MAX(MOTOHOURS) - MIN(MOTOHOURS) ) motohours_munutes
        FROM   EVENTSTATEARCHIVE
        WHERE  (TIME BETWEEN :param_time_from AND :param_time_to) and (MOTOHOURS > 0 and MOTOHOURS < 99999999)
        GROUP  BY VEHID
        ORDER  BY VEHID)
WHERE  (motohours_munutes > 0 and motohours_munutes < 9999)
"""


class Gto:
    @staticmethod
    def get_gto_report_dumptrucks_speed_lenght_height_trips() -> str:
        return """
WITH prms
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) param_date_from,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)   param_date_to
         FROM   DUAL)
SELECT VEHID,
       FIO_VEHID,
       COUNT(*)                      SUM_TRIPS,
       ROUND(AVG(SPEED_LOAD), 2)     AVG_SPEED_LOAD,
       ROUND(AVG(SPEED_UNLOAD), 2)   AVG_SPEED_UNLOAD,
       ROUND(AVG(SPEED_ALL), 2)      AVG_SPEED_ALL,
       ROUND(AVG(LENGTH_LOAD), 2)    AVG_LENGTH_LOAD,
       ROUND(AVG(LENGTH_UNLOAD), 2)  AVG_LENGTH_UNLOAD,
       ROUND(AVG(LENGTH_ALL), 2)     AVG_LENGTH_ALL,
       ROUND(AVG(DIFF_HEIGHT), 2)    DIFF_HEIGHT,
       ROUND(AVG(WEIGHT), 2)         AVG_WEIGHT,
       ROUND(SUM(WEIGHT), 2)         SUM_WEIGHT,
       ROUND(SUM(VOLUME), 2)         SUM_VOLUME,
       ROUND(AVG(VOLUME), 2)         AVG_VOLUME,
       ROUND(SUM(TIME_LOADING), 2)   SUM_TIME_LOADING,
       ROUND(AVG(TIME_LOADING), 2)   AVG_TIME_LOADING,
       ROUND(SUM(TIME_UNLOADING), 2) SUM_TIME_UNLOADING,
       ROUND(AVG(TIME_UNLOADING), 2) AVG_TIME_UNLOADING,
       ROUND(SUM(TIME_MOVE), 2)      SUM_TIME_MOVE,
       ROUND(AVG(TIME_MOVE), 2)      AVG_TIME_MOVE,
       ROUND(SUM(TIME_TRIP), 2)      SUM_TIME_TRIP,
       ROUND(AVG(TIME_TRIP), 2)      AVG_TIME_TRIP
FROM   (SELECT q.TIME_LOAD,
               q.TIME_UNLOAD,
               q.VEHID,
               TRIM(d.FAMNAME)
               || ' '
               || TRIM(d.FIRSTNAME)
               || ' '
               || TRIM(d.SECNAME)                FIO_VEHID,
               q.SHOVID,
               q.WORKTYPE                        AVG_WORKTYPE,
               q.SPEED_LOAD                      SPEED_LOAD,
               q.SPEED_UNLOAD                    SPEED_UNLOAD,
               ( SPEED_LOAD + SPEED_UNLOAD ) / 2 SPEED_ALL,
               q.LENGTH_LOAD                     LENGTH_LOAD,
               q.LENGTH_UNLOAD                   LENGTH_UNLOAD,
               LENGTH_LOAD + LENGTH_UNLOAD       LENGTH_ALL,
               q.DIFF_HEIGHT,
               q.WEIGHT,
               q.VOLUME,
               q.TIME_LOADING,
               q.TIME_UNLOADING,
               q.TIME_MOVE,
               q.TIME_TRIP
        FROM   (SELECT s.TASKDATE                                                                      TASKDATE,
                       s.TASKSHIFT                                                                     TASKSHIFT,
                       s.TIMELOAD                                                                      TIME_LOAD,
                       s.TIMEUNLOAD                                                                    TIME_UNLOAD,
                       NVL(s.TIME_LOADING, 0)                                                          TIME_LOADING,
                       NVL(s.TIME_UNLOADING, 0)                                                        TIME_UNLOADING,
                       NVL(s.TIME_MOVE, 0)                                                             TIME_MOVE,
                       NVL(( s.TIMELOAD_NEXT - s.TIMELOAD ) * 24 * 60, 0)                              TIME_TRIP,
                       s.VEHID                                                                         VEHID,
                       s.SHOVID                                                                        SHOVID,
                       NVL(s.SPEED_LOAD, 0)                                                            SPEED_LOAD,
                       NVL(SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED), 0) SPEED_UNLOAD,
                       NVL(s.WEIGHT, 0)                                                                WEIGHT,
                       NVL(s.VOLUME, 0)                                                                VOLUME,
                       NVL(s.LENGTH, 0)                                                                LENGTH_LOAD,
                       NVL(s.UNLOADLENGTH, 0)                                                          LENGTH_UNLOAD,
                       NVL(s.DIFF_HEIGHT, 0)                                                           DIFF_HEIGHT,
                       NVL(s.WORKTYPE, 0)                                                              WORKTYPE
                FROM   (SELECT GETCURSHIFTDATE(0, TIMELOAD)                                                   taskdate,
                               GETCURSHIFTNUM(0, TIMELOAD)                                                    taskshift,
                               TIMELOAD,
                               TIMEUNLOAD,
                               ( TIMEGOAFTERLOAD - TIMELOAD ) * 24 * 60                                       TIME_LOADING,
                               ( TIME_INSERTING - TIMEUNLOAD ) * 24 * 60                                      TIME_UNLOADING,
                               ( MOVETIME - TO_DATE('01.01.2000', 'DD.MM.YYYY') ) * 24 * 60                   TIME_MOVE,
                               VEHID,
                               SHOVID,
                               WORKTYPE,
                               NVL(LEAD(TIMELOAD)
                                     over (
                                       PARTITION BY VEHCODE
                                       ORDER BY TIMELOAD), PRMS.PARAM_DATE_TO)                                TIMELOAD_NEXT,
                               AVSPEED                                                                        SPEED_LOAD,
                               LENGTH,
                               UNLOADLENGTH,
                               ABS(UNLOADHEIGHT - LOADHEIGHT)                                                 DIFF_HEIGHT,
                               WEIGHT,
                               DECODE(NVL(WEIGHT, 0), 0, 0,
                                                      WEIGHT * 1 / NVL(DECODE(WRATE, 0, WEIGHT,
                                                                                     WRATE), WEIGHT) * VRATE) AS VOLUME
                        FROM   VEHTRIPS
                               inner join prms
                                       ON TIMELOAD BETWEEN PRMS.PARAM_DATE_FROM AND PRMS.PARAM_DATE_TO
                                          AND TIMEUNLOAD BETWEEN PRMS.PARAM_DATE_FROM AND PRMS.PARAM_DATE_TO
                        WHERE  SHOVID NOT LIKE '%Неопр.%'
                               AND AVSPEED > 5
                               AND AVSPEED < 70
                               AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' )
                                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' )
                                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' )
                                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' )
                                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' )
                                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' )
                                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                                     AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' )
                                     AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) )) s
                       left join SIMPLETRANSITIONS st
                              ON st.VEHID = s.VEHID
                                 AND st.AVGSPEED > 5
                                 AND st.AVGSPEED < 70
                                 AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT )
                                 AND st.MOVELENGTH > 0
                GROUP  BY s.TASKDATE,
                          s.TASKSHIFT,
                          s.VEHID,
                          s.SHOVID,
                          s.WORKTYPE,
                          s.TIMELOAD,
                          s.TIMEUNLOAD,
                          s.TIME_LOADING,
                          s.TIME_UNLOADING,
                          s.TIME_MOVE,
                          ( s.TIMELOAD_NEXT - s.TIMELOAD ),
                          s.SPEED_LOAD,
                          s.LENGTH,
                          s.UNLOADLENGTH,
                          s.DIFF_HEIGHT,
                          s.WEIGHT,
                          s.VOLUME)q
               left join SHIFTTASKS stk
                      ON stk.TASKDATE = q.TASKDATE
                         AND stk.SHIFT = q.TASKSHIFT
                         AND stk.VEHID = q.VEHID
               left join DRIVERS d
                      ON stk.TABELNUM = d.TABELNUM
        ORDER  BY VEHID)
GROUP  BY VEHID,
          FIO_VEHID
ORDER  BY VEHID 
    """

    @staticmethod
    def get_gto_trips_with_drivers() -> str:
        return """
SELECT vt.VEHID VEHID, 
       drivers_t.FAMNAME 
       || ' ' 
       || drivers_t.FIRSTNAME 
       || ' ' 
       || drivers_t.SECNAME      AS vehdriver, 
       vt.SHOVID SHOVID, 
       drivers_shov_t.FAMNAME 
       || ' ' 
       || drivers_shov_t.FIRSTNAME 
       || ' ' 
       || drivers_shov_t.SECNAME AS shovdriver
FROM   VEHTRIPS vt 
       left join DUMPTRUCKS trucks_t 
              ON vt.VEHID = trucks_t.VEHID 
       left join SHOVELS shovels_t 
              ON shovels_t.SHOVID = vt.SHOVID 
       left join SHIFTTASKS tasks_t 
              ON vt.VEHID = tasks_t.VEHID 
                 AND tasks_t.TASKDATE = TRUNC(vt.TIMELOAD) 
                 AND tasks_t.SHIFT = GETCURSHIFTNUM(1, vt.TIMELOAD) 
       left join DRIVERS drivers_t 
              ON tasks_t.TABELNUM = drivers_t.TABELNUM 
       left join SHOV_SHIFT_TASKS tasks_shov_t 
              ON vt.SHOVID = tasks_shov_t.SHOV_ID 
                 AND tasks_shov_t.TASK_DATE = TRUNC(vt.TIMELOAD) 
                 AND tasks_shov_t.SHIFT = GETCURSHIFTNUM(1, vt.TIMELOAD) 
       left join SHOVDRIVERS drivers_shov_t 
              ON tasks_shov_t.TABEL_NUM = drivers_shov_t.TABELNUM 
WHERE  vt.TIMEUNLOAD BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) 
                         AND GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)
ORDER  BY TIMELOAD ASC 
"""

    @staticmethod
    def get_gto_report_dumptrucks() -> str:
        return """
WITH prms
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) param_date_from,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)   param_date_to
         FROM   DUAL)
SELECT q.TIME_LOAD,
       q.TIME_UNLOAD,
       
       q.VEHID,
       TRIM(d.FAMNAME)
       || ' '
       || TRIM(d.FIRSTNAME)
       || ' '
       || TRIM(d.SECNAME)       FIO_VEHID,
       q.SHOVID,
       q.WORKTYPE               AVG_WORKTYPE,
       
       ROUND(q.SPEED_LOAD, 2)   SPEED_LOAD,
       ROUND(q.SPEED_UNLOAD, 2) SPEED_UNLOAD,
       q.LENGTH_LOAD            LENGTH_LOAD,
       q.LENGTH_UNLOAD          LENGTH_UNLOAD,
       q.WEIGHT                 WEIGHT,
       ROUND(q.VOLUME, 2)       VOLUME
FROM   (SELECT s.TASKDATE                                                                      TASKDATE,
               s.TASKSHIFT                                                                     TASKSHIFT,
               s.TIMELOAD                                                                      TIME_LOAD,
               s.TIMEUNLOAD                                                                    TIME_UNLOAD,
               s.VEHID                                                                         VEHID,
               s.SHOVID                                                                        SHOVID,
               NVL(s.SPEED_LOAD, 0)                                                            SPEED_LOAD,
               NVL(SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED), 0) SPEED_UNLOAD,
               NVL(s.WEIGHT, 0)                                                                WEIGHT,
               NVL(s.VOLUME, 0)                                                                VOLUME,
               NVL(s.LENGTH, 0)                                                                LENGTH_LOAD,
               NVL(s.UNLOADLENGTH, 0)                                                          LENGTH_UNLOAD,
               NVL(s.DIFF_HEIGHT, 0)                                                                DIFF_HEIGHT,
               NVL(s.WORKTYPE, 0)                                                              WORKTYPE
        FROM   (SELECT GETCURSHIFTDATE(0, TIMELOAD)                                                   taskdate,
                       GETCURSHIFTNUM(0, TIMELOAD)                                                    taskshift,
                       TIMELOAD,
                       TIMEUNLOAD,
                       VEHID,
                       SHOVID,
                       WORKTYPE,
                       NVL(LEAD(TIMELOAD)
                             over (
                               PARTITION BY VEHCODE
                               ORDER BY TIMELOAD), PRMS.PARAM_DATE_TO)                                TIMELOAD_NEXT,
                       AVSPEED                                                                        SPEED_LOAD,
                       LENGTH,
                       UNLOADLENGTH,
                       loadheight - unloadheight DIFF_HEIGHT,
                       WEIGHT,
                       DECODE(NVL(WEIGHT, 0), 0, 0,
                                              WEIGHT * 1 / NVL(DECODE(WRATE, 0, WEIGHT,
                                                                             WRATE), WEIGHT) * VRATE) AS VOLUME
                FROM   VEHTRIPS
                       inner join prms
                               ON TIMELOAD BETWEEN PRMS.PARAM_DATE_FROM AND PRMS.PARAM_DATE_TO
                                  AND TIMEUNLOAD BETWEEN PRMS.PARAM_DATE_FROM AND PRMS.PARAM_DATE_TO
                WHERE  SHOVID NOT LIKE '%Неопр.%'
                       AND AVSPEED > 5
                       AND AVSPEED < 70
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) )) s
               left join SIMPLETRANSITIONS st
                      ON st.VEHID = s.VEHID
                         AND st.AVGSPEED > 5
                         AND st.AVGSPEED < 70
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT )
                         AND st.MOVELENGTH > 0
        GROUP  BY s.TASKDATE,
                  s.TASKSHIFT,
                  s.VEHID,
                  s.SHOVID,
                  s.WORKTYPE,
                  s.TIMELOAD,
                  s.TIMEUNLOAD,
                  s.SPEED_LOAD,
                  s.LENGTH,
                  s.UNLOADLENGTH,
                  s.DIFF_HEIGHT,
                  s.WEIGHT,
                  s.VOLUME)q
       left join SHIFTTASKS stk
              ON stk.TASKDATE = q.TASKDATE
                 AND stk.SHIFT = q.TASKSHIFT
                 AND stk.VEHID = q.VEHID
       left join DRIVERS d
              ON stk.TABELNUM = d.TABELNUM
ORDER  BY VEHID,
          TIME_LOAD 
"""


class Develop:
    @staticmethod
    def get_target_report_weight_loads() -> str:
        return """
SELECT TRUNC(vt.TIMELOAD) TASKDATE, 
       GETCURSHIFTNUM(1, vt.TIMELOAD) TASKSHIFT, 
       vt.SHOVID, 
       drivers_shov_t.FAMNAME 
       || ' ' 
       || drivers_shov_t.FIRSTNAME 
       || ' ' 
       || drivers_shov_t.SECNAME AS shovdriver, 
       vt.VEHID, 
       drivers_t.FAMNAME 
       || ' ' 
       || drivers_t.FIRSTNAME 
       || ' ' 
       || drivers_t.SECNAME      AS vehdriver, 
       vt.AREA, 
       vt.WORKTYPE, 
       vt.UNLOADID, 
       vt.TIMELOAD, 
       vt.AVSPEED, 
       vt.WEIGHT 
FROM   VEHTRIPS vt 
       left join DUMPTRUCKS trucks_t 
              ON vt.VEHID = trucks_t.VEHID 
       left join SHOVELS shovels_t 
              ON shovels_t.SHOVID = vt.SHOVID 
       left join SHIFTTASKS tasks_t 
              ON vt.VEHID = tasks_t.VEHID 
                 AND tasks_t.TASKDATE = TRUNC(vt.TIMELOAD) 
                 AND tasks_t.SHIFT = GETCURSHIFTNUM(1, vt.TIMELOAD) 
       left join DRIVERS drivers_t 
              ON tasks_t.TABELNUM = drivers_t.TABELNUM 
       left join SHOV_SHIFT_TASKS tasks_shov_t 
              ON vt.SHOVID = tasks_shov_t.SHOV_ID 
                 AND tasks_shov_t.TASK_DATE = TRUNC(vt.TIMELOAD) 
                 AND tasks_shov_t.SHIFT = GETCURSHIFTNUM(1, vt.TIMELOAD) 
       left join SHOVDRIVERS drivers_shov_t 
              ON tasks_shov_t.TABEL_NUM = drivers_shov_t.TABELNUM 
WHERE  vt.TIMEUNLOAD BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift_from, :param_date_from) AND GETPREDEFINEDTIMETO('за указанную смену', :param_shift_to, :param_date_to)
       AND ( vt.WEIGHT <= :param_weight_low 
              OR vt.WEIGHT >= :param_weight_high ) and vt.shovid != 'Неопр.'
ORDER  BY TIMELOAD ASC 
"""

    @staticmethod
    def get_pto_analytic_tech_weight_loads() -> str:
        return """
SELECT t1.*,
       sd.FAMNAME
       || ' '
       || sd.FIRSTNAME
       || ' '
       || sd.SECNAME
       || ' '
       || sd.TABELNUM FIO
FROM   (SELECT vt.VEHID,
               vt.WORKTYPE,
               vt.TIMELOAD,
               vt.WEIGHT,
               ROUND(DECODE(NVL(vt.WEIGHT, 0), 0, 0,
                                               vt.WEIGHT * 1 / NVL(DECODE(vt.WRATE, 0, vt.WEIGHT,
                                                                                    vt.WRATE), vt.WEIGHT) * vt.VRATE), 3) AS Volume,
               TO_CHAR(vt.TIMELOAD, 'HH24')                                                                               HOUR_LOAD,
               NVL(vt.BUCKETCOUNT, -1)                                                                                    bucketcount
        FROM   VEHTRIPS vt
        WHERE  vt.TIMEUNLOAD BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE)) AND GETPREDEFINEDTIMETO('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE))
               AND ( vt.WEIGHT <= :param_low
                      OR vt.WEIGHT >= :param_high )
               AND vt.SHOVID = :param_shov_id
        ORDER  BY TIMELOAD ASC) t1
       left join SHOV_SHIFT_TASKS st
              ON st.TASK_DATE = GETCURSHIFTDATE(0, SYSDATE)
                 AND st.SHIFT = GETCURSHIFTNUM(0, SYSDATE)
                 AND st.SHOV_ID = :param_shov_id
       left join SHOVDRIVERS sd
              ON st.TABEL_NUM = sd.TABELNUM
       left join SHOVELS s
              ON st.SHOV_ID = s.SHOVID 
"""

    @staticmethod
    def get_target_report_avg_speed() -> str:
        return """
WITH b
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)   SDATETO
         FROM   DUAL)
SELECT q.VEHID,
       q.SHOVID,
       TRIM(d.FAMNAME)
       || ' '
       || TRIM(d.FIRSTNAME)
       || ' '
       || TRIM(d.SECNAME)                            fio,
       KEM_DATETODDMMYYYY(q.TASKDATE)                TASKDATE,
       q.SHIFT,
       q.TRIP                                        trips,
       q.WORKTYPE                                    worktype,
       q.TIMELOAD,
       q.TIMEUNLOAD,
       NVL(ROUND(q.AVSPEED, 2), -1)                           avgloadspeed,
       NVL(ROUND(q.AVSPEED_EMPTY, 2), -1)                     avgemptyspeed,
       NVL(ROUND(( q.AVSPEED + q.AVSPEED_EMPTY ) / 2, 2), -1) avspeed
FROM   (SELECT s.VEHID,
               s.VEHCODE,
               s.SHOVID,
               s.WORKTYPE,
               s.TIMELOAD,
               s.TIMEUNLOAD,
               s.TIMELOAD_NEXT,
               s.AVSPEED,
               s.TASKDATE,
               s.SHIFT,
               TRIP,
               SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED) AVSPEED_EMPTY
        FROM   (SELECT VEHID,
                       VEHCODE,
                       SHOVID,
                       WORKTYPE,
                       TIMELOAD,
                       TIMEUNLOAD,
                       NVL(LEAD(TIMELOAD)
                             over (
                               PARTITION BY VEHCODE
                               ORDER BY TIMELOAD), B.SDATETO) TIMELOAD_NEXT,
                       AVSPEED,
                       GETCURSHIFTDATE(0, TIMELOAD)           taskdate,
                       GETCURSHIFTNUM(0, TIMELOAD)            shift,
                       1                                      trip
                FROM   VEHTRIPS
                       inner join b
                               ON TIMELOAD BETWEEN B.SDATEFROM AND B.SDATETO
                                  AND TIMEUNLOAD BETWEEN B.SDATEFROM AND B.SDATETO
                WHERE  SHOVID NOT LIKE '%Неопр.%'
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) )
                ORDER  BY LENGTH(VEHID),
                          VEHID,
                          TIMELOAD) s
               left join SIMPLETRANSITIONS st
                      ON st.VEHCODE = s.VEHCODE
                         AND st.AVGSPEED > 5
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT )
                         AND st.MOVELENGTH > 0
        GROUP  BY s.VEHID,
                  s.VEHCODE,
                  s.WORKTYPE,
                  s.SHOVID,
                  s.TIMELOAD,
                  s.TIMEUNLOAD,
                  s.TIMELOAD_NEXT,
                  s.AVSPEED,
                  s.TASKDATE,
                  s.SHIFT,
                  s.TRIP)q
       left join SHIFTTASKS stk
              ON stk.TASKDATE = q.TASKDATE
                 AND stk.SHIFT = q.SHIFT
                 AND stk.VEHID = q.VEHID
       left join DRIVERS d
              ON stk.TABELNUM = d.TABELNUM
ORDER  BY q.TASKDATE,
          TIMELOAD 
"""

    @staticmethod
    def get_target_report_avg_speed_by_hours() -> str:
        return """
SELECT VEHID, TIME_GROUP, round(AVG(avgloadspeed), 1) avgloadspeed, round(AVG(avgemptyspeed), 1) avgemptyspeed, round(AVG(avspeed), 1) avspeed 
from (
SELECT q.VEHID,
       q.SHOVID,
       TRIM(d.FAMNAME)
       || ' '
       || TRIM(d.FIRSTNAME)
       || ' '
       || TRIM(d.SECNAME)                            fio,
       KEM_DATETODDMMYYYY(q.TASKDATE)                TASKDATE,
       q.SHIFT,
       TO_CHAR(q.TIMELOAD, 'HH24') TIME_GROUP,
       CASE TO_NUMBER(TO_CHAR(q.TIMELOAD, 'HH24'))
           WHEN 20 THEN -4
           WHEN 21 THEN -3
           WHEN 22 THEN -2
           WHEN 23 THEN -1
           ELSE TO_NUMBER(TO_CHAR(q.TIMELOAD, 'HH24'))
        END TIME_GROUP_ORD,
       q.TRIP                                        trips,
       q.WORKTYPE                                    worktype,
       q.TIMELOAD,
       q.TIMEUNLOAD,
       NVL(ROUND(q.AVSPEED, 2), -1)                           avgloadspeed,
       NVL(ROUND(q.AVSPEED_EMPTY, 2), -1)                     avgemptyspeed,
       NVL(ROUND(( q.AVSPEED + q.AVSPEED_EMPTY ) / 2, 2), -1) avspeed
FROM   (SELECT s.VEHID,
               s.VEHCODE,
               s.SHOVID,
               s.WORKTYPE,
               s.TIMELOAD,
               s.TIMEUNLOAD,
               s.TIMELOAD_NEXT,
               s.AVSPEED,
               s.TASKDATE,
               s.SHIFT,
               TRIP,
               SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED) AVSPEED_EMPTY
        FROM   (SELECT VEHID,
                       VEHCODE,
                       SHOVID,
                       WORKTYPE,
                       TIMELOAD,
                       TIMEUNLOAD,
                       NVL(LEAD(TIMELOAD)
                             over (
                               PARTITION BY VEHCODE
                               ORDER BY TIMELOAD), GETPREDEFINEDTIMETO('за указанную смену', 2, :param_date)) TIMELOAD_NEXT,
                       AVSPEED,
                       GETCURSHIFTDATE(0, TIMELOAD)           taskdate,
                       GETCURSHIFTNUM(0, TIMELOAD)            shift,
                       1                                      trip
                FROM   VEHTRIPS
                       where  TIMELOAD BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', 1, :param_date) AND GETPREDEFINEDTIMETO('за указанную смену', 2, :param_date)
                                  AND TIMEUNLOAD BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', 1, :param_date) AND GETPREDEFINEDTIMETO('за указанную смену', 2, :param_date)
                and  SHOVID NOT LIKE '%Неопр.%' AND AVSPEED > 5 AND AVSPEED < 70
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' )
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' )
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) )
                ORDER  BY LENGTH(VEHID),
                          VEHID,
                          TIMELOAD) s
               left join SIMPLETRANSITIONS st
                      ON st.VEHCODE = s.VEHCODE
                         AND st.AVGSPEED > 5 AND st.AVGSPEED < 70
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT )
                         AND st.MOVELENGTH > 0
        GROUP  BY s.VEHID,
                  s.VEHCODE,
                  s.WORKTYPE,
                  s.SHOVID,
                  s.TIMELOAD,
                  s.TIMEUNLOAD,
                  s.TIMELOAD_NEXT,
                  s.AVSPEED,
                  s.TASKDATE,
                  s.SHIFT,
                  s.TRIP)q
       left join SHIFTTASKS stk
              ON stk.TASKDATE = q.TASKDATE
                 AND stk.SHIFT = q.SHIFT
                 AND stk.VEHID = q.VEHID
       left join DRIVERS d
              ON stk.TABELNUM = d.TABELNUM
ORDER  BY q.TASKDATE,
          TIMELOAD )
          group by VEHID, TIME_GROUP_ORD, TIME_GROUP
          order by vehid, TIME_GROUP_ORD
"""

    @staticmethod
    def get_target_monitoring_weight_loads() -> str:
        return """
SELECT sd.FAMNAME 
       || ' ' 
       || sd.FIRSTNAME 
       || ' ' 
       || sd.SECNAME 
       || ' ' 
       || sd.TABELNUM AS FIO 
FROM   SHOV_SHIFT_TASKS st 
       inner join SHOVDRIVERS sd 
               ON st.TABEL_NUM = sd.TABELNUM 
       inner join SHOVELS s 
               ON st.SHOV_ID = s.SHOVID 
WHERE  st.TASK_DATE = :param_date 
       AND st.SHIFT = :param_shift 
       AND st.SHOV_ID = :param_shov_id 
ORDER  BY FIO 
"""

    @staticmethod
    def get_pto_analytic_tech_volumes_by_category() -> str:
        return """
select worktype, sum(Volume), sum(1) count from (SELECT tripcounter,
       vehid,
       shovid,
       unloadid,
       worktype,
       TO_CHAR(timeload, 'HH24')                                     HOUR_LOAD,
       timeload,
       timeunload,
       movetime,
       weight,
       nvl(bucketcount, -1) bucketcount,
       avspeed,
       length,
       unloadlength,
       loadheight,
       unloadheight,
       round(decode(nvl(vt.WEIGHT,0), 
                                 0,0, 
                                 vt.WEIGHT*1/nvl(decode(vt.wrate,
                                                                                    0,vt.WEIGHT,
                                                                                    vt.wrate),vt.WEIGHT)*vt.vrate), 3) as Volume
FROM   vehtrips vt
WHERE  vt.timeunload BETWEEN getpredefinedtimefrom('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE)) AND getpredefinedtimeto('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE))
ORDER  BY vehid ASC, timeload ASC ) group by worktype order by worktype asc
"""

    @staticmethod
    def get_pto_analytic_tech_volumes_by_hours() -> str:
        return """
select HOUR_LOAD, sum(Volume) from (SELECT tripcounter,
       vehid,
       shovid,
       unloadid,
       worktype,
       TO_CHAR(timeload, 'HH24')                                     HOUR_LOAD,
       timeload,
       timeunload,
       movetime,
       weight,
       nvl(bucketcount, -1) bucketcount,
       avspeed,
       length,
       unloadlength,
       loadheight,
       unloadheight,
       round(decode(nvl(vt.WEIGHT,0), 
                                 0,0, 
                                 vt.WEIGHT*1/nvl(decode(vt.wrate,
                                                                                    0,vt.WEIGHT,
                                                                                    vt.wrate),vt.WEIGHT)*vt.vrate), 3) as Volume
FROM   vehtrips vt
WHERE  vt.timeunload BETWEEN getpredefinedtimefrom('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE)) AND getpredefinedtimeto('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE))
ORDER  BY vehid ASC, timeload ASC ) group by HOUR_LOAD order by HOUR_LOAD asc
"""

    @staticmethod
    def query_get_elapsed_time() -> str:
        return """
select tm.fromTime, tm.toTime, round((tm.toTime-SYSDATE) * 24, 2) elapsed from (select 
getpredefinedtimefrom('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE)) fromTime,
 getpredefinedtimeto('за указанную смену', getcurshiftnum(0, SYSDATE)) toTime
  from DUAL) tm
"""

    @staticmethod
    def get_target_report_avg_speed_new() -> str:
        return """
WITH b 
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date)   SDATETO 
         FROM   DUAL) 
SELECT q.VEHID, 
       q.SHOVID, 
       TRIM(d.FAMNAME) 
       || ' ' 
       || TRIM(d.FIRSTNAME) 
       || ' ' 
       || TRIM(d.SECNAME)                                fio, 
       ROUND(q.AVG_SPEED, 2)                             avg_speed_load, 
       ROUND(q.AVG_SPEED_EMPTY, 2)                       avg_speed_empty, 
       ROUND(( q.AVG_SPEED + q.AVG_SPEED_EMPTY ) / 2, 2) avg_speed, 
       ROUND(q.AVG_WEIGHT, 2)                            avg_weight, 
       ROUND(q.AVG_LENGTH_LOAD, 2)                       avg_length_load, 
       ROUND(q.AVG_LENGTH_UNLOAD, 2)                     avg_length_unload, 
       ROUND(( q.AVG_LENGTH_LOAD + q.AVG_LENGTH_UNLOAD ) / 2, 2) avg_length, 
       ROUND(q.AVG_HEIGHT, 2)                            AVG_HEIGHT, 
       q.WORKTYPE                                        AVG_WORKTYPE, 
       ROUND(q.WORKTIME, 2)                              AVG_WORKTIME 
FROM   (SELECT s.VEHID, 
               s.VEHCODE, 
               s.SHOVID, 
               s.TASKDATE, 
               s.SHIFT, 
               NVL(s.AVSPEED, 0)                                                               AVG_SPEED,
               NVL(SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED), 0) AVG_SPEED_EMPTY,
               NVL(s.WEIGHT, 0)                                                                AVG_WEIGHT,
               NVL(s.LENGTH, 0)                                                                AVG_LENGTH_LOAD,
               NVL(s.UNLOADLENGTH, 0)                                                          AVG_LENGTH_UNLOAD,
               NVL(s.UNLOADHEIGHT, 0) - NVL(s.LOADHEIGHT, 0)                                   AVG_HEIGHT,
               NVL(s.WORKTYPE, 0)                                                              WORKTYPE,
               NVL(( s.TIMEUNLOAD - s.TIMELOAD ) * 24 * 60, 0)                                 WORKTIME
        FROM   (SELECT VEHID, 
                       VEHCODE, 
                       SHOVID, 
                       TIMELOAD, 
                       TIMEUNLOAD, 
                       NVL(LEAD(TIMELOAD) 
                             over ( 
                               PARTITION BY VEHCODE 
                               ORDER BY TIMELOAD), B.SDATETO) TIMELOAD_NEXT, 
                       AVSPEED, 
                       WEIGHT, 
                       LENGTH, 
                       UNLOADLENGTH, 
                       LOADHEIGHT, 
                       UNLOADHEIGHT, 
                       WORKTYPE, 
                       GETCURSHIFTDATE(0, TIMELOAD)           taskdate, 
                       GETCURSHIFTNUM(0, TIMELOAD)            shift 
                FROM   VEHTRIPS 
                       inner join b 
                               ON TIMELOAD BETWEEN B.SDATEFROM AND B.SDATETO 
                                  AND TIMEUNLOAD BETWEEN B.SDATEFROM AND B.SDATETO 
                WHERE  SHOVID NOT LIKE '%Неопр.%' AND AVSPEED > 5 AND AVSPEED < 70
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' ) 
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) ) 
                ORDER  BY LENGTH(VEHID), 
                          VEHID, 
                          TIMELOAD) s 
               left join SIMPLETRANSITIONS st 
                      ON st.VEHCODE = s.VEHCODE 
                         AND st.AVGSPEED > 5 AND st.AVGSPEED < 70
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT ) 
                         AND st.MOVELENGTH > 0 
        GROUP  BY s.VEHID, 
                  s.VEHCODE, 
                  s.SHOVID, 
                  s.TASKDATE, 
                  s.SHIFT, 
                  s.AVSPEED, 
                  s.WEIGHT, 
                  s.LENGTH, 
                  s.UNLOADLENGTH, 
                  s.LOADHEIGHT, 
                  s.UNLOADHEIGHT, 
                  s.WORKTYPE, 
                  s.TIMELOAD, 
                  s.TIMEUNLOAD)q 
       left join SHIFTTASKS stk 
              ON stk.TASKDATE = q.TASKDATE 
                 AND stk.SHIFT = q.SHIFT 
                 AND stk.VEHID = q.VEHID 
       left join DRIVERS d 
              ON stk.TABELNUM = d.TABELNUM 
"""

    @staticmethod
    def get_target_monitoring_loads_new() -> str:
        return """
WITH b 
AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE)) SDATEFROM,
        GETPREDEFINEDTIMETO('за указанную смену', getcurshiftnum(0, SYSDATE), getcurshiftdate(0, SYSDATE))   SDATETO 
 FROM   DUAL) 
SELECT s.*, 
       sd.FAMNAME 
       || ' ' 
       || sd.FIRSTNAME 
       || ' ' 
       || sd.SECNAME 
       || ' ' 
       || sd.TABELNUM FIO 
FROM   (SELECT SHOVID, 
               VEHID, 
               TIMELOAD, 
               TIMEUNLOAD, 
               WEIGHT, 
               LENGTH, 
               UNLOADLENGTH, 
               UNLOADHEIGHT - LOADHEIGHT HEIGHT, 
               WORKTYPE, 
               GETCURSHIFTDATE(0, TIMELOAD) taskdate, 
               GETCURSHIFTNUM(0, TIMELOAD)  shift,
               ROUND(DECODE(NVL(WEIGHT, 0), 0, 0, WEIGHT * 1 / NVL(DECODE(WRATE, 0, WEIGHT,  WRATE), WEIGHT) * VRATE), 2) AS Volume
        FROM   VEHTRIPS 
               inner join b 
                       ON TIMELOAD BETWEEN B.SDATEFROM AND B.SDATETO 
                          AND TIMEUNLOAD BETWEEN B.SDATEFROM AND B.SDATETO 
        WHERE  SHOVID NOT LIKE '%Неопр.%' 
               AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' ) 
                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' ) 
                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' ) 
                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' ) 
                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' ) 
                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' ) 
                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' ) 
                     AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' ) 
                     AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) ) 
        ORDER  BY TIMELOAD, 
                  SHOVID) s 
       inner join SHOV_SHIFT_TASKS st 
               ON st.TASK_DATE = s.TASKDATE 
                  AND st.SHIFT = s.SHIFT 
                  AND st.SHOV_ID = s.SHOVID 
       inner join SHOVDRIVERS sd 
               ON st.TABEL_NUM = sd.TABELNUM 
"""


class Old:
    @staticmethod
    def all_trips_dumptrucks_for_selected_date_and_shift():
        return """
WITH prms 
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', :param_shift, :param_date) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', :param_shift, :param_date) SDATETO
         FROM   DUAL) 
SELECT q.VEHID, 
       TRIM(d.FAMNAME) 
       || ' ' 
       || TRIM(d.FIRSTNAME) 
       || ' ' 
       || TRIM(d.SECNAME)                                     fio, 
       q.SHOVID, 
       ROUND(NVL(q.AVSPEED, -1), 2)                           avgloadspeed, 
       ROUND(NVL(q.AVSPEED_EMPTY, -1), 2)                     avgemptyspeed, 
       ROUND(NVL(( q.AVSPEED + q.AVSPEED_EMPTY ) / 2, -1), 2) avspeed, 
       ROUND(q.WEIGHT, 2)                                     WEIGHT, 
       ROUND(q.LENGTH, 2)                                     LENGTH_FULL, 
       ROUND(q.UNLOADLENGTH, 2)                               UNLOADLENGTH_EMPT, 
       ROUND(q.LENGTH + q.UNLOADLENGTH, 2)                    LENGTH_ALL 
FROM   (SELECT s.VEHID, 
               s.VEHCODE, 
               s.SHOVID, 
               s.WORKTYPE, 
               s.WEIGHT, 
               s.LENGTH, 
               s.UNLOADLENGTH, 
               s.TIMELOAD, 
               s.TIMELOAD_NEXT, 
               s.AVSPEED, 
               s.TASKDATE, 
               s.SHIFT, 
               TRIP, 
               SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED) AVSPEED_EMPTY
        FROM   (SELECT VEHID, 
                       VEHCODE, 
                       SHOVID, 
                       WORKTYPE, 
                       WEIGHT, 
                       LENGTH, 
                       UNLOADLENGTH, 
                       TIMELOAD, 
                       TIMEUNLOAD, 
                       NVL(LEAD(TIMELOAD) 
                             over ( 
                               PARTITION BY VEHCODE 
                               ORDER BY TIMELOAD), PRMS.SDATETO) TIMELOAD_NEXT, 
                       AVSPEED, 
                       GETCURSHIFTDATE(0, TIMELOAD)              taskdate, 
                       GETCURSHIFTNUM(0, TIMELOAD)               shift, 
                       1                                         trip 
                FROM   VEHTRIPS 
                       inner join prms 
                               ON TIMELOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                                  AND TIMEUNLOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                WHERE  SHOVID NOT LIKE '%Неопр.%' 
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' )
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' ) 
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) ) 
                ORDER  BY VEHID, 
                          TIMELOAD) s 
               left join SIMPLETRANSITIONS st 
                      ON st.VEHCODE = s.VEHCODE 
                         AND st.AVGSPEED > 5 
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT ) 
                         AND st.MOVELENGTH > 0 
        GROUP  BY s.VEHID, 
                  s.VEHCODE, 
                  s.WORKTYPE, 
                  s.WEIGHT, 
                  s.LENGTH, 
                  s.UNLOADLENGTH, 
                  s.SHOVID, 
                  s.TIMELOAD, 
                  s.TIMELOAD_NEXT, 
                  s.AVSPEED, 
                  s.TASKDATE, 
                  s.SHIFT, 
                  s.TRIP)q 
       left join SHIFTTASKS stk 
              ON stk.TASKDATE = q.TASKDATE 
                 AND stk.SHIFT = q.SHIFT 
                 AND stk.VEHID = q.VEHID 
       left join DRIVERS d 
              ON stk.TABELNUM = d.TABELNUM 
ORDER  BY TIMELOAD 
"""

    @staticmethod
    def speed_dumptrucks_for_now() -> str:
        return """
WITH prms 
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE)) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE))   SDATETO
         FROM   DUAL) 
SELECT q.VEHID                                                 VEHID, 
       TRIM(d.FAMNAME) 
       || ' ' 
       || TRIM(d.FIRSTNAME) 
       || ' ' 
       || TRIM(d.SECNAME)                                      FIO, 
       KEM_DATETODDMMYYYY(q.TASKDATE)                          TASKDATE, 
       q.SHIFT                                                 SHIFT, 
       ROUND(AVG(q.AVSPEED), 2)                                AVG_SPEED_FULL, 
       ROUND(AVG(q.AVSPEED_EMPTY), 2)                          AVG_SPEED_EMPTY, 
       ROUND(( AVG(q.AVSPEED) + AVG(q.AVSPEED_EMPTY) ) / 2, 2) AVG_SPEED_ALL, 
       SUM(q.TRIP)                                             SUM_TRIPS, 
       ROUND(AVG(q.WEIGHT), 2)                                 AVG_WEIGHT, 
       ROUND(AVG(q.LENGTH), 2)                                 AVG_LENGTH_FULL, 
       ROUND(AVG(q.UNLOADLENGTH), 2)                           AVG_UNLOADLENGTH_EMPTY, 
       ROUND(( AVG(q.LENGTH) + AVG(q.UNLOADLENGTH) ) / 2, 2)   AVG_LENGTH_ALL 
FROM   (SELECT s.VEHID, 
               s.VEHCODE, 
               ROUND(AVG(s.WEIGHT), 2)                                                 WEIGHT, 
               ROUND(AVG(s.LENGTH), 2)                                                 LENGTH, 
               ROUND(AVG(s.UNLOADLENGTH), 2)                                           UNLOADLENGTH,
               s.TIMELOAD, 
               s.TIMEUNLOAD, 
               s.TIMELOAD_NEXT, 
               s.AVSPEED, 
               s.TASKDATE, 
               s.SHIFT, 
               TRIP, 
               SUM(st.MOVELENGTH / 1000) / SUM(( st.MOVELENGTH / 1000 ) / st.AVGSPEED) AVSPEED_EMPTY
        FROM   (SELECT VEHID, 
                       VEHCODE, 
                       WEIGHT, 
                       LENGTH, 
                       UNLOADLENGTH, 
                       TIMELOAD, 
                       TIMEUNLOAD, 
                       NVL(LEAD(TIMELOAD) 
                             over ( 
                               PARTITION BY VEHCODE 
                               ORDER BY TIMELOAD), PRMS.SDATETO) TIMELOAD_NEXT, 
                       AVSPEED, 
                       GETCURSHIFTDATE(0, TIMELOAD)              taskdate, 
                       GETCURSHIFTNUM(0, TIMELOAD)               shift, 
                       1                                         trip 
                FROM   VEHTRIPS 
                       left join prms 
                              ON 1 = 1 
                WHERE  TIMELOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                       AND TIMEUNLOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
                       AND SHOVID NOT LIKE '%Неопр.%' 
                       AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' ) 
                             AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' ) 
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' ) 
                             AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' ) 
                             AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' ) )
                ORDER  BY LENGTH(VEHID), 
                          VEHID, 
                          TIMELOAD) s 
               left join SIMPLETRANSITIONS st 
                      ON st.VEHCODE = s.VEHCODE 
                         AND st.AVGSPEED > 5 
                         AND ( st.TIMEGO BETWEEN s.TIMEUNLOAD AND s.TIMELOAD_NEXT ) 
                         AND st.MOVELENGTH > 0 
        GROUP  BY s.VEHID, 
                  s.VEHCODE, 
                  s.TIMELOAD, 
                  s.TIMEUNLOAD, 
                  s.TIMELOAD_NEXT, 
                  s.AVSPEED, 
                  s.TASKDATE, 
                  s.SHIFT, 
                  s.TRIP)q 
       left join SHIFTTASKS stk 
              ON stk.TASKDATE = q.TASKDATE 
                 AND stk.SHIFT = q.SHIFT 
                 AND stk.VEHID = q.VEHID 
       left join DRIVERS d 
              ON stk.TABELNUM = d.TABELNUM 
GROUP  BY q.VEHID, 
          TRIM(d.FAMNAME) 
          || ' ' 
          || TRIM(d.FIRSTNAME) 
          || ' ' 
          || TRIM(d.SECNAME), 
          q.TASKDATE, 
          q.SHIFT 
ORDER  BY VEHID ASC 
"""

    @staticmethod
    def max_trips_for_dumptrucks_on_shovels() -> str:
        return """
WITH prms 
     AS (SELECT GETPREDEFINEDTIMEFROM('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE)) SDATEFROM,
                GETPREDEFINEDTIMETO('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE))   SDATETO
         FROM   DUAL) 
SELECT VEHID, 
       SHOVID, 
       SUM(TRIP) trips 
FROM   (SELECT VEHID, 
               SHOVID, 
               1 trip 
        FROM   VEHTRIPS 
               left join prms 
                      ON 1 = 1 
        WHERE  TIMELOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
               AND TIMEUNLOAD BETWEEN PRMS.SDATEFROM AND PRMS.SDATETO 
               AND SHOVID NOT LIKE '%Неопр.%' 
               AND ( TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП СКАЛА%' ) 
                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП ЩЕБЕНЬ%' ) 
                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ВКП%' ) 
                     AND TRIM(UPPER(WORKTYPE)) NOT LIKE ( '%ПСП%' ) 
                     AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%ВСП%' ) 
                     AND TRIM(UPPER (WORKTYPE)) NOT LIKE ( '%СНЕГ%' ) 
                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%АВТОДОРОГА%' ) 
                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ВНЕ ОТВАЛА%' ) 
                     AND TRIM(UPPER (UNLOADID)) NOT LIKE ( '%ДОРОГА ОБЩЕГО ПОЛЬЗОВАНИЯ%' ) )) 
GROUP  BY VEHID, 
          SHOVID 
ORDER  BY VEHID, 
          TRIPS DESC 
"""

    @staticmethod
    def query_get_shovels_volumes_by_hours() -> str:
        return """
    
    
    
    SELECT WORKTYPE, 
           SUM(VOLUME), 
           SUM(1) count 
    FROM   (SELECT TRIPCOUNTER, 
                   VEHID, 
                   SHOVID, 
                   UNLOADID, 
                   WORKTYPE, 
                   TO_CHAR(TIMELOAD, 'HH24')                                                                                  HOUR_LOAD,
                   TIMELOAD, 
                   TIMEUNLOAD, 
                   MOVETIME, 
                   WEIGHT, 
                   NVL(BUCKETCOUNT, -1)                                                                                       bucketcount,
                   AVSPEED, 
                   LENGTH, 
                   UNLOADLENGTH, 
                   LOADHEIGHT, 
                   UNLOADHEIGHT, 
                   ROUND(DECODE(NVL(vt.WEIGHT, 0), 0, 0, 
                                                   vt.WEIGHT * 1 / NVL(DECODE(vt.WRATE, 0, vt.WEIGHT,
                                                                                        vt.WRATE), vt.WEIGHT) * vt.VRATE), 3) AS Volume
            FROM   VEHTRIPS vt 
            WHERE  vt.TIMEUNLOAD BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE)) AND GETPREDEFINEDTIMETO('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE))
            ORDER  BY VEHID ASC, 
                      TIMELOAD ASC) 
    GROUP  BY WORKTYPE 
    ORDER  BY WORKTYPE ASC 
    
    
    
    """
