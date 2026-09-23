<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0903.txt",
      "sha256": "d9d8f3f6fddcba83aaee9e3912d73c3d0222bb3b2a92976c484fe6537f7a9487",
      "bytes": 14437
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "da3fb6d965792a1effa3523447d20ebfd7f75fc1f83cda94230f7145a8a8bb9b",
      "bytes": 965
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "03762930bd6c14ca28c0734406d2b6e2d061314fc31144f3f75a6b5109ed9ae4",
      "bytes": 927
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f7a3e34f8b8e10ac9a5f2860012f534106a1430b1f63acd41f9b566bbe6134ec",
      "bytes": 759
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "78ac775d3c5731441b49749f84f99cb75ba0ba84c7e157708a1f8dd783ebcefb",
      "bytes": 898
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "907ca7bd4c33e002b205c1800cea4d65c3053f8f8b2b7b80a9f2168ca78cc2f2",
      "bytes": 1445
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "57312238ee5704f38527db1fd1893fa3ef2aeb131254900133ab5d2b50214688",
      "bytes": 1369
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "16c14b4dd8d1c5bb17a8a4df8d67e44720c737a4c8fd9ed163fc113d2240eb7a",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "554645e98a5290dcf7789d2b4838c98c1fdc373a9aab10fddfd990901283c67b",
      "bytes": 973
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "a017606402fa178fb7e4c79c75ef25e8a526428dc2ea33e46a0f1f2563586da8",
      "bytes": 998
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "b1a8d0c9e905ceb82838dbd74c2f337001faf690e52696114fd52acf3c1f163a",
      "bytes": 900
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "64dc68508ce0fdd4b1da8027dd4f3d020d9da0704022ce5ab396dfc5f12adff9",
      "bytes": 715
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5d31a170643a68763b6051c8bb72b7164ac96924623cd667a766dfadede60f3a",
      "bytes": 685
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "81f03722a79e4575bfdfac661980848b0b869f2f8020d01da720aa08273e5429",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "852d5f73b9e4549b425f01d120cf2dd1002fa4e0bfe8e43a35aab4634191e961",
      "bytes": 262237
    }
  ],
  "estimated_tokens": 13804
}
-->

# Durable State Update — Chapter 903

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
1 and safe_through 903. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 903. Profile updates may replace only one
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
  "chapter": 903,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 903,
    "continuity_sources": [903],
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
    "The imperial birthday banquet is underway, and the Emperor has publicly declared Prince Shangshan his heir.",
    "Aehyang has arrived at the banquet under Embroidered Uniform Guard protection; she appears uneasy and touches her belly.",
    "Cang Gong and Taekyung are waiting for Cang Gong’s signal to act; Cang Gong says So Gyo must be dealt with and the Fire King is essential.",
    "The Fire King remains outside the banquet hall.",
    "Prince Shangshan still carries the Myriad-Poison Ring entrusted to him by Taekyung.",
    "The Murim Alliance has sent reinforcements against Dark Heaven."
  ],
  "continuity_sources": [
    901,
    902
  ],
  "open_questions": [
    "Why might the Emperor be smoking opium?",
    "What signal will Cang Gong give, and when will they act?",
    "What is So Gyo’s purpose in remaining beside Prince Shangshan?"
  ],
  "safe_through": 902,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 진태경 | 대설귀 | hostile_martial_opponents | old man | mocking, casual, and profane | Jin taunts the Great Snow Fiend while preparing to continue the fight. |
| 대설귀 | 진태경 | hostile_martial_opponent | Jin Taekyung | cold, incredulous, and confrontational | The Great Snow Fiend addresses Jin while demanding an explanation for his survival. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 892
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 902
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 725
- **Aliases:** Hanbaek (한백)
- **Role:** The Great Snow Fiend was the former ruler of Great Snow Mountain and a Supreme Peak fiend who killed Baekhwi and Venerable Wusang during the Great Faction War before Jin Taekyung killed him.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend was an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he was senior to Black Hand and served under the Southern Heaven Demon Empress before Jin Taekyung killed him.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 898
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 901
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, and Jin has signed its pledge and arranged for Ma to summon Murim Alliance reinforcements.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 901
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 893
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 902
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 902
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 892
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 897
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 892
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃903화



