import React from "react";

export default function About() {
  return (
    <div className="about">
      <h2>About</h2>
      <p>
        This is a demo full-stack application build using the following
        technologies:
      </p>
      <ul>
        <li>
          Front-end
          <ul>
            <li>React</li>
          </ul>
        </li>
        <li>
          Backend
          <ul>
            <li>Python</li>
            <li>Flask</li>
            <li>MySQL</li>
          </ul>
        </li>
      </ul>
      <article>
        <h3>Challenge statement</h3>
        <p>
          Given the hassle Kenyans have every time they have to buy furniture
          items, they have to dedicate a day or two to going through the
          multiple furniture stores. In Kenya and most of Africa, it’s still an
          underdeveloped market where carpenters and manufacturers build items
          by the roadside, on public grounds, e.t.c., which in turn lowers the
          customers' shopping experience.
        </p>
      </article>
      <article>
        <h4>There are issues that The Online Store will not solve: </h4>
        <ul>
          <li>
            The Price of the furniture since each furniture will be sourced from
            different manufactures.
          </li>
          <li>
            Sell named brands such as Crate & Barrel, Ashley Furniture La-Z-Boy
            since we aim to partner with local manufactures and promote local
            talent.
          </li>
        </ul>
        <h4>Who's intended for ?</h4>
        <p>
          The online store is intended to assist customers who do not want to go
          through multiple stores across cities and towns in search of their
          ideal furniture. Also, it might also help manufactures by providing
          them with a platform after proper vetting.
        </p>
      </article>
    </div>
  );
}
