<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0648.txt",
      "sha256": "6314b76b25b04a0636448b10ba5720e571a005fc1f36d8d1af0276fcd60f8c72",
      "bytes": 12720
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e4fa051052fab1c68d9e0694cf60c91391fba796860287e988b0b75d1266dbfe",
      "bytes": 2490
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c60d77664c271582e2323ff18e216f423a3d9b066bfd2d0518707c75257990ed",
      "bytes": 199345
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "87887ec9e914d02b39615280027a6b23b1b5de2d7e86a8c79bda41c89ae4fb7d",
      "bytes": 865
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "cb6f00e332da9d18b60e5dfec0f3c1504967ec0b344dee81eb409761d08f30b9",
      "bytes": 707
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1b873e8ada990f07fd7485f0a7b96aa5a50a01e05362f116b72876531fc3501d",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "fcf9c08f4564b6270e511ae411b0d36566bfd1116f6284a4a7abd418dbcb2145",
      "bytes": 623
    },
    {
      "path": "characters/Namho.md",
      "sha256": "5766a353d2b7896ac948755100dae15e97c596600ef1cf78c9368e14428bb65d",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "a99019fe3c187893f8c78b92a0d18e43c40b1f2d38d812a18a573079ae77f5f4",
      "bytes": 899
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "addb5fb5d4d9334ca0bdde287506f305f79903d7cc28c0fca47c48167fc808c0",
      "bytes": 528
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "f64d8e7384425fb89e1bb7ff4563a8c32cbeacedcafec2d5e289fb4fc9be2200",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "634ee76740dd1f8888e7e9c7f86b94b96db9ad200ed419b7980b365e55bf3084",
      "bytes": 204908
    }
  ],
  "estimated_tokens": 10444
}
-->

