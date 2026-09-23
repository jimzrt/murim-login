<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0912.txt",
      "sha256": "326d2b5a216498ca329b5fb4010f784c1a76ec60526fb58e84674e874a8ad8ac",
      "bytes": 14063
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5dc14846d897c27fac352591c0bf5e7f93540125809146ab37c729bd8cfaa9d8",
      "bytes": 606
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66855c040f4342a0b241cbbead8026d866de6b64af95427c21f76fe8c96ddd55",
      "bytes": 231435
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "67f4f1ffe4e9a20390c3235f38f9b098a125bab7f9609b4a41b907854c4c727d",
      "bytes": 739
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6329758a61914281e6eb4052e7d11761de8a8dd3a89acda34031a2bff259e465",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "a0c4620c15bc9218b1d588a8683956d6282c7e6d7f2b867ea43f1bf83a968b8d",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "54f7716cb481bdc290a775aa1cedb906b9b50a8fbf24de9a95f60861799e9e0f",
      "bytes": 1270
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "27b90f878b3a3415fcd25c596ca43b6b492ead27603590d08cda3dcdb14ba84a",
      "bytes": 628
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "8e285a5094b5f8528cf7e75877ce17c0d30b3ccfb9b1525bb1c91c80e8f7e585",
      "bytes": 973
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3cbc7f6a53f0b54c2a601eea6dce75f328680991b435b0653839103b4b8c3ef1",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "3f88d929c814731421f518bc18887e60ec27d1a8740fdf25b312c66e57d5f944",
      "bytes": 851
    },
    {
      "path": "characters/Namho.md",
      "sha256": "d9a2035a15677b6bd78f8dc4dd759a41e2d479e44339e1d215d3c810b94845e5",
      "bytes": 973
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "fff288977931206b08584c145a02a93c097c4738c67137bb1ea13a47b893aaa5",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bb2e9ffe6030c82ee0fc3aa420d5a44251aa3c4f19cae1a57d73b3e2a76ca588",
      "bytes": 263408
    }
  ],
  "estimated_tokens": 12935
}
-->

# Durable State Update — Chapter 912

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
1 and safe_through 912. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 912. Profile updates may replace only one
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
  "chapter": 912,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 912,
    "continuity_sources": [912],
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
    "Jeok Cheongang has surpassed the Three Saints and killed the Eastern Heaven Demon Lord.",
    "Jeok Cheongang vowed to kill every member of Dark Heaven after Hong Dao was killed by the Blood Lord.",
    "Jeok Cheongang suffers unexplained cold pain immediately after the duel."
  ],
  "continuity_sources": [
    911
  ],
  "open_questions": [
    "What caused the sudden pain that struck Jeok Cheongang after the duel?",
    "Can Jeok Cheongang fulfill his vow to kill every member of Dark Heaven?"
  ],
  "safe_through": 911,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 소생      | **I**; occasionally “this humble one” in highly formal dialogue |
| 공자      | **Young Master**                                                |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 마삼보 | 정호군 | East Depot de facto leader to Embroidered Uniform Guard Thousand Captain | Commander Jeong | courteous and controlled | Ma Sanbao addresses him as 정 천호 while asserting procedural limits and drawing him into a conversation. |
| 정호군 | 마삼보 | Embroidered Uniform Guard Thousand Captain to East Depot official | Eunuch Ma | formal and guarded | Jeong Hogun addresses him as 마 태감 and shows wariness despite his restrained replies. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 908
- **Aliases:** None
- **Role:** Cang Gong is a formidable martial artist who has taken the bestowed title Eastern Heaven Demon Lord and intends to take Jin Taekyung to the Lord of Heaven for recruitment.
- **Personality:** Calculating and self-assured, he admires Taekyung's ability while believing the Lord of Heaven's power will make him submit.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He serves the Lord of Heaven, recalls a former master and fellow disciples as family, and is Ma Sanbao's master; he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 911
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 910
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 911
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 911
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 910
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 911
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 909
- **Aliases:** None
- **Role:** Ma Sanbao was the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 910
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 909
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃912화



