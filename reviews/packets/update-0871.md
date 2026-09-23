<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0871.txt",
      "sha256": "166dd81052798900d0bb48a80f071afd6522cbe963edddd1de11397958452393",
      "bytes": 15361
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ad690a1bb26de76b0eac96cff6eaf2c56e63e88afcbae3ab3e32ef73b528c9bc",
      "bytes": 1539
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3291b7833512bf663761c7378a7587b0bd5178a4c5aa15c6bd322bfc5ce0ac8f",
      "bytes": 229780
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "60a079fad9f465b968a64e7f53424938a44a1c353cd12b3a982d30eaae88fcdd",
      "bytes": 983
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "f7cef51ed3817ef76225ea177cdd4ee9003f0e0aa39f5513ef1bf17722542e25",
      "bytes": 854
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "f45dc9081b2a1ba5f5efedf4b55753b0e6cac5411508caa969988839dcf1c74c",
      "bytes": 667
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "3f5a23524f4b470b599621368830c4a8e1afb4153c33b9e8757350f78b4c20bf",
      "bytes": 470
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "5fee4ba0d79c65cca598e1cbf74db0be59dcdfaee851a95e4769afee440e614e",
      "bytes": 771
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "eefff6855428ce82bc4db4e8f7f5a176ca8a81f85d5a2fe0c982a4730be5364b",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ab1269c576a56dcf6818ffbc2bdd365329cf84e0ca61a060b489185faa2a5487",
      "bytes": 622
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "c4ffc52f1779f87307fbacc1c1c81b6708228fcd49fc6f596ec6bce55341ee3e",
      "bytes": 3207
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "bca5a0a47f025e364377ffb426bb054d33b677210b7f322c0ca729bccab5264d",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "c8f89da67a2fdca6b53f2f8bbaaac9aca8109dbc8f151eb39519ed20c405e4ad",
      "bytes": 765
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "c15caf6066f8b4e04c8197b76e7bf701afa433195cadef1b43b565fe9ccd8fee",
      "bytes": 920
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "78f2a30d7157188be2aadbb18e2e9d210a30a8f5d3d7b635d5d58939f6cbf55e",
      "bytes": 256919
    }
  ],
  "estimated_tokens": 13530
}
-->

