<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0671.txt",
      "sha256": "efc4c3283a523c2aae5e51c734c59fd25c6a1127850a60225adea58ca2951692",
      "bytes": 13272
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d84c543ceaf07d624d55158e37609b96cc3c3a3d6a66176d36503a955f73f6e1",
      "bytes": 1785
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "90fbc5af66a53c979eb81e4f99d3a7bf49ae990d077ae46d7867ad560fdaf362",
      "bytes": 202324
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "7c08498bbcd7609e70d10e5412b4eba15cadd20ce4863325cbfa06c90239510e",
      "bytes": 1006
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "2f9a3125649cbaa1d18bc2ce126140a2889a4a511e54398d19617b753a038ebe",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ce804259a058a867272562327075282f0506449097f55bed00ad556327fca906",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "192a5455758e2e97a0e17185eb84704646db511c7dbd509c95a7503516577da5",
      "bytes": 686
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "df993c11a6f1ac9edc476530a1887a25467b2933fb91581096654cc61d5e6c3f",
      "bytes": 769
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "42b4159798173cd90588fdb749d23d471fcf1c4db071581d8fb2990ff6dd1880",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "365a40039c2d91514aed720d7d82b241acdc7d9c3f5b79ec0a58775c81723724",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7a9945796f1e386f4288bafdda7c83062cb668e6874c1a36caf3533c106563ae",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "5b629a158d599da4b06964632828bbdfd79ff36ef223c4afd277bf9ac866b9cf",
      "bytes": 843
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "4ae16b2a627164978564148c9340fdd8d5ebcabdf4ed48179db2d6cd815566b5",
      "bytes": 787
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "962aef47121f1c408558b66fb5e6a6a7daf301a9abc6218ad8aacfdeacb8264a",
      "bytes": 962
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "db6c69ee8549cb7f2cf42e69e8c155b3623c6c7ae6c48c809801c98c257b53ae",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4045b33709c85492f6e5a040817a29f9f908e64bbead101e589c38cbc6fe4ca0",
      "bytes": 208612
    }
  ],
  "estimated_tokens": 13188
}
-->

# Durable State Update — Chapter 671

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 671. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 671. Profile updates may replace only one
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
  "chapter": 671,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 671,
    "continuity_sources": [671],
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
    "Baeksang has chosen to oppose the Beast Miao King and has released Sword Force against him; the outcome remains unresolved.",
    "The Beast Miao King refused to turn back and sought half a shichen for the escape party to get away.",
    "Wonhu and the remaining Miao warriors stayed behind and are surrounded by more than a hundred Bai warriors under Baeksang.",
    "Jin is carrying the unconscious Yayul Mok on White Tiger after leaving the Outer Palace, though they remain within Nanman Beast Palace territory.",
    "Jin intends to prevent Yayul Mok from returning and prioritizes rescuing the Fire Dragon Pavilion members in the reconnaissance squad.",
    "Jin considers Dark Heaven's intervention and Baeksang's betrayal certain and expects a net over heaven and earth to spread across Nanman within half a day or a day.",
    "White Tiger detected Yohi's scent, triggering the Sudden Quest Yohi's Tracking Scent based on the scent pouch Jin found in the western Yao territory."
  ],
  "continuity_sources": [
    670
  ],
  "open_questions": [
    "Did the Beast Miao King survive Baeksang's Sword Force?",
    "Will Wonhu and the remaining Miao warriors survive their battle with Baeksang's Bai forces?",
    "Can Jin reach the reconnaissance squad and rescue the Fire Dragon Pavilion members?",
    "What will Yohi's Tracking Scent lead Jin to?",
    "How will Baeksang's betrayal affect the Beast Miao Palace and the wider Nanman conflict?"
  ],
  "safe_through": 670,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Palace Lord for 궁주.",
    "Use Sword Force for 검강 and half a shichen for 반 시진.",
    "Use Outer Palace for 외궁 and Yohi's Tracking Scent for 요희의 추종향."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 하오문    | **Lower District Sect**          |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 사형     | **Senior Brother**                           |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 670
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; despite his bond with Yayul Cheok, he has chosen to oppose the Beast Miao King's escape and has surrounded Wonhu's remaining force with Bai warriors.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 670
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 670
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 649
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 666
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 666
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 670
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 670
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 669
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 669
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 670
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese; he is currently unconscious on White Tiger while Jin carries him away from the Outer Palace.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 670
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃671화



