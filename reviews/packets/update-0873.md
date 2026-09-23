<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0873.txt",
      "sha256": "5ec00a1cca7cc0c43f71307f0f98406ae22632135ae3b13c1b866d93f4478893",
      "bytes": 14145
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5d4355be379fafe1ad066b0dd0d8e694ea3f623a2b9ffed03860d0526d0481f5",
      "bytes": 1384
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3291b7833512bf663761c7378a7587b0bd5178a4c5aa15c6bd322bfc5ce0ac8f",
      "bytes": 229780
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "06bc3f6443ad35376917d8f23119c73454d7e0551bf60ed0ab3e2f30303a9006",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5ac4b5e7751897533ce799719be3577d3810fc8074a8c34d491f03258727e87b",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "fffab9720ee83a1789e4c393a0a153316d84167e88465ac3184cfbbb6207283b",
      "bytes": 854
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bf25eb826fd5ae829a0544e7f70adb23306a1aa69a934d735cb18051e0f0dc4c",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "245dd906e02afa491e438516f2e6af7583a4dd83cdb6a471292d514c45eff79a",
      "bytes": 622
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "effd4cf9651a8be674f016aeb7b99b86110d76264f39ce99ea9719cf4c4ff321",
      "bytes": 801
    },
    {
      "path": "characters/Masked Man.md",
      "sha256": "65e98b0abb0053c09e50357fd705460a3e2b29bcbceb1678b7b68cf8ff840ffc",
      "bytes": 683
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "da595e18496c201a3a3d0aaa4c3f1311f4d5b555e34fb63e83975db61e5940ca",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "501c993e4d47803cfa79fce01fdc23b1e965702fa1baed2c12e6d55ec01b4fc6",
      "bytes": 257444
    }
  ],
  "estimated_tokens": 11376
}
-->

