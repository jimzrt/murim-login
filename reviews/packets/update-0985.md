<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0985.txt",
      "sha256": "5ae6264ec324a4182740bdb9834b821c0c617b3c1c9f93d65023ab8d14d46f36",
      "bytes": 13322
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1cea1c608503a8f9505b12c7b91cba3eb3e14b6ae285fa78464ffeb6af43f585",
      "bytes": 929
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d19a3f8bfc0e01b73efa4b9c3bc11e0cbb5feb4281651779354f72e23d424163",
      "bytes": 236240
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5428a81ba8941a508a1849aa06ea3549b09fd9fb62edea90c5a8802182534710",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "5144eae204865028f2e80b53d398f91dc934880c96acba4c7318f8f3a45d4e78",
      "bytes": 838
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "561589ec3e1bca1a7ed5633194040237749f7e6d1219eba3b3472d397dcfcbe1",
      "bytes": 1000
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ee5fff477a4237839cafecbd3a14db21c3acd88a6999564702803ac21c81cb30",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a3351dff31a0ad628a14128507db44df6455db82a67df5c9e96bf83ccdf74ca7",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "03e6dba4cefac2a11b71de2b2ddb62de27881a6d168991d7606927fa30655124",
      "bytes": 1665
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "1b8ba3bc0c2c6c7e17ca8bbf1bf56906df1550bdbdc890092373d27bb4eeadf3",
      "bytes": 1178
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "8782fa5248eb8ed432c34c5cf56e603c0cbfdbbe461f091891040a35dd26b221",
      "bytes": 1015
    },
    {
      "path": "characters/Murong Baek.md",
      "sha256": "a03f8977a2759c6073b30abd112f1793c0e5315bdbf758a788862c9689d0a81b",
      "bytes": 660
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "3b911d3047e134ba23e7bb46e75d3c4fb7b4bf10baaba8f4578eac3d07635730",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "6798158dfd357e9b0600ec650a6aa7e610d96aee4ccdb9708973332753cac38e",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0383ccfd72d4fbc4b38d48993234603f14d1f5c66c449dca8bf366ced2819cb9",
      "bytes": 272663
    }
  ],
  "estimated_tokens": 13597
}
-->

# Durable State Update — Chapter 985

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
1 and safe_through 985. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 985. Profile updates may replace only one
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
  "chapter": 985,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 985,
    "continuity_sources": [985],
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
    "The imperial proclamation declares Dark Heaven traitors and calls on martial artists to join the government in punishing them; the war has begun.",
    "At Eight Spring Gorge, tens of thousands honor the fallen with chrysanthemums and cornelian berries on the Double Ninth Festival.",
    "Lee Seowol is mourning the death of her uncle, Cheol Mubaek.",
    "About a hundred Murong Family survivors, including Murong Su, are to be interrogated; if proven innocent, they may rebuild as the Murong household under a new Family Head."
  ],
  "continuity_sources": [
    984
  ],
  "open_questions": [
    "Will the Murong survivors’ innocence be established, allowing the household to rebuild under Murong Su or another Family Head?",
    "What is the source or significance of the chime that sounds at the chapter’s end?"
  ],
  "safe_through": 984,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천하오대세가 | **Five Great Families** | Expanded source form of 오대세가. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 북천마군 | **North Heaven Demon Lord** | Title of Murong Baek. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 진위경 | 남천마후 | family_head_to_hostile_demon_empress | you | formal and defiant | Swears that she cannot touch Taekyung. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |
| 북천마군 | 적천강 | former battlefield adversaries | Fire King | calm and familiar | Addresses Jeok Cheongang as 화왕 while asking him not to rush. |
| 궁성 | 모용백 | opponents | Murong Baek; North Heaven Demon Lord | calm, formal, and admonitory | The Bow Saint directly addresses Murong while telling him to accept the consequences of his choices. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 984
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 980
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 911
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 982
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 982
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 982
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry and responsibility; losses deepen his self-reproach and resolve to grow strong enough to protect others.
- **Voice:** Quiet and resonant, clipped and blunt, with dry sarcasm in familiar exchanges.
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, who shares his own grief and encourages him to keep trying; Cheol Mubaek died protecting Mukyung and left him the Shura Annihilating Fist manual; their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 984
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 984
- **Aliases:** None
- **Role:** Lee Seowol is the eighteen-year-old Sect Leader of the reconstructed and rapidly growing Mount Heng Sword Sect, a vassal of the Jin Family of Taiyuan who still awaits Taekyung’s answer to her marriage proposal.
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek and niece of the deceased Cheol Mubaek, who entrusted her with the Shura Annihilating Fist manual; younger sister of the deceased Lee Seogeun and Lee Seogwang; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; asked Taekyung to address her as Young Lady rather than Sect Leader.

### Murong Baek.md

# Murong Baek (모용백)

- **Safe through:** Chapter 984
- **Aliases:** North Heaven Demon Lord, Divine Spear of the Imugi
- **Role:** Murong Baek was the North Heaven Demon Lord, known as the Divine Spear of the Imugi; Jin Taekyung killed him after he burned his life to gain power.
- **Personality:** He coveted the dragon pearl and the chance to become a dragon, rationalizing his pursuit while choosing to seize what belonged to others.
- **Voice:** Not established
- **Relationships:** Jeok Cheongang and the Bow Saint fought him alongside Jin Taekyung, who delivered the killing blow.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 977
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 977
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃985화



수많은 이들의 눈물과 하염없이 흩날리는 꽃비를 뒤로한 채, 무림인과 양민이 뒤섞인 수만여 명의 사람들은 팔천협을 떠나 각자의 자리로 돌아갔다.

떠난 이들을 위한 위령제이자 뒤늦은 중양절은 그렇게 끝났지만, 남은 이들은 계속해서 내일을. 모레를 향해 나아가야 했으니까.

그리고 태원진가로 귀환한 우리를 기다리고 있던 것은, 만일을 대비하여 남겨 둔 일부 가솔들뿐만이 아니었다.

“부족하지만 무림맹의 당주직을 맡고 있는 황 모라고 합니다. 맹주(盟主)님의 명을 전언을 전하고자 왔습니다.”

정중하기 이를 데 없는 태도로 자신의 신분을 밝힌 무림맹의 사자(使者)가 그렇게 덧붙이자, 사람들의 시선이 우리 삼 형제를 향해 쏠렸다.

보다 정확히는, 진위경을 향해 집중되었다.

“그렇습니까.”

아직 벌겋게 물든 눈가와는 달리 담담한 목소리.

마치 오랫동안 기다려왔던 손님을 맞이하는 것처럼, 진위경은 침착한 태도로 무림맹의 사자를 이끌었다.

“이야기를 나누기에 앞서, 우선은 안으로 드셔서 여독을 푸시지요.”

“진 대협께서 이리 신경 써 주시니 감읍할 따름입니다.”

그 순간, 태원진가에 속한 중진들과 산하 문주들의 낯빛 위로 숨길 수 없는 감회가 스쳤다.

그리고 그 이유는, 단지 깊게 고개를 숙이는 사자의 모습에서 진심으로 우러나오는 공경과 존경 때문만이 아니었다.

대협(大俠).

단 두 글자지만, 그것이 가진 의미는 남달랐다.

툭 하면 서로를 치켜세우며 허세 떨기 바쁜 어중이떠중이가 아닌, 무림맹에서도 당주라는 요직을 맡은 강호의 명숙(名宿)이 사자의 자격으로 찾아와 저리 불렀다는 점에서 더더욱.

‘변해 가는구나. 모든 것이.’

나 역시 새삼 감회가 새로웠다.