지금 내가 머무르고 있는 이곳, 무림에는 현대가 보유한 눈부신 과학 문명도, 기계 공학도, 더불어 마법도 존재하지 않는다.

하지만 이 세상에도 마법 못지않은 특별함이 곳곳에 녹아 있다.

공력을 축적하여 헌터 이상의 힘을 발휘하는 무림인. 현대에서는 찾아볼 수 없는 수많은 종류의 무공과 신묘하고도 기괴망측한 영물과 영약들.

그리고…… 추종향(追蹤香)도 그중 하나다.

띠링.



돌발 퀘스트, [요희의 추종향]이 생성되었습니다!

퀘스트 창을 열어 내용을 확인하시겠습니까?

Y  /  N



갑작스럽게 울려 퍼진 시스템 알림. 예상치 못한 상황에, 나는 홀린 듯이 고개를 끄덕였다.

띠링.



퀘스트



[요희의 추종향]



추격을 피해 도주하는 당신의 앞에 나타난 새로운 길.

이제 당신은 다시 한번 선택해야 합니다.

그러나 당신의 앞에 놓인 이 두 갈래 길의 끝에 무엇이 있을지는 알 수 없으며, 오직 선택에 따른 결과와 책임만이 존재할 뿐입니다.



등급 : 초절정

제한 : 진태경

임무 : 이동할 방향을 선택 (미완료)

보상 : 연계 퀘스트

 ???

실패 : ???





빌어먹을. 이건 또 뭐야.

허공을 가득 메운 홀로그램 창.

동시에 불과 하루밖에 되지 않은 짧은 기억이 섬광처럼 뇌리를 스친다.



‘한 판 제대로 붙은 모양이군.’

‘보고를 받았을 때는 이미 모든 것이 끝난 후였소. 요서부에 남아 있던 것은 피와 시체. 그리고…… 저것들뿐이었지.’



그날의 모든 것을 똑똑히 기억한다. 그건 홀연히 사라진 흑웅과 요희, 두 대족장이 남긴 유일한 단서였으니까.

‘흑웅은 손목이 잘렸고, 요희는…….’

그래, 향낭(香囊)을 남겼었지.

그러나 막 요서부에 도착한 상태였던 나는 향낭보다 흑웅이 남긴 손목에 집중했다.

잘려 나간 손목의 단면에 남은 상흔(傷痕)을 파악한다면 상대의 무공과 그 수준을 대략이나마 유추할 수 있기 때문이다.

‘그에 비해 요희의 향낭은 그리 중요해 보이지 않았고.’

심지어 향낭은 온전한 상태가 아니었다. 비단으로 만들어진 그것은 이미 훼손된 상태였고, 길게 찢어진 틈새로 향이 빠져나간 터라 무취(無臭)에 가까웠으니까.

하지만 나는 몰랐다. 아니, 뒤이어 연달아 벌어진 일들에 그 누구도 신경 쓸 겨를이 없었을 것이다.

그것이 요서부에서 가장 중요한 단서였으며, 누군가 자신을 찾을 수 있도록 요희가 남겨 놓은 추종향이라는 것을.

‘향이 빠져나간 게 아니었어. 처음부터 그랬던 것뿐이지.’

내가 아는 바에 의하면 추종향은 뜻 그대로 누군가를 자취를 쫓기 위해 만들어진 기물(奇物).

결코 흔히 찾아볼 수 있는 물건은 아니지만, 그렇다고 아예 사용되지 않는 것도 아니다.

정파에서 예를 들자면, 하오문과 개방이라던가.

그리고 그중에서도 엄청난 규모를 지닌 개방의 후개와 제법 많은 시간을 함께하며 여러 이야기를 나누었다는 건, 내게 있어 뜻하지 않은 행운이다.



‘추종향이라. 효과는 확실하지만 엄청나게 귀하지. 제조법도 워낙 은밀하고. 만들 수 있는 사람도 무림에 몇 없어.’

‘만리추종향(萬里追蹤香). 뭐 그런 것처럼?’

‘만리추종향이라. 흠, 꼴에 어디서 주워들은 건 있나 보군.’

‘잠시 후면 네 이빨이 다섯 개쯤 떨어질 것 같은데. 그것도 주워 줘?’

‘앗. 아아…….’

‘입이나 마저 털어 봐.’

