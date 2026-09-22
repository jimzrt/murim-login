<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0651.txt",
      "sha256": "063abfd4f1a5504bf27fcbfd756013d66560704e7c5591cf39264a6d8c00951c",
      "bytes": 16537
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "156ebc1d4135f61d9b7258f79768e692eea74a791648191e176c68742d56e6ce",
      "bytes": 1665
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "02de5e5d93d6c416d9f8bb7271204b73285d51875d03443ff8c17142c203c1bc",
      "bytes": 199622
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "296243d3a4ad8ecc0ee26e18681648f49a73a101736ba447c9194017e13f4fc7",
      "bytes": 748
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "54e3ceb0f9acbaedd9be5c89530070ce88bb20ba0a89577cf5978c0e0eebe193",
      "bytes": 766
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "77de0510f7059711ebc8e76307d0208cbe961eac13c594f0646b2002563d521c",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "05f56f500c96aa46beb1316c5399772be719c30543645ca931bcefb3a372be70",
      "bytes": 652
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "8d8306a63eb426f6a25e60db151fb9e6459965be18b1b4e24e2f7c1449efc10d",
      "bytes": 899
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "7f16e7114284617e520ca97fda03d266de92257ffa1d33a0b7b4808254522d9d",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f2da3ad5f9c1c3063cd501a9d48222004c7aed6e83a5e6bcfa6f0c152fd27c07",
      "bytes": 205682
    }
  ],
  "estimated_tokens": 11747
}
-->

