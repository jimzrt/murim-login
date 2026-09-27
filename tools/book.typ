// Literary PDF chrome matching the Astro reader (paper, ink, gold, navy).
#let murim-paper = rgb("#f3ead4")
#let murim-ink = rgb("#1a2744")
#let murim-muted = rgb("#6a624e")
#let murim-gold = rgb("#e6c86a")
#let murim-gold-deep = rgb("#d4af37")
#let murim-navy = rgb("#1c4a82")
#let murim-cap = 11pt
#let murim-arm = murim-cap * 13.6 / 56
#let murim-body-size = 11.5pt

#let murim-plaque(corner, dragon, body) = {
  set text(font: ("Noto Sans", "Noto Sans Mono"), size: murim-body-size, fill: rgb("#ffffff"), weight: "bold")
  set par(leading: 0.68em, spacing: 0.7em)
  show strong: set text(fill: rgb("#ffe7a8"), weight: "bold")
  set list(marker: [#box(width: 1.15pt, height: 0.72em, fill: murim-gold, baseline: 12%)])
  set enum(numbering: "1.")
  show list: it => align(left, block(inset: (x: 6pt), it))
  show enum: it => align(left, block(inset: (x: 6pt), it))

  let plaque-label = box(
    height: 15pt,
    fill: rgb("#3a78b8"),
    stroke: 1.05pt + murim-gold,
    inset: (x: 8pt, y: 0pt),
  )[
    #align(horizon)[#text(size: 7.5pt, tracking: 1.6pt, weight: "bold")[SYSTEM]]
  ]
  // Dragons sit outside the plate, and the whole crest is centered on the
  // top stroke so it reads as part of the frame rather than a heading.
  let banner = grid(
    columns: 3,
    column-gutter: 1.5pt,
    align: horizon,
    image(dragon, height: 15pt),
    plaque-label,
    scale(x: -100%)[#image(dragon, height: 15pt)],
  )

  let piece(flip-x: false, flip-y: false) = {
    let img = image(corner, width: murim-cap, height: murim-cap)
    let flipped = if flip-x and flip-y {
      scale(x: -100%, y: -100%, origin: center, img)
    } else if flip-x {
      scale(x: -100%, origin: center, img)
    } else if flip-y {
      scale(y: -100%, origin: center, img)
    } else {
      img
    }
    box(width: murim-cap, height: murim-cap, clip: false, flipped)
  }

  v(1.85em, weak: true)
  pad(x: 8%, box(width: 100%, clip: false)[
    #block(
      width: 100%,
      breakable: false,
      fill: gradient.linear(rgb("#4a90d0"), rgb("#3a78b8"), rgb("#2d6aad"), angle: 180deg),
      stroke: murim-arm + murim-gold,
      inset: (x: 1.15em, top: 12pt, bottom: 1.05em),
    )[
      #set align(center + top)
      #line(length: 100%, stroke: 1.75pt + murim-gold)
      #v(0.55em)
      #body
    ]
    #place(top + left)[#piece()]
    #place(top + right)[#piece(flip-x: true)]
    #place(bottom + left)[#piece(flip-y: true)]
    #place(bottom + right)[#piece(flip-x: true, flip-y: true)]
    #place(top + center, dy: -7.5pt)[#banner]
  ])
  v(1.55em, weak: true)
}

#set document(title: "Murim Login")
#set page(
  paper: "a4",
  fill: murim-paper,
  margin: (left: 26mm, right: 24mm, top: 26mm, bottom: 24mm),
  header: context {
    set text(size: 8pt, fill: murim-muted, font: "Noto Serif")
    grid(
      columns: (1fr, auto),
      [Murim Login],
      counter(page).display("1"),
    )
    v(0.35em)
    line(length: 100%, stroke: 0.6pt + murim-gold-deep)
  },
  footer: none,
)
#counter(page).update(1)
#set text(size: murim-body-size, fill: murim-ink, font: "Noto Serif")
#set par(leading: 0.74em, spacing: 0.92em)
#set heading(numbering: none)

#show heading.where(level: 1): it => {
  if it.outlined {
    pagebreak(weak: true)
  }
  set align(center)
  set text(fill: murim-navy, size: 1.38em, weight: "bold")
  block(below: 1.15em, it)
}

#show outline: it => {
  it
  pagebreak()
}

#show outline.entry: it => {
  block(above: 0.45em, below: 0.05em, {
    set text(size: murim-body-size, fill: murim-ink)
    it
  })
}

#show quote: it => block(
  width: 100%,
  stroke: (left: 2pt + rgb("#e2d4b0")),
  inset: (left: 12pt, y: 4pt),
  fill: none,
  {
    set text(fill: rgb("#3e4854"))
    it
  },
)

#show strong: set text(fill: murim-navy)
#show emph: it => text(style: "italic", it.body)
#show link: set text(fill: rgb("#9a7420"))
#show footnote.entry: set text(size: 9pt, fill: murim-muted)