# Durable State Update — Chapter 648

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 648. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 648. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 648,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 648,
    "continuity_sources": [648],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
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

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung has majority-backed admission to the Nanman tribal grand council.",
    "Baeksang attacked Jin Taekyung at the council and withdrew with the pro-Baeksang faction after being stopped; he remains coldly hostile toward Jin.",
    "More than ten thousand Bai people and roughly half of Nanman's chieftains remain hostile to Jin.",
    "The Blood Monk is an unidentified bald, beardless, apparently middle-aged martial artist using a steel Zen staff who has killed several hundred people in Guizhou.",
    "Namho considers it highly likely that Dark Heaven is behind the Blood Monk, though this remains unconfirmed.",
    "Ju Hwaran, Song Ilseom, and Hyuk Mujin are investigating the Blood Monk in Guizhou for reconnaissance and possible combat.",
    "Baeksang's hostility toward the Central Plains may come from grief over losing his only child or from a grudge against the orthodox Murim, and his possible alliance with Dark Heaven could endanger Nanman.",
    "Approximately two hundred Ailao Mountain warriors remain inside the Thousand-Year Spider webs, which appear to shield them from the Poison Mist.",
    "The missing ferocious beasts, Ailao Mountain's Wraith, and the pure-white eggs in the Poisonblood Grounds remain unexplained.",
    "An unidentified entity who recognizes Jin Taekyung has killed two informants.",
    "The Martial God once annihilated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone, later appeared as a young boy, and then disappeared; Jin suspects a possible connection to Cheon Taemin."
  ],
  "continuity_sources": [
    647
  ],
  "open_questions": [
    "What are the Blood Monk's identity, purpose, destination, and connection to Dark Heaven?",
    "Is Baeksang acting from grief, resentment toward the orthodox Murim, or an alliance with Dark Heaven?",
    "Where did the missing ferocious beasts go, and what does Ailao Mountain's Wraith intend to do with the pure-white eggs?",
    "Who is the hidden entity that recognizes Jin Taekyung, and what is the nature of their past connection?",
    "Are the Martial God and Cheon Taemin connected, and where did the Martial God go after disappearing?"
  ],
  "safe_through": 647,
  "temporary_decisions": [
    "Use Tribal Grand Council for 부족 대회의.",
    "Use Blood Monk for 혈승.",
    "Use Soul-Chasing Guest for 추혼객.",
    "Use Killing Buddha for 살불.",
    "Use Fire Courtyard for 화원."
  ],
  "version": 1
}
```

## Exact glossary matches

| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 사형     | **Senior Brother**                           |
| 정마대전   | **Great Faction War**         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 647
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he opposes the Nanman Beast Palace joining the Murim Alliance, attacked Jin Taekyung at the tribal grand council, withdrew with the pro-Baeksang faction after being stopped, and may resent the orthodox Murim over the loss of his only child or be secretly aligned with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 647
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 647
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 647
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 647
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 647
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 647
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 647
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃648화



마치 세상이 정지한 것 같았다. 약속이라도 한 것처럼 일시에 뚝 끊긴 연주와 움직임을 멈춘 사람들.

그리고 순식간에 찾아온 정적 속에서, 지그시 나를 응시하던 백상의 냉담한 눈빛을 가로막은 것은 야수묘왕의 한 마디였다.

“아우, 이만 자리에 앉지.”

내게 못 박혀 있던 시선이 천천히 떨어져 나간다.

그사이 의복이라도 갈아입었는지, 백상은 눈처럼 새하얀 옷소매를 휘날리며 멈춰 있던 걸음을 옮겼다.

“그러지요.”

저벅. 저벅.

대전에서는 마치 아무 일도 없었던 것처럼 단정한 복장과 담담한 목소리.

두 명의 대족장을 좌우로 두고 계단을 오르는 그의 모습을 바라보는 야수묘왕의 눈빛에 씁쓸함이 감도는 듯했다.

‘그럴 만도 하지.’

한 사람은 아우라 부르고, 한 사람은 궁주라 답한다.

비록 피는 섞이지 않았지만 두 사람은 어릴 적부터 함께 자란 의형제라고 했다.

하지만 나는 단 한 번도 들어 본 적이 없다. 백상이 야수묘왕을 형님이라 부르는 것을.

그와 동시에 문득 생각했다.

‘백상에게 야수묘왕은 어떤 존재일까.’

그래도 아직 마음속에 한 줄기의 정이 남아 있는 의형(義兄)?

혹은 단순히 상하 관계로 묶여 있는 남만야수궁의 궁주?

그것도 아니라면…….

‘정마대전에 참전하여 하나뿐인 아들을 잃게 만든 원수?’

글쎄. 잘 모르겠다.

하지만 얼마 지나지 않아 알게 될 것 같은 예감이 들었다.

그것이 좋은 방식으로든, 나쁜 방식으로든.

나로서는 가급적 전자이길 바랄 뿐이었고, 그건 야수묘왕 역시 마찬가지인 듯했다.

“오랜만에 이 우형(愚兄)이 잔을 채워 주마.”

야수묘왕의 손에 들린 술병을 말없이 바라보던 백상이 건조한 음성으로 대답했다.

“주색(酒色)을 멀리한 지 어언 수십 년입니다. 정중히 사양하지요.”

아무리 남만야수궁이 일종의 분할 통치제로 유지되는 부족 사회라 해도 궁주의 권위는 강력하다.

이는 그야말로 백상이라 가능한 거절이었다.

그는 백족의 대족장이기 이전에 야수묘왕의 의형제였으니까.

“넌 어릴 적부터 과실주를 좋아했지. 하지만 이제는 내가 따라 주는 술도 받지 않겠다는 말이냐? 아우를 위해 우형이 직접 담근 과실주다.”

“…….”

“백상.”

섭섭함과 씁쓸함이 담긴 나직한 부름에, 천천히 눈을 감았다 뜬 백상이 잔을 들었다.

“정 그러시다면, 어쩔 수 없군요.”

“그럼……”

“잔만이라도 받겠습니다.”

그제야 표정이 밝아진 야수묘왕은 백상의 술잔을 가득 채웠다. 그리고 나와 백상만이 들을 수 있을 만큼 작은 목소리로 속삭였다.

“두 사람 모두 대전에서의 일은 잊었으면 한다. 누구 하나를 탓하기에는 서로가 서로에게 잘못을 저질렀으니.”

내게 있어 백상은 여전히 수상쩍고 마음에 들지 않는 인물이다. 하지만 이런 상황에서조차 엑셀을 밟을 정도로 바보는 아니었다.

“알겠습니다. 사실 제가 좀 심하긴 했죠.”

“…….”

뜻을 알 수 없는 미묘한 눈빛으로 나를 응시하던 백상 역시 작게 고개를 끄덕였다.

“못난 꼴을 보여 송구합니다, 궁주.”

그것은 뜻밖이라고 느낄 만큼 순순한 대답이었다.

만면에 흡족한 미소를 띤 야수묘왕은 돌아서서 외쳤다.

“오늘은 남만의 모든 부족, 그리고 먼 길을 달려 중원에서 온 귀빈들이 함께하는 경사스러운 날이다. 모두 마음껏 먹고 마셔라!”

고요하던 연무장을 울리는 야수묘왕의 외침에, 잠시 멈췄던 연주가 시작되고 남녀가 뒤섞인 무희(舞戱)들이 춤사위를 이어 가기 시작했다.

비로소 부드럽게 풀리는 분위기.

하지만 다음 순간 내 귓가를 파고드는 전음(傳音)은 더할 나위 없이 딱딱했다.

- 중원에서 온 귀빈이라. 재미있군.

아하.

‘어쩐지. 너무 쉽게 풀린다 했지.’

나는 콧잔등을 긁으며 야수묘왕을 바라보았다. 자리에서 일어난 그는 주위의 여러 부족장들과 그들이 데려온 전사들을 독려하는 중이었다.

뒤에서 무슨 일이 벌어지는지도 모른 채.

- 떠나라. 이 땅에 너희가 머무를 곳은 없다.

계속해서 귓가로 전해지는 전음에, 술잔을 한입에 털어 넣은 나는 입술을 달싹였다.

- 우리 대족장님, 인심이 영 퍽퍽하시네. 아무리 한족이 미워도 그렇지. 내가 지난밤 애뇌산에서 구한 사람이 몇 명인데.

- 대가를 주마.

- 뭐?

- 무엇을 원하느냐? 황금? 은? 말하거라. 네놈의 몸뚱어리보다 무거운 금은보화를 내어줄 테니.

- ……흠.

달달하던 과실주의 향이 떫게 변한다. 마치 지금 내 기분처럼.

‘금은보화라.’

이거 참.

푸대접은 충분히 예상했지만, 생각했던 것보다 훨씬 기분이 더럽다. 나는 비어 있는 술잔을 채워 넣으며 재차 전음을 흘려보냈다.

- 딱히 그런 걸 노리고 한 일은 아니었는데. 혹시 남만에서는 사람 목숨을 재물이랑 비교하나?

- 그럴 리가. 부족민의 목숨은 무엇과도 맞바꿀 수 없다. 하지만 상대가 한족이라면 이야기는 달라지지.

- 어째서?

- 그건 네놈들이…….

이어지려던 전음이 흐릿해진다. 백상은 음울한 회색 눈동자로 가득 찬 술잔을 바라보다가, 이내 고개를 저었다.

- 쓸데없는 말을 했군. 더 이상 왈가왈부하지 말고 떠나라.

- 여기에서 끊어먹으면 나 오늘 잠 못 잘 것 같은데. 차라리 속 시원하게 털어놓고 해결책을 찾는 방법은 없나?

- 해결책이라.

피식.

처음 봤다. 백상이 웃는 모습은.

그리고 그가 흘린 실소에 담긴 감정은 명백한 경멸과 비웃음이었다.

툭, 챙그랑!

비록 시끄러운 연회의 소음에 파묻혀 버렸지만 나는 똑똑히 듣고 볼 수 있었다.

자기(磁器)로 만든 잔이 바닥으로 떨어져 산산조각 나고, 그 안에 가득 담겨 있던 술이 사방으로 튀는 것을.

주르륵. 투둑.

엎질러진 과실주가 돌계단을 적시며 방울방울 떨어지던 그때, 귓가로 백상의 전음이 이어졌다.

- 되돌리기에는 이미 늦었다. 저것들처럼.

- 흠.

늦어? 정말 그럴까.

그 광경을 물끄러미 바라보던 나는 불쑥 손을 뻗었다.

솨아악!

손가락의 끝으로 흘려보낸 한 줄기의 공력이 주변의 바닥을 잔잔하게 휩쓸었다.

동시에 시간을 거꾸로 돌리기라도 한 것처럼, 조금 전 형태를 잃은 것들이 솟구쳐 활짝 펼쳐진 내 손아귀로 빨려들었다.

쉬익. 티틱!

수십 개의 파편이 자석처럼 서로를 향해 들러붙는다. 공력을 접착제 삼아 단면을 잇고, 뭉친 끝에 마침내 하나의 잔이 되었다.

“……!”

“……!”

순간 술렁이는 주위의 공기.

슬쩍 고개를 돌려 살피니, 아까부터 이곳을 주시하던 이들의 반응이 제법 가관이다.

남호와 흑웅은 입을 딱 벌린 채 굳어 있고, 사마표와 요희의 눈동자에는 이채가 스쳤으며, 태산은 고기를 씹는 것도 잊은 채 멍한 표정을 짓는 중이었다.

‘쓸 만한데. 확실히 중단전을 연 이후로 공력 제어가 더 세밀해졌어.’

다른 건 제외하고서라도 태산의 식사를 멈추게 했으니 만족스러운 성과다.

“음, 좋아. 이 정도 허공섭물(虛空攝物)이면 훌륭하지.”

자화자찬하는 내 모습을 바라보던 백상이 덤덤한 목소리로 입을 열었다.

“무공을 자랑하고 싶었나? 하지만 그런 것치고는 터무니없이 형편없는 잔이로군.”

“형편없다고?”

“그런 것으로는 아무것도 담을 수 없다. 술을 담기도 전에 새어나가 버릴 테지.”

아주 틀린 말은 아니었다. 내가 무슨 신도 아니고, 시간을 완전히 되돌리지 않는 이상 완벽한 복구는 불가능하니까.

백상의 말처럼 미처 모든 파편을 찾지 못한 탓인지 잔은 실금투성이였고, 이미 바닥과 계단에 스며든 술을 건져 올리는 것은 나로서도 무리였다.

하지만…….

“거 더럽게 따지네. 그냥 마시면 되지.”

한 마디를 툭 내뱉은 나는, 망설임 없이 술병을 들어 잔을 채웠다. 아니, 넘치도록 들이부었다.

그리고 술이 흘러나오는 빈틈을 손아귀 전체로 감싸 쥔 뒤, 그대로 입안에 털어 넣었다.

꿀꺽.

불이라도 삼킨 것처럼 목이 화끈해진다. 입을 열자 과실주의 향긋한 주향과 함께 달아오른 목소리가 흘러나왔다.

“뭐 별거 있나? 실금이 가고 깨져도 뭔가를 담아서 마실 수만 있다면 그게 잔인데.”

“……!”

순간 백상의 눈빛이 깊게 가라앉았다.

- 이미 오래전 바닥에 엎질러진 술은 어찌하겠느냐?

모르는 이가 들었다면 무슨 귀신 씻나락 까먹는 소리를 하느냐고 생각했을지도 모르겠다.

하지만 앞서 백상과 전음을 주고받았던 내게는 다르게 들렸다.

‘잔은 믿음(信). 엎질러진 술은 사람(人).’

정마대전에서 남만야수궁은 무수한 부족민들을 잃어야만 했고, 그후 백상은 입에 담기도 싫어하는 모종의 사정으로 중원에 대한 믿음을 완전히 잃었다.

해서 나는 산산조각 난 잔을 이어붙이는 것으로 뜻을 전해 보였다.

‘그가 이걸 다시 한번 믿어 달라는 부탁으로 받아들일지, 마지막 경고로 받아들일지는 모르겠지만…….’

어찌 되었건 이것으로 뜻은 확실히 전했다.

나는 흥겨운 연회가 한창인 연무장을 바라보았다.

환호하는 수많은 이의 중심에 선 한 사람, 야수묘왕이 심유한 눈빛으로 이쪽을 응시하고 있었다.

‘깜짝이야. 하여간 눈치 하나는.’

왠지 모르게 사고 치다가 걸린 고등학생이 된 기분이다.

야수묘왕을 향해 짐짓 어깨를 으쓱해 보이고는 자리에서 일어나 휘적휘적 걸음을 옮겼다.

“어딜 가는 것이냐?”

등 뒤에서 들려오는 백상의 목소리.

나는 굵고 짧은 대답을 돌려주었다.

“오줌!”

과실주 그거, 의외로 독하더라.



* * *



“커……헉!”

곰 같은 사내였다. 하지만 팔척장신의 거구와 일 갑자가 넘는 공력도, 눈앞에 들이닥친 죽음을 피하기에는 역부족이었다.

콰득!

“컥, 네, 네놈은. 누구냐.”

빈틈없이 목을 옥죄는 손길. 정수리에서 흐른 핏물과 호흡 곤란으로 시야는 온통 붉고 흐릿했다.

사내는 젖먹던 힘을 쥐어 짜내어 말을 이어 갔다.

“제, 제발 사, 살려…….”

살고 싶었다. 미치도록. 그러나 사내의 목을 붙잡고 있는 괴인(怪人)의 생각은 달랐다.

우드득!

뼈가 부러지는 소리와 함께 드러나는 흰자위.

생기가 빠져나간 사내의 신형이 축 늘어지자, 괴인은 손아귀에 들어가 있던 힘을 풀었다.

쿵!

육중한 몸뚱어리가 땅을 뒹굴었고, 한 치의 망설임도 없이 그의 목숨을 거둔 괴인은 내심 중얼거렸다.

‘아. 방금 처리한 놈이 마지막이었나?’

불과 반 시진 전이었다. 갑작스럽게 협곡의 앞뒤에서 적들이 나타난 것은.

그러고는 대뜸 이렇게 외쳤다.



‘반드시 네놈을 찢어 죽여, 사형제들과 벗들의 원수를 갚겠다.’

‘놈을 죽여라!’



그렇게 일대 다수의 전투가 시작되었고, 사방에서 달려드는 놈들을 쉼 없이 죽이다 보니 숫자 세는 걸 잊었다.

‘한 이백 명쯤 되겠군.’

많이도 끌어모았다 싶었다. 어차피 결과는 처음부터 정해져 있는 것이나 마찬가지였지만.

시산혈해(屍山血海).

그것은 네 글자로밖에 설명할 수 없는 광경이었고, 귀주(貴州)의 어느 이름 모를 협곡에 다시 한번 자신의 족적을 새긴 괴인은 잠시 바위에 기대 두었던 자신의 무기를 집어 들었다.

쩔렁. 철그럭.

쇳소리와 함께 흔들리는 선장(禪杖).

피 웅덩이를 밟으며 나아가는 그의 발걸음은, 남쪽 어딘가를 향하고 있었다.
```

