<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0655.txt",
      "sha256": "9a15797969f4613b14ca7adc0259a7b061bea9e2ae5b4d5de653bdf4c13f8673",
      "bytes": 12987
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3aa695bf53b92d5d94ff28e9e21d14ded0d1abe4480fadb427d646e778695509",
      "bytes": 2177
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a70d22b4ca0b704ca8b47618b5e64460d3cabd6099366e083bc2086d5e0f729d",
      "bytes": 200089
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "5b795defbc388e710fa0b08900d1a67e99a390990f605d5d97793afe237e82b0",
      "bytes": 748
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "8ff6a3973bb440843ee391dfef9db4033092ea2665b33bb8d80e99d58df6d75b",
      "bytes": 766
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "dc1a9c6e94df487fb60b8ab202e1ccde54136716e5322372cd07ca8c9f7d5cae",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "57dc87cd051fd5e66e714895a81bca9d9b6b7dbf5866912268530168b1b08a0c",
      "bytes": 750
    },
    {
      "path": "characters/Namho.md",
      "sha256": "637cfae75d4ebd0a40081d913b6b911c33ee44c65497fd8b8a6ee16b646ec8cc",
      "bytes": 843
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "ea38c85818d2fdc483d60f36de356db0d6d4c4cd9908f4cd166b90e7f3e3e773",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "cbd73fcbb69a90e5952398f662ee8a43669f9abb371858d64d085e068b488cbf",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e1c51468df24b15e30318fcc6adc99254481d44af8e49443afda05aac083a41b",
      "bytes": 206083
    }
  ],
  "estimated_tokens": 10582
}
-->