# Durable State Update — Chapter 651

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 651. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 651. Profile updates may replace only one
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
  "chapter": 651,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 651,
    "continuity_sources": [651],
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
    "Jin Taekyung is staying in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "Jin secretly left the Fire Dragon Pavilion quarters at Insi and reached the crowded Outer Palace West Gate wearing a tiger mask.",
    "Heugung sent the arrow-bound missive and contacted Jin while disguised as a thin middle-aged food-stall patron.",
    "Heugung used the Bone-Shrinking Technique to alter his appearance and communicated with Jin through Sound Transmission.",
    "Heugung alleges that Baeksang has colluded with Dark Heaven.",
    "Jin has not disclosed Heugung's allegation or the missive to the Beast Miao King.",
    "Namho, Taishan, and Sama Pyo remained at the Fire Dragon Pavilion quarters while Jin went to the West Gate.",
    "Heugung's public foolishness and infatuation conceal an ability to plan and conduct covert operations."
  ],
  "continuity_sources": [
    650
  ],
  "open_questions": [
    "Is Heugung's allegation that Baeksang colluded with Dark Heaven true?",
    "What evidence does Heugung possess against Baeksang?",
    "Was the arrow intended only to summon Jin, or was Heugung genuinely willing to risk injuring him?",
    "Why is Heugung secretly acting outside Baeksang's apparent control?",
    "When and how should Jin inform the Beast Miao King?"
  ],
  "safe_through": 650,
  "temporary_decisions": [
    "Use Insi for 인시.",
    "Use West Gate for 서문.",
    "Use missive for 전서.",
    "Use Bone-Shrinking Technique for 축골공.",
    "Use Naked Divine Dragon for 노출신룡."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 삼류     | **Third Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 이족 | **Yi people** | One of Nanman's four great tribes. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 축골공 | **Bone-Shrinking Technique** | A martial art that stretches and shrinks bone and flesh to alter the user's appearance. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 650
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 650
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 650
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 650
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Heugung remains publicly entangled with Yohi and Baeksang but secretly contacted Jin Taekyung and alleges that Baeksang has colluded with Dark Heaven.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 650
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 650
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃651화



이 세상에는 심증(心證)만으로는 해결할 수 없는 일이 많다.

이건 내가 평생을 살아온 21세기 현대도, 그에 비하면 사실상 무법지대나 다름없는 무림도 마찬가지다.

하물며 남만이라는 광활한 땅에서 일인지하만인지상(一人之下萬人之上)의 위치에 있는 누군가에 관한 문제라면 말할 것도 없었다.

하지만…….

- 백상 대족장이, 암천과 결탁하고 있네.

“……!”

이렇게 되면 이야기가 좀 달라지지.

내심 중얼거린 나는 무심코 부러트려 버린 젓가락을 내려놓았다.

그 모습을 본 노점상의 늙은 주인이 불만 섞인 표정으로 웅얼거렸지만, 지금 내 모든 신경은 오직 한 사람. 흑웅에게만 쏠려 있었다.

- 방금 한 그 말, 확실합니까?

- 확실하네. 아니, 적어도 내가 생각하기로는 확실한 것 같네.

뭐라고?

나는 저절로 눈살이 찌푸려지는 것을 간신히 참았다.

- 결국 물증이 없다는 뜻으로 들리는데요. 이 문제는 확실한 것 같은, 이 아니라 확실해야 합니다.

- 하, 하지만.

마른침을 꿀꺽 삼킨 흑웅이 재차 전음을 이었다.

- 이것이 자네에게 말해 줄 수 있는 최선일세. 백상 대족장은 그만큼 비밀이 많은 사람이야. 나 역시 남만의 사대 부족 중 하나를 이끄는 대족장이지만…… 그는 내게 그 어떤 문제도 깊게 상의하지 않는다네.

짧은 순간이었지만 확실히 봤다. 마지막 한마디를 내뱉을 때 흑웅의 낯빛을 스치는 어떤 감정을.

그건 분명 모멸감이었다.

아마도 오래전부터 흑웅의 마음속에 켜켜이 쌓여 왔을.

그런 그의 모습을 빤히 바라보던 나는 문득 입술을 달싹였다.

- 그래서입니까?

- 그래서라니? 뭐가 말인가?

- 당신이 따르던 사람을 배반하고 내게 밀서(密書)를 보낸 이유. 이런 이야기를 털어놓는 이유가 백상에 대한 감정 때문이냐고 묻는 겁니다.

- 배, 배반이라니. 그건…….

- 이게 배반이 아니면 내가 한족이 아니라 남만인이지. 그러니까 아니라고 하진 마시고.

정곡을 찔린 듯, 입술을 질끈 깨문 흑웅이 작게 고개를 끄덕였다.

- 그래. 부정하지는 않겠네. 선친께서 정마대전에서 전사하신 직후, 난 코흘리개 시절부터 지금까지 백상 대족장의 그늘 아래서 자랐어. 아니, 보이지 않는 목줄이 채워진 채 끌려다녔다고 해야 옳겠지. 하지만 자네를 만나고자 결심한 것은 그런 이유에서만이 아니었네.

- 그럼 뭡니까?

- 남만을, 내 부족민들을 지키고 싶네.

- ……!

- 내가 기억하는 백상 대족장은 언제나 냉철하고 뛰어난 사람이었지. 그렇기에 결코 자신의 뜻을 굽히지 않을 걸세. 스스로의 선택이 옳다고 생각할 테니까. 하지만 이대로라면…… 남만은 끝장이야.

나는 말 없이 흑웅을 응시했다.

사람이 북적이는 거리 한 귀퉁이에 있는 작은 노점상에서 나눈 이 비밀스러운 대화를, 어디서부터 어디까지 믿어야 할지 감이 잡히지 않았다.

‘믿을 수 있을까.’

의문의 대상은 정보만이 아니었다. 느닷없이 비밀리에 접선해 온 흑웅 역시 포함이었다.

아니, 어떤 면에서는 내가 그를 믿을 수 있느냐가 가장 중요했다. 그래야 아직 그가 자세히 털어놓지 않은 정보 역시 믿을 수 있을 테니.

‘지금까지의 모습은 모두 진심 같았다. 하지만 저 모든 것이 연기라면?’

무림은 앞날을 예측할 수 없을 만큼 변화무쌍하며 치열한 세상이다.

협객. 삼류 왈패. 마두와 위선자. 이 수많은 인간군상이 뒤섞여 서로를 속고 속이고 비수를 뽑아 등을 찌른다.

‘무림에서는 무슨 일이 벌어져도 이상하지 않다.’

내가 조용히 이 상황을 가늠해 보고 있던 그때, 늙은 주인장이 짧은 침묵을 깨트렸다.

탁.

여간 힘에 부치는지, 그가 잘게 떨리는 손으로 내려놓은 대접에서 국물이 흘러넘친다.

고작 철전 몇 푼 하지도 않는 싸구려 소면은 그릇 안에서 제멋대로 뒤엉켜 있었다. 마치 내 머릿속 생각들처럼.

“드디어 나왔군. 우선 국물부터 마셔 보게. 그게 진짜거든.”

흑웅이 애써 밝은 목소리로 입을 열었지만, 빠르게 주위를 훑는 그의 눈동자에는 초조함이 감돌고 있었다.

- 주의하게. 백상 대족장에게는 보이지 않는 눈과 귀가 많아. 나 역시 최소한 한 식경 안에는 돌아가야 의심을 피할 수 있어.

- 혹시 함께 있던 도중에 빠져나온 겁니까?

- 아니. 하지만 늘 가까운 곳에 감시역이 있네. 오래전부터 내 동태를 파악하기 위해 심어 둔 끄나풀이지. 오늘은 안심해도 괜찮겠지만.

그 끄나풀을 심은 이에 대한 주어는 없었지만, 어차피 들으나 마나였다. 뒤에 나올 답은 이미 들은 것이나 다름없었으니까.

‘백상이겠지.’

김이 모락모락 피어오르는 소면을 앞에 두고도 멍 때리는 것만큼 눈에 띄는 짓도 없다.

나는 최대한 자연스럽게 소면을 먹으며 전음을 날렸다.

- 도대체 언제부터 감시당해 왔던 겁니까?

- 글쎄. 그 질문에 대한 답은 나도 잘 모르겠네. 다만 처음으로 눈치를 챈 것은 약관 무렵이었고, 그 후로 이십 년이 넘는 세월 동안 백상 대족장을 경계해 왔지. 비밀리에 축골공(縮骨功)을 익혔던 이유도 그 때문일세. 익히는 과정이 까다롭기는 해도 다른 무공과는 달리 수련의 흔적이 거의 남지 않으니까.

이쯤 되자 나 역시 흑웅에 대한 평가를 일부 수정할 수밖에 없었다.

‘제법인데.’

이미 불혹을 훌쩍 넘은 나이의 그에게 내가 이런 평가를 내리는 것도 웃기지만, 불과 몇 시진 전까지만 해도 사람들 앞에서 헤벌쭉 웃고 다니던 모습과 비교하면 천양지차(天壤之差)나 다름없었다.

‘자기 나름대로 살길을 찾았다, 이건가?’

갑작스럽게 접선해 온 흑웅도 의심스럽긴 매한가지지만, 이야기를 듣다 보니 처음 생각했던 것보다는 더 믿음이 갔다.

아마도 내심 생각했던 것보다 훨씬 괜찮은 소면 맛도 한몫했을 것이다.

후루룩.

진한 국물을 쭉 들이켠 나는, 품에서 철전 몇 개를 꺼내 빈 그릇 옆에 내려놓았다.

그리고 망설임 없이 자리에서 일어난 내 모습에 당황하는 흑웅의 어깨를 툭툭 두드려 주었다.

“당신 말이 맞았소. 이 집 국물 잘하네.”

“그, 그렇다니 다행이오. 한데 지금 어디 가는…….”

“왜? 다 먹었으면 슬슬 일어나야지. 그쪽도 갈 길 바빠 보이는데. 아니오?”

그때, 흑웅의 눈동자가 살짝 커지는 것이 보였다. 아마도 내가 말과 함께 흘려보낸 전음을 들었기 때문일 것이다.

- 따라와요. 거리 두고 천천히.

소면으로 에피타이저를 해결했으니, 이제 메인디쉬를 맛볼 차례다.

- 어디 한번 들어 봅시다. 당신이 지금껏 백상의 곁에서 보고 들었던 모든 것을.



* * *



발 디딜 틈 없이 북적이는 거리.

인파 속으로 스며든 나와 흑웅은 일장의 거리를 둔 채 천천히 이동하기 시작했다.

때로는 허공에서 터지는 폭죽도 구경하고, 자연스럽게 고개를 돌려 거리를 바라보았지만 달싹이는 입술 사이로 흘러나오는 전음은 단 한 시도 다른 곳을 향하지 않았다.

- 거두절미하고 묻겠습니다. 백상이 암천과 결탁한 정황이 있습니까?

- 비록 확실한 물증은 없지만, 지금껏 지켜봐 온 바로는 확실하네.

- 물증이 없다면 그 정도로는 부족합니다.

- 어쩔 수 없었네. 지금까지의 나는 백상 대족장이 쳐 놓은 울타리 안에서 살아가는 가축과 같은 처지였으니.

- 그럼 정확한 시기와 그렇게 짐작했던 이유는요?

- 내 비록 울타리 안의 가축처럼 길러졌으나, 울타리 밖을 엿볼 수조차 없었던 것은 아니라네. 허울뿐이지만 나 역시 이족을 이끄는 대족장이니까 종종 함께 자리할 수 있었지. 아니, 아마도 그는 나를 신경 쓸 것도 없는 놈이라 생각했을지도 모르겠군. 틀린 말도 아니고.

자조 섞인 한 마디와 함께 흑웅의 전음이 이어졌다.

- 자네는 백상 대족장이 어떤 사람인지 알고 있나? 백족에 대해서도?

- 남만에 대해서는 잘 알지 못하지만 믿을 만한 정보원에게 이런저런 이야기들을 들었습니다. 백상에 대해서도 스스로 어느 정도 판단을 내렸고요.

- 판단이라. 재미있군.

- 재미있다니. 뭐가요?

- 간단한 이야기야. 난 아주 어릴 적부터 백상 대족장을 알고 있었는데, 그에 관한 판단을 매번 수정해야 했거든. 해가 지날수록, 머리가 굵어지고 생각하는 것이 많아질수록 그랬지.

- ……!

- 그는 그런 사람일세. 빽빽한 나무와 깊은 늪. 온갖 험지(險地)로 이루어진 이 땅은 비밀이 새어 나가는 것을 용납하지 않지. 예를 들자면…….

흐려지는 말꼬리.

다음 순간 느껴지는 시선에 고개를 돌린 나는, 또렷하게 빛나는 흑웅의 눈동자를 마주할 수 있었다.

- 지금 이 순간에도 남만 어딘가의 비처(秘處)에서 때를 기다리고 있을 백족의 최정예 전사들이라든지.

순간 나도 모르게 발걸음이 우뚝 멈췄다. 최대한 자연스럽게 옆에 놓인 좌판을 향해 고개를 돌린 나는 입술을 달싹였다.

- 계속하십시오.

- 내 선친께서 어떤 분이셨는지 말한 적 있던가? 그분은 인망 두터운 대족장이었고, 한 사람의 뛰어난 전사셨네. 그분을 마음 깊이 따랐던 충복들은 자신들의 목숨을 바쳐 가며 나를 도왔지. 비처에 관한 것 역시 그들의 희생 덕분에 알 수 있었네.

- 정확한 위치를 알고 계십니까?

- 그랬지. 이십 년 전에는.

- ……이십 년 전이라고요?

- 그날 유일하게 돌아왔던 것은 충복들이 아니라, 피로 쓰인 한 통의 전서구였네. 다급해진 나는 며칠 후 맹수 토벌을 핑계 삼아 전서에 적혀 있던 위치로 향했고, 산어귀에 다다르기도 전에 산을 집어삼킨 거대한 불길을 볼 수 있었지.

- ……!

- 그 불길은 달포하고도 칠 주야가 흐른 뒤에야 사그라졌네. 그곳에 남아 있는 것은 잿더미밖에 없었어. 어때, 참 희한한 일이 아닌가?

흑웅은 씁쓸한 어조로 전음을 이어 갔다.

- 충복들이 하나둘씩 죽어 갈 때마다 새로운 사실을 알게 되었지. 백상 대족장이 매달 초하루, 인시와 묘시 사이에 목적지를 알 수 없는 전서를 주고받는다는 것. 또 석 달에 한 번은 홀로 어딘가로 사라진다는 것……. 아, 작년부터는 달에 한 번으로 바뀌었군. 그때 그의 뒤를 쫓았던 이가 내가 믿을 수 있는 마지막 수하였지. 그 후로 다시는 볼 수 없었지만.

그의 이야기가 끝나자 무거운 침묵이 감돌았다.

주위는 즐겁게 떠드는 목소리와 환호로 가득했지만 나와 흑웅만큼은 예외였다.

‘백상과 암천. 암천과 백상. 그리고…….’

흑웅.

이중 무엇이 진실이고, 무엇이 거짓일까.

독무(毒霧)에 휩싸인 것처럼 머릿속이 희끄무레하다.

하지만 그 너머에서는 분명 처음부터 지금까지 줄곧 눈과 마음으로 좇았던 한 사람의 인영이 어른거리고 있었다.

‘백상.’

그리고 아직 모습을 드러내지 않은 또 다른 한 사람.

문득 뇌리를 스치는 이름에, 나는 흑웅을 향해 전음을 흘려보냈다.

- 다른 사람은 어떻습니까?

- 다른 사람이라니. 누굴 말하는 건가?

- 또 다른 대족장. 요희 말입니다.

- ……!

- 줄곧 궁금했습니다. 그녀에 관해서는 한마디도 하지 않는 것이.

스쳐 지나가는 사람들 너머로 덜컥 흔들리는 메마른 신형이 보인다. 허공에서 맞닿은 흑웅의 시선이 가늘게 떨렸다.

- 그, 그녀는 아무런 잘못이 없네.

- 예?

- 그저 잘못된 선택을 한 것뿐이야. 단지 요족을 부흥시키기 위한 일념 하나로…….

서서히 흐려지는 말꼬리. 멍하니 눈을 깜빡이며 흑웅을 바라보던 나는 뒤통수가 얼얼해졌다.

빌어먹을, 이 인간이 설마?

- 설마 그게 다 연기가 아니라 진심이었습니까? 진짜 요희를 좋아해요?

- 좋아하는 게 아닐세. 사랑하는 거지.

- 저기 죄송한데. 혹시 미친 새낍니까?

- …….

미치고 환장하겠네. 진짜.

설마 했는데 요희만 보면 헤벌쭉 웃던 모습이 전부 사실이었다니.

게다가 매직 존슨이 울고 갈 만한 영혼의 실드까지 쳐 주고 자빠졌다.

어이가 없어진 나는 사람들 사이를 비집고 다가가고 싶은 마음을 간신히 참았다. 대신 그에게 윽박지르듯 전음을 날렸다.

- 야율 대협 앞에서도 그렇게 말할 수 있어요? 요희는 잘못 없다고?

- 그래서 자네를 찾아온걸세. 첫 번째로 궁주께서 백상 대족장보다 나를 신뢰하지 않으리라 짐작했고, 두 번째로는 우리 요희를 용서하시지 않을 것 같아서.

- 이야. 우리 요희 이 지랄.

- ……!

- 아, 미안합니다. 근데 진짜 병신 같아요. 어쨌든 느그 요희가 저쪽에 붙었다는 건 잘 알겠습니다.

단어 선택이 마음에 안 드는지 흑웅의 안색이 급격히 굳어 간다.

뭐라 말할 것처럼 입술을 달싹이던 그가 이내 한숨을 내쉬었다.

- 이곳에 나오기 전에 이미 마음을 굳혔네. 자네와 궁주께서 원한다면 당장 내일 대회의에서라도 증인으로 나설 수 있어. 단, 나와 요희의 안전을 보장한다는 약조는 받아야겠네.

전자는 좋은 제안이고, 후자는 찝찝한 제안이다.

그리고 이 두 가지 제안에 유일한 공통점이 있다면, 지금 당장 이 자리에서 내가 결정할 수 없는 문제라는 것이었다.

흑웅이야 그렇다 치고 요희의 경우에는 사실상 변절자에게 면죄부를 주는 셈인데, 내가 뭐 친일파 받아들인 이승만도 아니고 그걸 어떻게 혼자 결정하겠나. 기껏해야 UN군이지.

‘하지만 만약 야수묘왕의 허락이 떨어진다면…….’

그렇게 된다면 앞으로의 일은 일사천리다. 흑웅의 말이 사실일 경우, 남만에서 암천의 위협을 뿌리 뽑는 것으로도 모자라 남만야수궁이라는 특대 고구마가 무림맹에 딸려올 수도 있으니까.

단, 이 모든 것이 사실이라는 전제하에.

- 사실이어야 할 겁니다. 반드시.

스아아악!

오직 한 사람을 옥죄기 위해 흘려보낸 기파(氣波).

도저히 항거할 수 없는 힘을 느낀 흑웅이 창백한 얼굴로 입술을 달싹였다.

- 목숨. 내 목숨을 걸지.

말없이 흑웅을 노려보던 나는 기세를 거두어들였다.

선 채로 숨을 헐떡이던 그는 주위를 둘러본 뒤, 살짝 고개를 끄덕이고는 사람들 사이에 섞여 사라졌다.

어느덧 그가 말했던 한 식경이 흐른 것이다.

“……후.”

그제야 숨이 트인 나도 심호흡과 함께 걸음을 옮겼다.

이 소식을 야수묘왕에게 전하기 전, 처소에 들러 화룡각 대원들과 상의하기 위해서였다.

‘웬수 같은 인간들. 사고나 안 치고 있으면 다행이지.’



* * *



수련을 위해 처소 앞 공터로 나온 사마표는 문득 생각했다.

자신의 타고난 인생이 박복한 것인지, 아니면 빌어먹을 각주 놈이 저지른 업보가 물줄기가 되어 이곳까지 흐른 것인지.

“해서 묻는 것인데.”

스르릉.

서늘한 소리와 함께 흑룡도(黑龍刀)가 모습을 드러낸다. 애병을 든 사마표가 걸음을 떼며 말을 이었다.

“네놈들은 어떻게 생각하느냐?”

파스슥.

공터를 에워싼 풀숲이 흔들렸다.
```

## Final English reading copy

```markdown
# Chapter 651

There are many things in this world that cannot be resolved with mere suspicion.

That was true both of the modern twenty-first century where I had lived my entire life and the Murim, which was practically a lawless land by comparison.

All the more so if the matter concerned someone occupying a position second only to one person and above ten thousand others in the vast land of Nanman.

But…

—Great Chieftain Baeksang has colluded with Dark Heaven.

“…”

That changed things.

I muttered inwardly and set down the chopsticks I had unconsciously snapped in half.

The old owner of the food stall saw what I had done and grumbled with an unhappy expression, but all my attention was focused on a single person: Heugung.

—Are you certain?

—I am. No, at least, I believe I am certain.

What?

I barely managed to stop myself from frowning.

—That sounds like you’re saying there’s no concrete evidence. In that case, this cannot be something you merely believe to be true. It has to be true.

—Ha, but…

Heugung swallowed hard before continuing his Sound Transmission.

—This is the best I can tell you. Great Chieftain Baeksang is a man with that many secrets. I may also be a great chieftain leading one of Nanman’s four great tribes, but… he never discusses anything important with me in depth.

It lasted only a brief moment, but I saw it clearly—the emotion that passed over Heugung’s face when he uttered those last words.

It was unmistakably humiliation.

Perhaps it had been piling up inside him for a very long time.

As I stared at him, my lips parted.

—Is that why?

—Why? What do you mean?

—Is your resentment toward Baeksang the reason you betrayed the person you followed, sent me a secret missive, and told me all of this?

—Betrayal? That’s…—

—If this isn’t betrayal, then I’m not Han Chinese—I’m a Nanman native. So don’t try to deny it.

As if I had hit the mark, Heugung bit his lip hard and gave a small nod.

—Yes. I won’t deny it. After my late father died in the Great Faction War, I grew up under Great Chieftain Baeksang’s shadow, from the time I was a little child with a runny nose until now. No, it would be more accurate to say that I was dragged around with an invisible collar around my neck. But that isn’t the only reason I decided to meet you.

—Then what is?

—I want to protect Nanman. I want to protect my people.

“…”

—The Great Chieftain Baeksang I remember was always coolheaded and exceptional. That is why he will never bend his will. He must believe that his own choices are correct. But if this continues… Nanman is finished.

I silently stared at Heugung.

I had no idea how much of this secret conversation, held at a tiny food stall on a crowded street, I should believe.

*Can I trust him?*

The object of my doubts wasn’t just the information. It also included Heugung himself, who had suddenly contacted me in secret.

No—in some ways, whether I could trust him was the most important thing of all. Only then could I trust the information he had yet to reveal in detail.

*Everything he’s shown me so far seemed sincere. But what if all of it was an act?*

The Murim was a fierce and unpredictable world, too volatile to foresee.

Heroes. Third Rate thugs. Fiends and hypocrites. Countless kinds of people mixed together, deceiving and being deceived, drawing hidden blades and stabbing one another in the back.

*In the Murim, nothing is impossible.*

Just as I was quietly weighing the situation, the old owner broke the silence.

Clack.

The effort seemed almost too much for him; broth spilled over the rim as he set the bowl down with a trembling hand.

The cheap somyeon, which cost no more than a few iron coins, was tangled chaotically inside the bowl.

Just like the thoughts in my head.

“It’s finally here. Try the broth first. That’s the real specialty.”

Heugung spoke in an artificially cheerful voice, but his eyes darted around anxiously as he quickly swept his gaze over the surroundings.

—Be careful. Great Chieftain Baeksang has many unseen eyes and ears. I need to return within half an hour at the latest if I’m to avoid suspicion.

—Did you slip away while you were with him?

—No. But there is always an observer nearby. A plant he placed there long ago to keep track of my movements. Today, at least, you needn’t worry.

He didn’t say who had planted that observer, but there was no point asking.

I already knew the answer.

*Baeksang.*

Nothing would have drawn more attention than staring blankly at a bowl of steaming somyeon.

I ate as naturally as possible while sending him a Sound Transmission.

—How long have you been watched?

—I don’t know the answer to that myself. I first noticed it around the time I came of age, and I’ve been wary of Great Chieftain Baeksang for more than twenty years since then. That is also why I secretly learned the Bone-Shrinking Technique. The process is difficult, but unlike other martial arts, it leaves almost no trace of training.

At this point, I had no choice but to revise my assessment of Heugung.

*Not bad.*

It was funny for me to make that judgment about a man well past forty, but the difference between this Heugung and the man who had been walking around grinning foolishly in front of everyone only a few hours earlier was like the difference between heaven and earth.

*So he found a way to survive on his own terms?*

Heugung’s sudden contact was still suspicious, but after hearing his story, I trusted him more than I had at first.

The fact that the somyeon tasted much better than I had expected probably helped, too.

Slurp.

After drinking down the rich broth, I took a few iron coins from my clothes and placed them beside the empty bowl.

Then I rose without hesitation and patted Heugung’s startled shoulder.

“You were right. This place does make good broth.”

“I-I’m glad to hear it. But where are you going…?”

“Why? If we’ve finished eating, we should get moving. You look like you’re in a hurry to get somewhere, too. Aren’t you?”

At that moment, Heugung’s eyes widened slightly.

He had probably heard the Sound Transmission I let slip along with my words.

—Follow me. Slowly, and keep your distance.

I had dealt with the appetizer using somyeon.

Now it was time to taste the main course.

—Let’s hear it. Everything you’ve seen and heard while standing beside Baeksang all this time.

* * *

The streets were packed so tightly that there was barely room to set foot anywhere.

Heugung and I melted into the crowd and began moving slowly, keeping about ten feet between us.

Now and then, we watched fireworks bursting overhead or casually turned our heads to take in the street.

But the Sound Transmission passing between our moving lips never turned toward anything else for even a moment.

—Let me get straight to the point. Is there any indication that Baeksang has colluded with Dark Heaven?

—Although I have no concrete evidence, I am certain from everything I’ve observed until now.

—That isn’t enough without evidence.

—I had no choice. Until now, I’ve been in the position of livestock living inside the fence Great Chieftain Baeksang built around me.

—Then tell me the exact timing, and why you came to that conclusion.

—Although I was raised like livestock inside that fence, it isn’t as if I was unable to see even a glimpse of what lay outside. I may be a great chieftain in name only, but I still lead one of the tribes, so I was occasionally able to be in his company. No—perhaps he simply thought I was someone not worth worrying about. He wouldn’t have been wrong.

Heugung’s Sound Transmission continued with a self-deprecating edge.

—Do you know what kind of person Great Chieftain Baeksang is? What about the Bai people?

—I don’t know much about Nanman, but I’ve heard various things from a reliable source. I’ve also formed a certain judgment of Baeksang myself.

—A judgment. Interesting.

—What’s interesting about that?

—It’s simple. I’ve known Great Chieftain Baeksang since I was very young, but I had to revise my judgment of him every time. The older I got, the more mature I became, and the more I thought about things, the more often that happened.

“…”

—That is the kind of person he is. This land is made up of dense forests, deep swamps, and all kinds of difficult terrain. It does not tolerate secrets leaking out. For example…

His voice trailed off.

The next moment, I felt someone’s gaze and turned my head.

Heugung’s eyes shone clearly as they met mine.

—The Bai people’s finest warriors, who must even now be waiting for the right moment in some secret refuge somewhere in Nanman.

My feet stopped before I could help it.

I turned my head toward a nearby street stall as naturally as possible and moved my lips.

—Continue.

—Have I ever told you what kind of person my late father was? He was a great chieftain with tremendous popularity, and an outstanding warrior. The loyal retainers who followed him from the bottom of their hearts helped me even at the cost of their own lives. It was thanks to their sacrifice that I learned about the secret refuge.

—Do you know its exact location?

—I did. Twenty years ago.

—…Twenty years ago?

—The only thing that returned that day was not one of my loyal retainers, but a messenger pigeon carrying a missive written in blood. I grew desperate, and a few days later, I used a hunt for ferocious beasts as an excuse to head to the location written in that message. Before I had even reached the foot of the mountain, I saw a massive fire swallowing the entire mountain.

“…”

—The flames did not die down until a month and seven days had passed. Nothing remained there but ashes. What do you think? Isn’t it a truly strange thing?

Heugung continued his Sound Transmission in a bitter tone.

—Every time one of my loyal retainers died, I learned something new. Great Chieftain Baeksang exchanges missives to unknown destinations on the first day of every month, between Insi and the hour of the Rabbit.[^1] He also disappears somewhere alone once every three months… Ah, since last year, that changed to once a month. The person who followed him then was the last subordinate I could trust. I never saw him again after that.

When his story ended, a heavy silence settled between us.

The surroundings were filled with cheerful voices and shouts of excitement, but Heugung and I were exceptions.

*Baeksang and Dark Heaven. Dark Heaven and Baeksang. And…*

*Heugung.*

Which of these was true, and which was false?

My thoughts were hazy, as though I had been swallowed by Poison Mist.

But beyond that haze, I could clearly see the silhouette of one person I had followed with my eyes and heart from the beginning until now.

*Baeksang.*

And one other person who had yet to show themselves.

A name suddenly flashed through my mind, and I sent a Sound Transmission toward Heugung.

—What about the other person?

—The other person? Who are you talking about?

—The other great chieftain. Yohi.

“…”

—I’ve been curious about that for a while. You haven’t said a single word about her.

Beyond the people passing by, I saw Heugung’s gaunt frame jolt. His gaze met mine across the open air, trembling faintly.

—She hasn’t done anything wrong.

—What?

—She merely made the wrong choice. She did it solely out of her determination to revive the Yao people…

His voice gradually faded.

I blinked blankly at Heugung, and the back of my head began to tingle.

*For fuck’s sake. Surely this man didn’t…*

—Don’t tell me none of that was an act. Do you really like Yohi?

—I don’t like her. I love her.

—Excuse me, but are you some kind of crazy bastard?

“…”

This was driving me crazy.

I had suspected as much, but all those foolish grins whenever Yohi appeared had really been genuine.

He had even put up a soul shield strong enough to make Magic Johnson cry.

I barely managed to restrain myself from pushing through the crowd and marching over to him. Instead, I sent a Sound Transmission that was almost a shout.

—Would you say that in front of Sir Yayul, too? That Yohi did nothing wrong?

—That is why I came looking for you. First, I guessed that the Palace Lord would not trust me more than Great Chieftain Baeksang. Second, I thought he would not forgive our Yohi.

—Wow. Listen to this “our Yohi” bullshit.

“…”

—Ah, sorry. But you really are an idiot. Anyway, I understand now. Your Yohi defected to that side.

Heugung’s complexion hardened rapidly, as if he disliked my choice of words.

He moved his lips as though he intended to say something, then let out a sigh.

—Before I came here, I had already made up my mind. If you and the Palace Lord wish it, I can appear as a witness at tomorrow’s Tribal Grand Council. But you must promise to guarantee Yohi’s safety and mine.

The first was a good offer. The second left a bad taste in my mouth.

And if those two offers had one thing in common, it was that neither was something I could decide on my own, here and now.

Heugung was one thing, but in Yohi’s case, granting her safety would essentially mean giving a defector a get-out-of-jail-free card. I wasn’t Syngman Rhee, who had welcomed pro-Japanese collaborators, so how could I decide that alone? At best, I was the U.N. forces.[^2]

*But if the Beast Miao King gave his permission…*

If that happened, everything that followed would proceed at a breakneck pace.

If Heugung’s words were true, we could not only root out Dark Heaven’s threat from Nanman, but might even drag the Nanman Beast Palace into the Murim Alliance as one enormous headache.

But all of that depended on this being true.

—It had better be true. It absolutely must be.

Fsssh!

A wave of qi unleashed solely to bear down on one person.

Heugung felt power that he could not possibly resist. His face turned pale as his lips moved.

—My life. I stake my life on it.

I stared at Heugung in silence, then withdrew my aura.

He stood there panting, looked around, and gave a small nod before melting into the crowd and disappearing.

The half hour he had mentioned had passed.

“…Phew.”

Only then could I breathe freely. I took a deep breath and began walking.

Before reporting this to the Beast Miao King, I planned to stop by the quarters and discuss it with the members of the Fire Dragon Pavilion.

*Those damn men. I’ll consider it a success if they haven’t caused any trouble.*

* * *

Sama Pyo had come out to the clearing in front of the quarters to train when a thought suddenly occurred to him.

Was he simply born unlucky, or had the karma from that damn Pavilion Master’s misdeeds flowed all the way here like a stream?

“And so I ask you…”

Shing.

The Black Dragon Saber emerged with a cold ring.

Sama Pyo took a step forward with his treasured weapon in hand and continued.

“What do you lot think?”

Rustle.

The grass surrounding the clearing shook.

[^1]: Insi is the traditional time period from three to five in the morning; the hour of the Rabbit follows it, from five to seven.

[^2]: Syngman Rhee is often criticized for allowing many collaborators with Imperial Japan to retain influence in post-liberation South Korea.
```