더 이상 진위경은 어디 있는지도 모르는 아비를 대신해서 몰락해 가는 가문을 이끌던 소가주도, 소협도 아니다.

산서성의 패자이자, 이 땅의 모든 이에게 인정받은 또 한 사람의 맹주였다.

아니, 이제는…….

“무슨 생각을 그렇게 하세요?”

불쑥 귓가에 닿은 혁무진의 물음에, 나는 고개를 저었다.

“별거 아냐.”

“아닌 게 아닌 것 같은데.”

“무진아.”

“예.”

“살아도 산 것 같지 않게 만들어 줘?”

“……아니, 저는 그냥 얼른 뒤따라 가시라고 말씀드리려고 한 겁니다. 혼자서 가만히 서 있으시길래.”

혁무진이 한 말은 사실이었다.

당당하게 걸음을 내딛는 진위경의 뒤로, 무림맹의 사자와 가문의 중진들. 그리고 이소월과 같은 태원진가 산하의 문주들이 나란히 뒤를 따르고 있었다.

아직 지워지지 않은 슬픔과, 곧 현실로 이루어질 무언가에 대한 기쁨이 뒤섞인 얼굴로.

하지만 나는 그런 그들의 뒷모습을 말없이 바라보다, 이내 다른 방향으로 발걸음을 돌렸다.

“어라, 어디 가세요?”

“몰라. 그냥 가고 싶은 곳으로.”

“그게 무슨. 다른 분들은 몰라도 조장님이 저 자리에 빠지시면 안 될 것 같은데.”

“상관없어. 어차피 대충은 알고 있으니까.”

“예?”

어리둥절한 얼굴로 고개를 갸웃거리는 것도 잠시, 이내 헐레벌떡 내 뒤를 쫓아오는 혁무진의 인기척을 느끼며 나는 피식 웃었다.

동시에 문득 떠올렸다.

팔천협.

수많은 목숨을 집어삼킨 그 비좁은 협곡에서, 흩날리는 꽃비 사이로 울려 퍼졌던 맑은 종소리를.

또 다른 변화가 일어났음을 알리던 홀로그램 창을.

띠링. 띠리링.



- 세상이 열린 이래, 하늘 아래 영원한 것은 없습니다. 광활한 대지와 바다, 그 안에서 살아가는 무수한 생명체들과 그들 중 극소수만이 지닌 강대한 권력 역시 마찬가지입니다.

- 열흘 붉은 꽃은 없고(花無十日紅), 제아무리 높은 권세도 십 년을 넘기지 못하니(權不十年).

- 다만 나무의 뿌리가 깊으면 가지 또한 무성하고(根深枝茂), 샘이 깊은 물은 더 멀리 흘러가(源遠流長), 마침내 많은 이가 머물러 쉴 수 있는 또 하나의 세상이 될 것입니다.



시스템이 알려 주었듯이, 오래된 고목 나무처럼 썩어 가던 태원진가는 이제 하나의 숲이 되었다.

수많은 가지 끝에서 열매를 틔우고, 바다와 같은 호수를 만들었다.

지금껏 내가 보고 겪은 그들은 힘이 없을지언정 언제나 정당했으며, 인의로웠다.

분노와 탐욕에 사로잡혀 잘못된 길을 택한 누군가와는 달리.



- [모용세가]는 몰락했습니다. 그들은 더 이상 [천하오대세가]의 일원이 아닙니다.

- 바야흐로, [태원진가(太原進家)]의 명성이 온 천하에 울려 퍼집니다!

- [태원진가]의 명성과 권세가 [천하오대세가]의 일원으로 격상됩니다!



구파일방. 천하 오대세가.

지난 수백여 년간 천하 무림을 지탱해 왔던 열다섯 개의 기둥.

그리고 이제, 태원진가는 그 거대한 기둥이 되었다.

그것은 단순히 무림맹이 임명했기 때문도, 다른 강호의 명숙들이 강력하게 원했기 때문도 아니었다.