아무리 고민해도 답이 나오지 않는 수수께끼가 있다면, 해결하는 방법은 하나뿐이다.

모든 것을 거꾸로 뒤집는 것.

지금까지 파악한 정황, 단서를 모두 잊고 처음부터 시작하는 것만이 마지막 대책이다.

언제 흘렸는지 모를 귀중품을 찾기 위해 왔던 길을 되돌아가는 것처럼, 나 역시 시작점에서부터 크고 작은 하나하나를 되짚었다.

그리고 마침내, 하나의 가설에 도달할 수 있었다.

“황제는, 상산왕이 위기에 빠지는 걸 원치 않는다.”

“……!”

창공의 회색빛 눈동자에 일어난 미약한 파문.

그것은 찰나라고 부를 만큼 짧은 순간 만에 나타났다가 사라졌으나, 그의 작은 움직임 하나하나에 촉각을 곤두세우고 있던 내 이목을 피할 수는 없었다.

‘사실이었어.’

머릿속을 강타한 깨달음과 함께 찌릿한 전류가 등줄기를 타고 흐른다.

아직도 사그라지지 않은 사람들의 거대한 함성 속에서, 나를 물끄러미 바라보던 창공이 불현듯 입을 열었다.

“언제부터였나?”

다른 누군가였다면 이해하지 못했을, 맥락 없는 물음.

그러나 나는 즉각 그 말이 가리키는 의미를 깨달았다.

도대체 언제부터 자신들을 의심하기 시작했냐는 그 질문을.

“소교.”

그래, 정확히 그때부터였다.

도저히 실패할 수 없던 유리한 상황에서 날 놔준 그 날.

그 어떤 정황과 단서로도 소교가 보인 기이한 행동은 완전히 이해할 수 없었다.

마치 목에 걸린 생선 가시처럼.

“소교라…….”

내 짤막한 대답에 창공이 작게 고개를 끄덕였다.

“그래, 그랬겠지. 이 대계의 유일한 허점이었으니까. 이럴 줄 알았다면 저 정체 모를 여자를 진작 제거해야 했다. 설령 황제와 전면전을 치르는 한이 있더라도.”

뭐?

반사적으로 튀어나오려는 목소리를 애써 삼켰지만, 찰나의 동요까지는 숨기지 못했다.

‘창공조차도 소교의 정체를 모른다고?’

순간 나도 모르게 얼굴에 떠오른 당혹감을 읽어 낸 창공이 낮은 웃음을 흘렸다.

“보아하니 자네도 모르는 모양이군. 저 여자가 누구인지. 심지어 아군인지 적군인지조차.”

“……!”

“희한하군. 참으로 희한해. 조금 전까지는 무림맹의 끄나풀이 아닐까 의심했는데…… 이제는 도무지 모르겠군. 황실이 비밀리에 키워 낸 고수라고 해도 노부의 이목을 피할 수 없었을 터인데.”

이번만큼은 내가 처한 이 모든 상황을 떠나 창공이 느끼는 의문에 공감할 수밖에 없었다.

‘그렇다면 소교는, 저 여자는 누구지?’

무림맹에 속한 인물이었다면 이런 상황이 오기 전에 내게 모든 진실을 알려 주었을 테고, 암천이나 황실의 고수라면 창공이 모를 리 없다.

하지만 소교는 달랐다.

지금까지 확인된 바에 의하면 그녀는 제삼의 인물이었다.

그 어디에도 소속되지 않은.

‘도대체.’

소교는 누구일까. 지금쯤 어떤 표정으로, 무슨 생각으로 우리를 바라보고 있을까.

그리고…….

‘적군일까. 아군일까.’

나는 저 멀리, 높게 솟은 계단 위에 서 있을 소교를 향해 고개를 돌리고 싶은 충동을 애써 억눌렀다.