모든 것이 섬광과도 같았다.

적천강이 자신의 등 뒤에서 날아든 섬뜩한 기운을 느낀 것도, 머릿속 붉은 경종이 울리며 몸을 비튼 것도.

그러나 그것은, 이성보다 앞선 본능으로도 온전히 피할 수 없었던 일격이었다.

콰득.

뜨겁다. 동시에 차갑다.

옆구리로부터 시작된, 도무지 어울리지 않는 상반된 통증이 들불처럼 전신으로 번져 간다.

도무지 해결할 수 없는 의문과 함께.

“……!”

적천강은 파르르 떨리는 눈빛으로 자신의 옆구리를 반쯤 파고든 무언가를 내려다보았다.

살과 뼈를 부수고, 몸 안의 혈도와 공력을 가닥가닥 끊어 낸 그것은 새하얀 손이었다.

마치 시체의 그것처럼 창백한, 아니 분명 시체가 되어 널브러져 있었어야 할 누군가의 손.

“네놈이, 네놈이 어찌.”

쥐어 짜낸 목소리와 함께 고개를 든 적천강의 시야에, 결코 보여서는 안 될 한 사람의 얼굴이 담겼다.

“분명…… 숨이 끊어졌었거늘.”

손의 주인, 동천마군(東天魔君)이 대답했다.

“그래, 그랬겠지.”

그리고 언제 그랬냐는 듯 담담한 목소리로, 한 줌의 고통도 찾아볼 수 없는 무감각한 표정으로 덧붙였다.

“하지만 천하의 그 누가, 하나뿐인 목숨을 두 번이나 잃을 수 있겠나.”

“……뭐?”

결코 이해할 수 없는 의문.

적천강은 부릅뜬 눈으로 동천마군을 바라보았지만, 대답 대신 돌아온 것은 몸 안을 파고드는 얼음장 같은 기운이었다.

‘위험!’

거의 동시였다.

강력한 장력(掌力)이 몸속 깊숙이 침투해온 것과, 적천강이 섬광처럼 몸을 비틀어낸 것은.

그러나 예상치 못한 일격을 허용한 몸은, 그 공격을 완전히 피해내지 못했다.

퍼엉!

적천강은 일순간 아득해진 시야 속에서 입술을 깨물었다.

‘큭.’

상당한 격통.

전신을 둘러싼 호신강기(護身罡氣)가 연기처럼 흩어지는 것을 느끼며, 적천강은 쏘아지듯 뒤로 튕겨 나갔다.

쐐애애액!

시야가 흐릿하게 물든다. 하늘과 땅이 수없이 뒤집혔다.

이름 모를 누군가의 비명이, 포탄처럼 튕겨 나간 몸뚱어리에 부딪친 무언가의 파편이 사방으로 튀었다.

어지간한 초절정 고수라 해도 단번에 전투 불능 상태에 빠졌을 상황.

그러나 그는, 화왕(火王) 적천강은 아니었다.

콰드드득! 쾅!

허공에서 몸을 비틀어 균형을 바로잡은 그의 발끝이 지면을 밟았다.

수 장에 달하는 깊은 고랑을 만들어내며 아직 남아 있는 여파를 상쇄한 적천강의 신형이 불현듯 비틀거렸다.

쿨럭.

입술 사이로 넘쳐 흐르는 검붉은 핏물.

내상과 함께 차오른 울혈(鬱血)을 참지 못하고 토해 낸 적천강의 귓가에, 미세한 파공성이 닿은 것은 바로 그때였다.

쉭.

보지 못했다. 그러나 느껴진다.

자신의 머리 위로 내리꽂히는 일격이. 빙하처럼 차갑고 새하얀 빛을 뿜어내는 손을 뻗어오는 동천마군의 모습이.

적천강은 반 박자 앞서 머릿속에 그려진 그 광경을 떠올리며, 땅을 박찼다.