‘크흠. 사실 만리추종향은 나도 본 적 없다. 사실 말이 좋아서 만 리지. 그 긴 거리를 이동하는 동안 향이 남아 있다는 게 말이 되나 싶기도 하고.’

‘뭐야, 결국 사기였어?’

‘꼭 그런 것만은 아니다. 진태경 네가 귀동냥으로 들은 만리추종향만큼은 아니더라도, 실제로 무림에서 쓰이는 추종향의 종류는 상당해. 그중에서도 최상급을 흔히들 천리추종향(千里追蹤香)이라고 부르지.’

‘천리추종향?’

‘몇 가지 특징이 있다. 첫째, 제조 방식이 더럽게 까다롭다. 둘째, 제조 비용이 더럽게 비싸다. 셋째, 그렇게 제조된 천리추종향을 손에 넣기 위해서는 더럽게 많은 황금이 필요하다.’

‘누가 거지새끼 아니랄까 봐, 말 사이사이에도 더럽다는 건 꼭 끼워 넣네.’

‘내가 아무리 더러워도 네 인성만큼은…… 미안하다. 실언을 했군. 어쨌든 그 정도 되는 최상급 추종향은 같은 무게의 황금에 비교해도 수십 배가 넘는 값어치를 지녔다. 물론 그만큼 효능도 확실하지.’

‘예를 들자면?’

‘확인되지 않은 만리추종향과 달리 정말 천 리 정도는 향이 남아 있고, 후각이 극도로 발달한 일부 짐승들조차 알아채지 못할 만큼 무취(無臭)에 가깝다. 사람은 말할 것도 없고.’

‘뭐야. 그럼 추종향 한 번 바르면 만사형통 아니냐?’

‘대신 추종향이 지속되는 시간은 길어야 칠주야 정도다. 만약 표적이 옷을 태워 버린다거나, 전신을 물에 품 담그는 등의 특수한 상황이라면 향이 사라지진 않더라도 시간은 더 단축될 테고.’

‘그래도 우선 추종향에 당했다는 걸 알아야 그런 시도라도 할 것 같은데. 어지간한 짐승들도 냄새를 제대로 못 맡는다면서?’

‘맞다. 하지만 영물(靈物)이라면 다르지.’

‘아.’

‘그래서 추종향으로 표적을 쫓는 방법은 두 가지뿐이다. 고도의 추종술(追蹤術)을 익힌 자가 있거나, 추종향을 맡을 수 있을 만큼 뛰어난 영물을 앞세우거나.’



언젠가 궁기방과 나누었던 대화를 다시금 떠올린 나는 인정하지 않을 수 없었다. 그때 녀석이 했던 말들이 전부 사실이라는 것을.

그르릉. 킁킁.

낮은 울음소리와 함께 손바닥에 닿은 축축한 코가 연신 움찔거린다.

나는 약간 쓰라릴 만큼 까슬까슬한 혓바닥으로 내 손가락을 핥고 있는 백호를 바라보며 중얼거렸다.

“……그래. 네가 있었지.”

추종향을 맡을 수 있을 만큼 뛰어난 영물.

궁기방이 알려 준 그대로다. 심지어 이 백호, 무야호는 어릴 때부터 사람의 말을 이해하고 교감할 만큼 엄청난 지능을 지닌 영물이었다.

‘영물다운 지능과 평범한 맹수를 뛰어넘는 날카로운 감각.’

무취에 가까웠던 향낭 역시 지금 생각해 보면 천리추종향이었던 것 같다.

표적과의 거리가 천 리 이하라면, 특별한 상황이 아닌 이상 칠주야 동안 지속 된다는 최상급 추종향.

이는 무야호와 달리 멀뚱멀뚱 서서 기다리고 있는 두 마리의 호랑이만 봐도 짐작할 수 있는 사실이었다.

크르릉. 크릉.

낮은 울음소리를 흘리는 무야호가 내게 묻는 듯하다.

자신이 어디로 가야 하느냐고. 가야 할 길을 정해 달라고.

눈처럼 새하얀 털로 뒤덮인 녀석의 커다란 머리는, 지금 이 순간에도 두 방향을 향해 번갈아 움직이고 있었다.

한 곳은 척후대가 향한 북서쪽. 그리고 다른 한쪽은.

‘……남동쪽.’

우득.

