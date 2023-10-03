import * as navbars from "./navbar";
import * as footers from "./footer";

export function Base1({ children }: any) {
  return (
    <div>
      <navbars.Navbar1 />
      <main>{children}</main>
      <footers.Footer1 />
    </div>
  );
}
