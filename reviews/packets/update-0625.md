<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0625.txt",
      "sha256": "e36df005510b56e1d7b8209b7381f5eaf77a5a877e31c1c8ac64b2ed8eda996d",
      "bytes": 12870
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8f8b383848792259d0aa442fbdd89ed40c54c8a52e7b5d8870f67c11a3215cdd",
      "bytes": 1653
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0935525ca5e9db05317a58245bf31faa25ce4cdec90b67ac01faced137cfc8b1",
      "bytes": 193161
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "451c00c3baab9d946f79cfb80adf5f416e476c39804cdd3b6b855ebdbc26ad37",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "298672da3293764895f97bdb086412805444f79861896a13232bceeab7e335cb",
      "bytes": 1206
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "39749861a404924c9334475d703b3a9b0a3de17bc45ccae341d85d51942c3910",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4d1114092534e18a98b6543fd1d083f401bd94e4e452807d20a123b7063168f7",
      "bytes": 1857
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "97b730ae18af531f02919f2595e28eae4e3e05335b089c6a74325248b58d618a",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "47311654c7f5295046b44178b1794eb62807d581133b7855e1851abc09b83d83",
      "bytes": 1043
    },
    {
      "path": "characters/Namho.md",
      "sha256": "f9eec308b8af17fca47c454dec97da4235f15785f960a253037649de8f2c1792",
      "bytes": 843
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "e33adcd99b589cdcc5404df59f7667962b36254d8a9a1ba358db6d4bc4e28f91",
      "bytes": 528
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "8e6f5864c863efb50c6c5bd9285980ced4d400212cdbeae92a885f730b8c95d5",
      "bytes": 828
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ffd49db9c4d73a678f71ed2124ac4f51b29dde03142d5d819ad199657624ba9e",
      "bytes": 197019
    }
  ],
  "estimated_tokens": 12338
}
-->