나도 모르게 힘이 들어간 주먹이 파르르 떨린다. 그런 내 모습을 바라보던 태산이 퉁방울만 한 눈동자를 껌뻑거렸다.

“각주. 왜 그러나?”

나는 태산에게 대답해 주고 싶었다. 별일 아니라고. 아무 일도 아니니까 마저 가던 길을 가자고.

하지만 달싹이는 입술 사이로 흘러나오는 목소리는 없었다.

‘이런 씨발.’

미처 토해 내지 못한 욕설이 입속에서 맴돈다.

망설일 이유는 없었다. 길은 이미 정해졌고, 맹수들의 이동 속도는 예상했던 것 이상으로 신속했다.

설령 날이 밝은 직후 천라지망(天羅蜘網)이 펼쳐진다 해도 지금의 몸 상태라면 어떻게든 남만을 빠져나갈 수 있을 것 같았다.

하지만…… 그럼에도 망설여지는 이유는 무엇일까.

‘내가 지금 이들과 함께 함께 남만을 떠난다면? 그 다음은 어떻게 되는 거지?’

마음속으로 스스로 던진 물음에 대한 답을, 나는 이미 알고 있었다. 어쩌면 백호의 등에 올라탄 그 순간부터였을지도 모른다.

‘설령 내가 다시 돌아온다 해도…… 그때는 이미 늦어 있겠지.’

최대한 신속하게 전력으로 추격대를 따돌리고, 백상의 주도하에 펼쳐진 천라지망을 벗어난다 해도 며칠. 다시 돌아오는 시간까지 합친다면 칠 주야다.

그때까지 우리를 구출하기 위해 나섰던 이들이 남아 있을까.

아니, 이번 일로 야수묘왕까지 위태로워졌다면 암천이 더 이상 흉계(凶計)를 망설일 이유가 있을까?

‘죽겠지. 수십, 수백. 어쩌면 수천 명도 넘는 사람들이.’

나는 천천히 눈을 깜빡였다. 감을 때도, 뜰 때도 세상은 여전히 어둠에 잠겨 있고 동은 틀 기미가 보이지 않는다.

‘시발. 훈련소 막 입소했을 때가 이랬는데.’

갑자기 떠오르는 생각에 나는 피식, 하고 헛웃음을 흘렸다.

다시 생각해 보니 훈련소 때가 가장 나았던 것 같기도 하다.

그때의 나는 무슨 똥을 싸질러도 용서받을 수 있는 위치였지만, 이제는 모든 것이 바뀌어 버렸으니까.

죽음의 위기도 수도 없이 겪었고, 죽어 가는 동료들을 뒤로하고 살아남은 적도 있다.

며칠 동안 방구석에 틀어박혀 병신처럼 질질 짜면서, 두 번 다시는 내 사람들을 잃지 않겠다고 맹세했었지.

그러던 어느 날 시스템을 얻었고, 정신을 차리고 주위를 둘러보니 책임질 것이 많아졌다.

세상에서 벌어지는 모든 일이 내 탓 같았고, 그 과정에서 죄없이 목숨을 잃는 사람들이 안타까웠다.

그리고 그럴 때마다 생각했다.

‘만약 내가 저 자리에 있었다면.’

하지만 지금은 헛웃음만 나온다.

내가 했던 그 생각들이 전부 가식과 위선이고, 영웅의 껍데기를 닮고자 했던 코스프레인 것만 같아서.

그래. 나는 협객도, 히어로 무비 속에 등장하는 영웅도 아니다.

그러나 오늘, 도주하는 내 뒷모습을 끝까지 바라보던 이들은 진짜 협객이고, 영웅이었다.



‘고마워할 필요 없소.’

‘그럼. 그저 남만이 당신에게 진 빚을 갚은 것뿐이지.’

‘애뇌산에 제 형이 있었습니다. 은공 덕분에 다시 만날 수 있게 되었지요.’

‘소궁주를 부탁하오.’



어둠 속을 스치는 수십여 명의 얼굴. 그들 중에는 젊은 청년도 있고 늙수그레한 중년인도 있었다.

그들의 실력? 만약 내가 작정하고 손을 쓴다면 촌각 안에 모조리 쓰러트릴 수 있다.

오히려 그렇기에 더욱 대단한 것이다.

승리하기 위해 온 것이 아니라, 죽기 위해 남은 것이니까.

