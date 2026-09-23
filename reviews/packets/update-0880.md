<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0880.txt",
      "sha256": "db6637ba08fbe853cc2c7cf2fdbdb45d83d6c0802f12dcb38784de34abdd27ea",
      "bytes": 13610
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5a4b487811d4727905683345c1188497d57bace6e3d8747ac151ab18c3eb1549",
      "bytes": 2204
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "c8632de6a3309c5e85eb04d44868d1eeebc0c5b97f762f7b3ad3980414cfd6ba",
      "bytes": 837
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b9962c6fb7d19e7e781e0170cad5037e48bacc218825076c80b05d9b363a00bd",
      "bytes": 1432
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "84cb8f3d9d4896fbea8c664f2661b0250df5bacb2be841df77671150558eb98d",
      "bytes": 470
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "ac29227225544232597ab225c18f65c99996802f18649d0571f6d5b343fe709d",
      "bytes": 771
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "88bd394265e6f51bf7c0b3221f38d53a0091e34d181851782708853ab30fe545",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "403d7ab7dec97f30853b5763fb3d0a7f25f8bde7bddfbbf021d0689fbb72bd85",
      "bytes": 765
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "d6172377bcbc16d015a300434f0c00d436347debf5b0ab1faec7951e880be6ab",
      "bytes": 952
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d9384e9ac1b5e8435b4526eb3ad43743df747a3184af7f49792e9027db164ec5",
      "bytes": 258472
    }
  ],
  "estimated_tokens": 10609
}
-->

# Durable State Update — Chapter 880

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 880. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 880. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 880,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 880,
    "continuity_sources": [880],
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
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "Taekyung gave Shangshan the Myriad-Poison Ring for protection against poisoning.",
    "The Emperor and a hidden adviser suspect the East Depot, Jin Taekyung, or both of deliberately spreading rumors that Shangshan returned to the capital and the Emperor has an heir; neither claim is confirmed.",
    "The Emperor says they will make the heir rumor true and begins a great celebration; an actual pregnancy or birth is not confirmed.",
    "The Emperor says a long-standing target must be eliminated for his great undertaking; the target’s identity is undisclosed.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "Hong Jin believes Aehyang is very likely pregnant; the pregnancy and the Emperor’s plans remain unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received two letters, burned them, and said the group was formally invited to the imperial palace; their contents and the invitation’s purpose remain unknown."
  ],
  "continuity_sources": [
    879
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Will the Myriad-Poison Ring protect Shangshan from Blood Soul Gu?",
    "Who deliberately spread the rumors, and are they true?",
    "What is the Emperor’s long-standing target, and what is his great undertaking?"
  ],
  "safe_through": 879,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 기루     | **pleasure house**                               |                                                       |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 다스패치 | **Daspatch** | News outlet whose reporter published the article about Jin's lifelong single status. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |

## Listed compact profiles

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 878
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 877
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 871
- **Aliases:** Killing Ghost
- **Role:** A Hubei fisherman who disappeared for a month and returned as the Killing Ghost, a monster that grew stronger and more grotesque with each appearance.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 871
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** A Thousand Captain in the Embroidered Uniform Guard under Baek Yeon’s command, he is ordered to surveil Prince Shangshan’s party while leaving openings for someone to approach; he says he would give his life to obey an imperial command.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 876
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 877
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 879
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

## Korean source