슈확! 쾅!

찰나를 쪼개고 쪼갠 짧은 순간 속, 아슬아슬하게 스쳐 지나간 일격이 지면을 두부처럼 가르고 폭발하며 거대한 구덩이를 만들어 낸다.

운 없게도 주위에 있던 몇몇 금의위를 집어삼키며.

하지만 사냥감을 놓친 맹수의 추격은 그것으로 끝이 아니었다.

쉬릭.

마치 뱀처럼 매끄러운 움직임.

구덩이 속에서 몸을 일으켜 세운 동천마군은 물러나는 적천강을 향해 걸음을 뗐다.

파팟. 순식간에 거리를 지워 낸 그의 손끝에서 시리도록 눈부신 백광(白光)이 터져 나왔다.

화아악.

휘황하면서도 섬뜩한 그 빛이 어둠을 집어삼키며 부풀어 오르는 광경을 바라보며, 적천강은 이를 악물었다.

으득.

미약한 통증과 함께 입안에 감도는 혈향.

그제야 비로소 흐릿했던 시야에 초점이 잡힌다. 무뎌졌던 감각이 돌아오며 내상으로 말미암은 격통이 더욱 심각해졌지만, 적천강은 개의치 않고 전신의 공력을 끌어올렸다.

우우웅.

차갑게 식었던 공기가 달아오른다. 가닥가닥 끊겨 나간 혈맥이 비명을 지른다.

불안정한 통제 속에서 몸 안의 화룡이 거칠게 몸을 틀었다.

주인의 몸뚱어리마저 태워 버릴 듯이.

삼키고 불태워 잿더미로 만들어 버릴 듯이.

그러나.

“네놈이 어떤 괴이한 힘으로 되살아났는지는 모르겠으나.”

적천강은 한 치의 흔들림도 없는 눈동자로 동천마군을 직시했다. 용암처럼 이글거리는 목소리로 말을 이었다.

“그 질긴 목숨, 노부가 끊어내 주마.”

그것이 설령 수십, 수백 번이라 할지라도.

미처 흘리지 못한 뒷말은 굳게 다문 입술에 가로막혔으나, 사지백해를 뜨겁게 달구며 용솟음친 수 갑자의 열양지기는 아니었다.

콰우우우!

용의 포효와도 같은 굉음 속, 광염(光焰)과 백광(白光)이 서로를 향해 쏘아졌다. 마침내 맞닿았다.

미증유의 기운으로 일그러진 그 공간의 중심에서.

후퇴를 명령하는 정호군의 비명과도 같은 외침마저 집어삼키며.

화아악.

그리고 시야를 가득 채운 그 아득한 섬광 속에서, 적천강은 귓가로 전해져 오는 한 사람의 목소리를 들었다.

- 노야!

다음 순간.

구구구구궁!

온 세상이, 하늘과 땅이 뒤흔들렸다.



* * *



그런 순간이 있다.

세상이 멈췄다고 느낄 때가.

사방을 떨어 울리는 충격과 굉음으로 모든 감각이 마비되는 순간이.

내게는 바로 지금이 그랬다.

“……!”

어느 날 하늘 위에서 떨어진 태양을 코앞에서 마주한다면 이런 기분일까.

이목을 가리고 틀어막은 섬광과 굉음 앞에서, 내가 할 수 있었던 것은 곧 들이닥칠 거대한 여파로부터 가까이에 있는 사람들을 최대한 지키는 것뿐이었다.

“당장 엎드……!”

모르겠다. 내 다급한 외침이 화룡각 대원들에게 닿았을지. 과연 그들이 내 말을 따라 곧장 자세를 낮추었을지.

다만 한 가지 확신할 수 있는 것은, 촌각이라도 지체했다면 그들 중 누구도 두 발로 서 있지 못했을 거라는 사실뿐이었다.

콰아아아아!

드드드득!