창공과 나 사이의 거리는 불과 몇 걸음. 이런 상황에서 잠깐이라도 시선을 돌리는 것은 자살행위나 다름없다.

물론, 이렇게 배짱을 부리는 것도 창공이 당장 나를 죽일 수 없다는 확신이 있었기 때문이었지만.

“눈빛이 좋군. 투기(鬪氣)가 흘러넘쳐. 하지만 무슨 연유로 그분께서 자네에게 관심을 보이시는 걸까.”

그분.

이곳에 없는 누군가를 지칭하는 창공의 목소리에서, 숨길 수 없는 두려움과 경애를 느낀 것은 단순한 착각이 아닐 것이다.

혈주도, 서천마군도, 그리고 남천마후도 그러했으니까.

저들 암천(暗天)은, 천주(天主)라는 하늘이 있기에 존재하는 집단이었으니까.

“한번 말해 보게. 당사자라면 그분께서 이토록 자네를 찾는 연유를 알 수도 있겠지. 이토록 어린 나이에 전무후무한 성취를 보여 주어서? 아니면 그분만이 알아볼 수 있는 또 다른 진가 때문에?”

마치 죽은 이의 그것과 같은 회색빛 눈동자가 흐릿하게 빛났다.

내가 지금껏 느껴 보지 못한, 은밀하면서도 무시무시한 한기와 함께.

스아아아.

감히 장담컨대, 남만에서 나를 궁지에 몰아넣었던 대설귀(大雪鬼)의 음한지기(陰寒之氣)조차도 이 정도는 아니었다.

‘아니, 음한지기와는 달라.’

보다 원초적이고 순수한 무언가.

들어 본 적도, 겪어 본 적도 없는 또 다른 힘.

그러나 나는 본능적인 두려움을 이겨 냈다. 뼛속까지 스며드는 서늘한 기운을 견디며 대답했다.

“그걸 왜 나한테 묻고 지랄이야. 불알도 없는 새끼가.”

“……!”

크게 뜨인 눈동자로 나를 바라보던 창공이 희미하게 웃었다.

“그래, 당연히 모르겠지. 어찌 자네 따위가 감히 그분의 뜻을 헤아릴 수 있…….”

“응. 아무리 뜻을 헤아려도 찾아볼 수 없는 니 불알.”

“단어 선택에 신중을 기하는 것이 좋을 걸세. 제아무리 노부가 그분께 하해와 같은 은혜를 입었다고는 해도…….”

“응. 하해를 뒤져도 찾을 수 없는 니 고환.”

“…….”

“단어 선택에 신중을 기했는데, 무슨 문제라도?”

조금 전의 희미한 미소는 이미 사라진 지 오래.

아직도 그치지 않은 사람들의 환호성 속에서, 굳게 닫혀 있던 창공의 창백한 입술이 열렸다.

“어떤가. 혓바닥을 뽑는 정도라면, 그분께서도 충분히 이해해주실 거라 생각하지 않나?”

“맞아. 천주라면 그럴 수도 있겠지. 안 그래도 불알 없는 놈이라 수하 중에서도 유독 신경 쓰이는 아픈 불알…… 아니, 아픈 손가락일 테니까.”

고개를 끄덕여 수긍한 내가 말을 이었다.

창공의 어깨너머를 가리키며.

“하지만 저 양반은 이해 안 해 줄걸.”

그 순간.

느려진 시간 속에서, 모든 것이 동시에 이루어졌다.

무심코 등 뒤를 향해 고개를 돌리는 창공. 그런 창공을 향해 화염이 실린 일권(一拳)을 뻗는 나.

그리고 마치 홀로 시간을 역행하듯, 섬광 같은 속도로 쏘아진 내 주먹이 누군가의 육신에 닿기도 전에 앞질러 가로막은 단단한 손바닥.

콰아앙!

하늘이 쪼개지는 듯한 굉음이 느려졌던 시간을 되돌린다. 동시에 강대한 여파가 대연회장을 흔들었다.