이 모든 것이 이란격석(以卵擊石)이라 해도 그들은 물러서지 않을 것이다. 단단한 바위에 몸을 부딪치고, 끝내는 산산이 부서진다 하여도.

‘어쩌면 지금 이 순간에도.’

그리고 나는…… 그런 그들을 남기고 떠났다. 남은 자들의 최후를 직감하면서도 다시 돌아오리라는 헛된 다짐과 함께.

후우.

후텁지근할 때는 언제고, 이제는 심호흡 한 번에 새하얀 입김이 뿜어져 나온다.

다시 한번 느끼지만, 이놈의 남만은 참 좆 같은 땅이다. 지금 내 기분만큼이나.



- 퀘스트 임무를 선택하십시오.



허공에 떠 있는 홀로그램 창을 말없이 바라보던 나는, 이내 불쑥 입을 열었다.

“태산아.”

“응?”

“지금부터…….”

뒤이어 흘러나온 내 목소리에, 태산의 눈이 크게 뜨였다.



* * *



노인은 불현듯 눈을 떴다.

얼마나 의식을 잃었던 걸까. 뼈마디 곳곳이 쑤셨고, 거대한 맹수의 등에 묶인 몸은 쉼 없이 들썩이고 있었다.

‘호랑이?’

파파팟.

주위를 둘러보던 노인, 남호는 야율목의 계획이 성공했음을 알았다. 그리고 문득 이상한 점을 알아차렸다.

“……왜. 왜 그놈이 없지?”

의문이 담긴 늙수그레한 목소리에, 고개를 돌린 태산이 반응했다.

“남호. 일어났나?”

그러나 남호는 대답 대신 물었다. 불길한 직감이 가슴을 짓누르고 있었다.

“어디 있느냐.”

“……남호.”

“어디 있느냐고, 진태경 그놈!”

어스름히 밝아지는 동쪽 하늘과 달리 어두워지는 태산의 표정을 보며, 남호는 깨달았다.

자신이 느꼈던 불길함이, 결코 헛된 기우가 아니었다는 것을.
```

## Final English reading copy

```markdown
# Chapter 671

The place where I currently found myself—the Murim—had neither the dazzling scientific civilization nor the mechanical engineering of the modern world. Nor did it have magic.

But even this world was filled with special things scattered throughout it, things no less extraordinary than magic.

Murim people who accumulated internal energy and wielded power beyond that of Hunters. Countless kinds of martial arts unavailable in the modern world, along with mysterious and bizarre spiritual creatures and elixirs.

And… tracking scent was one of them.

Ding.

> **System**
>
> A Sudden Quest, **Yohi’s Tracking Scent**, has been generated!
>
> Would you like to open the Quest window and check its contents?
>
> **Y / N**

A System notification suddenly rang out. Faced with the unexpected situation, I nodded as if entranced.

Ding.

> **System**
>
> **Quest**
>
> **Yohi’s Tracking Scent**
>
> A new path has appeared before you as you flee from pursuit.
>
> Now, you must make a choice once more.
>
> However, you cannot know what awaits you at the end of the two roads before you. All that exists are the consequences of your choice—and the responsibility that comes with it.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Choose a direction to travel (Incomplete)
>
> **Reward:** Linked Quest
>
> **???**
>
> **Failure:** ???

*Goddamn it. What is this now?*

A holographic window filled the air before me.

At the same time, a short memory from barely a day ago flashed through my mind.

*Looks like they really went at it.*

*By the time I received the report, everything was already over. All that remained in the western Yao territory was blood and corpses. And… those things.*

I remembered everything from that day clearly. It was the only clue left behind by Heugung and Yohi, the two Great Chieftains who had vanished without a trace.

*Heugung’s wrist had been severed, and Yohi…*

That was right. She had left behind a scent pouch.

However, since I had only just arrived at the western Yao territory, I had focused on the wrist Heugung had left behind rather than the scent pouch.

If I could determine the traces of injury remaining on the severed wrist, I could at least roughly infer the opponent’s martial arts and level.

*Compared to that, Yohi’s scent pouch didn’t seem particularly important.*

The scent pouch had not even been intact. Made of silk, it had already been damaged, and the scent had escaped through a long tear in the fabric, leaving it almost odorless.

But I had not known.

No—given everything that happened one thing after another, no one had had the time to pay attention.

That it was the most important clue in the western Yao territory.