미친 듯이 휘몰아치는 광풍에 몸이 밀려 나간다. 화산지대처럼 지면이 뒤집히는 동시에 수십, 수백 개의 파편으로 나뉜 청석이 암기처럼 쏟아져 사방을 덮쳤다.

이미 숨이 끊긴 망자들의 시체. 그리고 그들의 묘비처럼 곳곳에 나뒹굴던 무수한 병장기들과 함께.

쉬쉬쉬쉭, 푸푹!

크아악!

이름 모를 누군가의 핏물이, 비명이 바람에 섞여 흩어진다.

하지만 나는 지면 깊숙이 두 발을 박아넣은 채 충격파를 온몸으로 견뎠다.

서서히 바닥을 드러낸 공력을 쥐어짜 이곳으로 날아드는 모든 것들을 쳐내고 베었다.

피핏!

몰아치는 바람 속에서 날아든, 작고 얇게 조각난 날붙이와 청석의 파편들이 전신 곳곳을 할퀴며 지나가도 아랑곳하지 않았다.

‘내가 피하면 다른 대원들이 다친다.’

필연적으로 누군가가 다칠 수밖에 없다면, 그 누군가가 나 자신인 것이 백배 천배 낫다.

‘노야 역시 그런 마음이었겠지.’

마지막 순간, 나는 똑똑히 보았다.

내 외침을 들은 그가 불현듯 신형을 틀어 우리가 향하는 방향을 가로막는 모습을.

콰아아아…….

도대체 얼만큼의 시간이 흐른 것일까.

영원처럼 길게 느껴졌던 시간 너머, 서서히 잦아들기 시작하는 굉음과 충격이 느껴진다.

곧이어 바람을 타고 허공으로 솟구쳤던 수많은 것들이 한둘씩 떨어져 내리고, 먹먹해졌던 귓가는 잠시 음소거되었던 주위의 소리를 받아들이기 시작했다.

“끄으으.”

“사, 살려. 살려 주…….”

적아를 불문하고 뒤엉켜 쓰러진 이들이 토해 내는 신음. 죽음을 앞둔 누군가의 간절한 부탁.

그리고 마지막으로 등 뒤에서 들려오는 익숙한 목소리들까지.

“다들, 다들 무사하십니까?”

“쿨럭, 소생은 괜찮습니다.”

“태산이, 오향장육 이백 접시 생각하면서 이 악물고 버텼다.”

“이런 상황에 정말 미안한 부탁이지만, 혹시 저 새끼 이빨 부숴 줄 사람 없나?”

남호의 말에 대답해 주고 싶었지만, 맥이 풀린 탓에 그조차도 쉽지 않다.

순간 비틀거리는 내 모습에 다급히 다가온 두 사람이 양팔을 붙잡았다.

“은인, 아니 진 공자, 아니 각주님.”

“조장님, 괜찮으세요?”

나는 주화란에게 호칭은 하나로 통일하라고 말해 주고, 지금 이게 괜찮아 보이냐는 뜻으로 혁무진을 지그시 노려본 다음, 수십여 장 밖에서 석벽을 타 넘고 있는 언데드 군단을 확인했다.

역적이 되지 않기 위해 말을 갈아탄 금위군들은, 이제 갑작스럽게 나타난 괴물들에 의해 분분히 피를 뿌리며 쓰러지고 있었다.

‘빌어먹을. 차라리 이곳까지 끌어들일 걸 그랬나.’

만약 그랬다면 놈들에게 조금이라도 타격을 줄 수 있지 않았을까 하는 아쉬움이 들었지만, 어떻게 되었을지는 아무도 모를 일이다.

저놈들은 말 그대로 언데드(Undead)니까.

팔다리가 무참히 뜯겨 나가도, 가슴이 관통당해도 일어나는 괴물들이니까.

하지만 괴물이라는 단어는, 꼭 흉측하거나 괴이한 힘을 지닌 것들에만 허락된 것이 아니다.

상식으로 재단할 수 없는 무언가를 보았을 때, 사람들은 그것을 괴물이라 부른다.