콰득, 드드드득!

지진이라도 난 것처럼 흔들리는 대지.

사방에서 터져 나오는 비명과 고함.

순식간에 극심한 혼란에 빠진 그 공간 속에서, 나를 응시하는 한 쌍의 새하얀 안광(眼光)이 있었다.

“고작, 이 정도였나?”

우둑.

담담한 목소리와는 달리 거대한 힘이 내 주먹을 옥죄인다.

정체를 알 수 없는 얼음 같은 기운이 그 안에 깃든 화염을 억누르고 꺼트렸다.

“이런 얕은 수작을 부리다니, 실망이군.”

으득. 으드득.

붙잡힌 주먹으로부터 끔찍한 고통이 전해진다.

아마도 인간의 경지를 벗어난 근골이 아니었다면 진작 가루처럼 으스러지고도 남았을 상황.

하지만 이 정도 고통은 이미 질릴 만큼 겪어 봤고, 이 정도 기습으로 놈을 쓰러트릴 수 있다는 생각은 처음부터 하지도 않았다.

그저, 이 상황을 알릴 수 있는 신호탄이 필요했을 뿐이었다.

“단순히 얕은 수작이라고 생각했다면 조금 섭섭한데.”

“뭐라?”

“마법이라고 들어 봤는지 모르겠는데, 이참에 직접 보여 줄 테니까 꼭 한 번 봐봐.”

“그게 무슨…….”

창공이 눈살을 찌푸린 그 순간.

콰아아앙!

어둠마저 집어삼키는 눈부신 화염과 함께, 높게 솟은 성벽처럼 대연회장을 둘러싼 암벽들이 터져나갔다.

그리고 조금 전 잠시나마 창공의 시선이 향했던 그곳으로, 한 인영이 성큼성큼 걸어 나왔다.

“노부가 처음이자 마지막으로 충고하건대.”

아무리 봐도 불가(佛家)와는 한참 동떨어진, 화염이 일렁이는 두 눈으로 좌중을 쓸어본 땡중이 말을 이었다.

“뼈와 살이 녹아내리고 싶은 놈만 앞으로 나서거라.”

“……!”

불청객의 정체를 알아차린 창공의 눈빛이 깊게 가라앉았고, 나는 웃으며 입을 열었다.

“아씨오, 화왕.”

그리고 동시에, 아직 자유로운 한 손을 뻗었다.

순간 멈칫한 놈의 가슴을 향해.

구 성에 이른 화염신장(火焰神掌)을.

꽈아아아앙!



* * *



“어?”

문득 걸음을 멈춘 청년이 고개를 돌렸다.

미간을 좁힌 채 자신이 왔던 길을 빤히 응시하는 그의 모습에, 한발 앞서가던 거한이 물었다.

“혁무. 왜 그러나?”

“아니, 그냥…….”

말꼬리를 흐린 혁무진은 입맛을 다셨다.

“그냥, 무슨 소리가 들린 것 같아서.”

그 말을 들은 거한, 태산이 눈썹을 치켜세웠다.

“소리? 그렇다면 적인가?”

“모르겠는데. 그냥 내가 착각했던 건가?”

“그럼 아니다. 혁무가 들었다는 그 소리. 태산이는 못 들었다.”

“하지만 분명히 뭔가 들은 것 같았다니까.”

“혁무. 무공 낮다. 태산이가 마음만 먹으면 잘 다진 오향장육으로 만들 수 있다.”

“……아니, 그런데 이 새끼가 진짜. 지금 나 무시하냐?”

“으음. 솔직히 약간.”

“…….”

“혁무. 우리 멈추면 안 된다. 이제 가야 한다. 모두들 기다린다.”

순간 울컥했던 마음을 가라앉힌 혁무진은 한숨을 푹 내쉬었다.

“그래, 간다. 가.”

하지만 대답과는 달리 걸음은 전처럼 가볍게 나아가지 않았다.