That it was a tracking scent Yohi had left behind so that someone could find her.

*The scent hadn’t escaped. It had been like that from the beginning.*

As far as I knew, tracking scent was an unusual object made for following someone’s trail, just as its name suggested.

It was by no means something commonly found, but it was not entirely unused, either.

Among the orthodox faction, for example, there were the Lower District Sect and the Beggars’ Sect.

And the fact that I had spent quite a lot of time with the Successor Beggar of the Beggars’ Sect—a man from an organization of truly enormous scale—and exchanged all kinds of stories with him had been an unexpected stroke of luck.

*Tracking scent. It’s definitely effective, but incredibly rare. The method of making it is highly secretive, too. There are only a few people in the Murim who can produce it.*

*Like the Ten-Thousand-Li Tracking Scent or something?*

*The Ten-Thousand-Li Tracking Scent? Hm. I guess even someone like you has picked up a thing or two somewhere.*

*Looks like about five of your teeth are going to fall out soon. Want me to pick those up for you too?*

*Oh. Ah…*

*Go on. Run your mouth some more.*

*Well, ahem. I’ve never actually seen the Ten-Thousand-Li Tracking Scent, either. Ten thousand li sounds impressive, but it’s hard to believe the scent could remain throughout a journey that long.*

*What? So it was a scam after all?*

*It isn’t necessarily that simple. Even if they aren’t as impressive as the Ten-Thousand-Li Tracking Scent you heard about through the grapevine, there are quite a few kinds of tracking scent actually used in the Murim. The highest grade among them is commonly called the Thousand-Li Tracking Scent.*

*The Thousand-Li Tracking Scent?*

*It has several distinguishing features. First, the manufacturing process is disgustingly difficult. Second, the manufacturing cost is disgustingly high. Third, acquiring the Thousand-Li Tracking Scent made that way requires a disgustingly large amount of gold.*

*No mistaking you for a fucking beggar. You can’t get through a sentence without working “filthy” in somewhere.*

*No matter how disgusting I am, your personality is still—*

*I’m sorry. That was a slip of the tongue. Anyway, tracking scent of that level is worth dozens of times its weight in gold. Of course, its effectiveness is just as certain.*

*For example?*

*Unlike the unverified Ten-Thousand-Li Tracking Scent, the scent of the Thousand-Li Tracking Scent really remains for about a thousand li, and it’s nearly odorless—so faint that even certain beasts with extremely developed senses of smell can’t detect it. Humans are out of the question.*

*What? Then wouldn’t applying tracking scent once solve everything?*

*The trade-off is that tracking scent lasts for seven days and nights at most. If the target burns their clothes or fully immerses themselves in water, for example, the duration will be shortened even if the scent doesn’t disappear entirely.*

*Even so, you’d have to know you’d been marked with tracking scent before you could try any of that. You said that even most beasts can’t smell it properly.*

*That’s right. But spiritual creatures are different.*

*Ah.*

*That’s why there are only two ways to pursue a target using tracking scent. Either you have someone who has mastered advanced tracking arts, or you lead a spiritual creature capable of smelling it.*

As I recalled the conversation I had once shared with Gung Gibang, I had no choice but to admit that everything he had said was true.

Grrr. Sniff, sniff.

Along with a low growl, the damp nose pressed against my palm kept twitching.

I looked down at White Tiger, who was licking my fingers with a rough tongue that stung slightly, and muttered,

“……Right. You’re here.”

A spiritual creature capable of smelling tracking scent.

Just as Gung Gibang had told me.

This White Tiger—Muyaho—was even a spiritual creature intelligent enough to understand and communicate with humans from a young age.

*Intelligence befitting a spiritual creature, and keen senses beyond those of an ordinary beast.*

Now that I thought about it, the scent pouch that had been nearly odorless had probably contained Thousand-Li Tracking Scent as well.

The highest-grade tracking scent, which supposedly lasted for seven days and nights as long as the target remained within a thousand li, barring any unusual circumstances.

I could tell that much just by looking at the two tigers standing there blankly and waiting, unlike Muyaho.

Grrr. Grrr.

Muyaho let out a low growl, as if asking me a question.

Where should he go? He wanted me to choose the path he should take.

The great head covered in snow-white fur moved back and forth between two directions.

One was northwest, where the reconnaissance squad had gone.

And the other was—

*……Southeast.*

Crack.

My clenched fist trembled.

