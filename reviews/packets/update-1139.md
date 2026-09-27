<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1139.txt",
      "sha256": "9365e52aa881b875621f17a37e19a830aa903e08281476fdde485a1335a4a27d",
      "bytes": 12192
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4f8120b32108e3504d575b11378a96124b7acaea8e2fb2c61de365b749704f9a",
      "bytes": 1545
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a77573feec836df54e35248f8b975bf7696cac58abec08a1c5a945ccb8c3d729",
      "bytes": 245575
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "38342aadc5266713e700dc97248addbcb5650a71463b171e21e94055210b11be",
      "bytes": 844
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "1469df48d57fe2dfaefad7acab2b30f56a941fdd47c075324a450a9809c09a9d",
      "bytes": 779
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "9928deda14b3eda1ea327664c7cd4f47929b9c827b7ef93ae5849cf0b7c308c1",
      "bytes": 777
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "400e80f7484d51386ca7b8430ea076b9da240a9c30c441bccf8f73978da0d623",
      "bytes": 554
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1c8fb7c890dfe2c3fc49b33a19203f85fc63d239746d51dff2d9f3f4d256a9bf",
      "bytes": 1513
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "2443c9b36d4e393a75afca5cd07cfdaf187695db9bccf5ad6b35e501c63beb5c",
      "bytes": 688
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "188468425dd33764ec71c14380cb81fadf7a561ee365524f1eb0f21dde398122",
      "bytes": 1822
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "128b07b790e2c539cd733aabb0cf3c89072bea2c4c82bc30b9fd6b067382793d",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "7e14eeb826e139730a98894f905cbb7fd92e12c2f8039f6df98e5629b6f1571d",
      "bytes": 700
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "3f7c78c4ed88be377cad50df73069bdf0389800889201305079c08622168643c",
      "bytes": 1084
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "334ad0a01705b69fc195f7f58d3e4d63b7f9711816d20e4c98503d0a57f8c085",
      "bytes": 779
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "eeac49b4362d1c9f3661803d34bd471de9210e9549634df5bfcd43b7244098f2",
      "bytes": 1043
    },
    {
      "path": "characters/Son of Heaven.md",
      "sha256": "fb02e8422dde31e66ef0ee079478a8a762b03d08d5fa45cabde7dd2303a90a7b",
      "bytes": 684
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5895951d60d69a56331fdfdc592502035283d3a48acfa6cb07fdeb7d2eb418c2",
      "bytes": 291096
    }
  ],
  "estimated_tokens": 12863
}
-->

# Durable State Update — Chapter 1139

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
1 and safe_through 1139. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1139. Profile updates may replace only one
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
  "chapter": 1139,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1139,
    "continuity_sources": [1139],
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
    "Jin Taekyung has awakened after seven days unconscious; his companions have also survived the battle, though some remain injured, and the group is grieving those who died.",
    "Before waking, Taekyung experienced a dream of a battle between fighter jets and monsters and a colossal winged being; its meaning is unknown.",
    "The search for an unnamed target remains unresolved and is to continue with reduced manpower.",
    "The Slaughter Saint still suspects the Bow Saint concealed another motive when Taekyung was in mortal danger.",
    "The coalition is beginning its westward campaign toward Xinjiang against the Lord of Heaven.",
    "The Son of Heaven has declared Great Ming and ordered a personal expedition to Xinjiang, vowing not to return to the palace until the traitors are rooted out."
  ],
  "continuity_sources": [
    1137,
    1138
  ],
  "open_questions": [
    "What was the target the searchers failed to find?",
    "What was the Bow Saint’s motive when Jin Taekyung was in mortal danger?",
    "What will happen in the campaign against the Lord of Heaven in Xinjiang?",
    "What did Taekyung’s dream of the winged being and battlefield signify?",
    "Why does the Son of Heaven’s title give the Slaughter Saint a sense of foreboding?"
  ],
  "safe_through": 1138,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”",
    "Render 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 천태민    | **Cheon Taemin**  |