자신이 이미 지나쳐 온 저 길이, 지금 이 순간에도 조금씩 멀어지고 있는 황도(皇都)의 성벽이 자꾸만 눈앞에 아른거렸다.

‘젠장. 이제는 하다 하다 환청까지 들리나?’

조금 울컥하긴 했지만, 아무 소리도 안 났다는 태산의 대답이 사실일 가능성이 높았다.

한 수 위의 절정고수인 그가 아니라면 아닌 거니까.

정말 뭔가를 들었다고는 해도 벌레나 짐승이 움직이는 미세한 소음 정도였을 것이다.

‘그런데 왜 이러는 거지?’

혁무진은 미간을 더욱 좁히며 자신의 가슴을 두드렸다.

안 그랬던 심장이 자꾸만 쿵쿵 뛴다. 마치 보이지 않는 손이 힘껏 쥐어짜고 있는 것처럼.

‘기분이 이상해.’

알 수 없는 불안감과 동시에, 문득 몇 시진 전 헤어졌던 한 사람의 얼굴이 눈앞을 스쳤다.



‘임무 하나만 하자.’



떠나기 직전 들었던 마지막 목소리가 귓가에 맴돌았다.



‘아, 한 가지만 더.’

‘예?’

‘몸조심해라. 너나, 다른 사람들 모두.’



열화신룡 진태경.

그의 당부에 혁무진은 씩 웃는 것으로 대답을 대신했고, 화룡각 전원과 함께 황도를 빠져나가 강소성과 절강성의 경계로 향하고 있었다.

진태경이 건네준 종이에 적혀 있던 바로 그 장소로.

‘임무는 잘 수행하고 있는데…… 왜 이러는지 모르겠네.’

순조롭게 진행되는 임무와는 달리 가슴은 답답하기 그지없다.

이상하리만치 평상시와 달랐던 조장님의, 진태경의 모습이 목에 걸린 가시처럼 따끔거렸다.

대수롭지 않은 이야기로 낄낄거리며 웃고, 건방지다며 때리고, 가차 없이 욕설을 퍼붓던 그 모습은 적어도 오늘만큼은 찾아볼 수 없었으니까.

“혁무!”

“……아.”

상념에서 벗어난 혁무진은 또 다시 자신이 발걸음을 멈췄음을 깨달았다.

그리고 얼마 떨어지지 않은 곳에서 자신을 기다리고 있던 일행들을 본 순간, 가슴이 철렁 내려앉는 것을 느꼈다.

깊게 가라앉은 눈빛.

착잡한 표정.

오직 한 사람, 태산을 제외한 모두가 같은 얼굴로 자신을 바라보고 있었다.

“다들…….”

혁무진은 가까스로 신음을 삼켰다. 아까 전부터 가슴을 옥죄던 이 알 수 없는 불안감의 정체를, 이제야 알 것 같았다.

“다들, 알고 있었습니까?”

힘겹게 뗀 입술 사이로 흘러나온 물음에, 남호가 무거운 목소리로 대답했다.

“그래. 어느 정도는.”

“조장님의 지시로요?”

“아니, 적 노선배께서 미리 언질하셨다. 당신의 제자가 어떤 선택을 하실지 알고 계셨던 게지.”

“그럼 어째서 제게만-”

“짐이 된다 하여 떠나라 했으면, 순순히 명령을 따랐겠느냐?”

“……!”

“나 역시 이 상황이 마음에 들지 않는다. 아니, 모두가 마찬가지야.”

혁무진은 순간 할 말을 잃었다.

도움은커녕 짐밖에 되지 못한다는 그들의 마음을, 거짓말까지 해 가며 자신을 보낸 진태경의 마음을 십분 이해할 수 있었으니까.

그리고 그것이 현실이었으니까.

하지만, 하지만…….

‘그래도 이건, 이렇게는 아니잖습니까.’

으득.

혁무진은 피가 나오도록 입술을 깨물며 고개를 돌렸다. 그리고 순간 이 모든 상황도 잊은 채, 넋 나간 목소리로 중얼거렸다.

