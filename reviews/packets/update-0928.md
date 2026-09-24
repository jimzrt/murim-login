<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0928.txt",
      "sha256": "1b567002c8224ecb2535c0165695024e131fe88f9ba1c11443554e72b190b4be",
      "bytes": 12787
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9e9dc46d481fd2fc02e9ccb0b0e51bff48f7207e7c1c522f7486fc043ea4f86d",
      "bytes": 1565
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4e803b1a75941ff24f0420e9fac65a1ecd0e64e62a4d7954a0080b6aecaf1e28",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "09f2c33179396225428da727c892c3e53699053a1527d60ad2dfdb825e5f08b4",
      "bytes": 838
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "85d3800ee48192f13770ed3efd9503579bb863d9e0118e6ae49ecfa133c4a081",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1cade2d7bf700d7f031fc5215aae24aa864fb51d614a3b321c911290c93bd59c",
      "bytes": 1290
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "555ca42c5dd4a96f2df7ffb2b787ee43cfa72655009c3167201330a61d8b84dc",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "57c0d001377387e61fecf55198ada488cd621c9b1edc332f533ccf893c13ce64",
      "bytes": 839
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f4cb7597df6e2e3b6621149821277f1cbaab9bc9cf705d626aaacff9cc908122",
      "bytes": 266209
    }
  ],
  "estimated_tokens": 10771
}
-->

# Durable State Update — Chapter 928

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
1 and safe_through 928. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 928. Profile updates may replace only one
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
  "chapter": 928,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 928,
    "continuity_sources": [928],
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
    "Zhu Bao is Crown Prince; the Emperor is his older brother and supports his compassionate vision of rulership.",
    "The Emperor ordered a purge of treason suspects while promising to spare the innocent after their connections are established.",
    "The Bow Saint found a pre-birth letter from the Martial God describing a chosen one who would bring a new dawn, and searched for that person for decades.",
    "The Bow Saint used the Imperial Palace’s information network while disguised as a palace attendant; the Emperor knows nothing of her mission beyond a vague suspicion.",
    "The Bow Saint considered Taekyung and Cheongpung possible chosen ones; Taekyung’s recovery from an apparently fatal state convinced her he is the one.",
    "Taekyung suspects the Bow Saint planted the Blood Soul Gu in the City Lord of Sichuan Province; her answer is unknown."
  ],
  "continuity_sources": [
    926,
    927
  ],
  "open_questions": [
    "Why did the Martial God’s letter describe a chosen one without pointing to only one person?",
    "Did the Bow Saint plant the Blood Soul Gu in the City Lord of Sichuan Province?",
    "What story has So Gyo kept to herself?",
    "Where is Ma Sanbao, and what is his current status?",
    "What did Wei Zhong tell Taekyung through Sound Transmission?"
  ],
  "safe_through": 927,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 황태제 as “Crown Prince” in this succession context."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 신법     | **movement technique**                           |                                                       |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 애향이 | **Aehyang** | Personal name of the Sichuan City Lord's favorite concubine. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 애향 | **Aehyang** | The City Lord’s favored concubine. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 사천성주 | 애향이 | lord_to_favorite_concubine | Aehyang | affectionate-familiar | The City Lord uses her personal name while discussing the visitors. |
| 애향이 | 사천성주 | favorite_concubine_to_city_lord | My lord | seductive-deferential | Aehyang repeatedly addresses the City Lord as 대인 while persuading him to receive Taekyung. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 927
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 927
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 927
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 927
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while her allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 927
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 927
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one who would bring a new dawn, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

## Korean source