그리고 그 괴물의 범주 안에는 화왕(火王)이라 불리는 이 또한 포함되어 있었다.

파팟!

만류하는 혁무진을 밀어 내며, 나는 최대한 빠른 걸음으로 적천강을 향해 다가갔다.

아니, 다가가려 했다.

다음 순간 들려온, 적천강의 한 마디가 아니었다면.

“물러나거라.”

평소와는 달리 깊게 가라앉은 목소리.

전신이 핏물과 그을림으로 가득한 그는, 몇 걸음 뒤에 있는 내게는 눈길 한 번 주지 않은 채 정면을 응시했다.

차츰 가라앉아 가는 먼지구름 너머, 홀로 우뚝 서 있는 그림자를.

그리고 바로 그때.

화악.

어디선가 불어온 한 줄기 바람이 먼지구름을 걷어 냈다. 그 너머에서 무수한 시체와 피 웅덩이를 밟으며 천천히 걸어오던 그림자의 모습이 드러났다.

“……!”

순간, 무의식적으로 숨을 삼킨 나는 비로소 깨달았다.

왜 적천강이 물러서라 했었는지.

비록 잠시뿐이지만 바로 옆자리에 있던 누군가에게서, 왜 조금의 인기척도 느낄 수 없었는지.

“대단하군, 화왕 적천강. 실로 대단해.”

철벅.

나아가는 발걸음과 함께, 발목까지 고여 있던 핏물이 사방으로 비산한다.

이름 모를 누군가의 것이었던 팔다리가 핏물에 밀려 둥둥 떠다닌다.

그러나 그중 무엇도, ‘저것’만큼 섬뜩한 분위기를 자아내지는 못했다.

“하마터면, 정말 죽을 뻔했지 뭔가.”

치직. 치이익.

지금 이 순간에도 남아 있는 불길에 타들어 가는 얼굴 아래, 유일하게 형태를 보존한 입술이 부드럽게 호선을 그린다.

창공은, 동천마군은, 아니 더는 인간이라 부를 수 없는 그는 웃고 있었다.

녹아내린 살갗과 그 안에 감춰져 있어야 할 뼈를 훤히 드러낸 채.

피륙으로 이루어진 사람이라면 몇 번이나 죽고도 남았을 끔찍한 모습으로 적천강을, 그리고 그의 어깨 뒤에서 굳어 버린 나를 바라보았다.

그리고 불쑥 입을 열었다.

“사제지간이 아주 돈독해 보이는군. 그렇게 생각하지 않으냐?”

그 순간, 두 번 다시 들을 수 없다고 생각했던 목소리가 귓가에 닿았다.

“예, 스승님.”

“늦었구나.”

“용서하십시오. 불초 제자의 공부가 부족했습니다.”

대답과 함께 비틀거리며 일어나는 또 하나의 인영.

내 손으로 직접 몸 깊숙이 심어 주었던 단창을 뽑아내며 다가오는 마삼보의 모습에, 적천강이 중얼거렸다.

“스승?”

“왜, 이상한가?”

동천마군이 걸음을 내디디며 말을 이었다.

“한때는 내게도 사문이 있었지. 부모가, 가족이 되어 주었던 스승과 수많은 사형제들이.”

“……네놈, 설마.”

“하지만 그들은 모두 죽었다. 사문의 터전을 지키기 위해서, 말도 안 되는 억압에 맞서 싸우다가 피를 흘리며 쓰러졌지.”

동천마군이 천천히 고개를 돌렸다. 공허한 그의 시선 끝에는, 높고 화려한 태사의에 앉아 있는 황제가 있었다.

아니, 이미 흘러 지나가 버린 과거가 있었다.

“천도(遷都)라는 명목하에, 나는 그렇게 모두를 잃어야만 했다.”

“……!”

“……!”

그 순간, 나는 깨달았다.

놈의 진짜 정체가 무엇인지. 암천의 동천마군이기 이전에, 동창의 창공이기 이전의 그가 어디에 속했었는지.