## Final English reading copy

```markdown
# Chapter 648

It was as though the world had stopped.

The music and movements had cut off all at once, as if by prior agreement, and the people had frozen in place.

And in the silence that descended in an instant, it was a single remark from the Beast Miao King that blocked Baeksang’s cold gaze as he stared fixedly at me.

“Little brother, take your seat now.”

The gaze that had been nailed to me slowly pulled away.

Perhaps he had changed his clothes in the meantime, because Baeksang swept his snow-white sleeves through the air and resumed his halted steps.

“Very well.”

Step. Step.

In the main hall, his clothes were neat and his voice calm, as though nothing had happened.

The Beast Miao King’s eyes seemed tinged with bitterness as he watched Baeksang climb the stairs with two great chieftains on either side of him.

*I suppose that’s understandable.*

One called him little brother, while the other replied, “Palace Lord.”

Although they shared no blood, I had heard that the two had grown up together as sworn brothers from childhood.

But I had never once heard Baeksang call the Beast Miao King hyung.

At the same time, a thought suddenly occurred to me.

*What kind of person was the Beast Miao King to Baeksang?*

Was he still a sworn elder brother, with a single thread of affection left in his heart?

Or merely the Palace Lord of the Nanman Beast Palace, bound to him by a simple hierarchy?

Or perhaps……

*An enemy who had joined the Great Faction War and caused him to lose his only son?*

Who knew? I didn’t.

But I had a feeling I would find out before long.

Whether in a good way or a bad one.

As far as I was concerned, I hoped it would be the former. And it seemed the Beast Miao King felt the same.

“For the first time in a long while, I’ll fill your cup myself. Your foolish elder brother will.”

Baeksang silently stared at the wine bottle in the Beast Miao King’s hand before answering in a dry voice.

“I have kept away from wine and women for decades now. I must respectfully decline.”

Even though the Nanman Beast Palace was a tribal society maintained through a kind of divided rule, the Palace Lord still wielded enormous authority.

That refusal was possible only because he was Baeksang.

Before he was the great chieftain of the Bai people, he was the Beast Miao King’s sworn younger brother.

“You liked fruit wine when you were young. But are you saying you won’t accept even wine poured by me now? I made this fruit wine myself for your sake.”

“……”

“Baeksang.”

At the quiet call filled with disappointment and bitterness, Baeksang slowly closed and opened his eyes before lifting his cup.

“If you insist, I suppose I have no choice.”

“Then……”

“I will accept the cup, at least.”

Only then did the Beast Miao King’s expression brighten. He filled Baeksang’s wine cup to the brim, then whispered in a voice soft enough for only Baeksang and me to hear.

“I hope you will both forget what happened in the main hall. It would be wrong to blame either one of you, since you both wronged each other.”

To me, Baeksang was still suspicious and thoroughly unlikeable. But I wasn’t stupid enough to hit the gas even in a situation like this.

“All right. I admit I went a little too far.”

“……”

Baeksang stared at me with an inscrutable look, then gave a small nod.

“I apologize for showing such an ugly side of myself, Palace Lord.”

It was a surprisingly compliant answer.

The Beast Miao King beamed with satisfaction, turned around, and called out,

“Today is a joyous occasion shared by every tribe of Nanman and our honored guests who have traveled all the way from the Central Plains. Eat and drink to your heart’s content!”

At the Beast Miao King’s shout, which rang across the quiet training ground, the music that had stopped began again. Dancers, both men and women, resumed their movements.

The atmosphere finally began to soften.

But the Sound Transmission that pierced my ear the next moment was anything but gentle.

—Honored guests from the Central Plains, are we? How amusing.

*Aha.*

*I knew it. I thought things were smoothing over too easily.*

I scratched the bridge of my nose and looked toward the Beast Miao King. He had risen from his seat and was encouraging the various chieftains around him and the warriors they had brought along.

Without knowing what was happening behind him.

—Leave. There is no place for you to remain in this land.

As the Sound Transmission continued to reach my ears, I drained my cup in one gulp and moved my lips.

—Our great chieftain is rather stingy. I mean, I know you hate the Han Chinese, but still. Do you have any idea how many people I rescued at Ailao Mountain last night?

—I will compensate you.

—What?

—What do you want? Gold? Silver? Speak. I will give you treasures heavier than your own body.

—……Hmm.

The sweet fragrance of the fruit wine turned bitter.

Much like my mood.

*Gold and silver treasures, huh.*

Well, this was something.

I had expected a cold reception, but it felt far worse than I had imagined. I refilled my empty cup and sent another Sound Transmission.

—I wasn’t doing it for something like that. Do people in Nanman really compare a person’s life to material wealth?

—Of course not. The life of a tribesman cannot be exchanged for anything. But if the other party is Han Chinese, that is a different matter.

—Why?

—That is because you people……

The Sound Transmission that had been about to continue faded away. Baeksang stared at his full wine cup with gloomy gray eyes, then shook his head.

—I said something unnecessary. Stop arguing and leave.

—If you stop there, I don’t think I’ll be able to sleep tonight. Why not get it all off your chest and see if we can find a solution?

—A solution?

Pfft.

It was the first time I had seen Baeksang laugh.

And the emotion contained in that quiet laugh was unmistakable: contempt and ridicule.

Thud. Crash!

The sound was swallowed by the noisy banquet, but I saw and heard it clearly.

The porcelain cup fell to the ground and shattered, and the wine that had filled it splashed in every direction.

Trickle. Drip.

As the spilled fruit wine soaked the stone steps and fell drop by drop, Baeksang’s Sound Transmission continued in my ear.

—It is already too late to turn things back. Just like those.

—Hmm.

Too late? Was it really?

As I gazed blankly at the scene, I suddenly reached out.

Fwoosh!

A thread of internal energy sent from my fingertips swept gently across the floor around us.

At the same time, as though time were running backward, the things that had lost their shape moments earlier shot upward and flew into my wide-open hand.

Sss. Tick, tick!

Dozens of fragments clung to one another like magnets. Using internal energy as adhesive, I joined the broken edges. After clumping together, they finally became a single cup.

“……!”

“……!”

The air around us stirred.

I subtly turned my head to look around. The reactions of those who had been watching us from earlier were quite a sight.

Namho and Heugung stood frozen with their mouths hanging open. A strange light flashed through Sama Pyo and Yohi’s eyes. Taishan had even forgotten to chew his meat and was staring blankly.

*Not bad. Ever since I opened my Middle Dantian, my control over internal energy has definitely become more precise.*

Even setting everything else aside, I had managed to stop Taishan from eating. That alone made it a satisfactory result.

“Hmm, good. Seizing an Object Through Empty Space at this level is excellent.”

Baeksang watched me praise myself and spoke in an even voice.

“Did you want to show off your martial arts? For all that, it is an absurdly pathetic cup.”

“Pathetic?”

“You cannot put anything in that. It will leak out before you can even pour in the wine.”

He wasn’t entirely wrong. I wasn’t some kind of god, and unless I completely reversed time, a perfect restoration was impossible.

As Baeksang had said, the cup was covered in hairline cracks, perhaps because I hadn’t found every fragment. And even I couldn’t retrieve the wine that had already seeped into the floor and stairs.

But……

“You’re so damn picky. Just drink it.”

I tossed out the words, then lifted the wine bottle without hesitation and filled the cup.

No—I poured until it overflowed.

Then I wrapped my entire hand around the gaps where the wine was leaking and tipped it straight into my mouth.

Gulp.

My throat burned as though I had swallowed fire. When I opened my mouth, my voice came out heated along with the fragrant scent of fruit wine.

“What’s the big deal? Even if it’s cracked or broken, if it can hold something and let you drink it, then it’s a cup.”

“……!”

Baeksang’s eyes sank deeply.

—What are you going to do about the wine that was spilled onto the ground long ago?

Anyone else who heard that might have wondered what kind of nonsense he was talking about.

But it sounded different to me after our earlier exchange of Sound Transmissions.

*The cup was trust. The spilled wine was people.*

During the Great Faction War, the Nanman Beast Palace had been forced to lose countless tribespeople. Afterward, because of some matter he did not even want to mention, Baeksang had completely lost his trust in the Central Plains.

So I had conveyed my meaning by piecing together the shattered cup.

*I don’t know whether he’ll take this as a plea to trust once more or as a final warning……*

Either way, I had made my meaning perfectly clear.

I looked out over the training ground, where the lively banquet was in full swing.

At the center of the countless cheering people stood the Beast Miao King, watching me with profound eyes.

*That startled me. The man certainly notices everything.*

For some reason, I felt like a high school student who had been caught causing trouble.

I deliberately shrugged at the Beast Miao King, then rose from my seat and ambled away.

“Where are you going?”

Baeksang’s voice came from behind me.

I threw back a brief answer in a deep voice.

“To take a piss!”

That fruit wine was surprisingly potent.

* * *

“Kh…… Urk!”

He was a bear of a man.

But even his towering, eight-foot frame and more than one jiazi’s worth of internal energy were not enough to escape the death rushing toward him.

Crunch!

“Urk…… Y-you. Who are you?”

A hand had clamped tightly around his throat. Blood flowing from the crown of his head and the lack of air had left his vision red and blurry.

The man squeezed out every last bit of strength he had and continued speaking.

“P-please…… s-save me……”

He wanted to live.

Desperately.

But the strange man gripping his throat thought otherwise.

Crack!

The whites of his eyes showed as his bones broke.

When the life drained from his body and he went limp, the strange man released his grip.

Thud!

The heavy body rolled across the ground. The man who had taken his life without a moment’s hesitation muttered inwardly.

*Ah. Was the man I just dealt with the last one?*

It had been only half a shichen earlier when enemies had suddenly appeared at both ends of the gorge.

Then they had immediately shouted,

“I’ll tear you apart and kill you to avenge my martial brothers and friends!”

“Kill him!”

That was how a one-against-many battle began. After endlessly killing the men rushing at him from every direction, he had forgotten to keep count.

*There must have been about two hundred.*

They had assembled quite a force.

The result had practically been decided from the beginning anyway.

A sea of corpses and blood.

It was a sight that only that four-character idiom could describe. The strange man, who had once again left his mark in an unnamed gorge in Guizhou, picked up the weapon he had left leaning against a rock.

Clang. Clatter.

His Zen staff swayed with a metallic sound.

Stepping through the pool of blood, he headed somewhere to the south.
```