# Durable State Update — Chapter 873

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
1 and safe_through 873. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 873. Profile updates may replace only one
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
  "chapter": 873,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 873,
    "continuity_sources": [873],
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
    "Taekyung and Prince Shangshan are in the Emperor’s bedchamber; the guide is the Emperor, a Supreme Peak master who concealed his strength and identity from Ma Sanbao.",
    "The Emperor knows Taekyung is connected to the Slaughter Saint and demands that Taekyung address him with fear and awe.",
    "The Emperor has summoned Prince Shangshan, his twelve-year-old younger brother, and said he will take care of him; Taekyung doubts his intentions.",
    "Ma Sanbao is secretly in the palace and leads a group seeking to enthrone Prince Shangshan; Taekyung has not accepted Ma Sanbao’s offer to help.",
    "Taekyung’s System and Inventory remain unavailable, and his condition worsens without the Divine Physician’s pills."
  ],
  "continuity_sources": [
    871,
    872
  ],
  "open_questions": [
    "What does the Emperor intend for Prince Shangshan and Taekyung?",
    "Will Taekyung agree to help Ma Sanbao enthrone Prince Shangshan, and what would the plan require?",
    "What do the twin Supreme Peak masters want, and why have they blocked the procession?",
    "What does Ma Sanbao know about Dark Heaven, and what reward is he offering?"
  ],
  "safe_through": 872,
  "temporary_decisions": [
    "Render 흠천감 as “Imperial Astronomical Bureau.”",
    "Render 형부 as “Ministry of Punishments.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 살성     | **Slaughter Saint**           | —              |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 살기     | **killing intent**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 복면인 | **Masked Man** | The Southern Heaven Demon Empress's trained hunting dog; identity remains unknown. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 똥개 | **Ddong Gae** | Taekyung's mocking misremembering of Hwang Gae's name. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 주원공 | opponent to exiled imperial relative | you | casual and mocking | Uses 네놈 and the 주인공/주원공 wordplay while ordering Ju Wongong down. |
| 주원공 | 진태경 | Qingxia Hall young master to Great Hero | Great Hero Jin | imperious, then deferential | Initially uses 네놈 and 역적놈아 while asserting imperial authority, then switches to 진 대협 and respectful forms after seeing Prince Shangshan's token. |
| 진태경 | 복면인 | hostile combatant to unknown hostile combatant | you | blunt, hostile, and incredulous | Jin directly questions the masked man about his identity and his relationship with the Great Snow Fiend. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 872
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 872
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 872
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 871
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 871
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 850
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and distant imperial relative who, while still under punishment, has been temporarily appointed acting City Lord of Sichuan Province by imperial order.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor, and Jin Taekyung is the benefactor who saved his life and can leverage Wongong’s temporary office.

### Masked Man.md

# Masked Man (복면인)

- **Safe through:** Chapter 707
- **Aliases:** None
- **Role:** The Masked Man is the Southern Heaven Demon Empress's trained hunting dog; after being crushed beneath a massive boulder in the Inner Palace ruins, he remains capable of twitching while awaiting his abnormal recovery.
- **Personality:** The Masked Man is emotionless, silent, and indifferent to extreme bodily damage.
- **Voice:** No spoken voice has been established.
- **Relationships:** He serves the Southern Heaven Demon Empress as her hunting dog; his identity and relationship with the Great Snow Fiend remain unknown.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 872
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him. The Emperor regards him warily but says he will take care of him.

## Korean source

```text
＃873화



같은 말이라도 누구의 입에서 나왔는지, 어떤 상황인지에 따라 그 의미가 다르다.

지금 이 순간, 황제가 내뱉은 말의 내용 역시 마찬가지였다.

“지금부터는, 짐이 널 보살펴 주겠다.”

“……!”

생각지도 못한 그 말에 상산왕은 엎드린 상태에서 번쩍 고개를 쳐들었고, 나는 입술 사이를 비집고 흘러나오는 침음성을 참지 못했다.

“음.”

아마도 그 때문일 것이다.

자신의 발치에 오체투지한 상산왕을 굽어보던 황제의 시선이 내게로 옮겨진 것은.

“무슨 할 말이라도 있느냐?”

할 말이라, 많지.

하지만 상대는 대륙의 지배자인 황제다. 나는 한쪽 무릎을 꿇으며 최대한 예의 바른 어투로 대답했다.

“외람되지만 한 말씀 드려도 되겠습니까, 폐하.”

“스스로 외람된다 생각하는 말이라면 입 밖에 내지 않는 것이 좋겠지. 그 목이 계속해서 붙어 있길 바란다면 말이다.”

“……!”

“허나 좋다. 어디 한번 지껄여 보거라. 지난 십여 년간 짐의 인내심이 얼마나 늘었는지 알아보는 것도 나쁘지 않겠지.”

권력자의 변덕은 종종 인내라는 단어로 포장되고는 한다.

바로 지금처럼.

‘아주 갖고 노는군.’

나는 재미있는 장난감을 발견한 아이처럼 눈을 반짝이는 황제를 보며 살짝 고개를 숙였다. 나도 모르게 악물어진 잇새를 감추기 위해서였다.

과연 저 광오한 황제의 인내는 어디까지일까.

만약 그가 정한 보이지 않는 선을 넘는다면, 내가 그 결과를 감당할 수 있을까.

문득 그런 의문들이 뇌리를 스쳤으나, 지금은 어떻게든 상산왕을 향해 뻗은 황제의 마수(魔手)를 쳐내야 할 때였다.

‘침착하자.’

작게 심호흡한 나는 천천히 입을 열었다.

“폐하의 뜻은 참으로 황송하지만, 상산왕 전하께서는 이미 충신들의 보살핌을 충분히 받고 계십니다. 아니, 더 이상 누구의 보살핌도 필요하지 않을지도 모르지요.”

“갑자기 예법이 늘었구나. 말에 뼈를 감추는 법은 아직 한참이나 미숙하지만.”

비웃는 표정으로 나를 바라본 황제가 말을 이었다.

“짐이 묻건대, 앞서 말했던 충신이 대관절 누구냐. 음흉하기 그지없는 환관? 아니면 대국의 법도를 무시하고 천하를 종횡하는 강호의 무뢰배?”

전자가 홍진이고 후자가 나라는 것쯤은 지나가는 똥개도 안다.

그러나 나는 동요하지 않고 길게 읍하며 대답했다.

“황공하오나 폐하께서 말씀처럼 저는 강호에 속한 몸입니다. 가문과 사문이라는 뿌리가 있지요.”

“내 아우의 신하가 아니라는 뜻이군. 그렇다면 무슨 자격으로 감히 짐의 앞에서 세 치 혓바닥을 놀리는 것인가?”

“비록 신하는 아니지만, 빈객(賓客)의 자격으로 상산왕 전하의 부름을 받았고, 또 폐하께서 허락하셨기에 이리 말씀드리는 것입니다.”

“점점 재미있어지는구나. 허나 축생(畜生)에게 의복을 입힌다 한들 사람이 될까. 어울리지도 않는 쓸데없는 허례허식에 짐의 귀중한 시간을 낭비하지 말고 본론을 말하라. 짧고, 간단하게.”

짧고 간단하게.

듣던 중 반가운 소리다.

하지만 지금은 만약의 상황을 대비해서라도 한 번 더 굽혀야 할 때. 나는 부드러운 융단을 내려다보며 말했다.

“어찌 그럴 수 있겠습니까.”

“일각(一刻)이면 충분하겠지.”

“예?”

“일각 동안은 네가 저지르는 무례를 용서할 테니 거리낌 없이 답하라. 이건 황명이다.”

됐다.

보험을 든 나는 그제야 푹 숙이고 있던 고개를 들었다. 그리고 황제를 바라보며 혀끝에서만 맴돌던 그 한 마디를 내뱉었다.

“이미 알고 계시지 않습니까.”

“뭐라?”

“상산왕 전하는 폐하의 보살핌 없이도 이리 훌륭하게 장성하셨습니다. 과거에도 그러했고, 앞으로도 그럴 겁니다.”

“……!”

황제의 눈동자가 번뜩인 그 순간.

솨아아악!

보이지 않는 칼날 같은 살기가 사방에서 뻗어 나와 나를 휘감았다.

이미 한 차례 모습을 드러낸 바 있는 수십여 명의 친위대. 아니 살수들이 동시에 쏘아 보낸 살기였다.

비록 일신에 지닌 무위는 절정이지만 살수로서의 역량은 초절정에 달하는 실력자들.

만약 저들이 목숨을 걸고 평생 연마한 일격필살(一擊必殺)의 살초를 쏟아낸다면 나 역시 결코 무사할 수 없다.

그러나 우려하던 일은 끝까지 벌어지지 않았다.

나를 향해 쏟아질 검광(劍光)보다 앞서 올라간 황제의 손이 그들을 가로막았기 때문이었다.

스륵.

사방의 어둠이 일렁인다.

당장이라도 허공에서 뚝 떨어져 내려 내 몸을 난자할 것 같던 살수들을 제지한 황제가 가늘게 뜬 눈으로 나를 응시했다.

“짐의 보살핌이 필요 없다?”

“예.”

“상산왕이 아직 열둘밖에 되지 않은 어린아이라는 것을 모르느냐?”

“알고 있습니다.”

“한데 어찌하여?”

“열둘밖에 되지 않은 그 아이가, 나는 새도 떨어트린다는 금의위 지휘사에게 호통을 쳤기 때문입니다.”

“……!”

“만약 그조차 누군가 시킨 일이라면 상산왕 전하께서는 아직 보살핌이 필요한 어린아이가 맞을 겁니다. 하지만 그 자리의 누구도 전하께 그리하라 조언한 적이 없습니다.”

상산왕 스스로 결정했고, 당당하게 행했다.

그것이 날 때부터 타고난 것인지, 혹은 환경에 의해 차츰 길러졌는지는 모르지만 이는 곧 어른의 자격이다.

아무런 대가 없이 주어지는 시간 속에서 나이만 먹은 성인들조차 할 수 없는 일을, 열셋의 상산왕은 이미 홀로 입증해 보였다.

“오랜 시간을 함께한 도지휘동지 홍진도 폐하께서 그러시듯 전하를 어린아이 취급하지만, 제 생각은 다릅니다. 적어도 제가 어릴 적에는 그런 건 꿈도 꾸지 못했거든요.”

“당연히 그랬겠지. 네놈은 황족도, 왕도 아니었으니.”

나는 어깨를 으쓱해 보이며 대답했다.

“제가 우연히 알게 된 황족이 한 분 계신데, 장담컨대 그분보다 상산왕 전하께서 열 배는 더 어른스럽습니다.”

“황족? 주원공을 말하는 것이냐?”

“역시 아시는군요.”

살성에 관한 비밀도 알고 있는 황제다.

나에 대한 정보를 얼마나 깊게 파고들었는지는 모르지만 몇 안 되는 황족 중 하나와 얽혀 있다는 것쯤은 그에게 있어 정보 축에도 들지 못한다.

대뜸 흘러나온 주원공의 이야기에 황제는 눈살을 찌푸렸다.

“모든 것은 결국 나이가 아니라 신분과 권위에서 나오는 것이다. 만약 이 아이가 주원공처럼 방계황족에 불과했다면, 백연에게 그토록 큰소리를 칠 수 있었을 것 같으냐?”

“애초에 일어나지 않은 일을 논하는 것만큼 무의미한 일도 없다고 들었습니다. 그리고 자신에게 주어진 것을 최대한으로 활용하는 것도 어린아이가 할 수 있는 일은 아니지요.”

막힘없이 흘러나오는 대답에 황제가 작게 혀를 찼다.

“혓바닥이 제법 매끄럽구나.”

“제 성명절기(成名絕技) 중 하나입니다.”

“한데 과연 그 성명절기로 황명(皇命)을 이겨 낼 수 있을까?”

“예?”

“짐이 이 자리에서 당장 황명으로 상산왕에게 주어진 산서성 임지를 철회하고, 관내후(關內侯)에 봉하여 내 곁에 둔다면 어찌하겠느냐?”

“……!”

개새끼가 말싸움 개같이 하네.

‘황명이 무슨 씨벌 원기옥도 아니고.’

당장이라도 입 밖으로 튀어나오려는 쌍욕을 꾹 참은 내가 되물었다.

“만약 그렇게 된다면, 상산왕 전하의 거취는 어찌 되시는 겁니까.”

어쩌면 선을 넘을 수도 있는 말이었다. 강호의 무뢰배 따위가 감히 그걸 알아서 뭐 어쩌겠냐 윽박질러도 딱히 대꾸할 말이 없을 정도로.

그러나 황제는 마치 어디까지 선을 넘는지 지켜보려는 심판처럼 선선히 대답해 주었다.

“본래 있어야 할 곳으로 돌아오는 것이다. 황궁에 머무르며 훌륭한 스승 아래에서 학문을 수양하고, 척박한 산서성과는 비교도 할 수 없는 좋은 환경에서 충직한 궁인들의 섬김을 받겠지.”

“혹시, 그 안에 홍진도 포함이 됩니까?”

“짐은 분명 충직한 궁인들이라 했다. 그자와 같은 음흉한 환관이 아니라.”

황제의 말은 하나만 맞고, 나머지는 모조리 틀렸다.

황궁은 본래 상산왕이 있어야 할 곳이 맞으나, 그를 가르치는 스승이며 궁인들은 모조리 황제의 사람들일 것이다.

그리고…….

‘황제의 뜻에 따라 상산왕의 일거수일투족을 감시하고, 명령만 떨어진다면 무슨 짓이든 하겠지.’

설령 그 명령이 암살이라 하더라도.

생각이 여기까지 이르자 머릿속이 차갑게 식었다.

“황공하오나, 폐하께서 이렇게까지 하시는 이유가 무엇입니까?”

황제가 재미있다는 듯 입꼬리를 말아 올리며 대답했다.

“그것이 순리(順理)니까.”

“순리?”

“형이 되어 하나뿐인 아우를 챙기겠다는데, 다른 이유가 필요한가?”

“그럴 리가요. 다만 조금 의문이긴 합니다.”

“무엇이 말이냐?”

“그 하나뿐인 아우를 십 년이 넘도록 보살피지 않으셨던 폐하께서, 왜 갑자기 뒤늦게 형 노릇을 하시려는지.”

차차차창!

그야말로 한순간이었다. 명령이 떨어지기도 전에 다시 모습을 드러낸 살수들이 나를 빽빽하게 에워싼 것은.

그리고 그중 한 사람의 새카만 복면 너머로 으르렁거리는 듯한 목소리가 흘러나왔다.

“정녕 죽고 싶은 것이냐.”

하지만 나는 대답하지 않았다. 단지 뜻 모를 표정을 짓고 있는 황제를 바라보며 담담한 어조로 입을 열었다.

“아직 일각이 지나지 않았습니다만.”

“놈!”

“폐하께서 직접 약조하셨습니다. 일각 동안은 어떤 무례도 용서하시겠다고. 저는 황명에 따라 제 생각을 솔직히 말씀드린 것뿐입니다.”

“그 요사스러운 주둥이 닥쳐라! 네놈이 감히……!”

서걱.

서늘하면서도 뜨거운 통증. 이미 앞서 한 번 목에 새겨진 것보다도 깊은 상처와 함께 핏물이 목을 타고 흘러내린 그때였다.

“폐하!”

내내 석상처럼 굳어 있던 상산왕의 외침이었다.

살수들에게 둘러싸인 내 모습을 본 그는 자신의 하나뿐인 형님을 향해 다급하게 말을 이었다.

“태원진가의 진태경은 제 빈객이자 벗입니다! 저자를 살려 주시옵소서! 부디 그의 무례를 용서하소서!”

쿵! 쿵! 쿠웅!

말릴 틈도 없었다. 오체투지한 채 스스로 지면에 이마를 부딪히는 어린 왕의 모습에 나는 입술을 깨물었고, 그 광경을 오연히 굽어보던 황제는 불현듯 입을 열었다.

“그만.”

그 한 마디에 모든 것이 멈췄다.

느리지만 조금씩 내 목줄기를 파고들던 한 자루의 단검도, 나를 살리기 위해 굴욕적으로 간청하던 상산왕의 움직임도.

그리고 벌겋게 달아오른 이마를 들어 자신을 바라보는 아우를 향해, 황제는 천천히 말을 이었다.

“저자는 감히 짐을 능멸했다. 비록 앞서 약조를 했다 해도 이는 정해진 선을 한참이나 넘었어.”

“폐, 폐하…….”

“허나 짐이 직접 약조했다는 사실은 변치 않는 법. 황제라는 자가 한 입으로 두말할 수는 없는 법이지. 그렇지 않나, 삼영(三影)?”

당장이라도 내 목을 베어 버릴 듯, 단검을 짓누르고 있던 삼영이라 불린 살수가 잠시 침묵했다.

“대답이 늦구나.”

“……황공하옵니다. 폐하.”

“짐은 분명 약조했다. 한데 그대는 명을 어기고 저자를 해하려 했지.”

“폐하. 그것은.”

“일영(一影). 행하라.”

서걱. 촤아악.

예리한 절삭음과 함께 힘이 실려 있던 단검이 스르륵 미끄러진다.

허공에서 뚝 떨어져 내림과 동시에, 한 치의 망설임도 없이 삼영의 목젖을 그어 버린 또 다른 복면인이 황제를 향해 부복했다.

“참(斬)했나이다.”

“……!”

“……!”

드넓은 처소 안의 공기가 차갑게 얼어붙었다.

얼굴에 튄 삼영의 핏물을 닦아 낸 나는 가늘게 호흡하는 상산왕의 앞을 가로막았고, 이번에는 그 누구도 나를 막지 않았다.

아니, 막지 못했다.

그들의 생사여탈권(生死與奪權)을 쥔 주인이 명령을 내리지 않았기 때문에.

‘이 개새끼가.’

나는 화염이 쏟아지는 눈으로 황제를 노려보며 입을 열었다.

“폐하.”

“이번에는 조금 신중하게 말하는 것이 좋을 것이다. 약속한 일각은 이미 지났으니.”

“……!”

“더불어 마지막 기회를 주마.”

“기회, 말입니까?”

“그래, 기회. 짐이 듣자 하니 상산왕의 벗이라지?”

황제가 낮게 웃으며 말을 이었다.

“이제 서로 마주할 일은 두 번 다시 없을 테니 마지막 인사나 나누거라. 그것이 짐의 마지막 아량이니.”

스륵.

황제의 말이 끝나기 무섭게 사방에서 조여 오는 살수들을 바라보며, 나는 깨달았다.

이 자리에서 상산왕을 지키는 것은 더 이상 불가능하다는 것을.

황제의 승리였다.
```

## Final English reading copy

```markdown
# Chapter 873

The same words can mean different things depending on who says them and the circumstances.

That was true of the Emperor’s words at this very moment, too.

“From now on, I’ll take care of you.”

“……!”

At the unexpected words, Prince Shangshan jerked his head up from his prostration. I couldn’t stop a groan from slipping through my lips.

“Mm.”

That was probably why the Emperor’s gaze shifted from Prince Shangshan, prostrated at his feet, to me.

“Do you have something to say?”

Plenty.

But the man before me was the ruler of the continent. I lowered myself onto one knee and answered as politely as I could.

“If I may be so bold as to say something, Your Majesty.”

“If you think it’s so bold, you’d be wise not to say it aloud—if you want to keep your head attached.”

“……!”

“Still, very well. Go on, then. It might be interesting to see how much my patience has grown over the past dozen years.”

Those in power often dressed their whims up as patience.

Just like now.

*He’s really enjoying this.*

I lowered my head slightly as I watched the Emperor’s eyes gleam like a child who’d found an amusing new toy. I was trying to hide the way I’d clenched my teeth without realizing it.

Just how far did that arrogant Emperor’s patience extend?

If I crossed some invisible line he’d drawn, could I bear the consequences?

Questions like those suddenly flashed through my mind, but right now I had to do whatever I could to fend off the Emperor’s grasping hand reaching for Prince Shangshan.

*Stay calm.*

I took a small, steadying breath and slowly spoke.

“Your Majesty’s offer is truly gracious, but His Highness Prince Shangshan is already well cared for by his loyal subjects. In fact, he may not need anyone to care for him anymore.”

“Your manners have improved all of a sudden. You’re still far from skilled at hiding the barbs in your words, though.”

The Emperor looked at me with a mocking expression, then continued.

“Tell me, who are these loyal subjects you spoke of? That devious eunuch? Or that martial-world ruffian who flouts the Great Nation’s rules of propriety and roams the land?”

Everyone, even a stray dog, knew the former meant Hong Jin and the latter meant me.

But I didn’t so much as flinch. I bowed deeply and answered.

“Your Majesty is right that I belong to the martial world. I have roots in my family and my school.”

“So you are not my younger brother’s subject. Then what gives you the right to wag that tongue of yours in front of me?”

“Though I am not his subject, I was summoned as His Highness’s guest, and Your Majesty gave me permission to speak.”

“This is getting more interesting by the moment. But dress a beast in clothes, and does that make it a person? Don’t waste my precious time on pointless formalities that don’t suit you. Get to the point. Briefly and simply.”

Briefly and simply.

That was music to my ears.

But now was the time to bow once more, just in case. I looked down at the soft carpet and said,

“How could I do that?”

“Fifteen minutes should be enough.”

“Pardon?”

“For those fifteen minutes, I’ll forgive whatever rudeness you commit. Speak freely. That is my imperial command.”

Good.

With that safety net in place, I finally lifted my head, which I’d been keeping bowed. Looking at the Emperor, I said the words that had been circling the tip of my tongue.

“You already know, don’t you?”

“What?”

“His Highness Prince Shangshan has grown up well without Your Majesty’s care. He did so in the past, and he’ll continue to do so.”

“……!”

The instant the Emperor’s eyes flashed—

Whoosh!

Killing intent like invisible blades shot in from all sides and wrapped around me.

It was the killing intent of dozens of imperial guards—or rather, assassins—who had already revealed themselves once before. They’d all sent it at me at the same time.

Their individual martial skill was Peak, but their ability as assassins had reached Supreme Peak.

If they unleashed the one-strike killing techniques they’d spent their whole lives honing, staking their lives on them, even I wouldn’t get away unscathed.

But the thing I’d feared never happened.

The Emperor raised a hand before the sword light could reach me, stopping them in their tracks.

Shff.

The darkness on all sides rippled.

The Emperor gazed at me through narrowed eyes, holding back the assassins who seemed ready to drop from the air at any moment and carve me to pieces.

“Prince Shangshan doesn’t need my care?”

“Yes.”

“Do you not know he’s only twelve years old?”

“I do.”

“Then how can you say that?”

“Because that boy, who’s only twelve, dared to shout at the Commander of the Embroidered Uniform Guard—the man said to be able to knock even a flying bird from the sky.”

“……!”

“If someone else had told him to do it, then His Highness would still be a child in need of care. But no one there advised him to do so.”

Prince Shangshan had made the decision himself, and he’d carried it out without flinching.

I didn’t know if that was something he’d been born with or something his circumstances had gradually taught him, but it meant he was fit to be an adult.

The thirteen-year-old Prince Shangshan had already proved on his own that he could do what even adults who’d done nothing but age with the time handed to them could not.

“Deputy Military Commissioner Hong Jin, who has been with him for so long, treats His Highness like a child, just as Your Majesty does. But I see it differently. When I was a child, I couldn’t even have dreamed of doing something like that.”

“Of course not. You weren’t a member of the imperial family, or a prince.”

I shrugged and answered.

“I happened to meet one member of the imperial family. I can say with confidence that His Highness Prince Shangshan is ten times more mature than that person.”

“An imperial relative? You mean Ju Wongong?”

“You know about him, too.”

The Emperor even knew about the Slaughter Saint.

I didn’t know how deeply he’d dug into my affairs, but the fact that I was involved with one of the few members of the imperial family probably didn’t even count as noteworthy information to him.

At the sudden mention of Ju Wongong, the Emperor furrowed his brow.

“Everything ultimately comes from status and authority, not age. If this boy were no more than a distant imperial relative like Ju Wongong, do you think he could have shouted at Baek Yeon so boldly?”

“I’ve heard there’s nothing more pointless than arguing about something that never happened. And making the most of what you’ve been given isn’t something a child can do, either.”

At my smooth reply, the Emperor clicked his tongue softly.

“That tongue of yours is quite slick.”

“It’s one of my signature skills.”

“But can that signature skill of yours defeat an imperial command?”

“Pardon?”

“What if I issued an imperial command right here and now to revoke Prince Shangshan’s assigned territory in Shanxi Province, grant him the title Marquis Within the Passes, and keep him by my side?”

“……!”

*What a fucking bastard. He’s playing this argument like a real piece of shit.*

*An imperial command isn’t some damn Spirit Bomb.*

I forced down the curses that were about to burst out of my mouth and asked,

“If you do that, where will His Highness stay?”

It might have crossed a line. A ruffian from the martial world had no business asking about that, and the Emperor could have shouted me down with that very argument.

But the Emperor answered readily, like a judge watching to see how far I’d cross the line.

“He’ll return to where he belongs. He’ll stay in the imperial palace, study under excellent teachers, and receive the care of loyal palace attendants in an environment far better than barren Shanxi Province.”

“Would Hong Jin be among them?”

“I said loyal palace attendants. Not a devious eunuch like him.”

The Emperor was right about one thing and wrong about everything else.

The imperial palace was where Prince Shangshan belonged. But the teachers who instructed him and the attendants who served him would all be the Emperor’s people.

And…

*They’ll watch his every move for the Emperor and do whatever they’re ordered to do.*

Even if that order were to assassinate him.

By the time my thoughts reached that point, my mind had gone cold.

“If I may ask, Your Majesty, why are you going this far?”

The Emperor curled his lips with amusement as he answered.

“Because it’s only natural.”

“Natural?”

“I’m his older brother. I’m taking care of my one and only younger brother. Do I need another reason?”

“Of course not. I just find it a little strange.”

“What do you find strange?”

“Why Your Majesty, who hasn’t cared for that one and only younger brother for more than a decade, would suddenly decide to play the part of an older brother.”

Clang! Clang! Clang!

It happened in an instant. Before any order had been given, the assassins appeared again and surrounded me on all sides.

From behind the pitch-black mask of one of them came a growling voice.

“Do you truly want to die?”

I didn’t answer. I simply looked at the Emperor, whose expression I couldn’t make sense of, and spoke in an even tone.

“The fifteen minutes aren’t up yet.”

“You bastard!”

“Your Majesty made the promise yourself. You said you’d forgive any rudeness for fifteen minutes. I’ve only been following Your Majesty’s command and speaking honestly.”

“Shut that foul mouth of yours! How dare you—”

Slice.

A cold, burning pain. Blood ran down my neck, from a wound deeper than the one I’d already received there.

“Your Majesty!”

It was Prince Shangshan, who’d been frozen like a statue all this time.

Seeing me surrounded by assassins, he hurriedly turned to his one and only older brother.

“Jin Taekyung of the Jin Family of Taiyuan is my guest and my friend! Spare him! Please forgive his rudeness!”

Thud! Thud! Thud!

There was no time to stop him. The young prince prostrated himself and struck his forehead against the ground. I bit my lip, while the Emperor, looking down on the scene with cool arrogance, suddenly spoke.

“Enough.”

Everything stopped at that one word.

The dagger that had been slowly pressing into my neck, and Prince Shangshan’s desperate, humiliating plea to save me.

Then the Emperor continued, slowly, to his younger brother, who lifted his reddened forehead and looked up at him.

“That man dared to insult me. Even if I made a promise earlier, he crossed the line by a wide margin.”

“Y-Your Majesty…”

“But the fact remains that I made that promise myself. An Emperor cannot go back on his word. Isn’t that right, Third Shadow?”

The assassin called Third Shadow, who had been holding his dagger down as if ready to cut my throat at any moment, fell silent.

“You’re slow to answer.”

“……I beg your forgiveness, Your Majesty.”

“I clearly made a promise. Yet you disobeyed my command and tried to harm him.”

“Your Majesty, that was—”

“First Shadow. Carry it out.”

Slice. Shhk!

With a sharp cutting sound, the dagger under pressure slid away.

Another masked man dropped from the air and, without the slightest hesitation, slashed Third Shadow across the throat. Then he bowed before the Emperor.

“I have executed him.”

“……!”

“……!”

The air in the vast bedchamber froze.

After wiping Samyeong’s blood from my face, I stepped in front of Prince Shangshan, who was breathing in short, shallow gasps. This time, no one stopped me.

No—they couldn’t.

Their master, the one who held the power of life and death over them, hadn’t given the order.

*You fucking bastard.*

I glared at the Emperor, my eyes burning, and spoke.

“Your Majesty.”

“This time, you’d better choose your words carefully. The fifteen minutes I promised you are already up.”

“……!”

“And I’ll give you one last chance.”

“A chance?”

“Yes. A chance. I hear you’re Prince Shangshan’s friend.”

The Emperor laughed softly and continued.

“You’ll never meet again after this, so say your final farewells. That is the last act of kindness I’ll grant you.”

Shff.

The moment the Emperor finished speaking, I looked at the assassins closing in from all sides and understood.

There was no longer any way to protect Prince Shangshan here.

The Emperor had won.
```