“어……?”

그 시선 끝에는, 저 멀리 숲을 뒤흔들며 어둠 속에서 움직이는 수많은 인영이 있었다.

헤아릴 수도 없을 만큼 무수한, 그러나 인기척조차 느껴지지 않는 형체들이.

‘저게 무슨.’

모두의 머릿속에 떠오른 의문. 그리고 알 수 없는 두려움.

이번만큼은 이성이 아닌 본능이 혁무진을, 아니 그들 모두를 움직이게 만들었다.

파파팟!
```

## Final English reading copy

```markdown
# Chapter 903

There are some mysteries that no amount of thought can solve. When that happens, there’s only one way to get to the answer.

Turn everything upside down.

Forget all the circumstances and clues you’ve gathered so far, and start over from the beginning. That’s the last resort.

Like retracing your steps to find some precious thing you don’t remember dropping, I went back to the starting point and reviewed every little detail, big and small.

And at last, I arrived at a hypothesis.

“The Emperor doesn’t want Prince Shangshan to be put in danger.”

“……!”

A faint ripple passed through Cang Gong’s gray eyes.

It appeared and vanished in less time than it took to blink, but I’d been watching his every tiny movement too closely to miss it.

*So it was true.*

The realization struck me, and a jolt of electricity ran down my spine.

Amid the people’s enormous, still-undiminished roar, Cang Gong, who’d been gazing steadily at me, suddenly spoke.

“When did you figure it out?”

It was a question without context, one anyone else would have struggled to understand.

But I immediately realized what he meant.

He was asking when I’d started suspecting them.

“So Gyo.”

Yes. It had started right then.

The day she let me go, even though everything was going so well that there was no way she could fail.

No matter what circumstances or clues I considered, I couldn’t make sense of So Gyo’s strange behavior.

It was like a fishbone stuck in my throat.

“So Gyo…”

At my brief answer, Cang Gong gave a small nod.

“Yes, I suppose it would be. She was the only flaw in this grand scheme. If I’d known this would happen, I should have eliminated that mysterious woman long ago. Even if it meant an all-out war with the Emperor.”

What?

I managed to swallow the words that almost burst from my mouth, but I couldn’t hide my momentary shock.

*Even Cang Gong doesn’t know who So Gyo is?*

Cang Gong caught the confusion that had appeared on my face and gave a low laugh.

“From the looks of it, you don’t know who she is either. Not even whether she’s an ally or an enemy.”

“……!”

“Strange. Very strange. Until just now, I suspected she might be a Murim Alliance spy, but… now I have no idea. If she were a master secretly trained by the imperial family, she still couldn’t have escaped my notice.”

This time, setting aside the situation I was in, I couldn’t help sharing Cang Gong’s bewilderment.

*Then who is So Gyo? Who is that woman?*

If she’d belonged to the Murim Alliance, she would have told me the whole truth before things got to this point. And if she were a master of Dark Heaven or the imperial family, Cang Gong would have known.

But So Gyo was different.

As far as I could tell, she was a third party.

Unaffiliated with anyone.

*Who the hell…*

Who was So Gyo? What expression was she wearing as she watched us right now? What was she thinking?

And…

*Is she an enemy or an ally?*

I fought the urge to turn and look toward So Gyo, who should have been standing atop the tall stairs in the distance.

Cang Gong and I were only a few steps apart. Taking my eyes off him, even for a moment, would be no different from suicide.

Of course, I was only acting this bold because I was sure Cang Gong couldn’t kill me right away.

“You have good eyes. Full of fighting spirit. But why would that person take an interest in you?”

*That person.*

There was no mistaking the fear and reverence in Cang Gong’s voice as he spoke of someone who wasn’t here.

The Blood Lord, the Western Heaven Demon Lord, and the Southern Heaven Demon Empress had all felt the same way.

Those people of Dark Heaven existed because they had a heaven of their own—the Lord of Heaven.

“Tell me. As the person concerned, you might know why that person is searching for you so relentlessly. Is it because you’ve achieved something unprecedented at such a young age? Or is it because of some other worth only that person can recognize?”