| 무신     | **Martial God**               | —              |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 삼류     | **Third Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 주화입마   | **qi deviation**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 홍길동 | **Hong Gil-dong** | Legendary Korean outlaw invoked in Taekyung's joke about the Divine Physician. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 황하 | **Yellow River** | River along which civilization began. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 백환강시공 | **White Illusion Jiangshi Art** | Martial art named on the old bamboo slip. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 강시공 | **Corpse Art** | Wei Zhong’s technique for creating or controlling jiangshi. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 적천강 | 혈주 | hostile_opponents | you | blunt and threatening | Jeok Cheongang blocks the Blood Lord’s final attack on Taekyung and rebukes him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1134
- **Aliases:** None
- **Role:** Deceased young-seeming high-ranking Dark Heaven figure who claimed command of its army after killing the Grand Mage.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He served the Lord of Heaven, killed the Grand Mage, and died after Jin Taekyung defeated him; at death, he recognized that the Lord had never valued his loyalty.

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1091
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1073
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1137
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1138
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1113
- **Aliases:** None
- **Role:** Deceased Thousand Captain of the Embroidered Uniform Guard, Jeong Hogun was a disciplined martial artist who led his guards in battle.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun served under Baek Yeon in the Embroidered Uniform Guard and is remembered by Jin Taekyung as a steadfast comrade who died protecting others.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1138
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1138
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1113
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1138
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1128
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 1135
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

### Son of Heaven.md

# Son of Heaven (천자)

- **Safe through:** Chapter 1137
- **Aliases:** Emperor, Zhu Di
- **Role:** The Son of Heaven is the Emperor of Great Ming and Zhu Bao’s elder brother; he has ordered a personal expedition to Xinjiang and will not return to the palace until the traitors are rooted out.
- **Personality:** Coldly strategic and imperious, he is willing to break taboos to remain with his younger brother.
- **Voice:** Calm and commanding, with dry, understated humor.
- **Relationships:** Zhu Bao is his younger brother and heir; Jin Taekyung gave him the White Illusion Jiangshi Art; he killed Ma Sanbao.

## Korean source