그리고 그것은 적천강 역시 마찬가지였다.

“……모산파(茅山派).”

신음 같은 한 마디가 그의 입술 사이로 흘러나온 그때.

드득. 드드득.

마침내 석벽을 함락시킨 망자의 군단이 대연회장으로 들이닥쳤다.
```

## Final English reading copy

```markdown
# Chapter 912

Everything happened in a flash.

Jeok Cheongang sensed the sinister energy flying at him from behind. The red alarm bells in his mind rang, and he twisted his body.

But even instinct, faster than reason, couldn’t help him fully evade that strike.

*Crunch.*

It was hot. And cold at the same time.

A pain that made no sense, beginning in his side, spread through his entire body like a wildfire.

Along with an impossible question.

“……!”

Jeok Cheongang looked down, his eyes trembling, at something buried halfway in his side.

It had crushed flesh and bone, severing the vital points and internal energy inside him strand by strand. The hand was as pale as a corpse’s—or rather, it belonged to someone who should have been lying dead.

“How could you… how could you…”

Jeok Cheongang lifted his head, squeezing the words out. In his field of vision was a face that should never have been there.

“You had… stopped breathing.”

The owner of the hand, the Eastern Heaven Demon Lord, replied.

“Yes. I had.”

Then he added, his voice as calm as if nothing had happened, his expression numb and free of even a hint of pain:

“But who in this world can lose his one and only life twice?”

“……What?”

Jeok Cheongang stared at the Eastern Heaven Demon Lord, eyes wide with an incomprehensible question. But instead of an answer, an icy energy burrowed into his body.

*Danger!*

It happened almost at the same time.

Powerful force from the palm drove deep inside him at almost the same instant Jeok Cheongang twisted away in a flash.

But his body, caught off guard by the unexpected blow, couldn’t evade the attack completely.

*Boom!*

Jeok Cheongang bit his lip as his vision blurred for an instant.

*Damn.*

The pain was intense.

Feeling the Body-Protecting Qi around him scatter like smoke, Jeok Cheongang shot backward.

*Whoooosh!*

His vision blurred. The sky and earth flipped over and over.

An unknown person’s scream rang out. Fragments of something that had struck his body as it shot away flew in every direction.

It was enough to knock even a Supreme Peak master out of a fight in one blow.

But he wasn’t just anyone.

He was Jeok Cheongang, the Fire King.

*Crack! Bang!*

He twisted in midair, righted himself, and landed on his feet.

Jeok Cheongang carved a deep furrow several *jang* long into the ground, absorbing the remaining force. Then his body suddenly staggered.

*Hack.*

Dark red blood spilled from between his lips.

Unable to hold back the congested blood that had risen with his internal injuries, Jeok Cheongang spat it out. That was when a faint whistle reached his ears.

*Whoosh.*

He hadn’t seen it. But he could feel it.

A strike plunging down toward his head. The Eastern Heaven Demon Lord reaching out with a hand that shone an icy, glacial white.

Picturing the scene that had formed in his mind half a beat ahead, Jeok Cheongang pushed off the ground.

*Shwaaack! Boom!*

In a brief moment split into ever smaller fractions, the strike narrowly missed him. It cleaved through the ground like tofu, then exploded, leaving a gigantic crater.

A few Embroidered Uniform Guards nearby were unlucky enough to be swallowed up by it.

But the pursuit of a predator that had missed its prey didn’t end there.

*Swish.*

The movement was as smooth as a snake’s.

The Eastern Heaven Demon Lord rose from the crater and stepped toward the retreating Jeok Cheongang.

*Papap!*

In an instant, he erased the distance between them. A dazzling, icy white light burst from his fingertips.

*Fwoosh.*

Watching that brilliant yet dreadful light swallow the darkness and swell, Jeok Cheongang gritted his teeth.

*Crack.*

A faint pain, and the taste of blood in his mouth.