# Durable State Update — Chapter 655

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 655. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 655. Profile updates may replace only one
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
  "chapter": 655,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 655,
    "continuity_sources": [655],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "Heugung alleges that Baeksang colluded with Dark Heaven, has secretly evaded Baeksang's surveillance for more than twenty years, and used the Bone-Shrinking Technique to meet Jin.",
    "Heugung genuinely loves Yohi and had promised to cooperate with Jin before the assault on the Fire Dragon Pavilion.",
    "The Fire Dragon Pavilion was attacked at night less than half a shichen after Jin left, and patrol warriors were also killed.",
    "Three masked Peak masters attacked the pavilion; they were Nanman infiltrators with tongues severed long ago and died after severing their own heart meridians.",
    "Jin could not identify the attack's organizer because the surviving infiltrator could not speak before dying.",
    "Jin suspects Dark Heaven knew he possessed the Myriad-Poison Ring and arranged the attackers' self-destruction to prevent interrogation.",
    "Baeksang, Yohi, and Heugung remain possible suspects, while Dark Heaven appears to be the broader force behind the assault.",
    "Sama Pyo survived the attack, and Taishan remains fiercely protective of him.",
    "Heugung and Yohi have disappeared from the Inner Palace.",
    "Yayul Mok arrived after the attack and reported the dead patrol warriors and the disappearance of the two great chieftains."
  ],
  "continuity_sources": [
    654
  ],
  "open_questions": [
    "Who ordered the assault on the Fire Dragon Pavilion, and how was Dark Heaven involved?",
    "Where are Heugung and Yohi, and were they involved in the attack or taken by its organizers?",
    "Is Baeksang truly colluding with Dark Heaven, and what evidence can Heugung provide?",
    "Will the Beast Miao King accept Heugung as a witness and guarantee Heugung's and Yohi's safety?"
  ],
  "safe_through": 654,
  "temporary_decisions": [
    "Use Finger Qi for 지풍.",
    "Use heart meridian for 심맥.",
    "Use Dark Heaven hound for 암천의 주구.",
    "Use Force for 강기.",
    "Use moon saber for 월도."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 이족 | **Yi people** | One of Nanman's four great tribes. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 654
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 651
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 654
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 654
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung remains publicly entangled with Baeksang, genuinely loves Yohi, has promised to cooperate with Jin Taekyung, is suspected by Jin of possibly arranging the assault on the Fire Dragon Pavilion, and has disappeared alongside Yohi.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 654
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 654
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 654
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃655화



남만은 중원과 분리된 소국(小國)과 같고, 남만야수궁은 한 나라의 중심이라 할 수 있는 왕궁이다.

당연히 내궁 역시 그 규모가 거대할 수밖에 없었다.

전사, 숙수, 하인, 맹수들을 관리하는 사육사 등 내궁에 머무르는 이들의 머릿수를 모두 합하면 일천에 달하고, 지금처럼 부족 대회의가 열리는 상황에서는 몇 배로 불어난다.

하지만 그 수많은 사람 사이에서도 가장 중요한 이들은 따로 있었다.

바로 네 명의 대족장들이다.

남만에 존재하는 서른두 개 부족 중 가장 강성한 네 개의 부족을 이끌고 있으며, 차기 남만야수궁주가 될 수 있는 실력자들.

그런 만큼 대족장들이 가진 영향력은 막강했고, 궁주를 제외한 세 명의 대족장들은 대대로 특혜를 보장받았다.

쉬쉬쉭!

현재 옆에서 내달리는 야율목이 하는 말처럼.

“아버님을 제외한 모든 부족장은 각 부족의 본거지에 머무르며 사전에 통보를 해야만 내궁에 출입할 수 있지만, 대족장들만큼은 예외다. 그들에게는 자유로운 통행과 함께 내궁의 거처가 주어지지.”

동(東), 서(西), 남(南), 북(北).

북쪽은 대대로 남만야수궁주가 맡았고, 다른 대족장들은 각 방위에 저마다의 거처를 마련했다고 했다.

고위 인물에게 내리는 일종의 관저(官邸)인 동시에, 중원식으로 해석하자면 천자가 휘하 제후에게 왕부(王府)를 여는 것을 허락해 준 셈이다.

하지만 지금 이 순간.

전력을 다해 달려온 나를 기다리고 있던 것은 흥건하게 고여 있는 핏물과 시신, 그리고 누군가에 의해 파괴된 건물의 잔해였다.

“이게 무슨…….”

귓가를 파고드는 남호의 침음성. 나는 전신의 피가 싸늘하게 식는 듯한 느낌을 받으며 고개를 들었다.

부서진 대문 위로 기울어져 있는 목판과 글씨가 보였다.

서요부(西瑤部).

이 장원이 누구의 소유인지 알려 주는 세 글자. 문득 고혹적인 눈웃음을 짓던 어느 여인의 모습이 눈앞을 스쳤다.

‘요족의 대족장. 요희.’

아름다움이라는 단어보다는 요사스럽다는 말이 더 어울리는 여인.

그녀가 정말 오늘 밤 벌어진 습격의 흉수인지는 모르겠지만, 두 가지 사실만은 확실하다.

요희의 취향이 듬뿍 들어간 이 화려한 장원은 더 이상 전처럼 아름답지 않다는 것.

그리고 씻은 듯이 자취를 감추었다는 것.

저벅.

반쯤 부서진 대문을 넘어 들어서자, 곳곳에 널브러진 시신과 맹수들의 사체가 보인다.

각자의 색을 지니고 있었을 형형색색의 꽃밭은 온통 붉은 핏물에 물들어 있었다.

“……시벌.”

참지 못하고 욕설을 중얼거린 그때, 나와 함께 나란히 걸어 들어오는 야율목을 발견한 전사 중 하나가 다가왔다.

“오셨습니까, 소궁주.”

야율목이 굳은 얼굴로 고개를 끄덕였다.

“고생이 많다. 추가로 발견된 점은?”

“없습니다. 시신이 늘었다는 것을 빼면요.”

무거운 목소리로 대답한 전사의 등 뒤로, 나란히 누워 있는 시신들이 보인다. 몇 걸음 떨어지지 않은 우물에서는 서너 명의 전사가 물에 젖어 축 늘어진 호랑이를 끌어 올리는 중이었다.

“지금까지 확인된 숫자만 말씀드리자면, 요족 전사와 그들이 부리는 맹수들을 합쳐 족히 일백을 헤아립니다.”

“생존자는?”

야율목의 물음에 잠시 침묵하던 전사가 대답했다.

“……현재로서는 전무합니다.”

현재로서는?

글쎄. 내 생각에는 앞으로도 전무할 것 같은데.

내심 중얼거린 나는 누워 있는 시신들을 향해 다가갔다.

반사적으로 앞을 막아서려던 전사가 나와 눈이 마주치자 움찔하며 물러났고, 나는 시신들의 몸에 난 상흔(傷痕)을 살폈다.

이들이 어떤 방식으로 의문의 습격자와 싸웠는지, 또 어떻게 죽음을 맞이했는지.

그리고 깨달음과 동시에 야율목의 목소리가 들려왔다.

“알아낸 것이 있나?

동시에 이쪽을 향해 쏠리는 수십여 쌍의 시선을 느끼며, 나는 짤막하게 대꾸했다.

“강기(罡氣).”

“……!”

“……!”

보이지 않는 동요가 퍼져 나간다. 나는 딱딱한 목소리로 말을 이었다.

“상대는 틀림없이 초절정 고수야. 이들 중 대부분은 마지막 순간까지 기습을 눈치채지 못했겠지. 그만큼 무공의 격차가 컸을 테니까.”

초절정은 극소수의 선택받은 자들에게만 허락된 영역.

무수한 고난 끝에 벽을 넘어 위대한 경지로 발돋움한 초절정 고수들은 말 그대로 초인(超人)이 된다.

단 한 번 검을 휘둘러 일류 고수 수십을 죽일 수도 있고, 적수공권으로도 십여 명의 절정 고수를 피떡으로 만들 수 있는 이들.

오늘 밤, 이곳을 습격한 흉수가 바로 그랬다.

‘극히 빠르고 간결하며, 더할 나위 없이 치명적인 솜씨.’

시신들에 남아 있는 상흔을 보자마자 알아차렸다. 흉수는 닳고 닳은 살인자라는 것을.

놈은 결코 부족하지도, 그렇다고 과하지도 않은 힘으로 장원 안의 모든 생명체를 도륙했다.

일 촌(寸)의 깊이만으로도 목숨을 빼앗을 수 있다는 것은 천하 무림의 모두가 아는 사실이지만, 그렇게 일백을 헤아리는 전사와 맹수를 몰살시킬 수 있는 것은 초절정 고수뿐이다.

그리고 이것이 의미하는 바는 분명했다.

- 이 모든 것이, 백상의 소행이라는 거냐?

귓가를 파고드는 나직한 전음(傳音). 나는 충격에 휩싸인 사람들 사이로 딱딱하게 굳어 있는 야율목의 얼굴을 바라보았다.

- 글쎄.

- 글쎄라니?

- 남만에서 이 정도의 경지에 다다른 고수는 둘밖에 없어. 한 명은 알다시피 백상이고. 다른 한 사람은……. 남만의 모두가 잘 아는 사람이지.

순간, 야율목의 얼굴이 새하얗게 질리는 것이 보였다. 소리라도 지를 듯이 입을 크게 벌린 녀석이 입술을 질끈 깨물었다.

- 너는, 이 일의 흉수가 아버님이라고 말하고 싶은 건가?

- 그럴 리가.

- 그렇다면 왜…….

- 이대로면 너무 뻔하다는 얘기지. 최소한 암천이 직접 개입했다는 건 확실하고.

초절정 고수는 중원에서도 극히 드문 수준의 고수지만, 남만에서는 더더욱 그렇다. 개인적으로 백상에 대한 의심이 있다고는 해도 이 정도의 돌대가리는 아니다.

아마도 최소한 암천에 소속된 초절정 고수를 동원했겠지.

‘한 발자국 떨어져서 상황을 지켜보는 것 같더니, 드디어 직접 나선 건가?’

하지만 무엇을 노리고?

머릿속에 떠오른 의문을 내심 중얼거린 나는, 전음 대신 소리 내어 물었다.

“직접 확인해 보고 싶은 게 있는데. 잠깐 자리를 옮길까?”

내 말뜻을 알아들은 야율목이 눈짓하자 주위의 시선들이 떨어져 나간다.

나와 야율목, 그리고 남호까지. 우리 셋은 장원의 중심에 위치한 전각 내부로 들어갔다.

그리고 모두가 예상했던 대로 온갖 진귀한 집기로 가득했을 그곳은 한바탕 폭풍우라도 휩쓸고 지나간 것처럼 엉망이었다.

“한판 제대로 붙은 모양이군.”

남호의 중얼거림에 야율목이 굳은 얼굴로 대답했다.

“하지만 전투는 불과 촌각 만에 끝났소. 상대가 초절정 고수였으니 당연했겠지.”

“자네가 그걸 어찌 아나?”

“짧지만 분명한 굉음이 들렸으니까. 내가 보고를 듣고 도착했을 때는 이미 모든 것이 끝난 후였소. 요서부에 남아 있던 것은 피와 시체, 그리고…….”

드르륵.

커다란 미닫이문을 열어젖힌 야율목이, 가라앉은 목소리로 말을 이었다.

“저것들뿐이었지.”

야율목이 ‘저것들’이라 부른 것은 두 개의 물건이었다.

난장판이 된 방 안에 떨어져 있는 향낭(香囊). 그리고 쓰임새는 그보다 더 귀하고, 끔찍한 향을 풍기는 무언가.

“으음.”

남호는 침음성을 흘렸고, 나는 망설임 없이 걸음을 옮겨 ‘그것’에 손을 댔다. 차갑게 식은 촉감과 함께 끈적한 핏물이 내 손가락을 적신다.

‘이건.’

눈이 달린 사람이라면 누구라도 알아볼 수 있는 물건이다.

‘그것’의 정체는 손목이었다. 깔끔하게 잘려 나간 누군가의 손목.

“누구의 것인지 알아볼 수 있겠나?”

못 알아볼 리가.

투실투실하게 살이 오른 손목을 말없이 응시하던 나는, 야율목의 물음에 나직한 목소리로 중얼거렸다.

“아마도 흑웅이겠지.”

“맞다. 호위 넷을 데리고 요희 대족장을 찾았다더군. 동이부(東夷部)에서 확인해 주었다.”

요족이 서쪽에 서요부를 세웠다면, 흑웅이 이끄는 이족은 동쪽에 자리 잡아 동이부를 세운 모양이었다. 나는 흑웅의 손목을 내려놓으며 물었다.

“그때 시각은?”

“반 시진은 넘지 않았고, 한 식경은 족히 지났다더군.”

대충 시간을 가늠해 보니 나와 헤어진 직후다. 우선 바로 동이부로 갔다가 요희를 찾아간 것이 틀림없었다.

‘……이 미친 사랑꾼 새끼. 그새를 못 참고.’

나는 입 밖으로 튀어나오려는 욕설을 참기 위해 안간힘을 써야 했다. 지금은 냉정해야 할 때다.

아직 흑웅이 요희를 찾아간 이유도 모를뿐더러, 죽음이 확인되지 않은 이상은 모두를 의심해 봐야 했으니까.

“흑웅이 데려왔다는 호위들은?”

“죽었다. 다른 요족 전사들과 함께.”

그럼 그렇지, 씨발.

혹시나 해서 물어본 건데, 역시는 역시다.

“후우.”

깊은 한숨을 내쉰 나는 방 안을 천천히 살폈다.

난장판이 된 내부에는 저항의 흔적이 곳곳에 남아 있었고, 아마도 강력한 장력(掌力)에 의해 무너졌을 벽면 너머에는 아직 화려한 모습을 유지하고 있는 후원이 보였다.

그곳에 남아 있는 아주 희미한 족적(足跡)도 함께.

‘신속하게 두 사람을 제압하고, 후원을 통해 빠져나갔군.’

비록 흔적이 너무 희미한 탓에 주인을 알아볼 수는 없지만, 족적을 통해 한 가지만큼은 확실해졌다.

흑웅이나 요희, 두 사람 중 하나가 벌인 자작극이 아니라 제삼자가 개입했다는 것.

불과 한 식경 전, 이 자리에는 적어도 세 사람이 있었다.

‘그중 한 사람은 당연히 초절정 고수고.’

그렇다면 이 족적의 주인은 누구일까. 남천마후? 아니면 그녀가 거느리고 있는 암천의 고수?

잠시 생각해 보던 나는 이내 고개를 저었다.

내가 잔뼈 굵은 노강호도 아니고, 이 정도 단서로 얻을 수 있는 정보에는 한계가 있었다.

내 옆에는 은영각 요원으로 활동하며 수많은 정보를 접한 남호가 있긴 하지만, 그건 마두의 용모파기나 외적인 특징에 한해서일 뿐이다.

‘결국 무공과 식견, 둘 다 높은 수준에 있는 사람이 필요하다는 건데.’

당장 머릿속에 떠오르는 이름은 두 개뿐이었고, 그중 하나는 도무지 믿지 못할 사람이다.

생각을 끝마친 나는 야율목을 향해 입을 열었다.

“야율 대협께서는 언제 오시는 거지?”

“이미 수하를 시켜 기별을 넣었다. 지금쯤이면 다른 족장들과 함께 오고 계시겠지.”

듣던 중 반가운 소식이다. 현장 보존을 위해 흑웅의 손목을 제자리에 놔둔 나는 요희가 남긴 행낭의 냄새를 맡았다.

비단 주머니의 옆구리가 터져서인지, 무취(無臭)에 가까운 희미한 향만이 감돌고 있었다.

‘밝혀 낸다. 반드시.’

그리고 내가 내심 중얼거리던 그 순간.

전각 밖에서 소란스러운 소리가 들렸다.

“드디어 오신 모양이군. 아버님이시라면 흉수의 정체를 알 수도 있을 거다.”

하지만 전각을 나서기도 전, 나는 야율목의 말이 틀렸다는 사실을 알아차릴 수 있었다.

가장 먼저 도착한 것은 야수묘왕이 아니었고, 그가 말한 흉수의 정체는 내가 예상치 못했던 누군가였다.

“죄인이 제 발로 나오는군.”

무미건조한 백상의 목소리를 듣는 순간, 나는 깨달았다.

지금 남만에서 이와 같은 일을 벌일 수 있는 초절정 고수는, 백상과 야수묘왕뿐만이 아니라는 것을.
```

## Final English reading copy

```markdown
# Chapter 655

Nanman was like a small country separated from the Central Plains, and the Nanman Beast Palace could be considered the royal palace at the heart of that country.

Naturally, the Inner Palace was enormous as well.

When the warriors, cooks, servants, beast keepers, and everyone else who lived in the Inner Palace were counted together, their number reached a thousand. And whenever the Tribal Grand Council was held, that number swelled several times over.

But even among all those people, there were some who mattered more than the rest.

The four great chieftains.

They led the four strongest tribes among the thirty-two tribes of Nanman and possessed enough power to become the next Palace Lord of the Nanman Beast Palace.

As befitted their position, the great chieftains wielded tremendous influence. Apart from the Palace Lord, the other three great chieftains had been guaranteed special privileges for generations.

Whoosh!

Just as Yayul Mok, running beside me, was explaining.

“Every chieftain other than Father remains at their tribe’s main base and must notify the palace in advance before entering the Inner Palace. But the great chieftains are exceptions. They have free passage, as well as residences within the Inner Palace.”

East, west, south, and north.

The northern residence had traditionally belonged to the Palace Lord of the Nanman Beast Palace, while the other great chieftains had each established their own residence in a different direction.

They were a kind of official residence granted to high-ranking figures. In Central Plains terms, it was as though the Son of Heaven had allowed his vassal princes to establish their own princely residences.

But what awaited me at that moment, after I had run there at full speed, was a pool of blood spread across the ground, corpses, and the wreckage of buildings destroyed by someone.

“What the…”

Namho’s groan pierced my ears. I raised my head, feeling as though all the blood in my body had turned cold.

A wooden plaque tilted over the shattered gate, with three characters written on it.

Western Yao Estate.

The three words revealed who owned the estate. For a moment, the image of a woman with captivating eyes curved into a smile flashed before me.

*The great chieftain of the Yao people. Yohi.*

She was a woman for whom the word bewitching suited her better than beautiful.

I did not know whether she was truly the culprit behind the attack that had taken place tonight, but two things were certain.

The splendid estate, so thoroughly filled with Yohi’s tastes, was no longer beautiful as it had once been.

And she had vanished without a trace.

Step.

As I crossed the half-destroyed gate, I saw corpses scattered everywhere, along with the bodies of beasts.

The colorful flower beds, which must once have possessed every shade imaginable, had been soaked in red blood.

“…Damn it.”

Just as I muttered the curse under my breath, one of the warriors who had spotted Yayul Mok walking beside me approached.

“Have you arrived, Young Palace Lord?”

Yayul Mok nodded with a grim expression.

“You’ve worked hard. Have you found anything else?”

“No. Apart from the number of corpses increasing.”

Beyond the warrior’s back, I saw bodies lying side by side. Not far away, three or four warriors were pulling a tiger out of a well, its drenched body hanging limp.

“To tell you only the number confirmed so far, there are at least a hundred Yao warriors and beasts under their command.”

“Any survivors?”

The warrior was silent for a moment before answering Yayul Mok’s question.

“…At present, there are none.”

*At present?*

*Well. I think there won’t be any in the future either.*

I muttered inwardly as I approached the bodies.

One of the warriors reflexively tried to block my path, but when our eyes met, he flinched and stepped aside. I examined the wounds on the corpses.

How they had fought the mysterious attackers.

And how they had met their deaths.

Then, just as I realized something, I heard Yayul Mok’s voice.

“Did you find anything?”

At the same time, I felt dozens of pairs of eyes turn toward me and answered briefly.

“Force.”

“……!”

“……!”

Invisible agitation spread through the crowd. I continued in a rigid voice.

“The attacker was undoubtedly a Supreme Peak master. Most of these people probably didn’t notice the ambush until the very last moment. That’s how vast the gap in martial arts must have been.”

The Supreme Peak realm was a domain granted only to a tiny number of chosen individuals.

After countless hardships, Supreme Peak masters crossed the wall and rose into a great realm. They became superhuman in the truest sense of the word.

With a single swing of the sword, they could kill dozens of First Rate masters. Even with their bare hands, they could turn a dozen Peak masters into bloody pulp.

The culprit who had attacked this place tonight had been exactly that kind of person.

*Extremely fast and simple, yet utterly lethal.*

I had realized it the moment I saw the wounds left on the bodies. The culprit was a thoroughly seasoned killer.

With neither too little nor too much force, they had slaughtered every living thing inside the estate.

Everyone in the Murim knew that a depth of one inch was enough to take a life. But only a Supreme Peak master could massacre a hundred warriors and beasts.

And what that meant was clear.

—Are you saying Baeksang did all this?

A low Sound Transmission slipped into my ear. I looked at Yayul Mok’s face, stiff with shock among the gathered people.

—Who knows?

—What do you mean, who knows?

—There are only two masters in Nanman who have reached this level. One is Baeksang, as you know. The other is… someone everyone in Nanman knows well.

For an instant, I saw Yayul Mok’s face turn deathly pale. He opened his mouth as though he were about to shout, then bit down hard on his lip.

—Are you saying Father is the culprit behind this?

—No way.

—Then why…

—I’m saying it would be too obvious if it were that simple. At the very least, Dark Heaven’s direct involvement is certain.

A Supreme Peak master was exceedingly rare even in the Central Plains, but even more so in Nanman. Even if I personally suspected Baeksang, he wasn’t this much of a blockhead.

They had probably mobilized at least one Supreme Peak master belonging to Dark Heaven.

*They seemed content to watch the situation from a step away. Have they finally decided to act directly?*

*But what are they after?*

I muttered the question inwardly, then asked aloud instead of using Sound Transmission.

“There’s something I want to check personally. Should we move somewhere else for a moment?”

Yayul Mok understood what I meant and gave a signal with his eyes. The surrounding gazes fell away.

The three of us—Yayul Mok, Namho, and I—entered the pavilion at the center of the estate.

And the interior, which everyone had expected to be filled with all kinds of rare furnishings, was a complete mess, as though a storm had swept through it.

“Looks like they had a proper fight.”

At Namho’s mutter, Yayul Mok answered with a grim expression.

“But the battle ended in a matter of moments. That was only natural, since the opponent was a Supreme Peak master.”

“How do you know?”

“Because I heard a short but unmistakable boom. By the time I heard the report and arrived, everything was already over. All that remained in the Western Yao Estate was blood, corpses, and…”

Creak.

Yayul Mok flung open a large sliding door and continued in a subdued voice.

“Those.”

The things he called “those” were two objects.

A scent pouch lying on the floor of the wrecked room.

And something whose use was more valuable than the pouch’s, and which gave off a terrible smell.

“Hmm.”

Namho groaned, while I walked over without hesitation and touched *it*. The cold sensation of flesh gone cold met my fingers, and sticky blood dampened them.

*This is…*

Anyone with eyes could identify the object.

*It* was a wrist.

Someone’s wrist, cleanly severed.

“Can you tell whose it is?”

How could I not?

I stared silently at the plump wrist as Yayul Mok asked the question, then muttered in a low voice,

“It’s probably Heugung’s.”

“You’re right. I heard he came to find the great chieftain Yohi with four guards. The Eastern Yi Tribe confirmed it.”

If the Yao people had established the Western Yao Estate in the west, then the Yi people led by Heugung must have settled in the east and established the Eastern Yi Estate. I set down Heugung’s wrist and asked,

“What time was that?”

“They said it had been less than half a shichen, but at least half an hour had passed.”

I roughly calculated the time. It had been right after Heugung and I parted. He must have gone straight to the Eastern Yi Tribe first, then come to find Yohi.

*…That lovesick bastard. He couldn’t even wait that long.*

I had to struggle to keep the curse from bursting out of my mouth. This was no time to lose my composure.

I still did not know why Heugung had gone to find Yohi. And until his death had been confirmed, I had to suspect everyone.

“What about the guards Heugung brought?”

“They’re dead. Along with the other Yao warriors.”

*Of course they are. Fuck.*

I had asked just in case, but the expected answer was still the expected answer.

“Phew.”

After letting out a deep sigh, I slowly surveyed the room.

Signs of resistance remained throughout the wrecked interior. Beyond a wall that had probably collapsed beneath powerful palm force, I could see a rear garden that had retained its splendid appearance.

And faint footprints remained there as well.

*They subdued the two of them quickly, then escaped through the rear garden.*

The traces were too faint to identify their owner, but they made one thing certain.

This had not been a staged attack carried out by either Heugung or Yohi. A third party had intervened.

Less than half an hour ago, there had been at least three people in this place.

*One of them was naturally a Supreme Peak master.*

Then who did the footprints belong to?

The Southern Heaven Demon Empress?

Or one of the Dark Heaven masters under her command?

After thinking for a moment, I shook my head.

I was not some battle-hardened old veteran of the martial world, and there was a limit to how much information I could obtain from clues like these.

Namho, who had spent his time as an agent of the Hidden Shadow Pavilion and encountered countless pieces of information, was beside me. But his knowledge was limited to descriptions of fiends’ appearances and outward characteristics.

*In the end, I need someone with both a high level of martial arts and a high level of insight.*

Only two names came to mind immediately, and one of them was someone I could never bring myself to trust.

After finishing my thoughts, I turned to Yayul Mok.

“When will Great Hero Yayul arrive?”

“I’ve already sent someone to notify him. By now, he should be on his way with the other chieftains.”

That was welcome news.

For the sake of preserving the scene, I returned Heugung’s wrist to its original place, then smelled the pouch Yohi had left behind.

Perhaps because the side of the silk pouch had split, only the faintest scent lingered. It was almost odorless.

*I’ll uncover the truth. I have to.*

And at that very moment, when I was muttering inwardly—

A commotion arose outside the pavilion.

“Father must have arrived at last. If it’s him, he may know the culprit’s identity.”

But before I could even leave the pavilion, I realized that Yayul Mok was wrong.

The first person to arrive was not the Beast Miao King, and the identity of the culprit he mentioned belonged to someone I had never expected.

“The guilty party is coming out on his own.”

The moment I heard Baeksang’s emotionless voice, I understood.

The Supreme Peak masters capable of carrying out something like this in Nanman were not limited to Baeksang and the Beast Miao King.
```