Taishan, who had been watching me, blinked his eyes as big as saucers.

“Pavilion Master. Why?”

I wanted to answer Taishan.

*It’s nothing. Nothing’s wrong, so let’s just keep going.*

But no words came from between my parting lips.

*Fuck.*

The curse I could not bring myself to spit out lingered in my mouth.

There was no reason to hesitate. The road had already been decided, and the beasts were moving faster than I had expected.

Even if the net over heaven and earth spread the moment dawn broke, I felt that, in my current condition, I could somehow make it out of Nanman.

But… why, then, was I hesitating?

*What happens if I leave Nanman with them now? What comes after that?*

I already knew the answer to the question I had asked myself.

Perhaps I had known it from the moment I climbed onto White Tiger’s back.

*Even if I come back again… it’ll already be too late by then.*

Even if we did everything we could to shake off our pursuers and escaped the net over heaven and earth Baeksang had spread, it would take several days.

If I added the time needed to return, it would take seven days and nights.

Would the people who had set out to rescue us still be there by then?

No. If this incident had even put the Beast Miao King in danger, would Dark Heaven have any reason to hesitate before carrying out its sinister scheme?

*They’ll die. Dozens. Hundreds. Maybe even thousands of people.*

I slowly blinked.

Whether my eyes were open or closed, the world remained shrouded in darkness. There was still no sign of dawn breaking in the east.

*Fuck. It was like this when I first entered boot camp.*

The sudden thought made me let out a hollow laugh.

Thinking back, maybe those days at boot camp had been the best.

Back then, I had been in a position where I could be forgiven no matter what kind of shit I pulled.

But now, everything had changed.

I had faced the threat of death countless times. I had even survived while leaving dying comrades behind.

I had locked myself in my room for days, crying like an idiot, and sworn that I would never lose my people again.

Then, one day, I obtained the System.

When I came to my senses and looked around, I found myself with a great deal to be responsible for.

Everything happening in the world felt like it was my fault, and I pitied the innocent people losing their lives in the process.

And every time that happened, I thought,

*What if I had been there?*

But now, all I could do was laugh hollowly.

Because all those thoughts seemed like affectation and hypocrisy, like I had merely been cosplaying as a hero.

That was right.

I was neither a heroic martial artist nor some hero from a superhero movie.

But today, the people who had watched me flee until the very end were true heroic martial artists—true heroes.

*No need to thank us.*

*Of course. Nanman was only repaying the debt it owed you.*

*My hyung was on Ailao Mountain. Thanks to you, I can see him again.*

*Please take care of the Young Palace Lord.*

Dozens of faces brushed through the darkness.

Among them were young men and middle-aged men who were already growing old.

Their skill?

If I truly made up my mind to act, I could knock every one of them down within moments.

And that was precisely why they were even more remarkable.

They had not come to win.

They had stayed behind to die.

Even if all of this was nothing more than striking an egg against a rock, they would not retreat.

They would hurl their bodies against the solid stone, even if they were ultimately smashed to pieces.

*Maybe even right now.*

And I… had left those people behind.

Even knowing what fate awaited those who remained, I had gone with the empty promise that I would return.

Haa.

The air had been muggy just moments ago, yet now a single deep breath produced a cloud of white vapor.

I felt it again: this damn Nanman was a truly shitty land.

Almost as shitty as my mood.

> **System**
>
> - Select a Quest mission.

I silently stared at the holographic window floating in the air.

Then, abruptly, I spoke.

“Taishan.”

“Hm?”

“From now on…”

At the words that followed, Taishan’s eyes widened.

* * *

The old man suddenly opened his eyes.

How long had he been unconscious?

Every joint in his body ached, and the body tied to the back of a huge beast was bobbing without pause.

*A tiger?*

His gaze darted around.

Namho realized that Yayul Mok’s plan had succeeded.

And then he noticed something strange.

“……Why? Why isn’t that bastard here?”

At the old man’s voice, filled with confusion, Taishan turned his head.

“Namho. You awake?”

But Namho did not answer.

He asked instead, an ominous intuition pressing down on his chest.

“Where is he?”

“……Namho.”

“Where is he, I said! That Jin Taekyung bastard!”

Unlike the eastern sky, which was beginning to grow faintly bright, Taishan’s expression darkened.

And Namho realized that the ominous feeling he had sensed had not been an empty fear at all.
```