```text
＃928화



혈혼고(血魂蠱).

과거 남만을 피로 물들인 오독문에 의해 탄생한 저주받은 독물(毒物).

사천성주를 끝끝내 죽음으로 몰고 간 그것의 정체를 깨달았을 때, 나를 비롯한 모두는 이것이 암천의 소행이며 황제와 깊은 연관이 있으리라 확신했었다.

하지만 이제는 잘 모르겠다.

무엇이 진실이고 거짓인지.

어디서부터 어디까지 믿어야 하는지.

지금 이 순간. 쓴웃음을 머금은 채 나를 바라보는 눈앞의 이 여자가 정말 아군이기는 한 것인지.

그리고…….

‘만약 혈혼고를 심은 것이 궁성의 소행이라면 그녀의 뒤에 있는 무신은, 내 등장을 예견한 그는 도대체 어떤 존재지?’

모든 것이 베일에 싸여 있는 무신에 대한 끝없는 의문도.

으득.

이를 악문 나는 궁성을 노려보았다.

“물었습니다. 사천성주에게 혈혼고를 심은 것이 누구인지.”

나를 물끄러미 바라보던 궁성이 불쑥 입을 열었다.

“그것이 내 소행이라면 어찌할 테냐.”

“……!”

찌르르 울리는 등골.

동요를 억누른 나는 애써 담담한 어조로 대답했다.

“충분한 설명을 해야 할 겁니다. 저를 포함한 모두를 납득시킬 수 있을 만한 설명을.”

“그것으로도 납득하지 못한다면?”

“그때는…….”

나는 나직이 숨을 삼켰다.

동시에 본능처럼, 미세하게 자세를 낮추고 언제든지 출수(出手)할 준비를 끝마쳤다.

세상에는 절대적인 선도, 악도 없다.

그러나 암천은, 천주(天主)는 분명 절대악에 가까운 존재.

그런 암천과 깊은 연관이 있는 혈혼고를 궁성이 사용했고, 이것이 암천과 밀접한 연관이 있다면 내가 해야 할 일은 하나뿐이다.

“저도 지금처럼 공손하게 굴지는 않겠죠.”

그 순간.

스아아.

강렬한 바람이 나와 궁성을 휘감았다.

아니, 맞부딪쳤다.

그리고 첨예하게 맞닿은 서로의 기파(氣波)가 크게 부풀어 오르려던 그때, 어느덧 가늘어져 있던 궁성의 눈매가 보름달처럼 휘었다.

“그래, 응당 이래야지.”

“……그게 무슨.”

“기대했던 것 이상이다. 모든 것이 전부 다.”

부드럽게 휘어진 눈매와 그 짧은 말에 담긴 의미를 깨닫기에는 그리 오랜 시간이 필요하지 않았다.

‘시험.’

불현듯 뇌리를 스치고 지나간 그 단어와 함께, 전신을 옥죄고 있던 긴장의 끈이 탁 풀렸다.

“젠장.”

한숨처럼 흘러나온 목소리에 궁성이 짐짓 눈살을 찌푸렸다.

“흠, 머리에 피도 안 마른 녀석이 어른 앞에서 못하는 말이 없구나.”

“진짜 어른이었으면 머리에 피도 안 마른 놈을 이런 식으로 놀리진 않습니다.”

“널 찾기 위해 바친 세월만 수십 년인데, 그깟 장난 몇 번이 대수일까.”

궁성은 흐릿하게 웃었다. 나를 바라보는 그녀의 눈빛에는 약간의 기특함이 깃들어 있었다.

“그래서, 결국 사천성주의 죽음이나 혈혼고와는 아무런 연관도 없는 겁니까?”

“연관이야 있지.”

폭탄 같은 말을 대수롭지 않게 내뱉은 궁성이 꽃을 쓰다듬으며 덧붙였다.

“머지않아 죽을 것을 뻔히 알면서도 사지(死地)로 돌려보냈으니까. 적어도 사천에서 죽음을 맞이한다면, 그곳에 있는 네 주변 인물 중 누군가가 그 사실을 알아차리라 생각했다.”

“죽을 걸 알고 있었다고요?”

“사천성주는 황도에 머무를 당시에도 이미 혈혼고에 중독된 상태였다. 당연하게도 암천, 보다 정확히는 그자의 애첩이 벌인 소행이었지.”

“설마, 애향?”

“맞다.”

생각지도 못한 이야기에 눈을 크게 뜬 내 모습에, 궁성이 담담한 어조로 말을 이었다.

“놀랄 것 없다. 뜻대로 조종해야 할 누군가가 사내라면, 미인계(美人計)야말로 확실한 방법이니.”

“하지만 그 정도로 암천의 끄나풀이라는 사실을 어떻게…….”

“직접 은밀히 살펴보니 뛰어난 수준의 미혼술(美魂術)을 익혔더구나. 여색에 홀려 업무를 소홀히 한다는 정보를 듣고 지켜보던 중에 황도로 소환한 것이었지.”

그 말에 그리 오래되지 않은 옛 기억이 뇌리를 스쳤다.

사천혈사(四川血史)라 명명된 그 사건이 일어나기도 전, 처음 대면한 자리에서조차 반쯤 벌거벗은 몸으로 있던 사천성주의 모습이.

‘그럼 그때 이미?’

불현듯 등골이 서늘해졌다.

암천의 끄나풀인 애향이 지척에 있었음에도 그 사실을 알아차리지 못해서가 아니다.

암천의 그늘이, 그 어두운 손길이 어디까지 미쳤는지 짐작조차 가지 않았기 때문이었다.

“그렇다면 혹시…….”

“그래.”

뒷말을 잇기도 전에 고개를 끄덕인 궁성이 입을 열었다.

“암천은 대국의 뿌리까지 침투했다. 어디까지가 끝일지 모를 만큼 구석구석, 치밀하게.”

“……!”

“동천마군의 죽음으로 모든 것이 끝난 것은 아니다. 아직도 크고 작은 실권을 쥔 지방관들과 일군(一軍)을 지휘하는 장수들도 상당수가 암천과 협력하고 있겠지. 물론 그중에는 각 성을 다스리는 성주들도 포함되어 있을 테고.”

나는 숨을 삼켰다.

말이 쉬워 성이지, 그 안에 포함된 대지의 면적과 인구는 어마어마하다.

괜히 과거 있었다는 난세의 시대에 수십여 명씩이나 되는 군웅이 칭왕(稱王)까지 해가며 패권 다툼을 벌였겠나.

그저 왕이라는 이름으로 자신만의 정통성을 내세우고 싶어서?

반은 맞고, 반은 틀렸다.

한 지방을 제패하여 그 땅의 역량이 지닌 흡수할 수만 있다면, 능히 일국의 왕을 칭할 만큼 세력을 구축할 수 있어서다.

물론 현재에 이르러서는 강력한 중앙 정부의 명령을 따르는 일개 신하에 불과하지만, 그 성주들이 역심(逆心)을 품고 작정하여 날뛴다면 대국 전체에 엄청난 피해를 입힐 수도 있다.

‘과장이나 거짓말 따위가 아니었어.’

모든 것을 받아들이고 내려놓기 전, 동천마군은 분노로 가득한 저주를 쏟아냈었다.

이건 시작에 불과하다고, 황도를 지켰다 해도 불길은 천하를 휩쓸 것이라고.

그러나 그것은 단순히 분노에 눈이 돌아가 아무렇게나 내뱉은 저주가 아니었다.

일말의 진실이 깃든, 어쩌면 그리 머지않은 미래에 폭발할 시한폭탄이었다.

‘빌어먹을.’

머리가 뜨겁다.

아무것도 하지 않았음에도 흐트러진 호흡에 가슴이 쿵쿵 뛰었다.

현대와 무림.

두 세상을 집어삼키려 하는 불길이 눈앞에 일렁이는 듯했다.

누구도 예측하지 못한 이러한 상황 속에서 불현듯 장막을 젖히고 등장한 거인(巨人)의 그림자도 함께.

“그럼 이제는, 이제부터는 어떻게 해야 합니까.”

나는 가쁜 호흡을 삼키며 궁성에게 물었다.

아니, 그것은 오랜 과거에 남긴 하나의 서신으로 그녀를 지금 이 순간까지 이끈 누군가를 향한 질문에 가까웠다.

무신(武神).

인간으로 태어나, 신이라 불리는 자.

이미 한 번 천하를 구하고, 또 다시 천하를 구하기 위한 안배를 남긴 자.

지금 나는 그를 향해 묻고 있었다.

궁성에게 남긴 무신의 서신 속에 담긴 또 다른 예지를, 이 캄캄한 길을 밝힐 수 있는 한 줄기의 빛을 원했다.

“내가, 씨발, 내가 도대체 어떻게 해야 하는 거냐고!”

그리고 발악하듯 외치는 나를 향해 돌아온 궁성의 대답에는, 희미한 빛조차 담겨 있지 않았다.

“모른다. 나도, 그분께서도.”

“……!”

일순간, 전신의 맥이 탁 풀렸다.

어지럽게 흐트러지는 시야 속에서, 나는 힘없이 고개를 떨궜다.

분명 뭔가, 뭔가 더 있을 거라고 생각했다.

바로 그 무신이라면.

언젠가 나라는 존재가 나타나리라 확신했던 그라면 다를 것이라고 생각했다.

심지어 한편으로는 있을 수 없는 생각까지 떠올렸었다.

만에 하나 무신이, 눈부신 업적과 신위를 지닌 저 고금제일인(古今第一人)이…….

‘어쩌면.’

이를 악문 채. 머릿속으로 그 믿기 힘든 생각을 이어 가려던 그때였다.

고개 숙인 내 귓가로 나지막한 목소리가 흘러들어온 것은.

“다만 한 가지.”

그 순간, 나는 마치 홀린 사람처럼 천천히 고개를 들었다.

깊게 가라앉은 두 눈으로 나를 응시하는 궁성이 그곳에 있었다.

“선택받은 자를 위해 남기신 전언(傳言)이 있다.”

“그게, 그게 무슨.”

“신력(神力).”

어째서일까.

신력, 그 짧은 두 글자에 나도 모르게 몸이 얼어붙었다. 알 수 없는 한기가 등골을 타고 흘렀다.

두 귓가로 전해지는 궁성의 목소리가, 그 차분하면서도 나직한 음성이 천둥처럼 울려 퍼졌다.

“선택받은 자만이 지닐 수 있는 신력과 의지로 헤쳐 가라 하셨다. 바로…….”

순간, 흐려지는 말꼬리와 동시에 세상이 느려졌다.

어느덧 드리워진, 보이지 않는 장막이 내 시야와 귀를 틀어막고 있었다.

오직 한 사람.

궁성밖에 보이지 않았다. 천천히 움직이는 그녀의 입술이, 그 사이로 흘러나오는 음성밖에 들리지 않았다.

“바로, 당신께서 그러했듯이.”

“……!”

멈췄던 시간이, 다시 흐른다.

그러나 나는 여전히 그대로였다. 빙하에 갇힌 사람처럼 얼어붙은 채 멍하니 궁성을 바라보고 있을 뿐이었다.

‘내가. 내가 지금…….’

도대체 무슨 소리를 들은 거지?

마치 머릿속이 텅 비어 버린 듯했다. 새하얗게 물든 그곳에는 앞서 들은 몇 가지 단어들이 둥둥 떠다녔다.

그리고 이내 거대한 벼락이 되어, 내 정수리를 관통했다.

바로 당신께서 그러했듯이.

당신, 무신이 그러했듯이.

이것이 의미하는 바는, 단 하나뿐이었다.

무신 역시 나와 같은 선택받은 자였다는 것.

아니. 정확히는…….

‘시스템 사용자.’

플레이어(Player).

비어 있던 뇌리를 채우며 터질 듯이 부풀어 오른 그 단어와 함께, 맑은 종소리가 울려 퍼졌다.

띠링.

그리고 그 순간.

스륵.

나는 서서히 뒤집혀 가는 하늘과 땅을 느끼며, 새카만 어둠으로 굴러떨어졌다.



* * *



모든 것이 동시였다.

잘게 떨려 오던 진태경의 신형이 실 끊어진 인형처럼 허물어진 것도, 불현듯 뻗어 나온 궁성의 손길이 그의 옷깃을 잡아챈 것도.

마지막으로, 버려진 정원을 감돌던 서늘한 새벽공기가 돌연 뜨겁게 달아오른 것도.

덥석. 화아아악.

진태경의 신형을 바로 세운 궁성이, 갑작스럽게 나타난 불청객을 향해 입을 열었다.

“희한하네요. 당신까지 초대한 기억은 없었던 것 같은데.”

불청객이 착 가라앉은 목소리로 대답했다.

“그래도 명색이 제자라고 부르는 놈인데, 어느 고약한 할망구와 단둘이 있으면 불안하지 않겠나.”

화왕 적천강.

차분한 목소리와는 달리, 그의 눈동자는 불길이 일렁이고 있었다.

“좋아, 무슨 헛짓거리를 했는지 들어나 보지.”

궁성이 실소와 함께 고개를 내저었다.

“세월이 많이 흘렀으니 변할 만도 한데, 여전하군요. 그 앞뒤 안 가리는 성미는.”

“두 번 말하게 할 생각인가?”

“쥐새끼처럼 숨어서 듣고 있었으니 알고 있을 텐데요. 그게 전부예요. 단지…… 이 아이가 한계 이상으로 지쳐있었을 뿐이지.”

궁성은 혼절한 진태경을 물끄러미 응시했다.

곳곳에 핏물이 말라붙은 청년의 얼굴에는 치열함이 묻어나와 있었다.

그가 보여 주었던 눈부신 분투와 숭고함의 흔적이기도 했다.

“데려가요. 이 아이가 조금이라도 더 푹 쉴 수 있도록.”

적천강의 망설임은 길지 않았다. 기다렸다는 듯이 진태경을 업고 경신법까지 발휘해 가며 멀어지는 그의 뒷모습을, 궁성은 끝까지 지켜보았다.

그리고 문득, 빛을 받아 서서히 벌어지는 꽃봉오리를 보았다.

서광(曙光)이었다.
```