Only then did his blurred vision come into focus. His dulled senses returned, and the pain from his internal injuries grew more severe. Jeok Cheongang paid it no mind and drew up the internal energy throughout his body.

*Wooooong.*

The air, chilled moments ago, grew hot. His torn meridians screamed.

Within his unsteady control, the fire dragon inside him writhed violently.

As if it would burn even its master’s body.

As if it would devour everything and reduce it to ashes.

And yet—

“I don’t know what kind of bizarre power brought you back to life.”

Jeok Cheongang stared straight at the Eastern Heaven Demon Lord, his gaze utterly unwavering. His voice burned like lava as he continued:

“But I’ll put an end to that stubborn life of yours.”

Even if he had to do it dozens, hundreds of times.

His tightly closed lips held back the words he left unsaid. But they could not hold back several *jiazi*’ worth of Scorching Yang Qi as it surged through his body, setting every limb and meridian ablaze.

*KWAOOOOO!*

Amid a roar like a dragon’s bellow, light-flames and white light shot toward each other. At last, they collided.

At the center of that space, warped by unprecedented energy—

Even Jeong Hogun’s scream-like cry for a retreat was swallowed up.

*Fwoosh.*

And in the blinding flash that filled his vision, Jeok Cheongang heard someone’s voice reach his ears.

“Old Master!”

The next moment—

*Rumble, rumble, rumble!*

The entire world—the sky and the earth—shook.

* * *

There are moments like that.

Moments when it feels as if the world has stopped.

Moments when every sense goes numb from the shock and roar reverberating in every direction.

That was exactly how it felt to me right then.

“……!”

If the sun fell from the sky one day and landed right in front of you, would it feel like this?

With the flash and roar blinding and deafening me, all I could do was protect the people nearby as best I could from the enormous impact about to hit us.

“Get down, ri—!”

I didn’t know. I didn’t know if my frantic shout had reached the Fire Dragon Pavilion members, or if they had immediately followed my order and dropped low.

There was just one thing I knew for certain: if they’d hesitated for even a moment, not one of them would still be standing.

*KWAaaaaa!*

*Rrrrcrack!*

My body was shoved back by the wildly raging gale. The ground overturned like a volcanic field, and the bluestone broke into dozens, hundreds of fragments that rained down in every direction like hidden weapons.

Along with the corpses of the dead, and the countless weapons that had been scattered all around like their gravestones.

*Sh-sh-sh-shik! Thud!*

“Aaargh!”

Someone’s blood and screams scattered on the wind.

But I drove both feet deep into the ground and endured the shock wave with my whole body.

I squeezed out the last of my internal energy, batting away and cutting through everything that came flying at us.

*Pit-pit!*

Even when small, thin fragments of blades and bluestone swept in with the gale and grazed me all over, I didn’t care.

*If I dodge, the others will get hurt.*

If someone was bound to get hurt, it was a hundred, a thousand times better for that someone to be me.

*Old Master must have felt the same way.*

At the very last moment, I’d seen it clearly.

He’d heard my shout and suddenly shifted to place himself across the path we were headed down.

*KWAaaaaa……*

How much time had passed?

Beyond what felt like an eternity, the roar and impact began to subside.

Then, one by one, the things that had been carried into the air by the wind fell back down. The muffled sounds around me, silenced for a moment, began to filter back into my ears.

“Ungh……”

“P-please. Someone, please……”

The groans of the fallen, tangled together, from both sides. Someone’s desperate plea as death approached.

And finally, the familiar voices behind me.

“Is everyone—everyone all right?”

“Cough. I’m fine.”

“Taishan gritted his teeth and held on while thinking about two hundred plates of five-spice pork.”

“I’m really sorry to ask at a time like this, but is there anyone who can break that bastard’s teeth?”

I wanted to answer Namho, but my strength had given out, and even that was difficult.

When I staggered, two people hurried over and grabbed me by both arms.

“Benefactor—no, Young Master Jin—no, Pavilion Master.”

“Captain, are you all right?”

