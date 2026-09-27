-- Style only blockquotes explicitly headed "System".
-- Other blockquotes, such as the Product User Manual, stay ordinary quotes.

local function is_system(block)
  local first = block.content[1]
  return first and first.t == "Para" and pandoc.utils.stringify(first) == "System"
end

local function ornament(name)
  local script_dir = pandoc.path.directory(PANDOC_SCRIPT_FILE)
  local repo = pandoc.path.directory(script_dir)
  return pandoc.path.join({repo, "reader", "src", "ornaments", name})
end

function HorizontalRule()
  if not FORMAT:match("typst") then
    return nil
  end
  return pandoc.RawBlock("typst", string.format(
    '#align(center, block(above: 1.6em, below: 1.6em, image("%s", width: 1.35em)))',
    ornament("yin-yang.svg")
  ))
end

function BlockQuote(block)
  if not is_system(block) then
    return block
  end

  if FORMAT:match("typst") then
    local result = {
      pandoc.RawBlock("typst", string.format(
        '#murim-plaque("%s", "%s")[',
        ornament("corner.svg"),
        ornament("dragon.svg")
      )),
    }
    for index = 2, #block.content do
      table.insert(result, block.content[index])
    end
    table.insert(result, pandoc.RawBlock("typst", "]"))
    return result
  end

  -- Corner pieces plus a top crest. Kindle Oasis drops border-image and
  -- absolute positioning, so the frame is a table and the dragons and SYSTEM
  -- plate sit in the top edge instead of as a heading inside the panel.
  local function picture(name, width, height)
    return pandoc.Image(
      {},
      ornament(name),
      "",
      pandoc.Attr("", {}, {width = tostring(width), height = tostring(height)})
    )
  end

  local function cell(content, classes, colspan)
    local blocks = content.t and {content} or content
    return pandoc.Cell(
      blocks,
      pandoc.AlignCenter,
      1,
      colspan or 1,
      pandoc.Attr("", classes)
    )
  end

  local function plain(inlines, classes, colspan)
    return cell(pandoc.Plain(inlines), classes, colspan)
  end

  local function blank(classes)
    return plain({pandoc.RawInline("html", "&#160;")}, classes)
  end

  local cols = function(count)
    local specs = {}
    for _ = 1, count do
      specs[#specs + 1] = {pandoc.AlignDefault, 0}
    end
    return specs
  end

  local function grid(classes, col_count, rows)
    return pandoc.Table(
      {},
      cols(col_count),
      pandoc.TableHead(),
      {pandoc.TableBody(rows)},
      pandoc.TableFoot(),
      pandoc.Attr("", classes)
    )
  end

  -- Rails are the gold rules beside the title. The plate and dragons share
  -- one row so the label centers on the dragons instead of sitting on the baseline.
  local crest = grid({"system-head", "system-crest"}, 5, {
    pandoc.Row({
      plain({pandoc.RawInline("html", "<span class=\"system-bar\"></span>")}, {"system-rail"}),
      plain({picture("dragon.png", 40, 32)}, {"system-ornament"}),
      plain(
        {pandoc.Span(block.content[1].content, pandoc.Attr("", {"system-plaque"}))},
        {"system-badge"}
      ),
      plain({picture("dragon-flip.png", 40, 32)}, {"system-ornament"}),
      plain({pandoc.RawInline("html", "<span class=\"system-bar\"></span>")}, {"system-rail"}),
    }),
  })

  local body = {}
  for index = 2, #block.content do
    body[#body + 1] = block.content[index]
  end

  return grid({"system-window"}, 3, {
    pandoc.Row({
      plain({picture("corner-tl.png", 48, 48)}, {"system-corner"}),
      cell(crest, {"system-top"}),
      plain({picture("corner-tr.png", 48, 48)}, {"system-corner"}),
    }),
    pandoc.Row({
      blank({"system-edge", "system-edge-left"}),
      cell(body, {"system-body"}),
      blank({"system-edge", "system-edge-right"}),
    }),
    pandoc.Row({
      plain({picture("corner-bl.png", 48, 48)}, {"system-corner", "system-corner-bottom"}),
      blank({"system-base"}),
      plain({picture("corner-br.png", 48, 48)}, {"system-corner", "system-corner-bottom"}),
    }),
  })
end