```text
＃880화



빽빽한 갈대밭에서 솟구친 불길은 거센 비바람으로도 쉬이 막을 수 없다.

어느 날부터 불현듯 황도를 휩쓸기 시작한 소문이 그러하듯이.

“그 이야기 들었나? 다름이 아니라 상산왕 전하께서 지금 황궁에…….”

“황제가 드디어 후사를 보았다는군.”

“조만간 큰 연회가 열릴 거라던데. 그래서 상산왕 전하께서도 십여 년 만에 돌아오신 거고.”

“한데 후사라면, 황후마마께서 회임하셨단 말인가?”

“그야 정확히는 모르지. 다만 옆집 장 씨한테 듣기로는 근래에 새로 들였다는 후궁이라는데…….”

“옆집 장 씨? 그 푸줏간 장 씨?”

“맞네. 자네와도 안면이 있었나?”

“알다마다. 그 친구가 도축 하나는 기가 막히게 하지. 그런데 그 장 씨가 그런 얘기를 당최 어디서 들었대?”

“누구라더라. 아, 그래. 건너편에서 점포 운영하는 오 씨.”

“그럼 그 오 씨는 누구한테…….”

“나무꾼 이 씨.”

나는 새도 붙잡아서 형옥으로 끌고 간다는 금의위로서도 그 수많은 입을 막는 것은 불가능에 가까웠다.

철벽처럼 높게 솟은 황궁의 성벽이 무색하리만치 소문은 급속도로 퍼졌고, 하룻밤 사이 수백 명이 넘는 이들이 금의위에 의해 끌려갔다.

“살고 싶으면 순순히 털어놓거라. 어느 놈이 그런 헛소문을 퍼트리고 다녔는지.”

“히, 히익! 말하겠습니다! 전부 말씀드리겠습니다!”

금의위가 어떤 곳인가.

한 번 끌려간 이상 죽은 목숨이나 다름없는, 내로라하는 고관대작들마저 잡초처럼 베어 내는 무시무시한 집단이 아닌가.

그런 악명을 익히 알고 있던 죄인들은 고문 기구를 들이대기도 전에 자신들이 아는 모든 사실을 털어놓았지만, 이 순조로운 취조에도 금의위가 얻은 소득은 아무것도 없었다.

“뭐라던가?”

“그것이, 하나같이 같은 말만 하고 있습니다. 황궁과는 어떤 연줄도 없는 평범한 이웃이나 길거리 상인, 객잔 혹은 기루에서 마주친 외지인에게 그런 소문을 들었다고 합니다.”

“빌어먹을.”

취조 과정에서 수많은 장삼이사(張三李四)의 이름이 나왔으나 모조리 빈 껍데기에 불과한 상황.

죄인들의 입에서 흘러나온 관련자들의 신분은 평범하기 그지없었고, 누군가로부터 광범위하게 퍼지기 시작한 이 소문의 실체는 묘연했다.

그러나 그들은 금의위였다.

이 광활한 천하에서 오직 단 한 사람. 황제에게 절대적인 충성을 바치는.

어떤 경우에도 유의미한 결과물을 만들어 내야 하는 금의위.

“본격적인 심문을 시작하라.”

“예?”

“무슨 방법을 동원하더라도 상관없다. 반드시 최대한 빠른 시일 내에 흉수들을 알아내야 해.”

“하, 하지만 저들은…….”

“그따위 헛소문으로 대국의 혼란을 야기하고, 지엄하신 황제 폐하의 명예에 먹칠을 한 놈들이다. 그런 자들이 이 나라의 백성인가, 아니면 역적인가?”

상관의 호령에 금의위 위사들은 입을 굳게 닫았다. 형옥에 갇혀 벌벌 떠는 저 죄인들이 단지 무지몽매한 백성들이라는 것을 알고 있기 때문이었다.

이는 아무것도 남지 않은 폐광(廢鑛)에서 금맥을 찾으라는 것과 별반 다를 것 없는 상황.

털어서 먼지 안 나는 곳간이 없듯이, 지금껏 금의위 형옥을 거쳐 간 무수한 고관대작들은 크건 작건 각각의 죄가 있었다.

하지만 저들 모두는 그저 한 사람의 백성에 지나지 않는다. 거센 바람이 불면 허리를 숙이고, 비가 내리면 젖어 버리는 이들.

한데 그런 힘없는 사람들을 상대로 고문을 가해야 한다.

참혹하게 죽이거나, 반병신으로 만들어서라도 상부에 올려보낼 결과물을 만들어야 한다.

부패하거나 불충한 권력자들을 벌하여 대국의 질서를 바로 세운다는 자부심을 갖고있는 금의위들로서는 마음 한구석이 찜찜할 수밖에 없었다.

그러나…….

“답하라!”

재차 떨어지는 상관의 불호령에, 침묵을 지키고 있던 이들은 더는 물러설 곳이 없음을 깨달았다.

본래 군문(軍門)의 규율은 엄격하고, 그중에서도 가장 강력한 권력 기관 중 하나인 금의위는 말할 것도 없었으니.

“천호(千戶)의 명을 받듭니다.”

그렇게 마지못해 대답한 그들이 고문을 위해 형옥으로 복귀하려던 그때였다.

“모두 멈춰라.”

나직한 목소리와 함께 나타난 중년 사내가 좌중을 쓸어보았다.

먼지 한 톨 묻어 있지 않은 황금빛 갑옷과 당당한 체구. 그를 즉각 알아본 금의위 천호가 눈을 동그랗게 떴다.

“정 천호 아니시오?”

무뚝뚝하게 고개를 끄덕인 정 천호, 정호군이 입을 열었다.

“오랜만이군, 홍 천호. 지난밤에 잡아들인 죄인들의 심문은 어떻게 되어 가고 있나?”

“곧 제대로 된 결과가 나올 거요. 한데 멈추라니, 그게 무슨?”

“말 그대로일세. 이만 멈추게. 더 파서 나올 것도 없으니.”

정호군의 단호한 대답에, 조금 전까지 수하들을 향해 불호령을 떨어트렸던 천호가 눈살을 찌푸렸다.

“오늘따라 참견이 과하시군. 이제는 월권(越權)이라도 할 셈이신가?”

“그럴 리가.”

“아니라면 도대체 뭐요? 정 천호께서 제아무리 지휘사 영감의 총애를 받는다고 해도 이건 명백한…….”

“황명(皇命)일세.”

“뭐라?”

“황명이라고 했네. 전달받는 그 즉시 간밤에 잡아들인 죄인들을 대상으로 한 심문이나 고문을 중단하고, 늦어도 한 식경 내에는 모조리 석방하라는 황제 폐하의 명령.”

“……!”

“다들 뭣 하고 있나? 어서들 황명을 따라 움직이지 않고.”

갑작스럽게 등장한 정호군은 상황을 순식간에 정리해 버렸다.

무릎을 꿇고 정식으로 황명을 받든 금의위 위사들은 수백여 명이 넘는 죄인들을 풀어주기 위해 썰물처럼 물러났고, 그들의 상관인 천호는 굳은 얼굴로 정호군을 향해 물었다.

“지금 상황이 어떻게 돌아가고 있는 거요? 이번 일에 대한 보고는 어찌하고?”

“모두 잊게. 그것이 폐하의 뜻이니.”

별다른 감정이 느껴지지 않는, 특유의 고저 없는 목소리로 대답한 정호군이 말을 이었다.

“본론부터 말하지. 소문은 사실일세.”

“뭐요?”

“전부 사실이라고 했네. 곧 황실에서도 정식으로 공표할 거야. 우리 금의위가 그 임무를 도맡게 될 테고.”

“……!”

“황제 폐하께서는 소문의 근원지가 어디인지는 능히 짐작하고 있으나, 정확한 사실을 밝혀 내는 것은 무의미하다 하셨네. 저들이 철저하게 계획하고 퍼트린 이상 증거는 거의 남지 않았을 테니.”

“하, 하면.”

“곧 머지않아 황궁에서 이를 축하하기 위한 연회가 열릴걸세. 상산왕 전하는 물론 모든 문무백관이 참여하겠지. 자네는 추후 새로운 명령이 내려올 때까지 안팎의 방비를 철저히 하게.”

황제의 후사에 관한 것은 극소수만이 알고 있던 극비.

상산왕의 귀환에 관한 소식을 알고 있었으나, 이와 같은 사실을 모르고 있던 천호의 얼굴이 돌처럼 딱딱하게 굳었다.

“그 모든 걸 시인하는 것으로도 모자라 백성들에게 공표한단 말이오? 지금 이 시점에서?”

“정확하네.”

“정 천호께서는 이게 무슨 의미인지 알고 있으시오? 아니면 알면서도 모르는 척하는 거요?”

“나 역시 충분히 인지하고 있네. 자네가 간과하고 있는 다른 것까지도.”

“내가 간과하는 사실이라니. 그게 무슨…….”

“우리 같은 일개 무관도 짐작할 수 있는 것을, 설마 황제 폐하께서 모르실까.”

“……!”

“명령에 따르게.”

정호군은 할 말을 잃은 천호를 남겨 둔 채 자리를 떴다. 그리고 어두컴컴한 형옥과 그 안에서 하나둘씩 풀려 나오는 사람들을 지나쳐 가며 생각했다.

‘이제부터가 시작이군.’

느껴진다.

곧 황도라 불리는 이 화려한 도시를, 아니 천하를 휩쓸 거대한 폭풍이.

그리고 앞으로 벌어질 모든 것의 시작을 알리는 효시(嚆矢)는 황실의 정식 공표가 될 것이다.

‘많은 사람이 모이고, 또 많은 말이 오가겠지.’

지금부터 나타날 이들은 널리고 널린 장삼이사가 아니다.

소위 식자층(識者層)이라 칭해지는 그들. 현재 벌어지는 상황을 이해하고 그에 따라 행동으로 보일 수 있는 권력자들이 움직이기 시작할 것이다.

그리고 그 과정에서…….

‘비로소 적아(敵我)가 나뉜다.’

전쟁이 시작되기 전까지는 누가 적이고 아군인지 알 수 없다.

그러나 각자의 병장기를 뽑고, 물러설 수 없는 싸움이 시작되었을 때, 진실이란 놈은 마침내 모습을 드러낸다.

그것이 어떤 형태로든.

‘이 전쟁 속에서, 그놈은 어떤 선택을 할까.’

정호군은 문득 떠올렸다.

도무지 종잡을 수 없던 한 청년을.

스스로 태풍의 눈 속으로 몸을 내던진 무모하기 그지없는 강호의 젊은 무뢰배를.



* * *



“역시 과감하네요. 마치 십여 년 전처럼.”

오랫동안 침묵하던 홍진이 불쑥 꺼내 든 말에, 나는 조용히 고개를 끄덕였다.

나 역시 그와 같은 마음이었기 때문이었다.

‘생각 이상이야.’

건청궁에 다녀온 직후, 내가 건넨 정보를 전달받은 마삼보는 즉각 행동에 나섰다. 믿을 만한 심복들을 풀어 황도 전체에 소문을 퍼트린 것이다.

상산왕의 거취. 그리고 아직 정확히 확인되지 않았던 황제의 후사에 관한 모든 것들을.

다만 그 직후에 보인 황제의 행보는 심히 당혹스러울 정도였다.

‘이걸 바로 인정해 버릴 줄이야.’

다스패치에 딱 걸린 연예인들도 하루 이틀은 침묵하며 열애설을 부정하기 마련인데, 황제는 그 소문들을 인정하는 것을 넘어 곧장 공표해 버렸다.

그것도 불과 하루밖에 되지 않는 짧은 시간 만에.

‘행동력 하나는 끝내주긴 하는데, 도대체 무슨 의도지?’

아무리 생각해도 이 상황이 알려지면 알려질수록 황제에게는 불리하다.

어깨 위에 달린 게 장식이 아닌 이상, 손에 먹물깨나 묻히고 머리 좀 굴러간다 하는 사람들은 죄다 엇비슷한 생각을 떠올릴 테니까.

- 어? 황제가 상산왕을 비밀리에 황궁에 입궁시켰네?

- 어? 황제 주니어가 생겼는데 그걸 또 숨겼다가 들켰네?

- 어? 열 받네?

이러한 일련의 과정을 거쳐 나올만한 결론은 하나다.

- 황제가 상산왕을 제거할지도 모른다!

평소 쌓아 놓은 이미지라도 좋으면 모를까. 피바람을 일으켜가며 황위에 오른 게 작금의 천자가 아닌가.

경범죄에 초범이면 집행유예라도 받지, 전과 기록이 있는 살인자를 믿어 줄 사람은 아무도 없다.

‘황제의 힘이 두려워서 모른 척한다면 모를까.’

바둑으로 치면 악수(惡手)를 놓은 것이나 다름없는 상황.

그러나 덕분에 우리는 한시름 놓을 수 있었다.

황제가 상산왕의 안위를 함부로 위협하지 못하도록 시간을 벌려던 것이, 더욱 확실해졌으니.

“괜찮은 상황 아닙니까? 어찌 되었건 황실의 이름으로 모든 것을 인정했으니, 당장은 상산왕 전하를 둘러싼 위협이 사라질 테니까.”

눈치를 살피던 혁무진이 조심스럽게 꺼낸 말에, 홍진이 고개를 끄덕였다.

“틀린 말은 아니에요. 하지만 언제나 최악의 상황을 생각해야지.”

“최악이라면…….”

“진 공자는 대충 느낌이 올걸? 지금의 황제가 어떤 사람인지 직접 겪어 봤으니까.”

두 사람의 시선에 입맛을 다신 나는 천천히 입을 열었다.

“개인적으로는 둘 중 하나일 것 같은데…… 하나는 좋은 쪽, 다른 하나는 나쁜 쪽. 뭐부터 들으실래요?”

“음. 저는 나쁜 쪽부터 듣는 게 좋을 것 같습니다.”

“무진아.”

“예.”

“눈치 챙겨.”

“예.”

조용히 입을 닥친 혁무진을 안쓰럽게 바라본 홍진이 입을 열었다.

“좋은 쪽부터.”

좋은 쪽이라.

다시 한번 머릿속 생각을 정리한 나는 천천히 입술을 뗐다.

“첫째. 공개적으로 밝힌 이상 하나뿐인 동생을 건드리기 힘들어진 황제가 연회가 끝난 후 곱게 돌려보내 준다.”

“마음에 드는 결론이긴 한데…… 나쁜 쪽은?”

“둘째. 기왕 이렇게 된 거, 욕 한 번 더 처먹을 거 감수하고 남아 있는 반동분자들까지 싸그리 죽여 버린다.”

홍진은 침묵했다. 그리고 한참의 시간이 흐른 뒤, 어두운 얼굴로 작게 뇌까렸다.

“이번 연회가…… 홍문연(鴻門宴)이 될 수도 있겠네.”
```