His gray eyes, like those of a dead man, glimmered dimly.

A secret, terrifying chill came with them, unlike anything I’d ever felt before.

*Fwoosh.*

I’d stake my life on it: even the Yin-Cold Qi of the Great Snow Fiend, who’d cornered me in Nanman, hadn’t been this intense.

*No. This isn’t Yin-Cold Qi.*

It was something more primal and pure.

Another kind of power, one I’d never heard of or experienced.

But I overcame my instinctive fear. Enduring the chill that seeped into my bones, I answered.

“Why the hell are you asking me? You’re the one without any balls.”

“……!”

Cang Gong stared at me with eyes wide, then smiled faintly.

“Yes, of course you wouldn’t know. How could someone like you possibly fathom that person’s intentions—”

“Yeah. I can look all I want, but I still can’t find your balls.”

“Be careful with your choice of words. No matter how much grace that person has shown me…”

“Yeah. I could search the whole ocean and still not find your testicles.”

“…….”

“I chose my words carefully. What’s the problem?”

His faint smile had vanished long ago.

Amid the people’s continued cheering, Cang Gong’s tightly shut, pale lips parted.

“What do you think? Surely that person would understand if I merely pulled out your tongue.”

“Sure. The Lord of Heaven might. You’re the one among his followers he worries about most. His sore ball—no, his sore finger. Especially since you haven’t got any balls.”

I nodded in agreement and kept talking.

Pointing over Cang Gong’s shoulder.

“But that guy won’t understand.”

At that moment—

In the slowed-down flow of time, everything happened at once.

Cang Gong reflexively turned to look behind him. I thrust a fist wreathed in flame at him. And a solid palm shot forward like a flash of light, as if reversing time all by itself, intercepting my fist before it could reach anyone.

*BOOM!*

A roar like the sky splitting apart brought time back to normal. At the same instant, a mighty shock wave shook the grand banquet hall.

*Crack! Rrrrmm!*

The ground shook as if there’d been an earthquake.

Screams and shouts erupted in every direction.

In the space that had plunged into chaos in an instant, a pair of pure white eyes stared at me.

“Was that all you had?”

*Crack.*

His voice was calm, but the immense force squeezing my fist was anything but.

An unknown, ice-cold energy within his hand suppressed the flames in mine and snuffed them out.

“I’m disappointed you’d resort to such a shallow trick.”

*Crunch. Crunch.*

Agonizing pain shot through my captured fist.

If my muscles and bones hadn’t long since surpassed the limits of an ordinary human, they would have been crushed to dust already.

But I’d suffered this much pain more times than I cared to count, and I’d never expected that surprise attack to take him down.

I’d only needed a signal flare to let everyone know what was happening.

“If you thought it was just a shallow trick, I’m a little hurt.”

“What?”

“I don’t know if you’ve heard of magic, but I’m going to show you some now. Make sure you watch.”

“What are you—”

The moment Cang Gong frowned—

*BOOOOM!*

With a blinding blaze that swallowed even the darkness, the rock walls surrounding the grand banquet hall like a towering fortress exploded.

And from the place Cang Gong had glanced at just moments earlier, a figure strode out.

“I’ll give you my first and last warning.”

The flames dancing in that damn monk’s eyes looked anything but Buddhist. He swept his gaze across the hall and went on.

“Only step forward if you want your flesh and bones to melt.”

“……!”

Cang Gong’s eyes sank when he recognized the uninvited guest. I smiled and spoke.

“Accio, Fire King.”

At the same time, I thrust out my one free hand.

Toward the bastard’s chest, which had stiffened for an instant.

With the Flame Divine Palm, now at nine-tenths mastery.

*BOOOOM!*

* * *

“Huh?”

The young man abruptly stopped walking and turned around.

A burly man walking ahead of him asked when he saw the young man staring back down the road with a furrowed brow.

“Mujin. What’s wrong?”

“No, it’s just…”