```text
＃1139화



쉼 없이 이어지는 이야기를 들으며, 나는 몇 번이고 숨을 참아야 했다.

중원 무림, 아니 천하(天下)의 총집결.

이미 예정된 것이나 다름없던 일이지만, 현직 무림 맹주의 입을 통해 들으니 그 소식에 담긴 무게감은 남달랐다.

물론, 그런 육중한 무게감을 만든 것은 어마어마한 숫자 때문이기도 했다.

십만.

무려 십 만이나 되는 정예 금위군이 빛살 같은 속도로 황하(黃河)를 따라 북상하고 있다고 한다.

다른 누구도 아닌, 천자(天子)의 지휘하에.

‘그 양반, 결국 살긴 산 모양이네.’

나는 문득 마지막으로 보았던 천자의 모습을 떠올렸다.

젊은 나이가 믿어지지 않는 늙수그레한 용모와 백지장처럼 파리한 안색. 광활한 대륙의 지배자는 죽음을 앞둔 상태였고, 분명 머지않아 그리되었을 터였다.

내가 이별의 선물로 건네준, 어느 낡아빠진 서책이 아니었다면.

‘백환강시공(魄環僵尸功).’

모산파의 비전이자, 동시에 상리를 초월한 마공(魔功).

무공을 익힐수록 강시화가 진행된다는 점에서 독이 든 성배나 다름없었지만, 천자는 그것을 기꺼이 받아마신 모양이다.

성배는 성배니까.

제아무리 삼강오륜이 살아 숨 쉬는 시대라고는 해도, 정말 숨을 못 쉬게 되면 의미가 없었다.

천자가 짊어진 모든 짐을 넘겨받을, 하나뿐인 혈육을 위해서라도.

그리고 누군가를 지켜야 하는 것은, 비단 천자뿐만이 아니었다.

“장강과 황하가 빈틈없이 메워졌네. 모두가 이곳으로 오고 있어.”

매종학이 말한 ‘모두’라는 표현은 결코 과장이 아니었다.

천자가 이끄는 십만의 금위군은 총집결 중인 대군세의 일부일 뿐이다.

거대 무림 방파는 물론, 심산유곡의 은거 기인부터 삼류 칼잡이까지.

이동진(移動陳)이라는 턱밑의 칼날이 부러지자, 그들 모두가 울타리를 부수고 뛰쳐나왔다.

무수한 선박이 강줄기를 뒤덮고, 힘차게 나아가는 말발굽은 대지를 뒤흔들고 있다.

오직 하나의 목표를 위해.

용암처럼 들끓는 가슴의 열기를 가라앉히기 위해.

“자네를 비롯한 수많은 이들의 희생이, 그들을 일으켜 세운 걸세.”

겁에 질려 웅크리고만 있던 누군가는 부끄러웠을 것이고, 누군가는 미처 함께하지 못한 스스로를 자책했을 것이다.

물론 인간이란 생각하는 것만큼 정의로운 존재가 아니니, 어떤 자는 그저 입신양명을 위해 병장기를 들었을 수도 있다.

하지만 그 이유야 어떻든 상관없다.

이렇게라도 완전한 하나로 뭉칠 수 있게 되었으니.

그랬기에, 나는 눈앞의 무림 맹주가 처했던 상황 역시 충분히 이해할 수 있었다.

“미안해하지 않으셔도 됩니다.”

불쑥 던진 한마디에, 시종일관 굳은 얼굴을 하고 있던 매종학이 입술을 깨물었다.

“……자네.”

“솔직히 말씀드리면, 네. 버려졌다는 생각을 했던 때도 있었습니다.”

모름지기 대어(大漁)를 낚으려면 미끼가 필요한 법.

이번 경우에는 서녕이 바로 그 미끼였다.

그것도 암천이라는 대어가 물지 않고서는 견딜 수 없을 만큼, 아주 먹음직스러운.

그러나 무림맹은 우리를 단순한 미끼나 버림패 따위로 생각하지 않았다.

극비리에 치밀한 계획을 수립했고, 비록 한 걸음 늦었을지언정 강력한 지원군을 보냈으며, 혈주가 남겨 둔 마지막 한 줌의 우환마저 뿌리 뽑았으니까.

“그러니, 사과하지 마십시오.”

매종학의 흔들리는 눈동자를 응시하며, 나는 나직이 덧붙였다.

“떠난 이들을 위해서라도.”

“……!”

“그들이 선택한 길이었습니다. 이미 죽음을 각오했고, 그 각오에 걸맞게 싸웠습니다. 그 누구보다 용감하게.”

매종학이 사과할 필요는 없다.

아니, 그가 사과한다면 오히려 죽은 이들을 모욕하는 것이나 다름없다.

정호군을 비롯한 일천의 금의위, 수많은 무림인과 관군. 심지어는 녹슨 도끼와 낫 따위를 들고 침입자들을 막아선 양민들까지.

그들 모두가 협객이고, 영웅이었다.

눈앞의 매종학처럼, 이 위대한 승리를 위해 물밑에서 고군분투한 이들 역시도.

그러니 앞으로의 목표는 하나뿐이다.

“이 혈채(血債)는 몇 배로 쳐서 갚아야 합니다. 우리 모두가 함께.”

그리고 이 핏값을 되돌려 받을 존재가 누구인지는 이 자리의 모두가, 온 천하가 알고 있다.

천주(天主).

혹은.

‘아스모데우스(Asmodeus).’

지고의 악마, 마계의 왕.

마침내 현실로 침범한 그 존재의 이름이 쓰디쓴 맹독처럼 혀끝에 감돌았다.

그와 맞닿아 있는, 또 다른 누군가도 함께.

‘천태민.’

아니.

무신(武神).



* * *



시간은 눈 깜짝할 사이에 흘렀다.

어느 날은 한겨울처럼 굵은 눈발이 흩날리고, 또 어느 날은 세상을 모조리 집어삼킬 듯한 비바람이 휘몰아치기도 했다.

그리고 내가 의식을 되찾은 지 사흘이 지났을 때, 강렬한 햇살이 피워올린 아지랑이 너머로 지금껏 본 적 없는 광경이 펼쳐졌다.

둥. 둥. 둥.

열흘 동안 잠잠하던 서녕성의 전고(戰鼓)가 깊은 울림을 토해 냈지만, 성벽 위로 몰려든 사람들의 얼굴에는 일말의 두려움조차 깃들어 있지 않았다.

다만, 서녕의 모든 이는 벅차오르는 가슴을 느끼며 지켜볼 뿐이었다.

동서남북.

굽이진 언덕과 드넓은 광야, 황하의 강줄기를 따라 밀려드는 무수한 깃발의 파도를.

“적이다! 적이 나타났다!”

“…….”

모두라고 했던 거 정정.

어딜 가나 분위기 파악 못 하는 미친놈은 있기 마련이다.

“본녀의 말이 들리지 않는가! 어서 전투에 대비하라!”

펄쩍펄쩍 뛰는 대인의 모습을 물끄러미 응시하던 적천강이 나를 향해 고개를 돌렸다.

“그, 혹시…….”

뺨에 와닿는 시선을 느낀 나는 말이 끝나기도 전에 선수를 쳤다.

“안 됩니다.”

“아직 아무 말도 안 했다.”

“죽이면 안 되냐고 물어보실 거잖아요.”

“음.”

“팔다리 분지르는 것도 안 됩니다.”

“아.”

“그냥 건드리지 마세요. 미친놈은 놔두는 게 상책입니다. 더군다나 도움 되는 미친놈이잖아요.”

“전투에 도움이 되면 뭐하느냐. 저놈이 입을 열 때마다 주화입마가 올 것 같은데.”

솔직히, 그 말에는 나도 동의할 수밖에 없었다.

전투 때는 홍길동이라도 되는지 동에 번쩍 서에 번쩍하면서 상당히 많은 아군을 살렸다는데, 전투 이후에는 그냥 길똥이가 되어 버렸다.

길가 한복판에 떡하니 놓인 똥이라, 모두가 슬금슬금 피해 버리는.

그나마 다행인 점은, 대인이 보통 미친놈이 아니라는 걸 이제는 일반 백성들까지 알고 있다는 점이다.

“저 양반 또 저러네…….”

“어후, 난 또 뭐라고. 적이라길래 순간 심장 떨어질 뻔했수.”

얼마나 잘 알려졌느냐면, 적이 나타났다는 외침에 깜짝 놀랐던 몇몇 백성들조차 대인의 모습을 확인하고 안심할 정도다.

“근데, 저 대협은 왜 저렇게 된 거요? 암천 놈들이랑 싸울 때는 아주 멀쩡해 보이던데.”

“몰러. 기연(奇緣)이라도 찾다가 절벽에서 떨어지기라도 했나 보지.”

“…….”

수상할 정도로 무협 클리셰에 능통한 백성들의 대화를 듣고 있던 그때.

두두두두두!

지축을 뒤흔드는 말발굽 소리와 함께, 약간의 웅성거림 따위는 단숨에 집어삼킬 거대한 함성이 터져 나왔다.

“와아아아아!”

동시에 그 열기 띤 함성을 따라, 때마침 저 멀리서 불어온 바람과 만난 깃발들이 크게 부풀었다.

천하 무림을 지탱하는 열다섯 개의 기둥.

구파일방(九派一幇), 오대세가(五大世家).

각 성의 패자이자 그런 그들을 따르는 크고 작은 무림 방파와, 몇몇 이들에게는 낯선 남만야수궁(南蠻野獸宮)이라는 다섯 글자.

그리고 창공을 향해 세차게 펄럭이는 그 수많은 이름 중, 가장 크고 높이 솟은 두 개의 깃발.

“무림맹(武林盟)……!”

서녕의 무림인들이 자신들을 상징하는 깃발을 보고 감격했다면, 관군과 백성들은 살아생전 단 한 번도 만날 수 없으리라 여겼던 한 사람의 존재에 눈을 부릅떴다.

“화, 황제 폐하!”

“친정(親征)하신다는 소문이 사실이었다니!”

짙은 아지랑이로도 가릴 수 없는, 깃발에 수놓아진 찬란한 황금빛 용을 발견한 사람들은 너나 할 것 없이 무릎을 꿇고 큰절을 올렸다.

대국.

아니, 대명국(大明國)의 지배자이자 자신들의 어버이에게.

“난리 났군. 아주 난리 났어.”

적천강의 뇌까림을 증명하듯, 온 사방이 난리였다.

피가 흐르도록 성벽에 꽝꽝 머리를 찍는 사람도 있고, 당장 실신이라도 할 것처럼 목놓아 우는 사람도 있다.

심지어 가까이에서 얼굴을 본 것도 아니고, 이제야 겨우 서서히 가까워지는데도 이 정도다.

이만하면 가히 북괴 삼부자, 언럭키 천주라 칭해도 할 말이 없을 지경.

“그러고 보니까 천주랑 한 글자 차이긴 하네.”

내 혼잣말은 들은 적천강이 떨떠름한 목소리로 입을 열었다.

“그런 말은 좀 작게 해라. 듣는 귀가 많다.”

“그래서 작게 했는데요.”

“더 작게 하라고.”

“에이, 이 정도면 됐어요. 저희가 언제부터 이런 거 눈치 봤다고.”

“아니, 틀린 말은 아니긴 한데 그래도 좀 보라고…….”

“제가 뭘요. 스승님이 예전부터 그렇게 가르치셨잖아요. 염라대왕 앞으로 끌려가도 할 말은 다 하고 살라고.”

“……!”

“왜요?”

아주 잠깐, 말없이 콧잔등을 씰룩거린 적천강이 휙 고개를 돌린다.

그러더니 빠르게 가까워지는 행렬을 바라보며 혼잣말처럼 중얼거렸다.

그러니까, 혼잣말.

“듣기 좋네.”

“예?”

“한데 몇 번 듣다 보니 스승님이라는 호칭은 너무 좀 딱딱한 것 같기도…….”

“지금 저한테 하시는 말씀이에요?”

“어후, 날 좋다. 날은 좋은데 제자랍시고 꼴랑 하나 있는 놈은 눈치가 더럽게 없고…….”

“그러게요. 날씨 좋네, 진짜.”

“…….”

“뭐요.”

슬슬 열 받을 거 같은데, 그만 놀려야 하나.

이제는 코까지 벌름거리는 그의 모습에 참고 있던 실소가 터져 나오려던 그때였다.

구구구구궁.

육중한 소음과 함께 해자(垓字)를 가로질러 내려가는 다리.

그와 동시에, 눈부시도록 새하얀 백마가 앞으로 나섰다.

기쁨과 눈물이 뒤섞인 백성들의 함성 아래로.

“황제 폐하 만세! 대명국 만만세!”

천자.

마침내 그가 왔다.

등장만으로도 까와 빠, 아니 백성들을 미치게 만들어 버리는 대륙의 지배자가.

하지만 저 사막 너머에 웅크린 어떤 빌어먹을 놈과는 달리, 이 유사 천주는 우리 편이라는 것이 중요하다.

그가 물고 빠는 막둥이 동생이 내 팬클럽 회장이며, 황실 전체가 내게 아주 큰 빚을 지고 있다는 것도.

“오랜만이구나, 상산후(上山侯) 진태경.”

마침내 성문을 넘어 서녕성에 발을 들인 그가, 무엄하게도 뻣뻣이 허리를 펴고 있는 나를 향해 부드럽게 웃었다.

“아니, 이제는 상산왕(上山王)이라 불러야겠군.”

“……?”

엄마.

나 왕 됐어.
```