온 천하가 그렇게 받아들였다. 그들이 인정했다.

수만의 대군에 맞서 싸운 태원진가의 용기를.

무림이라는 울타리뿐만 아니라 이 땅을, 백성들을 지키고자 했던 의기(義氣)를.

하여, 한때의 영광을 뒤로한 채 서서히 몰락해 가던 변방의 무가(武家)는 그 어느 때보다 하나가 되어 강해질 수 있었다.



- 칭호, [명가의 자제]가 삭제됩니다!

- 새로운 칭호, [명문세가의 직계]를 획득하셨습니다!

- 소속된 가문의 입지가 상승함에 따라, 막대한 명성치를 획득합니다!

- 히든 퀘스트, [켠 김에 오대세가까지]를 성공적으로 완료하셨습니다!

- 매우 희귀한 업적, [아빠, 어디 갔어]를 달성했습니다. 각자의 노력으로 숱한 고난과 역경을 딛고 일어난 태원진가의 삼 형제에게 영광과 축복이 있기를!

- [진위경]과 [진무경]에게 [놀라운 자연 치유]의 효능과 각종 보너스 버프를 부여합니다. 당연한 말이지만, 위의 효력은 해당 인물들에게 표시되지 않습니다.

- 업적 달성 보상으로 보너스 스탯 10을 획득했습니다!

- 막대한 경험치를 획득했습니다!

- 레벨 업!

- 막대한 명성치를 획득했습니다!

- 이제 당신의 이름과 명성은 무림을 넘어 천하 곳곳에 닿았습니다. 당신은 [천자]가 임명한 [제후]이며, [화왕 적천강]의 후인이자, 한 사람의 위대한 무인입니다.

- 당신의 족적(足跡)이 역사에 새겨집니다.

- 무림인들은 조심스럽게 이야기하기 시작합니다. 드넓은 하늘과 세 개의 별 아래, 단 열 명의 무인에게만 허락되었던 그 영광스러운 칭호를. 새로운 젊은 왕의 탄생을.

- 아직 정해진 것은 아무것도 없습니다. 나비의 작은 날갯짓이 저 멀리에서 태풍을 불러오듯이, 당신의 크고 작은 선택 하나하나가 이 세상을 조금씩 바꾸어 나갈 테니까요.

- 그러나 명심하십시오. 시간은 계속해서 흐르고 있다는 것을.

- 무운(武運)을 빕니다.



평소보다도 훨씬 길었던.

그래서 더욱 많은 변화를 느낄 수 있었던 시스템 창은 언제나 그렇듯 무운을 빈다는 인사를 마지막으로 끝났다.

아주 오랜만에, 별다른 후속 퀘스트도 없이.

하지만 바로 그 부분이, 마침내 찾아온 평화 속에서도 마음 한구석을 찜찜하게 만드는 유일한 이유이기도 했다.

‘뭐지? 분명히 또 다른 일이 터질 거라고 생각했는데.’

단순히 강해지는 게 좋았던 단계는 이미 오래전에 지났다.

꼬리에 꼬리를 물고 이어지는 퀘스트 속에서 누군가의 죽음은 필연적이라고 표현할 만큼 반드시 있어 왔고, 그만큼 내가 짊어진 마음의 짐도 무거워졌으니.

게다가 지금은, 그 어느 때보다 큰 위기가 무림 전체에 드리워진 시점이었다.

‘이번 계획이 실패로 돌아갔다고 해서, 주춤하고 있을 놈들이 아닐 텐데.’

항상 그랬다.

암천은 지금까지 무림 전역에서 여러 번의 흉계를 벌였고, 법왕(法王) 굉도를 시해하며 소림사의 신물인 녹옥불장을 탈취한 이후로는 딱히 성공이라 부를 만한 행보를 보이지 못했다.

그럼에도 불구하고 사천에서. 호북에서.