# Durable State Update — Chapter 625

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 625. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 625. Profile updates may replace only one
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
  "chapter": 625,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 625,
    "continuity_sources": [625],
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
    "The Fire Dragon Pavilion is inside the Nanman Beast Palace's territory and has now reached its massive Outer Hall under Yayul Mok's escort.",
    "Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, rides a long-bonded white tiger, and understands Han Chinese well enough to follow Taekyung's remarks.",
    "Yayul Cheok is the Beast Miao King, lord of the Nanman Beast Palace and leader of the Miao people.",
    "Taishan is a major Fire Dragon Pavilion asset but his childlike appetite creates immediate operational problems, including attacking animals for food.",
    "Nanman residents distrust Han Chinese because the Heavenly Demon Escort Bureau recently massacred a Miao village.",
    "Sama Pyo suspects the massacre's timing may be connected to a larger scheme, while Song Ilseom remains openly hostile toward him.",
    "Taekyung has sensed the Beast Miao King's powerful aura and identified him before their conversation begins."
  ],
  "continuity_sources": [
    624
  ],
  "open_questions": [
    "How will the Beast Miao King respond to the Fire Dragon Pavilion's arrival and the recent massacre's effect on Nanman's view of Han Chinese?",
    "Was the timing of the Heavenly Demon Escort Bureau massacre connected to Dark Heaven's scheme?"
  ],
  "safe_through": 624,
  "temporary_decisions": [
    "Use Yayul Mok for 야율목 and Yayul Cheok for 야율척.",
    "Use Young Palace Lord for 소궁주 and Beast Miao King for 야수묘왕.",
    "Render 一山有四季, 十里不同天 as “One mountain holds four seasons, and ten li bring a different sky.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 주화란    | **Ju Hwaran**      |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 평화 | **Peace Guild** | Guild name. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 숭산결의 | **Mount Song Resolution** | The event marking the formal gathering of the Murim Alliance at Mount Song. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 620
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 624
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 622
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 623
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 623
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 624
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, and someone who can understand the Miao and Bai languages.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 624
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 624
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 624
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and lord of the Nanman Beast Palace; his white tiger is a long-bonded companion; he orders Jin Taekyung and the Fire Dragon Pavilion to follow him after the pasture fire.

## Korean source

```text
＃625화



사람에게는 기세(氣勢)라는 것이 있다.

어떤 사람이 품은 기세는 미약하고 흐릿하여 거의 느껴지지 않지만, 또 다른 누군가의 기세는 강대하고 파도처럼 거칠어 마주하는 것만으로도 상대를 압도한다.

야수묘왕(野獸苗王) 야율척은 후자였다.

스윽.

천천히 몸을 일으키는 야율척의 모습은 마치 거산이 움직이는 것 같았다.

분명 팔순이 넘은 나이임에도 불구하고 전신을 갑옷처럼 둘러싼 근육은 탄탄했고, 한 발 한 발 옮기는 걸음은 거침없었으며 반백의 수염은 사자의 갈기처럼 흩날렸다.

저벅, 저벅.

넝쿨로 뒤덮인 계단을 맨발로 짓밟으며 다가오는 그의 모습을, 이제는 모두가 볼 수 있었다.

야율목과 그의 호위들은 즉각 안장에서 내려 한쪽 무릎을 꿇었다. 남만야수궁의 주인에게 바치는 그들만의 예법이었다.

“궁주를 뵙습니다.”

야수묘왕이 야율목을 물끄러미 응시했다.

“또 말도 없이 뛰쳐나갔더구나.”

“북동쪽의 목초지에서 화재가 일어났었습니다. 때마침 근처에 있던 터라…….”

“불길은 잡았느냐?”

“예.”

“흉수는?”

분명 야율목을 향한 질문인데, 야수묘왕의 시선은 나를 향하고 있었다.

나는 거친 안광을 뿜어내는 그의 호목(虎目)을 똑바로 응시하며 앞으로 나섰다.

“흉수라고 하기에는 좀 뭣하고, 실수가 좀 있었습니다.”

“오랜만에 보는 한인들이로군. 네놈이 화재를 일으킨 흉수냐?”

내가 뭐라 대답하기도 전, 으르렁거리는 듯한 목소리가 이어졌다.

“잘 생각하고 대답해야 할 것이다. 남만의 규율은 결코 자비롭지 않으니.”

잠깐 생각하던 내가 물었다.

“혹시 이런 경우에는 처벌이 어떻게 됩니까?”

“피해 정도에 따라 다르겠지만 심한 경우에는 맹수의 먹잇감이 된다. 독물이 가득한 구덩이에 처넣거나.”

“약한 경우에는요?”

“넝쿨에 목을 매달지.”

“그게 약한 겁니까?”

“물론. 시신은 온전히 보호할 수 있으니.”

“아하.”

고개를 끄덕인 내가 슬쩍 옆으로 비켜서며 한 사람을 소개했다.

“짠. 사실 흉수는 제가 아니라 이분입니다.”

평범한 사람이었다면 당황했겠지만 오십 년 경력의 은영각 요원은 확실히 달라도 뭐가 다르다. 남호가 침착한 목소리로 입을 열었다.

“자네 혹시 미친 새낀가?”

“아니, 틀린 말은 아니잖아요.”

“이 씨벌 놈이…….”

남호가 본격적으로 쌍욕을 퍼부으려던 그때, 야수묘왕이 거친 음성을 툭 내뱉었다.

“동료를 버리고 살길을 찾겠다는 거군.”

“음. 오해가 있으신 모양인데, 버린다고는 한 적 없습니다.”

“오해?”

“우선 팩트, 아니지. 사실을 짚고 넘어간 것뿐입니다. 솔직히 만난 지는 얼마 되지 않았지만 그래도 좋은 분이라서요. 무림맹 체면도 있고.”

의도적으로 무림맹을 운운했으니 이쯤에서 물러설 만도 한데, 한번 타오르기 시작한 야수묘왕의 안광은 조금도 수그러들지 않았다.

“남만에 들어온 이상, 남만의 규율을 따라야 하는 법. 이 중 누군가는 반드시 책임을 져야 한다면?”

“정 그러시다면 뭐…….”

나는 뒤통수를 긁적이며 말을 이었다.

“어떻게든 막아야 하지 않겠습니까.”

그리고 그 순간.

후웅!

주위의 공기가 사라졌다. 짧고 묵직한 파공성보다 먼저 쏘아진 일권(一拳). 공성추와도 같은 힘이 실린 그것을 향해, 나는 양팔을 교차시켰다.

꽈앙!

하늘이 갈라지는 듯한 굉음이 울려 퍼지고, 격돌의 충격파가 사방을 휩쓸었다.

엄청난 거력에 의하여 일 장을 밀려난 나는 한숨을 내쉬었다.

“이 정도면 충분합니까?”

야수묘왕이 서릿발 같은 안광을 뿜어내며 물었다.

“무엇을 말이냐?”

“첫인사요.”

“뭐라?”

“남만에 오기 전, 어느 분한테 그런 말씀을 들었습니다. 야수묘왕은 겉보기에는 무식하고 앞뒤 안 가릴 것처럼 보이지만, 알고 보면 정 많고 장난 좋아하는 놈이다. 그러니 적당히 받아 주고 사이좋게 지내라.”

“……!”

“……!”

입을 딱 벌린 화룡각 대원들의 반응은 애교다.

소궁주인 야율목과 호위들은 경악에 찬 눈빛으로 나를 바라보다가 이내 번개 같은 속도로 병장기에 손을 가져갔다.

하지만 그들이 미처 행동에 나서기도 전, 내 말에 입꼬리를 씰룩이던 야수묘왕이 폭소를 터트리며 말했다.

“크하하하! 적 노(老)께서는 여전하시군.”

나는 얼얼한 팔뚝을 주무르며 대답했다.

“뭐, 워낙에 정정하시죠.”

“제자를 들였다는 소문은 들었지만 이렇게 일찍 만날 줄이야.”

새삼스러운 눈빛으로 나를 바라보던 야수묘왕이 씩 웃으며 말을 이었다.

“반갑구나. 노부는 야율척이라 한다.”

다른 사람이라면 모를까, 상대는 남만야수궁의 주인이기 이전에 적천강의 지인이다.

나는 야수묘왕 야율척을 향해 공손히 포권을 취해 보였다.

“열화문(烈火門)의 십구 대 계승자, 진태경이 야수묘왕 야율척 대협을 뵙습니다.”

“오냐. 으하하하!”

거칠면서도 시원한 웃음을 터트린 야수묘왕이 호의가 듬뿍 담긴 목소리로 말을 이었다.

“나누어야 할 이야기가 많을 터. 따라오너라.”

호쾌한 걸음으로 멀어지는 그의 뒷모습을 얼떨떨하게 바라보던 사람들의 시선에 나를 향한다.

어떻게 된 거냐고 묻는 듯한 그들의 눈빛에 나는 어깨를 으쓱하며 대답했다.

“우리 스승님이랑 좀 친해.”

역시 인생은 학연, 지연, 혈연이다.



* * *



야수묘왕은 즐거워 보였다. 아니, 즐거운 게 확실했다.

평소에도 제법 유쾌한 성격의 소유자라는 건 이미 적천강에게 들어 알고 있었지만, 남만야수궁 내부의 대전(大殿)에 앉아 옛이야기를 꺼내는 그의 모습은 마치 덩치 큰 어린아이 같았다.

“적 노를 처음 뵈었던 날이 생각나는군. 나를 보더니 대뜸 화염신장을 날리셨다.”

“……노야. 아니 스승님 말씀으로는 날리진 않고, 날릴 뻔했다고 하셨는데요.”

“아니다. 확실히 맞았어. 숨이 턱 막히고 똥줄이 바싹 타들어 가는 느낌이었지.”

지금까지 만났던 명문 대파의 문주나 가주라면 어느 정도의 체통을 지키기 마련이었는데, 애초에 호피로 만든 바지 하나만 덜렁 걸치고 다니는 야수묘왕은 체통이고 나발이고 신경 안 썼다.

물증으로 옆구리에 찍힌 화염신장의 흔적을 보여 준 그가 대수롭지 않다는 듯이 덧붙였다.

“아주 강렬한 첫 만남이었지. 두 번 정도 피똥을 싸고 다시 찾아갔더니 상처를 소독하라며 술 한잔을 따라 주셨다. 아주 호쾌하신 분이셨어.”

“……아, 예.”

내가 아는 호쾌함의 뜻이 맞나, 하는 의문이 들었지만 맞은 사람이 괜찮다니 뭐라 할 말이 없다.

굳이 말해 봤자 상대가 적천강이니 누워서 침 뱉기고.

“정마대전이 끝난 이후에는 뵙지 못해 아쉬웠는데, 이렇게 적 노의 제자를 만나니 반갑기 그지없군. 술은 좋아하나?”

“술이야 당연히 좋아하긴 하는데, 지금 당장은 어려울 것 같습니다.”

“왜?”

“술보다 급한 일이 있으니까요.”

세상이 평화로웠다면 나도 기꺼이 한바탕 술판을 벌였을 거다.

야수묘왕이랑 건배도 하고, 야율척이 좋아하는 랜덤 게임을 외치면서 각종 술 게임으로 이민족들을 뿅 가게 만들었겠지.

하지만 지금 같은 시기에는 불가능하다.

“이번에는 스승님의 제자가 아니라, 무림맹의 각주로 온 겁니다.”

내 나직한 목소리에, 야수묘왕의 입가에 맺혀 있던 미소가 살짝 흐려졌다.

“암천 때문인가?”

“역시 알고 계셨군요.”

“그렇지 않아도 그에 관한 전서응을 받았다. 중원으로부터 수만 리나 떨어져 있다 보니 전달이 늦었지. 하지만 중원의 사정을 아주 모르는 것은 아니야.”

“실례지만 전서응을 받으셨던 때가…….”

“글쎄. 벌써 한 달은 넘은 듯싶군.”

하남과 남만 사이의 거리. 그리고 시기를 생각해 본다면 숭산결의(崇山決意)라 이름 붙여진 무림맹 결성 이전에 보낸 서신이 틀림없다.

숭산결의에는 가급적이면 많은 문파가 참석해야 했고, 은영각주 천면호리는 그 정도도 계산하지 않고 서신을 보낼 만한 사람은 아니었다.

그리고 그 말은 즉…….

“입맹(入盟)을 거절한 거군요. 남만야수궁은.”

답신을 보낼 시간도, 이민족 중 일부를 이끌고 숭산에 올 시간도 있었다.

하지만 남만야수궁이 무림맹에 어떠한 답도 돌려주지 않았다는 것은, 완곡한 거절의 표현이라고밖에 받아들여지지 않는다.

내 말에 잠시 침묵을 지키던 야수묘왕이 불쑥 입을 열었다.

“완전한 거절은 아니다. 다만 결론을 내지 못했을 뿐이야.”

“결론이라면 궁주님께서…….”

이어지려던 내 목소리는 야수묘왕의 손짓에 가로막혔다.

마치 맹수의 갈기 같은 자신의 수염을 쓰다듬은 그가 재차 입을 열었다.

“적 노의 제자. 아니, 진태경이라고 했지.”

“예.”

“네가 데려온 이들에게 한 가지 묻지. 그대들은 내가 누구인지 알고 있느냐?”

머뭇거리는 분위기도 잠시. 가장 먼저 야수묘왕과 시선이 마주친 혁무진이 마른침을 꿀꺽 삼키며 대답했다.

“야수묘왕 야율척 대협이십니다. 십왕(十王)에 속한 초절정 고수시기도 하고요.”

“맞다. 그 옆에 있는 여인. 그래, 자네는?”

주화란이 막힘없이 대답했다.

“모두가 알고 있듯이, 남만야수궁의 궁주십니다.”

“그 역시 맞다. 하지만 내가 원하는 대답은 아니지. 그럼 이번에는 바로 옆에 있는 자네가 말해 보게.”

미처 막을 새도 없이, 퉁방울만 한 눈동자를 껌뻑거린 태산이 대답했다.

“태산이. 배고프다.”

태산이 너란 새끼. 자동 응답기 같은 새끼. 이 시벌 새끼…….

예상했던 것을 아득하게 벗어나는 대답에 야수묘왕이 떨떠름한 표정을 지었다.

“저놈은 누구냐?”

잠깐 생각하던 내가 솔직하게 대답했다.

“이제는 저도 잘 모르겠는데요.”

“희한한 놈이 하나 있군. 그럼 그 옆의 노인장이 대답해 보시게.”

작은 목소리로 태산을 향해 속사포 같은 쌍욕을 퍼붓던 남호가 입을 열었다.

“묘족을 이끄는 대족장이시오.”

“그래, 옳다.”

고개를 끄덕인 야수묘왕이 말을 이었다.

“나는 수많은 묘족을 대표하는 대족장이다. 그들을 한 깃발 아래 모으고, 다른 부족장들의 지지를 얻어 남만야수궁의 궁주가 되었지. 목아, 우리 땅에 존재하는 부족들의 수가 몇이나 되는지 아느냐?”

조용히 시립해 있던 야율목이 대답했다.

“남만 전체를 아우른다면 서른두 개의 부족이 존재하고, 묘족을 비롯한 네 개의 거대 부족이 있습니다.”

“그래, 그것이 남만야수궁이다.”

나는 야수묘왕이 무슨 말을 하려는지 알아차렸다. 아니, 나뿐만이 아니라 이 자리의 모두가 마찬가지였다.

물론 태산은 빼고.

“그 말씀은…….”

“나는 궁주이기 이전에 묘족의 대족장이고, 남만야수궁의 궁주는 왕이 아니다.”

모든 것을 야수묘왕 혼자서 결정할 수는 없다는 뜻이다.

분명 남만야수궁은 중원과 동떨어진 별개의 왕국과도 같은 곳이었지만, 그 왕국을 이루는 것은 크고 작은 부족체의 연합이었다.

그럼 굳이 이 이야기를 솔직하게 털어놓는 이유는 뭘까.

‘다른 부족이 반대하고 있지만, 야수묘왕 본인은 입맹에 동의할 생각이 있다는 건가?’

내가 문득 떠오른 의문을 입 밖으로 꺼내려던 그때, 굳게 닫힌 대전의 문 너머로 나직한 목소리가 들려왔다.

“궁주, 잠시 이야기를 나눌 수 있겠습니까?”
```

## Final English reading copy

```markdown
# Chapter 625

People possess something called an aura.

Some people’s auras are so faint and hazy that they can barely be felt, while others possess auras so powerful and rough as waves that they overwhelm anyone who stands before them.

The Beast Miao King, Yayul Cheok, was the latter.

*Whoosh.*

Yayul Cheok slowly rose to his feet, looking as though a massive mountain had begun to move.

Despite being well over eighty years old, the muscles covering his entire body were as solid as armor. His steps were firm and unhesitating, and his half-gray beard streamed like a lion’s mane.

*Thud. Thud.*

Everyone could now see him as he approached, trampling down the vine-covered stairs with his bare feet.

Yayul Mok and his guards immediately dismounted and dropped to one knee. It was their own form of etiquette for showing respect to the lord of the Nanman Beast Palace.

“Greetings, Palace Lord.”

The Beast Miao King stared intently at Yayul Mok.

“You ran off again without saying a word.”

“There was a fire in the northeastern pasture. I happened to be nearby…”

“Did you put it out?”

“Yes.”

“And the culprit?”

The question was clearly directed at Yayul Mok, but the Beast Miao King’s gaze was fixed on me.

I stared straight into his tiger-like eyes, which radiated a fierce light, and stepped forward.

“‘Culprit’ would be putting it a bit strongly. There was a little mistake.”

“It’s been a long time since I’ve seen Han Chinese. Are you the culprit who started the fire?”

Before I could answer, his voice continued with a growl.

“Think carefully before you answer. Nanman’s laws are far from merciful.”

After thinking for a moment, I asked,

“How are people punished in a case like this?”

“It depends on the severity of the damage, but in serious cases, they become food for wild beasts. Or they are thrown into a pit filled with venomous beasts.”

“What about minor cases?”

“They are hanged from a vine.”

“That’s considered minor?”

“Of course. At least the body can be kept intact.”

“Ah.”

I nodded, then casually stepped to the side and introduced someone.

“Ta-da. Actually, this is the culprit.”

An ordinary person might have panicked, but a Hidden Shadow Pavilion agent with fifty years of experience was clearly different. Namho calmly opened his mouth.

“Are you fucking insane?”

“No, I’m not exactly wrong.”

“You fucking bastard…”

Namho was just about to unleash a proper stream of abuse when the Beast Miao King abruptly spoke in a rough voice.

“So you intend to abandon your companion and save your own life.”

“Hmm. There seems to be a misunderstanding. I never said I was abandoning him.”

“A misunderstanding?”

“I’m just pointing out the facts. No, not facts. The truth. We haven’t known each other for very long, but he’s still a good person. And there’s the Murim Alliance’s reputation to consider.”

I had deliberately brought up the Murim Alliance, so the Beast Miao King might have let the matter drop at that point. But the fierce light in his eyes, once kindled, did not fade in the slightest.

“Now that you have entered Nanman, you must follow Nanman’s laws. If one of you must take responsibility, then what?”

“If you insist…”

I scratched the back of my head and continued.

“Wouldn’t we have to stop that somehow?”

And then, in that very moment—

*Whoom!*

The air around us vanished.

Before the short, heavy sound of air splitting could even be heard, a single punch shot toward me. It carried enough force to resemble a battering ram, and I crossed both arms in front of myself.

*Boom!*

A deafening roar rang out as though the sky itself had split open, and the shock wave from the collision swept in every direction.

The tremendous force drove me back a full ten feet. I let out a sigh.

“Is that enough?”

The Beast Miao King asked, his eyes emitting a glacial light.

“What are you talking about?”

“Our first greeting.”

“What?”

“Before coming to Nanman, someone told me something. The Beast Miao King may look ignorant and reckless, but he’s actually warmhearted and loves playing pranks. So take him in stride and get along with him.”

“……!”

“……!”

The Fire Dragon Pavilion members’ reaction—standing there with their mouths hanging open—was nothing compared to what came next.

Yayul Mok, the Young Palace Lord, and his guards stared at me in shock before reaching for their weapons at lightning speed.

But before they could act, the Beast Miao King, whose lips had been twitching at my words, burst into laughter.

“Ha ha ha ha! Old Master Jeok hasn’t changed a bit.”

I rubbed my stinging forearms and answered,

“Well, he’s still remarkably healthy.”

“I heard he had taken a disciple, but I never expected to meet you so soon.”

The Beast Miao King looked at me with renewed interest and continued with a broad grin.

“Good to meet you. This old man is called Yayul Cheok.”

It might have been different with someone else, but before he was the lord of the Nanman Beast Palace, the man before me was an acquaintance of Jeok Cheongang.

I respectfully clasped my hands toward Yayul Cheok, the Beast Miao King.

“Jin Taekyung, nineteenth successor of the Fire Gate Clan, pays his respects to Great Hero Yayul Cheok, the Beast Miao King.”

“Good. Ha ha ha ha!”

The Beast Miao King let out a rough but refreshing laugh and continued in a voice full of goodwill.

“We have much to discuss. Follow me.”

Everyone watched his retreating back with bewildered expressions before turning their eyes toward me.

Their looks seemed to ask what had just happened, so I shrugged and answered,

“He’s kind of close with my master.”

As expected, life was all about school ties, regional ties, and blood ties.

* * *

The Beast Miao King looked happy.

No, he was definitely happy.

I already knew from Jeok Cheongang that he was normally a fairly cheerful person. But as he sat in the main hall inside the Nanman Beast Palace and brought up old stories, he looked like a huge child.

“I remember the day I first met Old Master Jeok. The moment he saw me, he immediately sent a Flame Divine Palm flying.”

“……According to the Old Master—no, according to my master—he didn’t actually let it fly. He said he only almost did.”

“No. It definitely hit me. It knocked the breath out of me and scared the shit out of me.”

The Sect Leaders and Family Heads of the prestigious factions I had met so far generally maintained a certain degree of dignity.

But the Beast Miao King, who walked around wearing nothing but a pair of tiger-skin pants, did not care about dignity or anything else.

As proof, he showed me the mark of the Flame Divine Palm stamped into his side and added casually,

“It was quite a first meeting. I shit blood twice, then went back to see him, and he poured me a drink, telling me to disinfect the wound. What a bighearted man.”

“……Ah. Yes.”

I wondered whether he and I understood the meaning of “forthright” in the same way, but the person who had been hit said he was fine, so what could I say?

Besides, the person in question was Jeok Cheongang. Criticizing him would only be like spitting in my own face.

“I was disappointed that I couldn’t see Old Master Jeok after the Great Faction War ended, but meeting his Disciple like this is truly a pleasure. Do you like alcohol?”

“I do, of course, but I don’t think I can drink right now.”

“Why not?”

“There’s something more urgent than drinking.”

If the world had been at peace, I would gladly have held a drinking party with him.

I would have toasted the Beast Miao King, shouted, “Yayul Cheok’s favorite—random games!” and gotten all the people of other ethnicities completely wasted on drinking games.

But at a time like this, that was impossible.

“This time, I didn’t come as my master’s Disciple. I came as the Pavilion Master of the Murim Alliance.”

At my quiet words, the smile around the Beast Miao King’s lips faded slightly.

“Is it because of Dark Heaven?”

“So you already know.”

“I received a messenger eagle concerning it. Since we’re tens of thousands of li from the Central Plains, the message arrived late. But it’s not as though I know nothing about the situation in the Central Plains.”

“If you don’t mind me asking, when did you receive it?”

“Let me think. It seems to have been over a month ago.”

Considering the distance between Henan and Nanman, as well as the timing, the letter must have been sent before the formation of the Murim Alliance, an event called the Mount Song Resolution.

As many sects as possible had needed to attend the Mount Song Resolution, and Chief of the Hidden Shadow Pavilion Thousand-Faced Fox was not the kind of person who would send a letter without taking even that into account.

And that meant…

“You refused to join the alliance. The Nanman Beast Palace did.”

There had been enough time to send a reply and to lead some of the people of other ethnicities to Mount Song.

But the fact that the Nanman Beast Palace had sent no response to the Murim Alliance could only be interpreted as a polite refusal.

The Beast Miao King remained silent for a moment before abruptly opening his mouth.

“It was not an outright refusal. We simply haven’t reached a conclusion.”

“If it’s a conclusion, then, Palace Lord…”

My words were cut off by a gesture from the Beast Miao King.

He stroked his beard, which resembled a wild beast’s mane, and spoke again.

“Disciple of Old Master Jeok. No, you said your name was Jin Taekyung.”

“Yes.”

“I have a question for those you brought with you. Do you know who I am?”

The hesitant atmosphere lasted only a moment.

Hyuk Mujin was the first to meet the Beast Miao King’s gaze. He swallowed dryly before answering.

“You are Great Hero Yayul Cheok, the Beast Miao King. You are also a Supreme Peak master among the Ten Kings.”

“That is correct. The woman beside him. Yes, you.”

Ju Hwaran answered without hesitation.

“As everyone knows, you are the Palace Lord of the Nanman Beast Palace.”

“That is also correct. But it is not the answer I want. This time, you beside her—tell me.”

Before anyone could stop him, Taishan blinked his enormous eyes and answered.

“Taishan. Hungry.”

*You bastard, Taishan. You answering-machine bastard. You fucking bastard…*

The answer went so far beyond what I had expected that the Beast Miao King wore a distinctly awkward expression.

“Who is that fellow?”

After thinking for a moment, I answered honestly.

“I’m not really sure anymore, either.”

“What a strange fellow. Then let the old man beside him answer.”

Namho, who had been firing a rapid stream of profanity at Taishan in a low voice, opened his mouth.

“You are the great chieftain who leads the Miao people.”

“That is correct.”

The Beast Miao King nodded and continued.

“I am the great chieftain who represents countless Miao people. I gathered them under one banner and became the Palace Lord of the Nanman Beast Palace with the support of the other tribal chiefs. Mok, do you know how many tribes exist in our land?”

Yayul Mok, who had been standing silently at attention, answered.

“If we include all of Nanman, there are thirty-two tribes, including four great tribes such as the Miao people.”

“Yes. That is the Nanman Beast Palace.”

I realized what the Beast Miao King was trying to say.

No, I was not the only one. Everyone here had realized it as well.

Except Taishan, of course.

“Does that mean…”

“Before I am the Palace Lord, I am the great chieftain of the Miao people. And the lord of the Nanman Beast Palace is not a king.”

He meant that the Beast Miao King could not make every decision by himself.

The Nanman Beast Palace was certainly like a separate kingdom, cut off from the Central Plains. But that kingdom was made up of an alliance of large and small tribes.

Then why was he being so honest about all this?

*Are the other tribes opposed, while the Beast Miao King himself is considering agreeing to join the alliance?*

Just as I was about to voice the question that had suddenly occurred to me, a quiet voice came from beyond the firmly closed doors of the main hall.

“Palace Lord, may I speak with you for a moment?”
```