## Final English reading copy

```markdown
# Chapter 880

A fire that sprang up in a dense bed of reeds could not easily be stopped, even by a fierce storm.

Neither could the rumors that had suddenly begun sweeping through the imperial capital.

“Have you heard? It’s about His Highness, Prince Shangshan. He’s in the imperial palace right now…”

“They say His Majesty the Emperor has finally had an heir.”

“I heard they’ll hold a great banquet soon. That must be why His Highness, Prince Shangshan, returned after more than ten years.”

“But an heir? Does that mean Her Majesty the Empress is pregnant?”

“Who knows for sure? All I heard from Zhang next door is that it’s a new concubine the Emperor recently took…”

“Zhang next door? The butcher, Zhang?”

“That’s the one. You know him too?”

“Of course. He’s incredible at slaughtering livestock. But where on earth did Zhang hear something like that?”

“From someone, what was his name… Oh, right. Mr. Wu, who runs a shop across the street.”

“Then who did Mr. Wu hear it from?”

“Li the woodcutter.”

Even the Embroidered Uniform Guard, who could catch a bird in flight and drag it off to prison, found it all but impossible to silence so many tongues.

The rumors spread so fast that the towering, impregnable walls of the imperial palace might as well have been nothing. In a single night, the Embroidered Uniform Guard dragged away hundreds of people.

“If you want to live, tell us everything. Which bastard has been spreading this nonsense?”

“Eek! I’ll tell you! I’ll tell you everything!”

What kind of place was the Embroidered Uniform Guard?

Once you were dragged in, you were as good as dead. It was a terrifying organization that cut down even the most prominent high officials like weeds.

The accused knew its reputation well. Before the guards even brought out the torture devices, they confessed everything they knew. Yet despite these smooth interrogations, the Embroidered Uniform Guard had gained nothing.

“What did they say?”

“They’re all saying the same thing. They heard the rumors from ordinary neighbors with no ties to the imperial palace, street vendors, or strangers they met at inns and pleasure houses.”

“Damn it.”

During the interrogations, countless names of ordinary people had come up, but every one of them was a dead end.

The people named by the accused were as ordinary as they came, and the true source of the rumors—which had begun spreading far and wide from somewhere—remained elusive.

But they were the Embroidered Uniform Guard.

In this vast realm, they gave their absolute loyalty to one person alone: the Emperor.

The Embroidered Uniform Guard, who had to produce meaningful results under any circumstances.

“Begin the real interrogation.”

“Pardon?”

“It doesn’t matter what methods you use. We must find the culprits as soon as possible.”

“B-But they…”

“They caused turmoil throughout the Great Nation with that sort of baseless rumor, and tarnished His Majesty the Emperor’s most august reputation. Are they subjects of this country—or traitors?”

At their superior’s shout, the Embroidered Uniform Guard officers fell silent. They knew the trembling prisoners in the cells were simply ignorant commoners.

This was little different from being told to find a gold vein in an abandoned mine that had been stripped bare.

Just as no storeroom was so clean that shaking it wouldn’t stir up dust, countless high officials had passed through the Guard’s prison, each with a crime or two to their name, great or small.

But these people were just ordinary subjects. When strong winds blew, they bent; when it rained, they got wet.

And now they were to be tortured.

They had to produce results for their superiors—even if that meant killing the prisoners horribly or leaving them half-crippled.

The Embroidered Uniform Guard took pride in punishing corrupt or disloyal officials to set the Great Nation in order. They could hardly help feeling uneasy about this.

But…

“Answer me!”

At their superior’s renewed roar, those who had remained silent realized there was nowhere left to retreat.

The rules of the military were strict by nature, and that was doubly true of the Embroidered Uniform Guard, one of the most powerful institutions in the realm.

“We obey the Thousand Captain’s orders.”

They answered reluctantly and were about to return to the prison to carry out the torture when—

“Everyone, stop.”

A middle-aged man appeared with a quiet voice and swept his gaze across the room.

His golden armor was spotless, and his build was imposing. The Embroidered Uniform Guard Thousand Captain recognized him at once, his eyes widening.

“Thousand Captain Jeong?”

Jeong Hogun gave a curt nod and spoke.

“It’s been a while, Thousand Captain Hong. How are the interrogations of the prisoners brought in last night going?”

“We’ll have proper results soon. But what do you mean, stop?”

“Exactly what I said. Stop here. There’s nothing more to dig up.”

At Jeong Hogun’s firm reply, the Thousand Captain, who had been shouting at his subordinates moments earlier, furrowed his brow.

“You’re interfering more than usual today. Are you planning to overstep your authority now?”

“Of course not.”

“Then what is this? No matter how much the Guard Commander favors you, this is clearly—”

“An imperial order.”

“What?”

“I said it’s an imperial order. The moment you receive it, you are to stop interrogating and torturing the prisoners taken last night, and release every one of them within half an hour at the latest. That is His Majesty the Emperor’s command.”

“……!”

“What are you all waiting for? Hurry up and obey the imperial order.”

Jeong Hogun had appeared out of nowhere and settled the matter in an instant.

The Embroidered Uniform Guard officers knelt and formally received the imperial command, then streamed away like the tide to release the hundreds of prisoners. Their superior, the Thousand Captain, asked Jeong Hogun with a stony expression,

“What’s going on? And what about our report on this incident?”

“Forget the whole thing. That is His Majesty’s will.”

Jeong Hogun answered in his characteristically flat voice, betraying no particular emotion, then continued.

“I’ll get straight to the point. The rumors are true.”

“What?”

“I said they’re all true. The imperial court will make an official announcement soon. The Embroidered Uniform Guard will be responsible for the task.”

“……!”

“His Majesty can well guess where the rumors originated, but he said there’s no point in uncovering the precise facts. They planned and spread them so thoroughly that there’s almost certainly no evidence left.”

“T-Then…”

“There’ll soon be a banquet in the imperial palace to celebrate. His Highness, Prince Shangshan, will be there, along with every civil and military official. Until further orders arrive, secure the palace and its surroundings.”

Only a handful of people knew the closely guarded secret concerning the Emperor’s heir.

The Thousand Captain had heard that Prince Shangshan had returned, but not this. His face stiffened like stone.

“You mean to confirm all of that—and announce it to the people? At this point?”

“Exactly.”

“Do you understand what that means, Thousand Captain Jeong? Or do you understand and pretend not to?”

“I understand it well enough. Including something else you’re overlooking.”

“Something I’m overlooking? What do you mean?”

“What a mere military officer like me can guess, surely His Majesty the Emperor knows.”

“……!”

“Obey the order.”

Leaving the speechless Thousand Captain behind, Jeong Hogun turned and walked away. Passing through the dark prison and the people emerging from it one by one, he thought:

*This is where it begins.*

He could feel it.

A great storm would soon sweep through this splendid city called the imperial capital—or, rather, across the whole realm.

And the imperial court’s official announcement would be the arrow that heralded the start of everything to come.

*So many people will gather, and so many words will be exchanged.*

Those who appeared from this point on would not be ordinary people by the dozen.

They were the so-called literati and educated classes—the powerful, who could understand what was unfolding and respond with action, beginning to move.

And in the process…

*At last, friend and foe will be divided.*

Until war begins, it’s impossible to tell who’s an enemy and who’s an ally.

But once each side draws its weapons and a battle begins from which there’s no retreat, the truth finally shows itself.

In whatever form it takes.

*What choice will that bastard make in this war?*

Jeong Hogun suddenly thought of a young man he could never quite figure out.

A reckless young ruffian of the martial world who had thrown himself into the eye of the storm.

* * *

“As daring as ever. Just like a little over ten years ago.”

At Hong Jin’s sudden remark after a long silence, I quietly nodded.

I felt the same way.

*This is more than I expected.*

As soon as Ma Sanbao received the information I’d given him after visiting Qianqing Palace, he acted. He sent out trusted subordinates and spread the rumors across the entire imperial capital.

Everything about Prince Shangshan’s whereabouts, and the Emperor’s heir—something that had yet to be confirmed for certain.

But the Emperor’s actions right afterward were astonishing.

*I can’t believe he admitted it outright.*

Even celebrities caught red-handed by Daspatch tend to keep quiet for a day or two and deny the dating rumors. The Emperor had gone beyond admitting them—he’d immediately announced them.

In less than a day.

*He sure is quick to act, but what on earth is he up to?*

No matter how I looked at it, the more people learned about this situation, the worse it was for the Emperor.

Unless the thing on his shoulders was purely decorative, anyone with a drop of ink on their hands and a working brain would come to roughly the same conclusion.

—Huh? The Emperor secretly brought Prince Shangshan into the imperial palace?

—Huh? The Emperor’s got a junior now, and he hid it until people found out?

—Huh? That pisses me off.

There was only one conclusion to draw from all that.

—The Emperor might eliminate Prince Shangshan!

It would be one thing if he had a good reputation to begin with. But wasn’t the current Son of Heaven the one who’d come to the throne after unleashing a river of blood?

A first-time offender might get probation for a minor crime, but no one would trust a murderer with a criminal record.

*Unless they’re too afraid of the Emperor’s power to say anything.*

In terms of Go, he’d played a terrible move.

Still, this had given us some breathing room.

Our attempt to buy time so the Emperor couldn’t recklessly threaten Prince Shangshan’s safety had become all the more certain.

“Isn’t this a decent situation? Whatever else, the imperial court has acknowledged everything in its own name. For now, the threats surrounding His Highness, Prince Shangshan, will disappear.”

Hong Jin nodded at Hyuk Mujin’s cautious suggestion.

“That’s not wrong. But you should always consider the worst-case scenario.”

“And the worst case would be…”

“Young Master Jin, you can probably guess. You’ve experienced for yourself what the current Emperor is like.”

At their gaze, I smacked my lips and slowly began.

“I can think of two possibilities. One good, one bad. Which do you want to hear first?”

“Hmm. I think it’d be better to hear the bad one first.”

“Mujin.”

“Yes?”

“Read the room.”

“Yes.”

Hong Jin looked sympathetically at Hyuk Mujin, who had quietly shut his mouth, then spoke.

“Start with the good one.”

The good possibility.

I sorted through my thoughts once more, then slowly parted my lips.

“First: now that he’s made it public, the Emperor will find it hard to lay a hand on his only younger brother, and he’ll send him back safely after the banquet.”

“I like that conclusion, but… what’s the bad one?”

“Second: since things have come to this, he’ll accept getting cursed out one more time and slaughter every remaining dissident.”

Hong Jin fell silent. After a long while, he murmured, his expression dark.

“This banquet… could become a Hongmen Banquet.[^1]”

[^1]: At the historical Feast at Hong Gate, a banquet became the setting for an attempt on Liu Bang’s life.
```