그리고 남만과 황궁에 이어 이곳 산서성에서조차 놈들은 쉼 없이 피바람을 불러일으켰다.

‘모용세가의 배신과 유목민들의 침공은 분명히 엄청난 일이었지. 하지만 이런 과정에서 드러난 암천의 전력은, 아직 예상치에 훨씬 못 미쳐.’

암천 내에서도 핵심 인물임이 틀림없을 네 명의 마군과 마후를 제외한다면, 지금껏 맞서 싸운 적들은 절반 이상이 배신자들과 하수인에 불과하다.

쉽게 말해, 현지에서 전력을 조달한 것과 같았다는 소리다.

‘그런데도 나서지 않고 있다. 왜지? 그리고 왜 이런 실패뿐인 소모전을 계속해서 이어 가는 거지?’

무의식적으로 나아가던 발걸음도 멈춰 세운 채. 나는 미간을 찌푸렸다.

동시에 문득 떠올렸다.

모용세가의 가주 모용백. 북천마군(北天魔君)이라는 이름으로 최후를 맞이했던 그와 나누었던 대화의 일부를.



‘너희가 그렇게 믿는다면, 그래. 계속해서 희망을 품는 것도 나쁘지는 않겠지.’

‘뭐?’

‘이런 상황에 처하고 나니 문득 그런 생각이 드는군. 서천마군이, 남천마후가, 그리고 동천마군이 왜 실패했을까. 분명 오랫동안 치밀하게 준비했던 계획이 어찌하여 한순간에 수포로 돌아간 것일까.’



그 알 수 없는 말에 담긴 의미를, 우리는 끝끝내 확인할 수 없었다.

북천마군은 결국 그 말의 의미를 말해 주지 않은 채 죽었으니까.

그러나 나는 놈의 심장에 창날을 박아 넣은 후에도, 마침내 모든 전투가 끝나고 며칠이 지난 지금까지도 그 순간의 모든 것을 똑똑히 기억하고 있었다.

담담하기 그지없었던 목소리와 표정을.

그때의 북천마군은 죽음을 각오한 상태였고, 직후 선천지기(先天之氣)마저 끌어올림으로써 그것을 증명했다.

‘단순히 평정심을 흔들기 위한 말은 아니었어.’

나는 안다.

예정된 죽음 앞에 선 이가 얼마나 진솔해질 수 있는지를.

스스로 선택한 생애의 끝자락에서, 거짓을 입에 담는 사람은 없다는 것을.

‘그렇다면 무엇 때문일까. 굳이 그런 말을 한 이유는.’

물론 당시의 북천마군이 보인 어투와 태도를 보면, 짐작 가는 부분이 없지는 않았다.

다만, 그 예측이 너무나도 현실성이 없었기에 깊게 생각하지 않았을 뿐이다.

‘마치 처음부터 이 상황이 운명처럼 정해져 있다는 듯이, 혹은 본인 역시 이용당했다는 듯한 느낌이긴 했지만…….’

아무리 생각해도, 역시 말이 안 되는 이야기다.

치열했던 전투가 끝난 이후, 이런 내 의견을 들은 적천강 역시 그 어느 때보다 단호하게 대답했었다.



‘운명은 니미럴 놈의 운명. 그리고 비록 쳐죽일 연놈들이긴 하지만, 저만한 실력을 지닌 고수들은 뭐 땅 파서 캐낸다더냐?’

‘음. 아무래도 좀 이상하긴 하죠?’

‘천주(天主). 그놈이 제아무리 날고 긴다고 해도 저런 놈들을 한낱 버리는 패로 쓸 수는 없다. 멸염신권으로 대가리 두어 번 깨진 후라면 모를까.’



맞다.

세상 그 어디에도 최상위의 초절정 고수들을 졸(卒)로 쓰는 미친놈은 존재하지 않는다.