## Final English reading copy

```markdown
# Chapter 1139

As I listened to the unending account, I had to hold my breath again and again.

The Central Plains Murim—or rather, the whole realm—was coming together.

It had been all but inevitable, but hearing the news from the current Alliance Leader himself gave it a weight unlike any other.

Of course, the sheer numbers were part of what made it so weighty.

A hundred thousand.

No fewer than a hundred thousand elite Imperial Guards were racing north along the Yellow River, swift as shafts of light.

Under the command of none other than the Son of Heaven.

*Looks like that old man managed to stay alive after all.*

I suddenly remembered the last time I’d seen the Son of Heaven.

His aged appearance belied his youth, and his face was as pale as a sheet. The ruler of a vast continent had been on the brink of death. He surely would have died before long.

If not for the worn-out old book I’d given him as a parting gift.

*White Illusion Jiangshi Art.*

A secret art of the Maoshan Sect—and, at the same time, demonic martial arts that defied all common sense.

The more one practiced it, the more one became a jiangshi. It was no better than a poisoned Holy Grail, but the Son of Heaven seemed to have drunk from it willingly.

A Holy Grail was still a Holy Grail, after all.

Even in an age when the Three Bonds and Five Relationships were held sacred, they meant nothing if you couldn’t breathe.

Not when he had only one blood relative who could take on all the burdens he carried.

And the Son of Heaven wasn’t the only one who had someone to protect.

“The Yangtze and the Yellow River are packed from bank to bank. Everyone’s coming here.”

Mae Jonghak hadn’t exaggerated when he said “everyone.”

The hundred thousand Imperial Guards led by the Son of Heaven were only part of the enormous force gathering.

From the great Murim sects to reclusive masters hidden deep in the mountains, all the way down to Third Rate swordsmen.

Once the blade at their throats—the Moving Formation—had been broken, they all smashed through the fence and poured out.

Countless ships covered the rivers, while the thunder of galloping hooves shook the earth.

All for one goal.

To cool the heat raging in their hearts like molten lava.

“The sacrifices made by you and so many others are what made them rise up.”

Some of those who had cowered in fear must have felt ashamed. Others must have blamed themselves for not being there to fight alongside us.

Of course, people weren’t as righteous as they liked to think. Some might have taken up arms simply to make a name for themselves.

But the reason didn’t matter.

At least now, we could come together as one.

That was why I could understand the position the Alliance Leader before me had been in.

“You don’t have to apologize.”

At my sudden words, Mae Jonghak—whose face had been stern the entire time—bit his lip.

“…My friend.”

“To be honest, yes. There were times when I thought we’d been abandoned.”

To catch a big fish, you needed bait.

This time, Xining had been the bait.

The kind so tempting that Dark Heaven couldn’t help but bite.

But the Murim Alliance hadn’t thought of us as mere bait or pawns to be discarded.

They’d drawn up an elaborate plan in the strictest secrecy. Though they’d been a step too late, they’d sent powerful reinforcements—and even uprooted the last lingering threat the Blood Lord had left behind.

“So please, don’t apologize.”

I met Mae Jonghak’s wavering gaze and added quietly:

“If only for the sake of those who are gone.”

“……!”

“They chose their path. They’d already accepted that they might die, and they fought as though they meant it. More bravely than anyone.”

Mae Jonghak had no reason to apologize.

No. If he did, it would be no different from insulting the dead.

Jeong Hogun and a thousand Embroidered Uniform Guards. Countless martial artists and government troops. Even the common folk who’d taken up rusty axes and sickles to hold back the invaders.

Every one of them had been a hero.

And so had those who, like Mae Jonghak before me, had struggled behind the scenes for this great victory.

That left us with only one goal.

“We have to repay this blood debt many times over. All of us, together.”

Everyone here knew who we had to collect that debt from. So did the whole realm.

The Lord of Heaven.

Or—

*Asmodeus.*

The supreme demon. The king of the Demon Realm.

The name of the being that had finally intruded into reality lingered on my tongue like a bitter poison.

And someone else, bound up with him.

*Cheon Taemin.*

No.

The Martial God.

* * *

Time flew by.

One day, thick snow fell like it was the middle of winter. The next, a storm of wind and rain swept through as if it meant to swallow the whole world.

Then, three days after I regained consciousness, a sight I’d never seen before came into view beyond the shimmering heat haze raised by the blazing sun.

Boom. Boom. Boom.

The war drums of Xining City, silent for ten days, began to toll with a deep resonance. But not a trace of fear showed on the faces of the people crowding the walls.

Everyone in Xining simply watched, their hearts swelling.

North, south, east, and west.

Across the winding hills, the vast plains, and along the Yellow River—a wave of countless banners surged toward us.

“The enemy! The enemy’s here!”

“……”

Take that back about everyone.

There’s always some lunatic who can’t read the room, wherever you go.

“Are you not listening to me? Prepare for battle at once!”

Jeok Cheongang watched the Great Sir hopping up and down, then turned to me.

“Er, would you happen to…”

I felt his gaze on my cheek and cut him off before he could finish.

“No.”

“I haven’t said anything yet.”

“You were about to ask if you could kill him.”

“Hmm.”

“You can’t break his arms and legs, either.”

“Ah.”

“Just leave him alone. Best to leave a madman be. Besides, he’s a useful madman.”

“So what if he’s useful in battle? Every time that man opens his mouth, I feel like I’m about to suffer qi deviation.”

Honestly, I couldn’t disagree.

They said he’d been darting all over the battlefield like Hong Gil-dong, saving a whole lot of our people. But after the battle, he’d become plain old Gil-dung.

Like a pile of shit right in the middle of the road, he was someone everyone edged around.

The one saving grace was that even ordinary people now knew the Great Sir wasn’t just any lunatic.

“That old man’s at it again…”

“Whew, I thought something serious had happened. When he shouted ‘enemy,’ I nearly had a heart attack.”

He was so well-known that even the people who’d jumped at the shout calmed down as soon as they saw him.

“But what happened to that Great Hero? He looked perfectly fine when he fought those Dark Heaven bastards.”

“Who knows? Maybe he fell off a cliff looking for a fortuitous encounter.”

“……”

I was listening to a conversation between commoners who knew a suspicious amount about martial-arts clichés when—

Thud-thud-thud-thud!

The pounding of hooves shook the earth, and an enormous cheer erupted, swallowing up the scattered murmurs in an instant.

“Waaah!”

The flags swelled as the wind that had just blown in from far away caught them, carrying that feverish roar with it.

The fifteen pillars that upheld the realm’s Murim.

The Nine Sects and One Gang. The Five Great Families.

The overlords of the various provinces, the large and small Murim sects that followed them—and five words unfamiliar to some: Nanman Beast Palace.

And among all those names fluttering fiercely toward the sky, two banners rose higher and larger than the rest.

“The Murim Alliance…!”

The martial artists of Xining were moved at the sight of the banner that represented them. The government troops and commoners, meanwhile, stared wide-eyed at the sight of a man they’d thought they would never meet in their lives.

“T-The Emperor!”

“So the rumors that he’d lead a personal expedition were true!”

The people who spotted the brilliant golden dragon embroidered on a banner, impossible to hide even behind the thick heat haze, all dropped to their knees and bowed.

To the ruler of the Great Nation.

No, to the ruler of Great Ming—their father.

“This is a sight. What a sight.”

As if to prove Jeok Cheongang’s muttering right, the whole place was in an uproar.

Some people slammed their heads against the wall until blood ran down. Others wailed as though they were about to faint.

They weren’t even close enough to see his face yet, and this was how they were acting.

At this rate, you could call him the three-generation ruling family of North Korea—or an unlucky Lord of Heaven—and no one could argue.

“Come to think of it, he’s only one character away from the Lord of Heaven.”

Jeok Cheongang heard me mutter and spoke in a slightly uneasy voice.

“Keep your voice down. There are plenty of ears around.”

“That’s why I kept it down.”

“Lower.”

“Come on, this is fine. Since when have we worried about stuff like this?”

“No, you’re not wrong, but you should still watch it…”

“What did I do? You’ve always taught me, Master, to speak my mind—even if I’m dragged before Yama.”

“……!”

“What?”

Jeok Cheongang silently twitched his nose for a moment, then turned away.

Watching the procession rapidly draw nearer, he muttered as though to himself.

To himself, mind you.

“That sounds nice.”

“Huh?”

“But the more I hear it, the more I think ‘Master’ sounds a bit too stiff…”

“Are you talking to me?”

“God, what a nice day. It’s a beautiful day, but my one and only Disciple is so damn clueless…”

“Yeah. Really beautiful out.”

“……”

“What?”

Maybe I should stop teasing him before he got annoyed.

I was just about to let out the snicker I’d been holding back at the sight of his nostrils flaring now too, when—

Grrrummmble.

With a heavy rumble, the bridge lowered across the moat.

At the same time, a dazzlingly white horse stepped forward.

Beneath the people’s cheers, joy and tears mingled together.

“Long live the Emperor! Long live Great Ming!”

The Son of Heaven.

At last, he had arrived.

The ruler of the continent, who could drive both fans and haters—or rather, the common people—mad just by showing up.

But unlike some miserable bastard lurking beyond that desert, this ersatz Lord of Heaven was on our side. That was what mattered.

His baby brother, whom he doted on, was the president of my fan club, and the entire Imperial House owed me a very big debt.

“It’s been a long time, Marquis of Shangshan Jin Taekyung.”

At last, he crossed the city gates and stepped into Xining. He smiled gently at me as I stood there with my back impudently straight.

“No, I suppose I should call you Prince Shangshan now.”

“……?”

*Mom. I’m a king now.*
```