## Final English reading copy

```markdown
# Chapter 928

Blood Soul Gu.

A cursed venomous creature created by the Five Poisons Sect, which had once drenched Nanman in blood.

When I realized what had driven the City Lord of Sichuan Province to his death, everyone—including me—had been certain it was Dark Heaven’s doing, and that it had deep ties to the Emperor.

But now, I wasn’t so sure.

What was true, and what was false?

Where should I begin—and where should I stop—believing?

And right now, was this woman before me, looking at me with a bitter smile, really an ally?

And…

*If the Imperial Palace was the one that planted the Blood Soul Gu, then what kind of being is the Martial God behind her—the one who foresaw my appearance?*

That was only one of the endless questions I had about the Martial God, a man shrouded in mystery.

*Grind.*

I clenched my teeth and glared at the Bow Saint.

“I asked you. Who planted the Blood Soul Gu in the City Lord of Sichuan Province?”

The Bow Saint watched me in silence, then abruptly spoke.

“What would you do if I were the one who did it?”

“……!”

A shiver ran down my spine.

Suppressing my agitation, I forced myself to answer in a calm voice.

“You’d have to give me an explanation. One that could convince everyone, myself included.”

“And if it still doesn’t convince you?”

“Then…”

I drew a quiet breath.

At the same time, instinctively, I lowered my stance ever so slightly and readied myself to strike at any moment.

There is no absolute good or absolute evil in this world.

But Dark Heaven—Lord of Heaven—was unquestionably close to absolute evil.

If the Bow Saint had used the Blood Soul Gu, which was deeply connected to Dark Heaven, and it had close ties to Dark Heaven, there was only one thing I could do.

“I wouldn’t be as polite as I am now.”

At that moment—

*Whoosh.*

A powerful gust of wind swept around the Bow Saint and me.

No—our winds collided.

Our opposing waves of qi met head-on, poised to swell. Just then, the Bow Saint’s narrowed eyes curved like a full moon.

“Good. That’s how it should be.”

“What…does that mean?”

“You exceeded my expectations. In every way.”

It didn’t take me long to understand the meaning in those softly curved eyes and the brief words she’d spoken.

*A test.*

The word suddenly flashed through my mind, and the tension constricting my whole body snapped loose.

“Damn it.”

At my sigh, the Bow Saint furrowed her brow in mock disapproval.

“Hm. Still wet behind the ears, and you talk to your elders like that?”

“If you were really an elder, you wouldn’t toy with someone who’s still wet behind the ears.”

“I’ve spent decades searching for you. What does it matter if I tease you a few times?”

The Bow Saint smiled faintly. As she looked at me, there was a hint of approval in her eyes.

“So, in the end, you had nothing to do with the City Lord’s death or the Blood Soul Gu?”

“I had something to do with it.”

The Bow Saint tossed out the bombshell as if it were nothing. She stroked a flower and continued.

“Knowing full well he would die soon, I sent him back to a place of death. I thought that if he died in Sichuan, at least one of the people around you there would notice.”

“You knew he was going to die?”

“The City Lord of Sichuan Province was already infected with the Blood Soul Gu while he was staying in the Imperial Capital. Naturally, it was Dark Heaven’s doing—or, more precisely, the doing of the City Lord’s favorite concubine.”

“Don’t tell me…Aehyang?”

“That’s right.”

My eyes widened at this unexpected revelation. The Bow Saint continued in an even tone.

“Don’t be surprised. If you need to control someone and that someone is a man, there’s no surer method than using a beautiful woman.”

“But how did you know she was working for Dark Heaven just from that?”

“I discreetly investigated her myself. She had mastered an impressive level of Soul Bewitchment. I’d heard he was neglecting his duties, besotted with women, so I summoned him to the Imperial Capital while I was keeping an eye on him.”

An old memory, not so long ago, came back to me.

The City Lord of Sichuan Province, half naked even when I’d first met him—before the incident that came to be known as the Sichuan Blood Tragedy.

*So even back then…?*

A chill suddenly crept down my spine.

It wasn’t because I hadn’t realized Aehyang, an agent of Dark Heaven, was right beside him.

It was because I couldn’t even begin to guess how far Dark Heaven’s shadow—its dark hand—had reached.

“Then, could it be…”

“Yes.”

The Bow Saint nodded before I could finish and spoke.

“Dark Heaven has infiltrated the Great Nation down to its roots. Thoroughly, into every corner, so deeply that no one knows where it ends.”

“……!”

“The death of the Eastern Heaven Demon Lord wasn’t the end of everything. A considerable number of local officials wielding various degrees of real power, along with generals commanding armies, are likely still working with Dark Heaven. Of course, that probably includes the City Lords who govern the provinces.”

I swallowed.

A province was more than just a word. Its land and population were enormous.

Why else, in the chaotic age of the past, had dozens of warlords proclaimed themselves kings and fought for supremacy?

Was it only because they wanted to claim legitimacy by calling themselves kings?

That was half right, and half wrong.

If you conquered a region and absorbed all the strength of its land, you could build enough power to claim the title of king of an entire nation.

Of course, these days they were nothing more than officials following orders from a powerful central government. But if those City Lords harbored treasonous ambitions and rose up in earnest, they could inflict tremendous harm on the Great Nation.

*So it wasn’t an exaggeration or a lie.*

Before he accepted everything and let go, the Eastern Heaven Demon Lord had poured out a curse filled with rage.

*This is only the beginning. Even if you protected the Imperial Capital, the flames will sweep across the land.*

But that hadn’t been a curse he’d spat out at random, blinded by anger.

It held a grain of truth—perhaps it was a time bomb that would explode in the not-too-distant future.

*Damn it.*

My head was burning.

My breathing had grown ragged, though I hadn’t done anything, and my heart was pounding.

It felt as if I could see the flames that threatened to swallow two worlds—modern society and Murim—flickering right before my eyes.

And with them, amid a situation no one could have foreseen, came the shadow of a giant who had suddenly swept aside the curtain and appeared.

“Then what should we do now? From this point on?”

I asked the Bow Saint, drawing in a ragged breath.

No—it was more like a question for the person who had led her to this very moment by leaving a letter long ago.

The Martial God.

A man born human, yet called a god.

A man who had saved the world once, then left behind an arrangement to save it again.

I was asking him now.

I wanted another prophecy from the Martial God’s letter to the Bow Saint—one ray of light to illuminate this pitch-black road.

“What am I—fuck—what am I supposed to do?!”

But the Bow Saint’s reply held not even a glimmer of light as it reached me, shouting in desperation.

“I don’t know. Neither do I, nor does he.”

“……!”

In an instant, the strength drained out of my whole body.

As my vision blurred, I lowered my head helplessly.

I’d been sure there was something more. Something more to it.

If it was the Martial God…

I thought he would be different, if anyone could. He was the one who had been certain that a person like me would appear someday.

I’d even entertained a thought that should have been impossible.

*What if the Martial God—the greatest of all time, with his dazzling achievements and divine authority—*

*Maybe…*

I clenched my teeth and was about to follow that unbelievable thought to its conclusion when a quiet voice reached my lowered head.

“But there is one thing.”

At that moment, I slowly lifted my head as if I were under a spell.

The Bow Saint was there, gazing at me with eyes sunk deep.

“He left a message for the chosen one.”

“What…what do you mean?”

“Divine strength.”

Why?

At those two brief words, my body stiffened without my knowing why. An inexplicable chill ran down my spine.

The Bow Saint’s voice reached my ears. Her calm, quiet words rang out like thunder.

“He said to forge ahead with the divine strength and Will that only the chosen one can possess. Just as…”

In that instant, her voice faded, and the world slowed.

An invisible curtain had fallen, blocking my sight and muffling my ears.

There was only one person.

I could see no one but the Bow Saint. I could hear nothing but her lips moving slowly and the voice slipping between them.

“Just as you did.”

“……!”

Time, which had stopped, began to flow again.

But I still couldn’t move. I could only stare blankly at the Bow Saint, frozen as if trapped in a glacier.

*I…what did I just…*

What on earth had I heard?

My mind felt as though it had emptied completely. A few words floated there, bright against the blankness.

Then, in an instant, they became a great bolt of lightning and pierced the crown of my head.

*Just as you did.*

Just as *you*, the Martial God, did.

There was only one meaning this could have.

The Martial God had also been a chosen one like me.

No. To be precise…

*System user.*

*Player.*

The word filled my empty mind, swelling until it felt like it would burst. A clear chime rang out.

*Ding.*

And at that moment—

*Slip.*

I felt the sky and the ground slowly turn over as I fell into pitch-black darkness.

* * *

It all happened at once.

Jin Taekyung’s trembling form crumpled like a puppet with its strings cut. The Bow Saint’s hand shot out and seized his collar. And finally, the cold dawn air that had drifted through the abandoned garden suddenly grew hot.

*Grab. Fwoosh!*

The Bow Saint steadied Jin Taekyung, then spoke to the uninvited guest who had suddenly appeared.

“How strange. I don’t remember inviting you, too.”

The uninvited guest answered in a low voice.

“I do call him my Disciple, after all. How could I not worry when he’s alone with some nasty old hag?”

The Fire King, Jeok Cheongang.

Despite his calm voice, fire flickered in his eyes.

“Fine. Let’s hear what kind of nonsense you’ve been up to.”

The Bow Saint let out a soft laugh and shook her head.

“A lot of years have passed. You could have changed, but you’re still the same. Still acting without thinking.”

“Do I have to say it twice?”

“You were hiding like a rat and listening, so you should know. That’s all there is to it. This child was simply more exhausted than he could handle.”

The Bow Saint gazed at the unconscious Jin Taekyung.

Dried blood clung to his face in several places, and his features bore the marks of a fierce struggle.

They were proof of the dazzling fight and nobility he had shown.

“Take him with you. Let him get a little more rest.”

Jeok Cheongang didn’t hesitate for long. He carried Jin Taekyung on his back as if he’d been waiting for the chance, then used his movement technique to hurry away. The Bow Saint watched him until he was gone.

Then, suddenly, she saw a flower bud slowly opening in the light.

The first light of dawn.
```