궁성은 딱히 긍정도 부정도 하지 않은 채 오묘한 표정을 지었지만, 아마 무슨 말을 했더라도 적천강의 그것과 크게 다르지는 않았을 것이다.

‘아니. 그럼 도대체 그 말을 한 이유가, 이상할 만큼 잠잠한 이 상황이 뭐냐고.’

나는 있는 대로 인상을 찡그리며 곰곰이 생각했다.

그저 죽기 전에 한번 씨부려 본 헛소리인지. 아니면 나를 비롯한 모두가 짐작할 수 없는 또 다른 의미인지.

그리고 끝없이 이어지는 생각의 고리를 붙잡고 있던 그때, 익숙한 목소리가 불쑥 귓가를 파고들었다.

“어쩐지 한참을 기다려도 안 오더니만, 여기에 있었구먼.”

적천강.

어느 때보다 무거운 얼굴을 한 그가, 침잠하게 가라앉은 목소리로 말을 이었다.

“따라오너라. 네 녀석을 보고 싶어 하는 놈이 있으니.”
```

## Final English reading copy

```markdown
# Chapter 985

Leaving behind the tears of countless people and the ceaseless shower of falling petals, tens of thousands of people—martial artists and ordinary folk mixed together—departed Eight Spring Gorge and returned to their respective places.

The memorial for the departed, and the belated Double Ninth Festival, had come to an end. But those who remained had to keep moving forward, toward tomorrow and the day after.

And waiting for us when we returned to the Jin Family of Taiyuan were more than just the few family members who had stayed behind in case of an emergency.

“My name is Hwang. I serve, though inadequately, as a Hall Master of the Murim Alliance. I’ve come to deliver a message from the Alliance Leader.”

When the Murim Alliance’s envoy introduced himself with impeccable courtesy and added those words, everyone’s gaze turned toward the three of us brothers.

More precisely, they focused on Jin Wikyung.

“I see.”

His voice was calm, though the corners of his eyes were still red.

As if welcoming a guest he had been waiting for a long time, Jin Wikyung led the Murim Alliance’s envoy with a composed air.

“Before we talk, please come inside and rest from your journey.”

“I’m deeply grateful for the consideration you’ve shown me, Great Hero Jin.”

In that moment, an unmistakable emotion passed over the faces of the Jin Family of Taiyuan’s senior members and the Sect Leaders under its protection.

And it wasn’t only because the envoy bowed so deeply, with genuine respect and reverence.

*Great Hero.*

Just two words, but they meant something special.

This wasn’t some nobody, one of those self-important fools forever puffing each other up. A renowned master of the martial world, entrusted with the important position of Hall Master in the Murim Alliance, had come as an envoy and addressed him that way.

*Everything is changing.*

I, too, felt the weight of it all over again.

Jin Wikyung was no longer the Young Hero or Lesser Family Head who had led a fading family in place of a father whose whereabouts were unknown.

He was the ruler of Shanxi Province, and another Alliance Leader recognized by everyone in this land.

No, now he was…

“What are you thinking about so hard?”

At Hyuk Mujin’s sudden question in my ear, I shook my head.

“Nothing.”

“Doesn’t look like nothing.”

“Mujin.”

“Yes?”

“Want me to make your life a living hell?”

“…No. I was just going to tell you to hurry up and follow them. You were standing there by yourself.”

Hyuk Mujin was right.

Behind Jin Wikyung, who strode forward with confidence, came the Murim Alliance’s envoy, the family’s senior members, and the Sect Leaders under the Jin Family of Taiyuan, including Lee Seowol.

Their faces held a mixture of grief that had not yet faded and joy over something soon to become reality.

But after silently watching them from behind, I turned and headed in another direction.

“Huh? Where are you going?”

“No idea. Wherever I feel like.”

“What do you mean? Maybe someone else could miss it, but you of all people shouldn’t, Captain.”