# Durable State Update — Chapter 871

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
1 and safe_through 871. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 871. Profile updates may replace only one
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
  "chapter": 871,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 871,
    "continuity_sources": [871],
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
    "The Emperor summoned only Prince Shangshan and Jin Taekyung to an audience; Hong Jin and Hyuk Mujin were not summoned. They are being escorted through the imperial palace.",
    "Two identical middle-aged Supreme Peak masters have blocked the procession before the audience.",
    "Taekyung’s System and Inventory are unavailable during the update; he has no divine weapons on hand, and his condition worsens without the Divine Physician’s pills.",
    "Ma Sanbao secretly remained in the palace, leads a group seeking to enthrone Prince Shangshan, and offered Taekyung a reward for helping; Taekyung has not accepted.",
    "Hong Jin left the East Depot to serve Prince Shangshan, while Ma Sanbao stayed behind.",
    "The Emperor relies on opium, which he calls medicine, and broke his pipe to clear his mind. "
  ],
  "continuity_sources": [
    870
  ],
  "open_questions": [
    "What does the Emperor intend for Prince Shangshan and Taekyung?",
    "Who are the twin Supreme Peak masters, and why have they blocked the procession?",
    "Will Taekyung agree to help Ma Sanbao enthrone Prince Shangshan, and what would the plan require?",
    "What does Ma Sanbao know about Dark Heaven, and what reward is he offering?",
    "Who sent the assassin to Qianqing Palace, and what was the intended target?"
  ],
  "safe_through": 870,
  "temporary_decisions": [
    "Render 흠천감 as “Imperial Astronomical Bureau.”",
    "Render 형부 as “Ministry of Punishments.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 조필     | **Jopil**          |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 일격     | **One Strike**                         |
| 스킬               | **Skill**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 귀가      | **your family**                                                 |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 야명주 | **night-shining pearls** | Pearls embedded in the cavern ceiling that provide light. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 869
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 870
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 869
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 846
- **Aliases:** Killing Ghost
- **Role:** A Hubei fisherman who disappeared for a month and returned as the Killing Ghost, a monster that grew stronger and more grotesque with each appearance.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 870
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** A Thousand Captain in the Embroidered Uniform Guard under Baek Yeon’s command, he is ordered to surveil Prince Shangshan’s party while leaving openings for someone to approach; he says he would give his life to obey an imperial command.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 870
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 870
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 665
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan; dead after fighting Jin Taekyung and drawing on his innate qi, with half his upper body destroyed; he left behind the Supreme Peak martial art Flame Divine Palm; he was an orphan named Jangcheon whom Jeok Cheongang rescued after an epidemic in Anhui Province and eventually accepted as his Disciple
- **Personality:** Cruel, amused by violence, motivated by both payment and the pleasure of hunting his targets; a born Slaughter Saint who rationalizes murder through Might Makes Right and feels empty when victims die
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 870
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 870
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 870
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃871화



동창과 함께 황제의 수족이라 불리는 금의위라 해도 정해진 한계는 있었던 모양이다.

정호군은 이름 모를 쌍둥이 중년인에게 나와 상산왕을 인도하며 짧은 전음을 남겼다.

- 지금부터는 말 한마디, 행동 하나하나에 신중해야 할 것이다. 그렇지 않다면 결코 살아서 나올 수 없을 테니.

시벌놈이 누굴 놀리나.

그렇지 않아도 이미 피부로 생생하게 느끼는 중이다.

난데없이 나타난 저 쌍둥이 초절정 고수는 물론이고, 아직 들어서지도 않은 궁 내부의 수많은 인기척까지.

‘더럽게 삼엄하네.’

모래라도 삼킨 것처럼 입안이 텁텁하다. 나는 눈치채지 못할 만큼 천천히 공력을 끌어올리며 입술을 달싹였다.

- 하나만 묻자. 도대체 날 부른 이유가 뭐지?

- 모른다고 했을 텐데.

- 정말 몰라서 모른다고 하는 거야, 아니면 알아도 모르는 거야?

- 둘 다.

빌어먹을. 물어본 내가 등신이지.

나는 언제나처럼 무뚝뚝한 얼굴로 서 있는 정호군을 노려본 뒤, 사인교에서 내린 상산왕과 함께 건청궁(乾淸宮)이라고 적힌 현판을 지나쳤다.

저벅. 저벅.

유난히도 크게 울려 퍼지는 발걸음 소리.

나는 한 치의 오차도 없이 똑같은 움직임으로 나아가는 쌍둥이의 뒷모습을 보며 조용히 가늠했다.

‘합격술(合擊術)을 익힌 게 틀림없는데…… 정확히 무슨 무공을 익힌 거지?’

아무리 생각해도 상황이 좋지 않다.

상대가 익힌 무공을 유추할 수 없다는 것은 둘째치고, 이미 완숙한 경지에 오른 두 명의 초절정 고수가 펼치는 합격술은 상상만 해도 속이 쓰렸다.

게다가…….

‘뭔 놈의 박쥐 새끼들이 이렇게 많은지.’

은은한 불빛 속에서도 드러나지 않은 그림자들.

어둠 속에서 모든 일거수일투족을 감시하고 있는 저들은 황실에서 키워 낸 호위이자 살수(殺手)가 틀림없다.

그리고 만약 최악의 상황이 닥친다면, 무려 일백에 달하는 저 살수들은 평생을 연마해 온 일격필살의 수법으로 나를 난자할 것이다.

뱃속에서부터 합격술을 익혔을 것 같은 쌍둥이 초절정 고수와 함께.

‘십왕(十王). 아니, 어쩌면 삼성(三星)에 버금가는 고수가 아닌 이상 십중팔구는 이곳에서 뼈를 묻는다.’

세인들은 말한다. 무림은 도산검림(刀山劍林)의 세상이라고.

하지만 틀렸다.

이곳이야말로 진정한 도산검림이다. 오직 황제의 뜻에 따라 생사가 결정되는 공간.

‘도대체 얼마나 많은 고수를 거느린 거지?’

명문대파로 불리는 구파일방과 오대세가가 많아야 둘. 기껏해야 한 명 정도를 보유하고 있는 초절정 고수를 무려 둘이나 문지기로 부리다니.

마치 칼날 위를 걷는 듯한 기분이다.

나도 모르는 사이에 식은땀 한 방울이 목덜미를 타고 흘러내린 그때. 나는 문득 어느 자그마한 손에 의해 옷소매가 당겨지고 있음을 깨달았다.

꾸욱.

옷소매가 구겨지도록 힘주어 움켜잡은 손. 그제야 어린 왕의 가파른 호흡이 느껴진다.

‘떨고 있어.’

황족이고, 왕이기 전에 어린아이다.

처음 만났던 그때에도 그랬고, 지금도 다르지 않았다.

기억도 나지 않을 만큼 어린 시절에 황궁을 떠났다고 했으니, 당연히 천자에 대한 기억도 없겠지.

‘그런데 이제는 유일한 가족이자, 하나뿐인 형에게 목숨을 위협받는 중이고.’

문득 그런 생각이 들었다.

황도까지 오는 길에 상산왕이 보였던 낙천적인 모습은, 어쩌면 그런 두려움과 실망을 감추기 위한 노력이 아니었을까 하는 생각이.

천자의 위협을 경고하는 홍진의 말에도 그럴 리 없다며 고개를 내젓던 그 모습은, 믿기 힘든 현실을 마주한 어린아이가 할 수 있는 유일한 선택이었을지도 모르겠다.

‘분명 아무것도 몰라야 할 아이인데…… 철이 너무 일찍 들어 버렸어.’

마음이 복잡해졌다.

칼바람이 휘몰아치던 산서성의 그해 겨울, 부모를 잃고 고사리 같던 손으로 어린 여동생을 꼭 붙잡고 언덕을 기어오르던 어느 소년의 얼굴이 생각나서.

그리고 아버지의 장례식장에서 엎드려 울던 어머니의 등을 토닥이던 어린 하연이가 떠올라서.

‘빌어먹을.’

나는 흘러나오려는 한숨을 삼키기 위해 입술을 질끈 깨물었다.

무림과 현대는 무엇 하나 닮은 것 없는. 전혀 다른 세상이다.

그러나 딱 하나, 사람은 변함없이 같았다.

처음에는 이 모든 것이 게임이라 생각했던 내가 무림을 또 하나의 현실로 받아들이기 시작한 것도 그 때문이었다.

그들도 결국 사람이었다. 분노하고, 기뻐하고, 슬퍼하는.

죽어 마땅할 악인(惡人)도 있었고, 투명하리만치 맑은 눈을 한 선인(善人)들도 있었다.

전자의 경우에는 한 치의 망설임도 없이 목숨을 끊었으나, 후자라면 내 목숨을 걸고 도운 적도 있었다.

그리고 나는 지금, 이 어린 왕에게 안쓰러움을 느끼고 있다.

파르르 떨리는 숨소리에서 조필의 습격으로 모든 것을 잃고 도망친 어린 남매를 떠올렸고, 옷소매를 꽉 붙잡은 자그마한 손을 보며 내 동생 하연이를 생각했다.

‘냉정하게 생각해야 하는데. 반드시 그래야 하는 문제인데…….’

아무리 생각해도 자신이 없다.

역모냐, 순응이냐는 양자택일(兩者擇一)의 상황이 온다면 내가 이 아이를 두고 떠날 수 있을지.

오랜 시간이 흐른 뒤에 아무렇지도 않게 그 기억을 회상할 수 있을지.

‘거참, 여러모로 힘들게 하네.’

나는 씁쓸하게 웃으며 가슴팍에도 닿지 않은 상산왕을 가만히 내려다보았다.

그리고 반쯤은 충동적으로 손을 들어 머리를 툭툭 쓰다듬어 주었다.

“……!”

크게 뜨인 두 눈. 살짝 벌어진 입술 사이로는 지금 당장이라도 무엄하다는 일갈이라도 튀어나올 것 같았지만, 놀란 얼굴로 나를 올려다보던 상산왕은 입만 오물거릴 뿐 아무 말도 하지 않았다.

아니, 오히려 안심하듯 내 옷소매를 힘껏 움켜쥐고 있던 손을 느슨하게 풀었다.

지금껏 감히 그 누가 이 아이의 머리를 쓰다듬을 수 있었을까.

저 나이 또래라면 누구나 당연하게 겪어 보았을 이 단순한 것조차도, 상산왕 주표에게는 아니었을 것이다.

‘지금으로서는 겨우 이 정도가 내가 해 줄 수 있는 최선일 따름이고.’

내가 내심 중얼거린 그때. 거침없이 나아가던 쌍둥이의 발걸음이 커다란 문 앞에서 멈췄다.

철컥. 구구구궁.

육중한 소리와 함께, 마치 살아 있는 것처럼 생생하게 용이 음각(陰刻)된 철문이 열린다. 궁 안으로 들어온 직후부터 한마디도 하지 않았던 쌍둥이가 침묵을 깨트린 것도 그때였다.

“안으로 드십시오.”

“안으로 드십시오.”

어차피 더 이상 선택의 여지도 없는 상황이다.

초절정 고수와 떨어진다는 것만으로도 듣던 중 반가운 소리.

고개를 끄덕인 나는 상산왕을 호위하듯 앞서 철문 안으로 걸음을 내디뎠다.

드르륵. 쿵.

이내 다시 한번 들려오는 육중한 소음과 함께 등 뒤에서 문이 닫힌 그때. 천장에서 흐릿하게 빛나는 수많은 야명주(夜明珠)의 불빛 아래에서 한 사람이 걸음을 내디뎠다.

저벅.

가벼운 발걸음만큼이나 비쩍 마른 체구.

나이는 어림잡아 오십쯤 되었을까. 소매가 바닥이 끌릴 만큼 긴 장삼을 걸친 중년인의 모습을 발견한 상산왕이 먼저 입을 열었다.

“게 누구냐.”

게 누구냐. 게 누구냐. 게 누구냐…….

인적은커녕 개미 새끼 한 마리 찾아볼 수 없는 텅 빈 복도에 긴장한 목소리가 겹겹이 울려 퍼진다.

굳은 얼굴을 한 상산왕과 비스듬히 그 앞을 가로막은 나를 물끄러미 바라보던 중년인이 입을 연 것은 메아리가 사라진 그때였다.

“장성하신 상산왕 전하를 이리 가까이서 뵙고 보니, 지난 세월이 참으로 감개무량합니다.”

머뭇거리던 상산왕이 물었다.

“과인을…… 아는가?”

“물론입니다. 전하께서는 저를 기억하지 못하시겠지만.”

주름진 입가에 흐릿한 미소가 걸린다. 상산왕에게서 시선을 뗀 중년인이 나를 향해 고개를 돌렸다.

“그대는 초면이군.”

나는 대답 대신 잠시 침묵하는 것을 택했다. 중년인을 보자마자 쌍욕이 튀어나오려는 것을 간신히 참고 있었기 때문이었다.

이유? 간단하다.

눈앞의 중년인은, 아니 중년인‘도’ 초절정 고수였다.

‘아니 시팔…… 진짜 더러워서 못 해 먹겠네.’

황궁에 도착한 지 이제 겨우 이틀째다.

그것도 말이 좋아서 이틀이지, 실제로 머무른 시간만 따지면 하루인 열두 시진도 채 지나지 않았다.

그런데 지금까지 대면한 초절정 고수만 무려 다섯 명째.

‘제대로 좆 됐다.’

앞으로 옷 대신 콘돔을 입고 다녀야 하나 심각하게 고민하고 있던 그때, 중년인이 재차 입을 열었다.

“굳이 말해 주지 않아도, 이미 그대가 누구인지는 알고 있다네. 태원진가의 진태경.”

젠장. 이렇게 된 이상 어쩔 수 없다.

나는 한숨을 푹 내쉬며 대답했다.

“이 동네는 뭐 어딜 가나 다 알아보네.”

“황실의 눈과 귀는 어디에나 존재하고, 그대는 꽤나 눈에 띄는 편이니까.”

“잘생겨서?”

“아니, 한눈에 보아도 무뢰배 같기 때문이지.”

말하는 본새 보소.

“그럼 당신은 이 황실에서 어떤 위치지? 눈? 아니면 귀?”

“흠. 그대의 눈에 나는 무엇에 더 가까운 것 같나?”

“청소 담당.”

“뭐?”

“일단 지금도 옷소매가 질질 끌리는 게, 바닥 하나는 기똥차게 닦을 것 같은데.”

잠시 멍하니 나를 바라보던 중년인이 이내 소리 내어 웃었다.

“하하. 듣던 대로군.”

“듣긴 뭘 들어. 벌써 소문이라도 퍼졌나?”

“말했잖나. 어디에나 눈과 귀가 있다고. 이미 알 만한 이들은 다 알지. 감히 황궁에 발을 디딘 어느 간 큰 강호인에게 사람 웃기는 재주가 있다는 것쯤은.”

“그건 좀 희한하네. 나는 보통 사람을 웃기기보다는 속을 긁는 편이라.”

“전해 들은 여러 말에서 상당히 순화했다는 표현을 깜빡했군.”

“…….”

“물론 말해 주는 사람마다 평가가 뒤죽박죽이라 개인적으로 궁금하기도 했지. 자, 우선 이리로.”

대답할 틈도 없이 휙 돌아선 중년인은 자연스럽게 앞장서서 걷기 시작했다. 뒤도 돌아보지 않은 채.

“어딜 가는 거지?”

“재미있는 질문이군. 자네가 왜 이곳에 왔는지 잊었나?”

혹시나 했는데 역시나.

아무래도 저 중늙은이가 황제에게 향하는 세 번째 환승지이자, 우리를 종착역으로 데려다줄 마지막 안내자인 듯싶었다.

‘당연히 청소부는 아니고.’

도대체 정체가 뭘까. 복장으로도 판별하기가 어렵다.

동창? 아니면 금의위?

비쩍 마른 체구만 보면 환관에 가까운데, 천근처럼 묵직한 목소리는 금의위 귀싸대기도 후릴 정도다.

무엇보다 마치 제집을 드나드는 듯한 저 자연스러운 태도까지.

‘쌍둥이조차 여기까지 들어오지는 않았다. 그렇다면 황제가 신임하는 최측근 중의 최측근이라는 뜻인데…….’

지난밤 마삼보의 말에 의하면, 젊은 황제는 성정이 폭급하고 의심이 많아 거처인 건청궁에는 극소수의 고관대작과 검증받은 충복(忠僕)들만이 드나들 수 있다고 했다.

그뿐인가.

호위는 물론이거니와 궁내에 머무르며 각종 수발을 드는 환관과 여러 궁인까지.

그야말로 황제의, 황제에 의한, 황제를 위해 마련된 장소인 셈이다.

과연 이런 건청궁에, 그것도 이렇게 깊은 공간까지 아무나 드나들 수가 있을까.

모르긴 몰라도 금의위 지휘사 백연과 엇비슷한 위치는 되어야 가능할 것이다.

‘그렇다면 설마 이 자가 동창의 수장이라는 창공? 아냐, 그는 훨씬 더 늙은 데다 몇 년 전부터 병환으로 앓아누웠다고 했는데.’

재빨리 머리를 굴려봤지만 도통 떠오르는 인물이 없다.

마삼보가 짧게나마 언급한 이들의 숫자가 너무나도 많았던 데다, 그중 독특한 특징을 지닌 일부 인물들과도 일치되지 않았기 때문이었다.

‘이럴 때 기감 스킬이라도 사용할 수 있었다면…….’

아쉽지만 지금으로서는 어쩔 수 없다.

목마른 자가 우물을 파는 법.

어떻게라도 정보를 캐물어 보는 수밖에.

느긋하게 앞서가는 중년인의 뒤를 따라 걷던 나는 한 마디를 툭 던졌다.

“폐하는 언제쯤 알현할 수 있는 거지?”

“곧.”

“이 속도면 내일쯤 도착할 것 같은데.”

중년인이 뒤도 돌아보지 않고 피식 실소를 흘렸다.

“보이는 것만큼이나 참을성이 없군. 조금만 기다리게. 황상께서는 잠시 오랜만의 여흥을 즐기시는 중이거든.”

“여흥을 즐겨? 사람을 불러 놓고?”

“그래서, 불만이라도 토로할 셈인가?”

“……!”

“각자에게 주어진 위치가 있기 마련이지. 황위(皇位)에 올랐다는 것은 그들 모두를 굽어볼 수 있다는 의미고. 참으로 간단명료한 세상의 이치가 아닌가?”

나는 얼굴을 굳혔다.

황제의 행동에 불만이 있거나, 중년인의 대답이 정곡을 찔렀기 때문이 아니었다.

조금 전 그에게서 엿본, 대수롭지 않다는 표정과 말투. 작은 움직임 하나하나에 묻어 나오는 자연스러운 기세.

거기에 더해 마삼보가 언급한 황제의 측근 중 그 누구와도 겹치지 않는 용모까지.

‘설마.’

내심 침음성을 흘린 그 순간.

저벅.

중년인의 발걸음이 우뚝 멎었다. 어느덧 앞을 가로막은, 금은보화로 장식된 문을 망설임 없이 열어젖힌 그가 입을 열었다.

“폐하. 지엄하신 황명에 따라 말씀하신 두 사람을 데려왔나이다.”

그러나 어디에서도 들려오는 대답은 없었다.

아니, 그 어떤 인기척도 없었다.

이 거대한 침소에 두 발을 딛고 서 있는 것은 한 사람뿐이었다.

중년인.

그가 천천히 돌아선다. 우리를 향해 새하얀 이를 드러내며 웃었다.

“짧은 여흥이었으나, 제법 즐거웠다.”

“……!”

“……!”

한 줄기 번개가 등줄기를 타고 흘러내렸다.
```

## Final English reading copy

```markdown
# Chapter 871

Even the Embroidered Uniform Guard, called the Emperor’s hands and feet alongside the East Depot, apparently had its limits.

Jeong Hogun led Prince Shangshan and me over to the middle-aged twins, whose names I didn’t know, and sent us a brief Sound Transmission.

—From now on, you must be careful with every word you say and every move you make. Otherwise, you won’t come out of here alive.

Who the fuck did that bastard think he was kidding?

I could already feel it in my bones.

Not just because of those twin Supreme Peak masters who’d appeared out of nowhere, but because of all the people inside the palace whose presence I could sense even though we hadn’t entered yet.

*This place is insanely well guarded.*

My mouth felt dry, as if I’d swallowed sand. I slowly drew on my internal energy, carefully enough that no one would notice, and moved my lips.

—Just answer me one thing. Why the hell was I summoned?

—I told you I don’t know.

Are you saying you really don’t know, or that you know but won’t tell me?

—Both.

Damn it. I was an idiot for asking.

I glared at Jeong Hogun, who stood with his usual impassive face, then passed beneath the plaque reading Qianqing Palace alongside Prince Shangshan, who had climbed down from his palanquin.

Clop. Clop.

Our footsteps rang out unusually loudly.

I quietly sized up the twins’ backs as they walked in perfect sync, their movements identical down to the smallest detail.

*They’ve definitely trained in a combined attack technique…but what martial art, exactly?*

No matter how I looked at it, the situation was bad.

Not being able to guess what martial arts they’d learned was one thing. Just imagining two fully accomplished Supreme Peak masters using a combined attack technique made my stomach hurt.

And on top of that…

*Why the hell are there so many bats?*

Shadows that didn’t show even in the faint light.

Those watching our every move from the darkness had to be imperial guards trained by the royal family—and assassins.

If the worst came to pass, those assassins, nearly a hundred of them, would carve me up with the one-strike killing techniques they’d spent their lives honing.

Along with the twin Supreme Peak masters, who looked as if they’d learned their combined technique in the womb.

*Unless you’re one of the Ten Kings—or maybe a master on par with the Three Saints—you’re almost certainly going to be buried here.*

People say the martial world is a mountain of sabers and a forest of swords.

But they’re wrong.

This was the real mountain of sabers and forest of swords. A place where the Emperor alone decided who lived and who died.

*How many masters does he have under his command?*

The Nine Sects and One Gang and the Five Great Families might have two Supreme Peak masters at most. Some had only one. And here the Emperor had two of them working as gatekeepers.

It felt as if I were walking along a blade’s edge.

Just then, as a bead of cold sweat trickled down the back of my neck before I even realized it, I noticed a small hand tugging at my sleeve.

Squeeze.

A hand gripping so tightly that my sleeve crumpled. Only then did I notice the young prince’s ragged breathing.

*He’s trembling.*

Before he was a member of the imperial family or a prince, he was a child.

He’d been the same the first time I met him, and nothing had changed now.

He’d said he left the imperial palace when he was so young he couldn’t even remember it. Of course he wouldn’t remember the Son of Heaven, either.

*And now his only family, his one and only older brother, is threatening his life.*

A thought suddenly occurred to me.

The cheerful side Prince Shangshan had shown on the way to the imperial capital—maybe it was an attempt to hide his fear and disappointment.

When Hong Jin warned him that the Son of Heaven was a threat and he shook his head, saying that couldn’t be true…maybe that was the only choice a child could make when faced with a reality too hard to believe.

*He shouldn’t have to understand any of this…but he’s had to grow up far too soon.*

My feelings grew complicated.

I thought of the boy from that winter in Shanxi Province, when icy winds howled through the mountains. He’d lost his parents and climbed a hill with his tiny, fern-like hands clinging tight to his little sister.

And I remembered young Hayeon patting our mother’s back as she lay facedown, sobbing at our father’s funeral.

*Damn it.*

I bit my lip hard to hold back a sigh.

Murim and the modern world had nothing in common. They were completely different worlds.

But there was one thing that never changed.

People.

That was why I, who’d once thought all of this was a game, had started accepting Murim as another reality.

They were people, after all. They got angry, felt joy, and grieved.

There were evil people who deserved to die, and good people with eyes as clear as glass.

I’d killed the former without a moment’s hesitation. When it came to the latter, I’d even risked my life to help them.

And now, I felt sorry for this young prince.

His trembling breaths reminded me of the young siblings who’d lost everything and fled after Jopil’s attack. His small hand clutching my sleeve made me think of my own little sister, Hayeon.

*I need to think about this coldly. I have to. I can’t afford not to…*

But no matter how much I thought about it, I wasn’t sure I could.

If I had to choose between treason and submission, could I really leave this child behind?

Could I look back on it years later as if it meant nothing?

*Man, he really knows how to make things difficult.*

I smiled bitterly and looked down at Prince Shangshan, who didn’t even reach my chest.

Then, almost on impulse, I raised a hand and gently patted his head.

“……!”

His eyes flew wide, and his lips parted slightly, as if he were about to shout that I’d overstepped my bounds. But Prince Shangshan only stared up at me in surprise, his mouth working soundlessly.

Instead, the hand that had been gripping my sleeve so tightly loosened, as though he felt relieved.

Who had ever dared to pat this child on the head?

Even this little thing that every child his age should have experienced was something Prince Shangshan, Zhu Bao, had probably never known.

*This is the best I can do for him right now.*

Just then, the twins, who had been striding forward without hesitation, stopped in front of a massive door.

Click. Grrrrr.

With a heavy rumble, an iron door swung open, its surface carved with a dragon so lifelike it seemed to move. The twins, who hadn’t said a word since we entered the palace, broke their silence.

“Please enter.”

“Please enter.”

It wasn’t as though we had any choice left.

Besides, hearing that we’d be separated from the Supreme Peak masters was a welcome surprise.

I nodded, then stepped through the iron door ahead of Prince Shangshan, shielding him as I went.

Rrrr. Thud.

The heavy door shut behind us with another rumble. Beneath the faint light of countless night-shining pearls glowing on the ceiling, a man stepped forward.

Clop.

A slender frame, as slight as his light footsteps.

He looked about fifty. A middle-aged man in a long robe whose sleeves dragged along the floor. Prince Shangshan spoke first when he saw him.

“Who goes there?”

Who goes there? Who goes there? Who goes there…

His tense voice echoed again and again through the empty corridor. Not another person in sight—not even an ant.

The middle-aged man gazed at the tense-faced Prince Shangshan and at me, standing slightly in front of him to shield him. Only when the echoes had faded did he speak.

“To see His Highness Prince Shangshan grown so tall, and from so close, fills me with deep emotion after all these years.”

After hesitating, Prince Shangshan asked, “Do you…know me?”

“Of course. Though Your Highness does not remember me.”

A faint smile appeared on his wrinkled lips. The man turned his gaze from Prince Shangshan to me.

“You’re a stranger to me.”

I chose silence instead of answering. The moment I saw him, I’d had to fight to keep a string of curses from spilling out.

Why? Simple.

The middle-aged man in front of me—no, this middle-aged man, too—was a Supreme Peak master.

*No, fuck me… This is so goddamn unfair.*

I’d only been at the imperial palace for two days.

And that was being generous. If you counted the actual time I’d spent here, it hadn’t even been twelve shichen—a full day.

And yet this was already the fifth Supreme Peak master I’d come face-to-face with.

*I’m so screwed.*

Just as I was seriously wondering if I should start wearing a condom instead of clothes, the middle-aged man spoke again.

“You needn’t tell me who you are. I already know. Jin Taekyung of the Jin Family of Taiyuan.”

Damn it. There was no way around it now.

I let out a deep sigh and answered.

“Does everyone around here recognize me wherever I go?”

“The imperial court’s eyes and ears are everywhere. And you do stand out.”

“Because I’m handsome?”

“No. Because you look like a thug at first glance.”

Listen to the way this guy talks.

“Then what do you do around here? The eyes? Or the ears?”

“Hmm. Which do you think I’m closer to?”

“The cleaning crew.”

“What?”

“Your sleeves are dragging on the floor, so I figure you must be great at mopping.”

The middle-aged man stared at me blankly for a moment, then burst out laughing.

“Ha ha. Just as I’d heard.”

“Heard what? Are the rumors already spreading?”

“I told you—there are eyes and ears everywhere. Everyone who needs to know already does. They’ve heard that some audacious martial artist dared to set foot in the imperial palace and has a knack for making people laugh.”

“That’s strange. I usually get under people’s skin more than I make them laugh.”

“I forgot to mention that ‘making people laugh’ was a considerably toned-down version of what I’d heard.”

“……”

“Of course, the stories I heard were all over the place, so I was curious myself. Now, this way.”

Without giving me a chance to answer, the middle-aged man spun around and naturally took the lead, not even looking back.

“Where are we going?”

“Interesting question. Have you forgotten why you came here?”

I’d had my suspicions, and I’d been right.

Apparently, this old guy was the third transfer point on our way to the Emperor—and the final guide who would take us to our destination.

*Obviously, he wasn’t a cleaner.*

Who the hell was he? His clothes didn’t offer much of a clue.

The East Depot? Or the Embroidered Uniform Guard?

His gaunt frame made him look more like a eunuch, but his voice was so weighty it could knock even an Embroidered Uniform Guard off his feet.

And there was the way he moved around as naturally as if this were his own home.

*Even the twins didn’t come this far. So he must be one of the Emperor’s closest, most trusted confidants…*

According to Ma Sanbao last night, the young Emperor was hot-tempered and suspicious. Only a handful of high-ranking officials and trusted servants who’d proven their loyalty were allowed into his residence, Qianqing Palace.

And that wasn’t all.

The guards, of course, as well as the eunuchs and palace attendants who stayed inside to see to every need…

This place had been created for the Emperor, by the Emperor, and in service of the Emperor.

Could just anyone come and go in Qianqing Palace—let alone somewhere this deep inside?

I didn’t know for sure, but he’d probably need to be close in standing to Baek Yeon, Commander of the Embroidered Uniform Guard.

*Then could this guy be the East Depot’s leader, the Director? No. I heard he was much older, and that he’d been bedridden with illness for years.*

I quickly racked my brain, but no one came to mind.

Ma Sanbao had mentioned far too many people, and the man didn’t match the distinctive features of any of the few he’d described.

*If only I could use my Qi Sense Skill right now…*

But there was nothing I could do about that.

If you’re thirsty, you dig a well.

I’d just have to pry the information out of him somehow.

Walking behind the middle-aged man as he strolled along at an unhurried pace, I tossed out a question.

“When do I get to meet the Emperor?”

“Soon.”

“At this rate, we’ll get there tomorrow.”

The middle-aged man gave a quiet laugh without looking back.

“You’re as impatient as you look. Just wait a little. His Majesty is enjoying a rare diversion.”

“Enjoying a diversion? After summoning us?”

“And what, do you intend to complain?”

“……!”

“Everyone has a place of their own. To ascend the throne means to look down upon them all. Isn’t that a simple and straightforward truth of the world?”

My expression hardened.

Not because I objected to the Emperor’s behavior, or because the middle-aged man’s answer had struck a nerve.

It was the casual look and tone he’d just shown me. The effortless confidence that came through in every small movement.

And on top of that, he didn’t look anything like any of the Emperor’s confidants Ma Sanbao had mentioned.

*No way.*

The moment I let out a quiet groan inwardly—

Clop.

The middle-aged man came to an abrupt stop. He threw open the door before them, decorated with gold, silver, and jewels, without the slightest hesitation, then spoke.

“Your Majesty. In accordance with your solemn imperial command, I have brought the two people you requested.”

But there was no answer from anywhere.

In fact, there wasn’t a hint of anyone else’s presence.

Only one person stood within this enormous bedchamber.

The middle-aged man.

He slowly turned around. Then he smiled at us, showing his white teeth.

“It was a brief diversion, but I enjoyed it.”

“……!”

“……!”

A bolt of lightning shot down my spine.
```