Hyuk Mujin trailed off and clicked his tongue.

“I thought I heard something.”

At that, the burly man, Taishan, raised an eyebrow.

“A sound? Enemy?”

“I don’t know. Maybe I imagined it.”

“Then no. That sound Mujin heard. Taishan didn’t hear it.”

“But I’m telling you, I definitely heard something.”

“Mujin. Weak martial arts. Taishan can make you into well-prepared five-spice pork if he wants.”

“……Hey, what the hell? Are you looking down on me?”

“Mm. Honestly, a little.”

“…….”

“Mujin. We can’t stop. We have to go now. Everyone is waiting.”

Hyuk Mujin swallowed the flare of anger and let out a long sigh.

“Yeah, I’m going. I’m going.”

But despite his answer, his steps didn’t come as easily as before.

The road he’d already traveled and the walls of the Imperial Capital, growing a little more distant with every passing moment, kept appearing before his eyes.

*Damn it. Am I hearing things now, too?*

He was a little annoyed, but Taishan was probably right that there hadn’t been a sound.

If Taishan, a Peak master a step above him, said there was no sound, then there was no sound.

Even if Mujin had heard something, it must have been a faint rustle from an insect or an animal moving.

*So why do I feel like this?*

Hyuk Mujin frowned even harder and thumped his chest.

His heart, which had never behaved this way before, kept pounding. It was as if an invisible hand were squeezing it hard.

*I have a bad feeling.*

Along with the inexplicable unease, the face of someone he’d parted with a few shichen ago suddenly flashed through his mind.

*Just one mission.*

The last words he’d heard before leaving still echoed in his ears.

*Oh, one more thing.*

*Yes?*

*Be careful. You, and everyone else.*

Blazing Flame Divine Dragon Jin Taekyung.

Hyuk Mujin had answered his warning with a grin, then left the Imperial Capital with everyone from the Fire Dragon Pavilion, heading for the border between Jiangsu and Zhejiang Provinces.

For the very place written on the note Jin Taekyung had given him.

*I’m carrying out the mission just fine… so why do I feel like this?*

The mission was going smoothly, but his chest felt unbearably tight.

The way the Captain—Jin Taekyung—had acted so unlike himself had been like a fishbone caught in Mujin’s throat.

He’d laughed and joked about nothing, hit him for being cheeky, and cursed him without holding back. But he hadn’t seen any of that from Taekyung today.

“Mujin!”

“……Ah.”

Snapping out of his thoughts, Hyuk Mujin realized he’d stopped walking again.

Then he saw his companions waiting for him not far away, and his heart sank.

Their eyes were grave.

Their expressions troubled.

Everyone except Taishan was looking at him with the same face.

“Everyone…”

Hyuk Mujin barely swallowed a groan. At last, he thought he understood what the unaccountable unease that had been squeezing his chest all this time meant.

“Did… did you all know?”

At his question, forced out through stiff lips, Namho answered in a heavy voice.

“Yes. More or less.”

“On the Captain’s orders?”

“No. Senior Jeok warned us in advance. He knew what choice his Disciple would make.”

“Then why was I the only one—”

“If he’d told you to leave because you’d be a burden, would you have obeyed without a fuss?”

“……!”

“I don’t like this situation either. No—none of us do.”

Hyuk Mujin was momentarily at a loss for words.

He understood perfectly well how they felt, knowing they could only be burdens rather than help, and why Jin Taekyung had lied to send him away.

And it was the truth.

But, but…

*Still, it shouldn’t be like this.*

*Grit.*

Hyuk Mujin bit down on his lip until it bled and turned his head. Then, for an instant, he forgot the entire situation and muttered in a dazed voice.

“Huh…?”

At the end of his gaze, countless figures moved in the darkness, shaking the distant forest.

Too many to count, yet not a trace of their presence could be felt.

*What is that?*

The same question rose in everyone’s mind. So did an inexplicable fear.

This time, instinct—not reason—moved Hyuk Mujin.

No, it moved all of them.

*Whoosh!*
```