“Doesn’t matter. I more or less know what they’re going to say anyway.”

“What?”

I heard Hyuk Mujin’s bewildered pause, then the sound of him hurrying after me. I let out a quiet laugh.

At the same time, a memory came to me.

Eight Spring Gorge.

The narrow gorge that had swallowed so many lives, and the clear chime that rang out amid the shower of falling petals.

The holographic window that had announced yet another change.

*Ding. Ding-ding.*

> **System**
>
> Since the world first began, nothing beneath the heavens has been eternal. The vast land and sea, the countless lives that dwell within them, and even the mighty power held by the rarest few are no exception.
>
> No flower stays red for ten days (*花無十日紅*), and no matter how great one’s power, it does not last ten years (*權不十年*).
>
> But when a tree’s roots run deep, its branches grow thick (*根深枝茂*). When a spring runs deep, its waters flow far (*源遠流長*). At last, it will become another world where many can dwell and find rest.

As the System had told me, the Jin Family of Taiyuan, once rotting like an ancient tree, had now become a forest.

It bore fruit at the ends of countless branches and created a lake as vast as the sea.

Though they might lack strength, everyone I had seen and known among them had always been just and righteous.

Unlike those who had chosen the wrong path, seized by anger and greed.

> **System**
>
> The Murong Family has fallen. They are no longer one of the Five Great Families.
>
> At long last, the fame of the Jin Family of Taiyuan resounds throughout the world!
>
> The fame and power of the Jin Family of Taiyuan have risen to that of a member of the Five Great Families!

The Nine Sects and One Gang. The Five Great Families.

Fifteen pillars that had upheld the martial world for hundreds of years.

And now, the Jin Family of Taiyuan had become one of those mighty pillars.

It wasn’t simply because the Murim Alliance had appointed them, or because renowned masters from across the martial world had strongly urged it.

The whole world had accepted it. They had recognized the Jin Family’s courage in standing against an army of tens of thousands.

They had recognized its sense of justice in seeking to protect not just Murim, but this land and its people.

And so, the provincial martial family that had once been slowly fading, its glory behind it, had become stronger than ever by uniting as one.

> **System**
>
> The Title Scion of a Great Family has been removed!
>
> You have acquired a new Title: Direct Descendant of a Prestigious Family!
>
> As your family’s standing has risen, you have gained a tremendous amount of Fame!
>
> Hidden Quest Might As Well Go All the Way to the Five Great Families successfully completed!
>
> You have earned the very rare Achievement Dad, Where Are You? Glory and blessings to the three Jin Family brothers, who overcame countless hardships and trials through their own efforts!
>
> Jin Wikyung and Jin Mukyung have been granted the effects of Amazing Natural Healing and various bonus buffs. It goes without saying that these effects will not be displayed to the individuals in question.
>
> You have acquired 10 bonus stat points as an Achievement reward!
>
> You have gained a tremendous amount of EXP!
>
> Level Up!
>
> You have gained a tremendous amount of Fame!
>
> Your name and reputation have now reached beyond Murim and across the world. You are a feudal lord appointed by the Son of Heaven, a successor of the Fire King Jeok Cheongang, and a great martial artist in your own right.
>
> Your footsteps have been inscribed in history.
>
> Martial artists have begun to speak cautiously of the glorious Title granted to only ten martial artists beneath the vast sky and its three stars. They speak of the birth of a new young king.
>
> Nothing has been decided yet. Just as the small flap of a butterfly’s wings can bring a typhoon from afar, each of your choices, big or small, will gradually change this world.
>
> But remember: time keeps moving.
>
> May you have good fortune in Murim.

The System window, far longer than usual and full of more changes than ever, ended as always with a wish for good fortune in Murim.

For the first time in a long while, there was no follow-up Quest.

And yet that was the only thing that left me uneasy, even in the peace that had finally arrived.

*What is this? I was sure something else was going to happen.*

