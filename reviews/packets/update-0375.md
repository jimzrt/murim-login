<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0375.txt",
      "sha256": "1d96babc0185becd710988c04518920d8460d80320b7eee0cfb4282dfda7e49d",
      "bytes": 13574
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d931b692576c1a8b595ab11d2f02826db3dd36adbfe1b0b11c1caeb9823a4a06",
      "bytes": 2622
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fdb0cabb1c583498429c1340c6c797d4a5a110e6996cbff6295af45542566af1",
      "bytes": 2473
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e91f2d81e52355253bfe9259006577aba3b8a2cc6e15316a542b0252b4e421aa",
      "bytes": 5010
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "a8e2c2f62f2bac24b525a2e60122ff7529c854f78e58a5348f1560dc5531f7cf",
      "bytes": 8064
    },
    {
      "path": "characters/Tang Horyong.md",
      "sha256": "8e236881e9b1d0fbaed303c1cd07f6529e447ab5577e7d94ba0d0b9f765885d9",
      "bytes": 562
    }
  ],
  "estimated_tokens": 10587
}
-->

# Durable State Update — Chapter 375

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 375. Keep at most
2 continuity_sources. Use only chapter
numbers through 375. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. Beat plot paragraphs are plain strings; continuity and translation
decisions are concise list items.

Return this exact shape:

{
  "chapter": 375,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 375,
    "continuity_sources": [375],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name or profile change is required.

## Prior durable context

```json
{
  "active_continuity": [
    "By the end of the source-only bridge, Jin Taekyung has reached the Supreme Peak realm and Level 120; exact current Fame, titles, martial-art stages, and unassigned points must be taken from the current Korean source rather than inferred across the skipped range.",
    "Jin Mukyung is Taekyung's second older brother, twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and substantially stronger than Taekyung.",
    "Dark Heaven rescued the former conspirators from the Demonic Cult, implanted gu in them, and its larger purpose and reason for sparing Taekyung remain unresolved.",
    "The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by the recent Dark Heaven attacks; Tang Sadok has awakened, and Tang Horyong remains acting Family Head.",
    "Slaughter Saint is concealing his identity as the young physician Mungyeong and intends to leave Murim after intervening in the recent crisis.",
    "A hidden, currently inactive transport formation associated with Dark Heaven was found near Sichuan; its origin and function remain unresolved.",
    "Jin Wikyung has proposed relocating the Sichuan Tang Clan and has been assigned to escort Samgoe toward Henan.",
    "Taekyung's return to his original world is imminent, with roughly six hours having passed there.",
    "The previously unnamed Inventory-bound item is the Myriad Poison Ring."
  ],
  "continuity_sources": [
    374
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved in the accepted local anchor.",
    "Dark Heaven's agents, purpose, and connection to the transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination remain unresolved.",
    "The outcome and timing of the planned Samgoe escort to Henan remain unresolved."
  ],
  "safe_through": 374,
  "temporary_decisions": [
    "This expedition deliberately skips accepted translation of Chapters 65–370.",
    "Chapters 371–373 are source-only bridge summaries and must not be treated as complete English continuity.",
    "When bridge context conflicts with the current Korean source, preserve the current source and record the uncertainty.",
    "Use Reformation Fist for 갱생권, grappling technique for 금나수, and retain hyung for 형 where the accepted anchor requires them.",
    "Render 반 시진 and 한 시진 as half a shichen and one shichen, with a footnote explaining that a shichen is a traditional two-hour period.",
    "Render 종형 as older cousin in this chapter's family context."
  ],
  "version": 1
}
```

## Expedition bridge dossier

# Expedition Seed Dossier

This dossier is intentionally conservative. It is supplied to the Chapter 374
expedition as orientation, not as a substitute for translating Chapters 65–373.
Only facts explicitly listed here may be treated as bridge context.

## Hard boundary

- Accepted English continuity is reliable through Chapter 64.
- Chapters 65–370 are skipped and have no accepted local English in this
  expedition.
- Chapters 371–373 are summarized from Korean source below. These summaries do
  not establish every event, name, or terminology choice in the skipped range.
- When the Korean source of the current chapter conflicts with this dossier,
  the current source wins. Do not invent missing backstory; preserve ambiguity
  and flag an unresolved continuity issue for later review.

## Chapter 371 — source bridge

Jin Taekyung is publicly hailed under the new epithet **Flame Divine Dragon**
(열화신룡) after reaching the Supreme Peak realm. Jeok Cheongang is privately
proud of Taekyung's growth despite pretending to be annoyed by the celebration.
The Qingcheng Sect Leader Cheongpung Gogeom and the Emei Sect Leader
Myeoljeol Sini arrive and ask Taekyung and Jeok Cheongang to accompany them.
They explain that questioning Samgoe revealed a strange formation connected to
Dark Heaven. Taekyung agrees to investigate. On the way, he encounters the
physician Mungyeong, whom he still treats as the same cheerful young healer.
The chapter ends as Taekyung discovers that Mungyeong is actually the legendary
assassin Slaughter Saint (살성), and that he has just addressed him with an
embarrassingly familiar joke.

## Chapter 372 — source bridge

The group reaches a hidden cave concealed by a **phantom formation**
(환영진). The cave is large enough to house roughly a thousand people and
contains supplies, weapons, and an enormous patterned formation. The sect
leaders identify it as a possible ** 이동진** (a formation that transports
people across great distances), based on Samgoe's testimony. Taekyung's
Integrated Language Pack does not interpret the patterns as writing, so he
suspects they are not a language. The formation appears inactive and devoid of
qi; Samgoe reportedly tried to use it to escape but failed. Slaughter Saint
says the evidence points to Dark Heaven being a successor of the Demonic Cult.
Taekyung studies the formation and suspects it may be something he recognizes,
but has not yet explained why.

## Chapter 373 — source bridge

On the return to Sichuan Tang Clan territory, Slaughter Saint says he intends
to abandon his assassin identity and return to living as the young physician
Mungyeong. He says he is sick of Murim and once swore never to kill again.
Taekyung realizes that Slaughter Saint deliberately chose to intervene in the
recent crisis, but sincerely thanks him for preventing many deaths. Slaughter
Saint permits Taekyung to call him Mungyeong and warns that only the people who
were present know his identity. Taekyung returns to his residence, reads a
large backlog of System messages, reaches Level 120, and learns that a new
unnamed item has become bound to him alongside Baekyeom and can be summoned
through his Inventory in either world. Hyuk Mujin announces that an
investigative party from Henan has arrived.

## Chapter 374 opening position

Chapter 374 opens at the Sichuan Tang Clan's Poison Dragon Pavilion. Tang
Horyong, acting head of the clan while Tang Sadok remains unconscious, receives
Jin Wikyung. The Sichuan Tang Clan has suffered catastrophic losses in the
recent attack. Jin Wikyung proposes that the clan relocate and says orthodox
Murim will help it establish a new base; Shanxi is offered as one possible
location. He has also come to escort Samgoe back toward Henan. Jin Taekyung
will reunite with Jin Wikyung and continue that journey.

## Translation guardrails

- Treat the Korean source as authoritative for every line of Chapter 374 and
  later chapters.
- Do not back-project titles, names, ranks, or skills from web searches into
  the skipped range without current-source evidence.
- Use established local terminology where it exists: **Dark Heaven**, **Demonic
  Cult**, **Slaughter Saint**, **One Flash**, **Peak**, **Supreme Peak**, and
  **Internal Energy**.
- For new terms such as 열화신룡, 독룡각, 당호룡, 삼괴, and 이동진, follow the
  ledger and first-use rules. If no binding English exists, choose a faithful
  rendering, record it through the normal update stage, and do not pretend it
  was established in Chapters 65–373.
- The light, self-mocking first-person voice and the source's jokes remain
  important, but missing continuity must never be filled by invented exposition.

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 독룡각 | **Poison Dragon Pavilion** | Pavilion led by Tang Horyong |
| 당호룡 | **Tang Horyong** | Acting Family Head of the Sichuan Tang Clan |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 경천신니 | **Heaven-Shaking Divine Nun** | Murder victim named alongside Tang Sadok |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 구파일방 | **Nine Sects and One Gang** | Major orthodox organizations |
| 오대세가 | **Five Great Families** | Major orthodox families |
| 소림혈사 | **Shaolin Bloodbath** | Earlier attack that galvanized orthodox Murim |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 만독지환 | **Myriad Poison Ring** | Item Taekyung considers taking before departure |

## Exact glossary matches

| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 아이템              | **Item**                       |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 당호룡 | **Tang Horyong** | Acting Family Head of the Sichuan Tang Clan |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 만독지환 | **Myriad Poison Ring** | Item Taekyung considers taking before departure |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 63
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 374
- **Aliases:** None revealed
- **Role:** Thirty-five-year-old Lesser Family Head of the Jin Family of Taiyuan
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Tang Horyong.md

# Tang Horyong (당호룡)

- **Safe through:** Chapter 374
- **Aliases:** None
- **Role:** Pavilion Master of the Poison Dragon Pavilion and acting Family Head of the Sichuan Tang Clan
- **Personality:** Responsible and candid; burdened and anxious about leading the devastated clan without Tang Sadok
- **Voice:** Polite and formal, with frank expressions of concern
- **Relationships:** Tang Sadok's younger cousin and acting successor; receives Jin Wikyung's offer of support and relocation

## Korean source

```text
＃375화



병문안에도 순서가 있는 법.

가주이자 가문의 웃어른인 당사독이 깨어났다는 소식에, 당문의 식솔들은 만사를 제치고 달려왔다.

그러나 백여 명이나 되는 인원 모두가 당사독을 볼 수 있는 것은 아니었다.

“은인, 우린 언제쯤 당 할아버지를 뵐 수 있어요?”

“글쎄. 앞에 사람들이 들어간 지 꽤 됐으니까 슬슬 나오지 않을까.”

“아, 그렇구나.”

내 대답에 청풍이 고개를 끄덕인다.

아니, 잠깐만. 청풍?

“뭐야, 언제 왔어?”

“방금요.”

너무 자연스럽게 끼어들어서 있는 줄도 몰랐다. 그런데 이놈이 여길 왜 찾아왔지?

내 의문을 읽기라도 한 것처럼 청풍이 자신의 가슴팍을 가리키며 대답했다.

“미미가 보고 싶다고 해서요.”

“……?”

내가 지금 도대체 뭘 들은 거지.

이제는 하다 하다 의사소통까지 하다니. 이 자식 혹시 화산파가 아니라 슬리데린 출신인가.

심상치 않은 내 시선에 청풍이 고개를 갸웃했다.

“제 이마는 갑자기 왜 쳐다보세요? 뭐 묻었어요?”

“그냥. 이마에 번개 모양 흉터라도 있나 확인해 봤어.”

“네?”

“그런 게 있다.”

말이 끝난 그 순간.

덜컥.

굳게 닫혀 있던 의방의 문이 열리고 십여 명의 사람들이 모습을 드러냈다.

그들은 몇 남지 않은 사천당문의 직계들로, 그중에는 일면식이 있는 당호룡 역시 포함되어 있었다.

“후우…….”

붉게 충혈된 눈으로 하늘을 올려다본 그가 이쪽을 향해 걸어왔다.

“가주께서 뵙고자 하시오.”

“기다리고 있었습니다.”

고개를 끄덕인 진위경이 앞장서고, 나와 청풍이 그 뒤를 따라 의방으로 들어갔다.

사방에서 진동하는 탕약 냄새를 맡으며 얼마나 걸었을까. 하얀 천으로 코와 입을 가린 의원이 안내해 준 의실로 들어서자, 마침내 낯익은 얼굴들과 마주할 수 있었다.

“쿨럭, 왔는가.”

힘겹게 잔기침을 내뱉는 당사독의 상태는 한눈에 보기에도 심각했다.

부러진 팔다리와 내상으로 인해 불안정한 기운.

상반신을 일으키려는 그를, 우리와 눈인사를 주고받은 신의(神醫)가 만류했다.

“가주, 제가 움직이지 말라 하지 않았습니까.”

“노부는 죄인일세. 죽어 마땅한 죄를 지었으니 벌을 청하는 것이 이치지.”

창백한 얼굴로 고개를 저은 당사독이 나를 똑바로 응시하며 말을 이었다.

“구차한 변명은 하지 않겠네. 서천마군이 지하 뇌옥으로 향한 것은, 노부가 알려 주었기 때문일세.”

나는 비스듬히 팔짱을 꼈다.

“아, 어쩐지.”

“……?”

“왜요.”

당사독이 당황한 얼굴로 물었다.

“아, 알고 있었나?”

“당연히 처음에는 몰랐죠. 그때는 워낙 정신이 없기도 했고. 그런데 나중에 곰곰이 생각해 보니까 서천마군. 그 새끼가 어떻게 만독지환의 위치를 알았나 싶더라고요.”

애당초 만독지환의 위치를 아는 사람은 극소수.

청풍은 겉보기에는 꽃잎처럼 가벼워 보여도 나무뿌리처럼 단단한 놈이니, 발설할 만한 사람은 당사독 한 명밖에 없었다.

“왜 그랬습니까?”

“……만독지환의 위치를 알려 주면 가문의 명맥을 보존해 주겠다 하더군.”

“그걸 믿었어요?”

“노부가 어리석었네. 잠시 판단력이 흐려져, 해서는 안 될 일을 저질렀지.”

“알고는 계시네요.”

나를 바라보는 당사독의 눈빛이 파르르 떨렸다.

“이 늙은이가 목숨을 건사할 수 있었던 것은, 자네들에게 사죄하고 벌을 받으라는 하늘의 뜻이겠지.”

“그럼 가주께서는 어떤 벌을 원하십니까.”

불쑥 들려온 차가운 목소리의 주인은 아무 말 없이 대화를 듣고 있던 진위경이었다.

“태원진가의 소가주 되시는가.”

“예. 두 아우를 자식처럼 키운 형이기도 하지요.”

깊게 가라앉은 진위경의 눈동자에서 숨길 수 없는 분노가 진득하게 묻어나왔다.

“정도(正道)를 걷는 이라면 해서는 안 될 짓이었습니다.”

“알고 있네. 아니, 알고 있소. 그렇기에 죄를 청하는 것이오.”

“자결하라 한다면 어쩌시겠습니까.”

“……!”

나를 포함한 모두가 놀란 눈빛으로 진위경을 바라봤다.

그러나 한 사람, 당사독만은 예외였다.

그는 담담하기 그지없는 표정으로 입을 열었다.

“나는 도의(道義)를 저버렸으나, 그대들이 목숨을 내놓고 싸워 준 덕분에 본가의 명맥을 이을 수 있게 되었소. 이 보잘것없는 늙은이의 목숨으로 사죄를 대신할 수 있다면, 흔쾌히 그리하리다.”

짧은 침묵 뒤에 이어진 것은 진위경의 한숨이었다.

“후우…….”

복잡한 눈빛으로 당사독을 바라보던 그가 나를 향해 고개를 돌렸다.

“어찌하겠느냐?”

“……뭘요. 자결?”

“그 무엇이든.”

갑자기 손에 칼자루가 쥐어지니 심장이 쫀득해지는 기분이다.

더군다나 그 칼자루 끝에 달린 것이 사천당문 가주의 목숨이라고 하니 더더욱 그랬다.

‘갑자기 분위기 싸해진 것 보소.’

물론 허허 웃고 넘어갈 일은 아니다. 내가 무슨 공명정대하고 속 넓은 인의대협도 아니고, 솔직히 사건의 전말을 깨달았을 때는 슬그머니 분노가 솟구치기도 했다.

당시에는 나뿐만 아니라 모두의 목숨이 걸려 있는 상황이었으니까.

하지만…….

“됐습니다. 그렇게까지 하고 싶지는 않네요.”

그래, 한편으로는 당사독의 입장을 이해한다.

얼굴 몇 번 본 것이 고작인 외부인과 일가의 가주로서 목숨 걸고 지켜야 할 혈육을 저울에 올려 둔다면 나 역시 그와 같은 선택을 했을 것 같았다.

‘그전에 빚도 있었고.’

적천강이 깨어날 수 있었던 것에는 당사독의 도움도 크게 한몫했다.

비록 모종의 거래가 있었다고는 하나, 한 핏줄에게도 알리지 않은 신물을 빌려준 사람 역시 당사독이었다.

“그러니까 이걸로 쌤쌤. 퉁 치죠. 아니, 그건 너무 나갔고 이번 일로 사천당문이 저희에게 큰 빚을 진 것으로 하자고요.”

내 말이 끝나자 청풍과 신의가 입을 열었다.

“은인이 위험해졌던 건 분명히 당 할아버지의 잘못이지만…… 저도 은인의 뜻에 따를래요.”

“전 이미 잊었습니다. 다만 의원으로서 바라는 것이 있다면 가주께서 하루빨리 쾌차하는 것이지요. 아직 살아남은 식솔들이 있지 않습니다.”

마지막으로 입을 연 것은 진위경이었다. 처음과 달리 그에게서는 더 이상 어떤 분노도 느껴지지 않았다.

아니, 어쩌면 진위경은 처음부터 내 대답을 알고 있었을지도 모르겠다.

“그렇다는군요. 가주의 생각은 어떠하십니까.”

“……!”

우리를 바라보는 당사독의 눈동자가 격동으로 떨렸다.

짧은 침묵이 흐른 뒤, 갈라진 목소리가 그의 입술 사이로 흘러나왔다.

“노부가, 사천당문이 그대들에게 큰 은혜를 입었구려.”

당사독이 진심을 담아 고개를 숙인 바로 그 순간이었다.

띠링. 띠링. 띠링.



- 자신의 죄를 고백하는 것은 어렵지만, 그보다 더 큰 용기를 필요로 하는 것이 있습니다. 바로 용서입니다.

- 히든 퀘스트, [사죄와 용서]를 성공적으로 완료했습니다!

- [Lv.115 당사독]이 당신들의 호의에 깊은 감사를 표합니다. 그와 [사천당문]은 결코 오늘의 호의와 도움을 잊지 않을 것이며, [사천당문]의 사람들은 당신을 은인으로 기억할 것입니다!

- 칭호, [당문의 은인]을 획득했습니다!

- 히든 퀘스트 완료 보상으로 막대한 경험치와 명성을 얻었습니다!

- 레벨 업!



뭐야, 이거. 갑자기 히든 퀘스트라니.

내가 뜬금없이 울려 퍼진 시스템 알림에 얼떨떨해하던 그때, 차가운 무언가가 다리 사이를 스치며 지나갔다.

취릭, 취리리릭.

“미미, 이 녀석.”

오랜만에 해후하는 미미와 당사독의 모습에, 잠시 깜빡하고 있던 물건 하나가 떠올랐다.

“아, 그러고 보니 만독지환 말인데요. 다행히 제가 지금까지 잘 갖고 있었…….”

“그런가?”

내가 미처 말을 끝맺기도 전에, 불쑥 입을 연 당사독이 말을 이었다.

“그럼 계속 갖고 있으시게.”

“예, 그럼 제가 계속…… 예?”

“자네에게 본가의 신물을 맡기겠네. 은인에 대한 증표이니 부디 거절하지 말아 주게.”

띠링.



- 소유자의 뜻에 따라 [만독지환]이 당신에게 양도되었습니다!

- 새로운 아이템이 당신에게 종속됩니다!

- 현재 보유 중인 종속 아이템 : [백염], [만독지환], [???].

- 아직 이름이 정해지지 않은 종속 아이템이 있습니다. 새로운 이름을 부여해 주십시오.



아니, 오늘 무슨 날이야?

도대체 앞으로 어떤 개 같은 일들이 벌어지려고 이렇게 퍼 주나 싶어 불안하기까지 할 지경이다.

금붕어처럼 입만 벙긋거리는 내 모습에, 당사독이 희미한 미소를 머금었다.

“다들 원하는 것들이 있다면 말씀하시구려. 본가의 역량이 닿는 한 무엇이든 들어드리리다.”

신의가 따라 웃으며 대답했다.

“원하는 것이라면, 그저 병자들이 하루빨리 낫길 바랄 뿐입니다.”

“허어.”

과연 신의다운 대답이다. 아니, 이제는 동봉이라고 해야 하나.

하지만 한 가지 확실한 것은, 그 역시 또 다른 한 사람의 신의(神醫)라는 사실이었다.

“자네는 무엇을 원하는가?”

갑작스러운 질문에 청풍이 화들짝 놀랐다.

“저, 저요?”

당사독이 고개를 끄덕이자 청풍이 손발을 배배 꼬며 대답했다.

“저어는…… 그러니까요. 으음. 없어요.”

“정말인가?”

“네에. 없는 것 같아요.”

“…….”

“…….”

야, 이 자식아. 미미쨩한테서 눈이나 떼고 얘기해.

거울을 가져와서 보여 주고 싶다. 지금 청풍의 눈동자에는 미미쨩을 향한 애절함과 갈망이 떠올라 있었다.

저러다가 뱀 가죽이 뚫리겠다 싶던 그때, 당사독이 입을 열었다.

“이 녀석은 내 오랜 친우일세. 지난 수십 년 동안, 노부가 아무에게도 드러내지 못했던 희로애락(喜怒哀樂)을 나눌 수 있었던 유일한 존재였지.”

청풍이 측은해진 눈빛으로 당사독을 바라봤다.

“당 할아버지께서는 다른 친구가 없으시군요.”

“만들지 않았다네. 노부에게 당문의 가주란 그런 자리였으니까.”

“그래서 친구가 없으시군요.”

“없던 게 아니라. 만들 수 있었는데…….”

“친구 하나 없었군요. 불쌍해라.”

“…….”

신의가 다급하게 당사독의 어깨를 붙잡았다.

“가주. 진정하십시오. 호흡이 너무 가파릅니다!”

“후욱, 후우욱.”

“크고 천천히 호흡하십시오. 자, 저를 따라서 하나, 둘…….”

“후우우우욱…….”

잠시 후, 간신히 고혈압의 위기에서 벗어난 당사독이 청풍을 바라보며 입을 열었다.

“하지만 자네에게 미미를…….”

청풍이 두 손으로 입을 틀어막았다.

“아니에요. 당 할아버지. 할아버지의 유일한 친구를 데려갈 수는 없어요.”

“……아직 맡기겠다고 하지 않았는데.”

“앗. 아앗.”

당사독이 한숨을 푹 내쉬었다. 잠깐이었지만 저런 놈한테 미미쨩을 맡겨도 되나, 하는 생각을 했음이 틀림없었다.

“그래, 자네의 짐작대로일세. 향후 본가의 향방이 어떻게 될지 모르는바, 노부는 자네에게 미미를 맡기고자 하네. 물론 임시로.”

“와아!”

“마지막에 했던 말 들었나? 임시일세.”

“와아아!”

못 들었다에 혁무진 오른손 손목을 건다.

미미의 임시보호자가 된 청풍은 기뻐서 어쩔 줄을 몰라 했다.

“걱정 마세요. 잘 돌볼게요!”

“지난번에 본 바에 의하면 미미가 자네를 잘 따르는 것 같긴 하지만, 녀석은 본래 성정이 까다롭고 낯을 많이 가리니…….”

“미미. 회오리치기 후 뱅글뱅글 돌고 인사하기!”

취리리릭!

“오메, 시벌.”

여기서 신기술을 써 버리네.

생전 처음 보는 광경에 반쯤 넋이 나가 있던 진위경이 얼빠진 목소리로 중얼거렸다.

“가주께서 걱정하시는 일은 없을 것 같군요.”

당사독의 눈동자에 지진이 일어났다.

당사독은 진위경과 긴히 나눌 말이 있다며 따로 자리를 청했고, 나와 청풍은 먼저 방을 빠져나왔다.

아니, 지금 막 한 사람이 추가되었다.

“진 소협. 잠시 이 늙은이에게 시간을 내어줄 수 있겠소?”

“저요?”

신의가 잔잔한 웃음과 함께 고개를 끄덕였다.

“떠나기 전에 꼭 부탁하고 싶은 것이 있소.”
```

## Final English reading copy

```markdown
# Chapter 375

Even hospital visits had a proper order.

When word spread that Tang Sadok—the Family Head and elder of the clan—had awakened, the members of the Tang household dropped everything and came running.

However, not all of the more than one hundred people could see Tang Sadok.

“Benefactor, when can we see Grandpa Tang?”

“I don’t know. It’s been quite a while since the people in front of us went in, so they should be coming out soon.”

“Oh, I see.”

Cheongpung nodded at my answer.

Wait. Cheongpung?

“What are you doing here? When did you get here?”

“Just now.”

He had joined the conversation so naturally that I hadn’t even noticed he was there. But why had this guy come here?

As though he had read my thoughts, Cheongpung pointed to his chest and answered.

“Because Mimi said she wanted to visit.”

“……?”

*What did I just hear?*

Now Mimi was communicating with him, too. Was this bastard from Slytherin instead of Huashan?

At my suspicious gaze, Cheongpung tilted his head.

“Why are you suddenly staring at my forehead? Is there something on it?”

“I was just checking whether you had a lightning-shaped scar on your forehead.”

“What?”

“Never mind.”

The moment the words left my mouth—

Clunk.

The tightly closed door of the medical ward opened, and more than ten people emerged.

They were among the few remaining direct-line members of the Sichuan Tang Clan. Tang Horyong was among them, and I had met him before.

“Hoo……”

After looking up at the sky with bloodshot eyes, he walked toward us.

“The Family Head wishes to see you.”

“We’ve been waiting.”

Jin Wikyung nodded and led the way. Cheongpung and I followed him into the medical ward.

Who knew how long we walked through the pervasive smell of medicinal decoctions? At last, the physician whose nose and mouth were covered with white cloth led us into a treatment room, where we came face-to-face with several familiar faces.

“Cough, cough. You’ve come.”

Tang Sadok’s condition was visibly serious. His limbs were broken, and his internal injuries had left his qi unstable.

As he tried to raise his upper body, the Divine Physician who had exchanged a nod with us stopped him.

“Family Head, didn’t I tell you not to move?”

“This old man is a sinner. I committed a crime deserving of death, so it is only right that I ask for punishment.”

Pale-faced, Tang Sadok shook his head, stared straight at me, and continued.

“I will not make any pathetic excuses. The reason the Western Heaven Demon Lord headed for the underground prison was because I told him about it.”

I folded my arms at an angle.

“Ah. That explains it.”

“……?”

“Why are you looking at me like that?”

“Ah, you knew?”

“Of course I didn’t know at first. There was too much going on at the time. But later, when I thought about it carefully, I started wondering how that bastard, the Western Heaven Demon Lord, had known the location of the Myriad Poison Ring.”

Only a handful of people knew where the Myriad Poison Ring was in the first place.

Cheongpung might look as light as a flower petal, but he was as sturdy as a tree root. That left Tang Sadok as the only person who could have revealed it.

“Why did you do it?”

“He said that if I revealed the location of the Myriad Poison Ring, he would preserve the family line.”

“And you believed him?”

“This old man was foolish. My judgment was clouded for a moment, and I committed an act I should never have committed.”

“At least you know that.”

Tang Sadok’s eyes trembled as he looked at me.

“The reason this old man was able to keep his life is surely heaven’s will. I must apologize to you all and accept my punishment.”

“What punishment do you want, then?”

The owner of the cold voice was Jin Wikyung, who had been listening to the conversation in silence.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

“Yes. I am also an older brother who raised my two younger brothers as though they were my own children.”

Unconcealed anger clung heavily to Jin Wikyung’s deeply sunken eyes.

“It was something no one walking the righteous path should have done.”

“I know. No—I understand. That is why I ask to be punished.”

“What will you do if I tell you to take your own life?”

“……!”

Everyone, myself included, looked at Jin Wikyung in surprise.

Everyone except Tang Sadok.

He opened his mouth with an expression of utter calm.

“I abandoned righteousness, but thanks to the fact that all of you fought while putting your lives on the line, my family will be able to continue. If this insignificant old man’s life can serve as an apology, I will gladly give it.”

After a brief silence, Jin Wikyung sighed.

“Hoo……”

He stared at Tang Sadok with complicated emotions before turning to me.

“What will you do?”

“……About what? His suicide?”

“Whatever you wish.”

Having the hilt of a knife suddenly thrust into my hand made my heart feel strangely taut.

Even more so when I was told that the life attached to the end of that hilt was the life of the Family Head of the Sichuan Tang Clan.

*Look at how suddenly the mood turned cold.*

Of course, this wasn’t something to laugh off. I wasn’t some impartial, broad-minded Great Hero. To be honest, when I realized the whole truth of what had happened, a quiet anger had risen inside me.

After all, everyone’s lives had been on the line at the time—not just mine.

But……

“That’s enough. I don’t want to take things that far.”

That was right. On the other hand, I could understand Tang Sadok’s position.

If, as the head of a family, I had to weigh blood relatives I was duty-bound to protect with my life against outsiders I’d met only a few times, I probably would’ve made the same choice.

*I had a debt to him, too.*

Tang Sadok’s help had played a major role in Jeok Cheongang’s recovery.

There may have been a transaction involved, but Tang Sadok had still lent us a sacred artifact without even telling his own blood relatives.

“So let’s call it even. We’ll let it slide. No, that’s going too far—let’s say the Sichuan Tang Clan owes us a huge debt over this.”

When I finished speaking, Cheongpung and the Divine Physician spoke up.

“It was definitely Grandpa Tang’s fault that the Benefactor was put in danger, but… I’ll follow the Benefactor’s wishes, too.”

“I’ve already forgotten about it. But if there is one thing I wish for as a physician, it is that the Family Head recovers as soon as possible. There are still surviving members of the household, after all.”

The last person to speak was Jin Wikyung. Unlike before, there was no anger to be felt from him anymore.

No—perhaps Jin Wikyung had known my answer from the very beginning.

“So that is their decision. What do you think, Family Head?”

“……!”

Tang Sadok’s eyes trembled with emotion as he looked at us.

After a short silence, a hoarse voice slipped between his lips.

“This old man—and the Sichuan Tang Clan—have received a great kindness from you.”

The instant Tang Sadok bowed his head with genuine sincerity—

> **System**
>
> Confessing one's sins is difficult, but there is something that requires even greater courage. That is forgiveness.
>
> **Hidden Quest:** **Atonement and Forgiveness** successfully completed!
>
> **Level 115 Tang Sadok** expresses his deep gratitude for your kindness. He and the **Sichuan Tang Clan** will never forget the favor and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their **Benefactor**!
>
> **Title Acquired:** **Benefactor of the Tang Clan**
>
> You have gained a tremendous amount of EXP and Fame as a reward for completing the Hidden Quest!
>
> **Level Up!**

*What was this? A Hidden Quest, all of a sudden?*

As I stood there dumbfounded by the System notification that had suddenly rung out, something cold brushed between my legs.

Ssssk. Ssssss.

“Mimi, you little……”

At the sight of Mimi and Tang Sadok reunited after so long, I remembered something I had momentarily forgotten.

“Ah, now that I think about it, the Myriad Poison Ring. Thankfully, I’ve been keeping it safe all this time……”

“Is that so?”

Before I could finish speaking, Tang Sadok interrupted.

“Then continue to keep it.”

“Yes, then I’ll keep—what?”

“I am entrusting the sacred artifact of our family to you. It is a token of our gratitude to our Benefactor, so please do not refuse.”

> **System**
>
> According to the owner's wishes, **Myriad Poison Ring** has been transferred to you!
>
> A new item is now bound to you!
>
> **Currently bound items:** **White Flame**, **Myriad Poison Ring**, **???**
>
> You have a bound item that has not yet been named. Please give it a new name.

*What kind of day was today?*

I was getting downright nervous, wondering what kind of shitty things were about to happen for them to be giving so much away like this.

At the sight of me opening and closing my mouth like a goldfish, Tang Sadok smiled faintly.

“If any of you have something you want, speak up. I will grant you anything within the limits of our family’s abilities.”

The Divine Physician smiled along with him and answered.

“If there is something I want, it is simply for the patients to recover as soon as possible.”

“Good heavens.”

That was certainly an answer worthy of the Divine Physician. No, should I be calling him Dongbong now?

But one thing was certain: he, too, was another Divine Physician.

“What do you want?”

Cheongpung jumped at the sudden question.

“M-Me?”

Tang Sadok nodded, and Cheongpung answered while fidgeting with his hands and feet.

“Well, I…… Let me think. Um. Nothing.”

“Are you sure?”

“Yeees. I don’t think there’s anything.”

“……”

“……”

*Hey, you idiot. Take your eyes off Mimi-chan and talk.*

I wanted to bring him a mirror and show him his face. Cheongpung’s eyes were filled with aching longing and desire for Mimi-chan.

*At this rate, he’s going to stare a hole through the snake’s hide.*

Just then, Tang Sadok spoke.

“This creature is an old friend of mine. For the past several decades, it has been the only one with whom this old man could share the joys and sorrows he could reveal to no one else.”

Cheongpung looked at Tang Sadok with pity.

“So you don’t have any other friends, Grandpa Tang.”

“I never made any. Being the Family Head of the Tang Clan was that kind of position.”

“So you have no friends.”

“It wasn’t that I had none. I could have made them, but……”

“You didn’t have a single friend. How pitiful.”

“……”

The Divine Physician hurriedly grabbed Tang Sadok by the shoulders.

“Family Head, please calm down. Your breathing is too rapid!”

“Huuk, hoo-oo.”

“Take deep, slow breaths. Come on, follow me. One, two……”

“Huooooo……”

A little while later, Tang Sadok barely managed to escape a hypertensive crisis before opening his mouth again.

“But I could entrust Mimi to you……”

Cheongpung covered his mouth with both hands.

“No, Grandpa Tang. I can’t take away your only friend.”

“……I haven’t even said I was going to entrust her to you yet.”

“Oh. Oh!”

Tang Sadok let out a deep sigh. It had only been for a moment, but he had undoubtedly wondered whether he could entrust Mimi-chan to someone like that.

“Yes, just as you guessed. Since we do not know what path our family will take from here on, I wish to entrust Mimi to you. Temporarily, of course.”

“Yaaay!”

“Did you hear what I said at the end? Temporarily.”

“Yaaay!”

*I’ll bet Hyuk Mujin’s right wrist that he didn’t hear that.*

Cheongpung, now Mimi’s temporary guardian, didn’t know what to do with his happiness.

“Don’t worry. I’ll take good care of her!”

“From what I saw last time, Mimi does seem to like you, but she has a rather difficult temperament and is very wary of strangers, so……”

“Mimi. Do Whirlwind, then spin round and round and say hello!”

Sssriririk!

“Oh, for fuck’s sake.”

*He’s using a new trick here.*

Jin Wikyung had been half out of his mind at the sight he was seeing for the first time in his life. He muttered in a dazed voice.

“It seems you have nothing to worry about, Family Head.”

An earthquake struck Tang Sadok’s eyes.

Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first.

No, one person had just been added.

“Young Hero Jin. Could you spare this old man a little of your time?”

“Me?”

The Divine Physician nodded with a gentle smile.

“There is something I would like to ask you before you leave.”
```