I told Ju Hwaran to pick one form of address and stick to it. Then I gave Hyuk Mujin a pointed glare that meant, *Do I look all right to you?* After that, I looked beyond him and saw the undead army climbing over the stone wall several dozen *jang* away.

The Imperial Guards, who had changed sides to avoid being branded traitors, were now falling in droves, blood spilling beneath the sudden attack of those monsters.

*Damn it. Maybe I should’ve lured them here after all.*

I couldn’t help wondering if we might have done some damage to them if I had, but there was no way to know what would’ve happened.

Those things were undead, plain and simple.

Monsters that got back up even when their arms and legs were torn off, or their chests were pierced.

But the word *monster* wasn’t reserved only for those with grotesque appearances or strange powers.

When people see something that can’t be judged by common sense, they call it a monster.

And among those monsters was the man known as the Fire King.

*Papap!*

I pushed Hyuk Mujin aside as he tried to stop me, and hurried toward Jeok Cheongang as fast as I could.

No—I tried to.

If not for the one thing Jeok Cheongang said next.

“Stand back.”

His voice was far deeper than usual.

His entire body was covered in blood and soot, but he kept his eyes fixed ahead without even glancing at me, though I stood a few steps behind him.

At the solitary figure standing upright beyond the dust cloud as it slowly settled.

And right then—

*Fwoosh.*

A breeze blew from somewhere, sweeping away the dust cloud. Beyond it, the figure came into view, walking slowly over countless corpses and pools of blood.

“……!”

I instinctively caught my breath. Only then did I understand.

Why Jeok Cheongang had told me to stand back.

And why I hadn’t sensed even the slightest sign of life from someone who had been right beside us, if only for a moment.

“Impressive, Fire King Jeok Cheongang. Truly impressive.”

*Squish.*

With each step, blood that had pooled to his ankles sprayed in every direction.

Arms and legs that had belonged to someone unknown bobbed in the blood as it pushed them along.

But none of it created as dreadful an atmosphere as *that thing*.

“I very nearly died, you know.”

*Crackle. Sizzle.*

Beneath his face, still burning in the flames, the only part that had kept its shape—his lips—curved into a gentle smile.

Cang Gong—the Eastern Heaven Demon Lord—or rather, the man who could no longer be called human, was smiling.

His melted skin and the bones that should have been hidden beneath it were exposed for all to see.

His appearance was so horrific that anyone made of flesh and blood would have died several times over. He looked at Jeok Cheongang, then at me, frozen behind his shoulder.

Then he spoke without warning.

“You two seem very close, master and disciple. Don’t you think?”

At that moment, I heard a voice I’d thought I’d never hear again.

“Yes, Master.”

“You’re late.”

“Forgive me. Your unworthy Disciple’s training wasn’t sufficient.”

As he answered, another figure staggered to his feet.

Ma Sanbao pulled the short spear I’d driven deep into his body and approached. Jeok Cheongang murmured:

“Master?”

“Why? Is that strange?”

The Eastern Heaven Demon Lord stepped forward and continued:

“I once had a sect, too. A Master who became a parent to me, and countless Senior and Junior Brothers who became my family.”

“……You bastard. Don’t tell me…”

“But they all died. They bled and fell while trying to protect their sect’s home, fighting against an oppression that made no sense.”

The Eastern Heaven Demon Lord slowly turned his head. At the end of his empty gaze sat the Emperor, on a tall, ornate throne.

No—what lay there was a past that had long since slipped away.

“Under the pretext of moving the capital, I had to lose them all.”

“……!”

“……!”

At that moment, I realized who he really was. Before he became the Eastern Heaven Demon Lord of Dark Heaven, before he became Cang Gong of the East Depot, where had he belonged?

Jeok Cheongang realized it, too.

“……The Maoshan Sect.”

As those words, like a groan, slipped between his lips—

*Crick. Crrrick.*

At last, the army of the dead breached the stone wall and poured into the grand banquet hall.
```