It had been a long time since I’d cared about getting stronger just for the sake of it.

In the Quests that came one after another, someone’s death had been so inevitable that it might as well have been written into the bargain. And the burden I carried had grown just as heavy.

On top of that, the greatest crisis Murim had ever faced was hanging over the entire martial world.

*They’re not the type to back off just because this plan failed.*

It had always been like that.

Dark Heaven had carried out numerous schemes across Murim. Since murdering the Dharma King Hong Dao and stealing Shaolin Temple’s divine artifact, the Green Jade Buddha Staff, they hadn’t made a move anyone could call a success.

And yet, in Sichuan. In Hubei.

Then Nanman, the Imperial Palace, and now even here in Shanxi Province, they had brought one blood-soaked disaster after another.

*The Murong Family’s betrayal and the nomads’ invasion were certainly huge events. But the forces Dark Heaven has revealed in the process are still far below what I expected.*

Other than the four Demon Lords and the Demon Empress, who were certainly key figures within Dark Heaven, more than half the enemies we had fought so far had been traitors and underlings.

In other words, it was as if they had recruited their forces locally.

*And they still haven’t shown themselves. Why? And why keep up this string of costly battles that lead only to failure?*

My steps had carried me onward without my noticing, but I stopped and frowned.

Then another memory came to me: part of a conversation with Murong Baek, Family Head of the Murong Family, who had met his end as the North Heaven Demon Lord.



*“If that’s what you believe, fine. There’s nothing wrong with continuing to hope.”*

*“What?”*

*“Now that I’m in this situation, I find myself wondering why the Western Heaven Demon Lord, the Southern Heaven Demon Empress, and the Eastern Heaven Demon Lord failed. How did a plan prepared so carefully for so long fall apart in an instant?”*



We never found out what those incomprehensible words meant.

The North Heaven Demon Lord died without ever explaining them.

But even after I drove the spearhead into his heart, and even now, days after all the fighting had finally ended, I remembered every detail of that moment clearly.

His voice and expression had been utterly calm.

The North Heaven Demon Lord had been ready to die. He had proved it moments later by drawing on even his innate qi.

*He wasn’t just saying it to shake my composure.*

I know how honest a person can become when standing before an inevitable death.

When someone stands at the end of their life by their own choice, they don’t speak lies.

*Then why? Why say that at all?*

Of course, there were hints in the North Heaven Demon Lord’s words and demeanor.

I just hadn’t thought much about them, because the idea seemed so utterly unrealistic.

*It was as if he thought this situation had been fated from the beginning—or as if he, too, had been used…*

No matter how I looked at it, it made no sense.

After the fierce battle ended, I’d shared my thoughts with Jeok Cheongang. He answered more firmly than ever.



*“Fate, my ass. And as much as those bastards deserve to die, you think masters that powerful grow on trees?”*

*“Yeah. Something does seem off, doesn’t it?”*

*“Lord of Heaven. No matter how powerful that bastard is, he can’t use men like them as disposable pawns. Not unless they’ve had their heads cracked open a couple of times by my Flame-Extinguishing Divine Fist.”*



He was right.

There wasn’t a madman anywhere in the world who would use Supreme Peak masters as pawns.

The Bow Saint hadn’t agreed or disagreed. She’d only made an inscrutable face, but whatever she might have said probably wouldn’t have differed much from Jeok Cheongang’s answer.

*No. Then why say it at all? What’s with this suspiciously quiet stretch of time?*

I screwed up my face and thought it over.

Had he just been spouting nonsense before he died? Or had his words carried some other meaning none of us, myself included, could guess?

As I clung to that endless chain of thoughts, a familiar voice suddenly broke in.

“No wonder you never came, even after I waited all that time. So this is where you were.”

Jeok Cheongang.

His expression was heavier than ever. His voice was low and subdued as he continued.

“Come with me. There’s someone who wants to see you.”
```
