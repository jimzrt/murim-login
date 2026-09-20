<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0527.txt",
      "sha256": "47b21f1ccd82a9f9bf5bafbe3350a324c7f310d7bdcca66c292828fba32ef548",
      "bytes": 13017
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "017530c038f9a049da40d27f93f0c3d434d0266a65e8214380c0b6b22085589a",
      "bytes": 3339
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf6e6d62a5df90bae233361ba869b69a1d3a480a540d6d13b2298cab7cdec8f9",
      "bytes": 168289
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "dff88a7c47d896703f5053d3765ed59ab9057d92b6a09b091a857c8a31f09b30",
      "bytes": 1006
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "175f0331c3d3f5d6c4f460f77075e91d4e135cc0cf20cce1954b98557992965e",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "63486ff2f64793ebcbe07cb980a9bffa02dee9ece23b888d027aad5ac5a9c60d",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ee17e0a7efd6a57082a3552de63a3289df1550b3d5eaf1e5e2bdab828ac62652",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "011f8c1feebe8cb8dbecbc17ad67ecde8474b382e5e1d5d05fcc3387063e94b5",
      "bytes": 2021
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "9647bb5f07f0f2810096eb38a1ada0034b8410875cfa3e9c7583587db4567fee",
      "bytes": 1210
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "972e219cd0c37bdd236e9b4bd74edee1dcd7821bbb5ab5776bf48caef45b1af7",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "084441990ac4c46dab5e9fc5f7b487e73a8a85362fbe9e0fcb97ae5cdd7668cc",
      "bytes": 985
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5055fd089787aa6ed7851e0569df53546ad0b97272966a57ddd5f2bcd686b8b4",
      "bytes": 158189
    }
  ],
  "estimated_tokens": 12959
}
-->

# Durable State Update — Chapter 527

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 527. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 527. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 527,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 527,
    "continuity_sources": [527],
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
    "The Murim Alliance was formally founded beneath its flag at Mount Song, and factions, wandering martial artists, reclusive masters, and veterans are mobilizing for war against Dark Heaven.",
    "Mungyeong recognizes Jin Taekyung as a new hero after seeing him carry the Murim Alliance flag.",
    "Jin Taekyung and Cheongpung are publicly regarded as the Two Dragons, above the Ten Dragons and Phoenixes among young prodigies.",
    "Reclusive masters and legendary veterans who had withdrawn from the martial world are returning to it in response to the coming conflict.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; he has ended Taekyung's direct training and assigned him a final task.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate, and Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "Mae Jonghak leads the formally inaugurated Murim Alliance, while Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Wudang's second report identifies Jang Sam as the Killing Ghost and links his transformation to the Blood Fish.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license."
  ],
  "continuity_sources": [
    526,
    525
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Did the Blood Fish cause Jang Sam's transformation, and could similar Blood Fish or Gate-related transformations occur elsewhere?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 526,
  "temporary_decisions": [
    "Render 숭산결의 as Mount Song Resolution and 이룡 as Two Dragons.",
    "Retain Ten Dragons and Phoenixes for 십봉룡 and Blazing Flame Divine Dragon for 열화신룡.",
    "Render 홍적 as Hong Jeok, 모용영휘 as Murong Yeonghwi, and 복마전 as demon-slaying battleground.",
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Retain the established renderings for Dark Heaven, Murim Alliance, Old Master, wandering martial artist, and the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남궁세가   | **Nangong Family**               |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 큰형     | **eldest brother**                           |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 소협      | **Young Hero**                                                  |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 산동악가 | **Shandong Yue Family** | Family to which Ak Bulgun belongs. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 숭산결의 | **Mount Song Resolution** | The event marking the formal gathering of the Murim Alliance at Mount Song. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 종남삼수 | 노호검객 | junior_Zhongnan_martial_artists_to_sect_elder | Elder | fearful-deferential | The Three Hands of Zhongnan plead with Song Il after he blames them for his humiliation. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 526
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 525
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 524
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 525
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 526
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 516
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 526
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 525
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
＃527화



세인들이 숭산결의(嵩山決意)라 부르는 그 날 이후로 어느덧 칠 주야가 흘렀다.

수많은 무림 군웅의 함성 아래 무림맹의 깃발은 다시 세워졌고, 수십 년 만에 무림맹이 정식으로 부활했다는 소식은 순식간에 하남을 넘어 천하 무림을 뒤흔들었다.

‘시간이 정신없이 흘러갔지.’

처음에는 나까지 바쁠 일이 뭐가 있겠냐 싶었지만, 그것이 안일한 생각이었다는 건 무림맹이 결성된 지 불과 반나절이 지나기도 전에 깨닫게 되었다.

“조장님. 아래에 손님이 찾아오셨다는데요.”

“찾아오신 것도 아니고 찾아오셨다는데요는 뭐야?”

“청 소협이 만두 사러 다녀오는 길에 만났대요. 아래에서 기다리고 계신다는데.”

“갑자기 만두 먹고 싶다. 그리고 안 만날 거야.”

“슬쩍 얼굴만 보고 왔는데, 귀한 분 같아요.”

“난 천한 놈이냐? 귀하게 돌려보내 드려.”

“제가 어떻게 그럽니까. 약속 잡고 오셨다던데.”

“뭔 개소리야. 내가 여기 와서 약속을 잡은 적이 없는데. 그리고 아는 사람이 몇이나 된다고.”

“그건 그러네요. 조장님 친구 없으시잖아요.”

“그래? 넌 목이 없어질 것 같은데.”

“음. 소가주님과 이야기하신 것 아닐까요?”

“이 자식은 이제 쫄지도 않네.”

“혁무진 삼 년이면 목숨이 세 개쯤 됩니다.”

“헛소리 그만하고 돌려보내. 아, 그런데 그 귀한 분이 정확히 누구냐?”

“어, 잠시만요. 물어보고 올게요.”

“그래라.”

그리고 느긋하게 내려간 혁무진은, 미친 듯한 속도로 다시 돌아왔다.

“고, 고, 공동파! 공동파 장문인!”

“당장 모셔! 모셔엇!”

아니, 형이 거기서 왜 나와.

무려 구파일방에 속한 공동파의 장문인을 시작으로, 이른바 무림의 명사(名師)라고 불리는 이들의 방문이 줄줄이 이어졌다.

이미 일면식이 있는 남궁세가의 가주는 물론이고 무림을 종횡하며 인연을 맺은 문파 및 세가의 인물들이 연이어 찾아오기 시작한 것이다.

물론 그보다는 새로 안면을 트기 위해 오는 이들이 압도적으로 많았지만.

“저기, 조장님.”

“……이번엔 또 누구야.”

“산동악가요. 가주님이 직접 왔던데요.”

“……정중히 모셔라.”

“귀주 무림에서도 대표로 사람을 보냈는데…….”

“……같이 모셔라.”

“아, 그리고 조장님.”

“……모셔.”

내가 이렇게 유명한 사람인 줄은 몰랐다. 아니, 정확히 말하자면 ‘이 정도까지’일 줄은 몰랐다고 해야 맞겠다.

그리고 정신없이 찾아오는 사람들과의 만남을 이어 가던 나는 결국 사흘 만에 탈진 상태에 이르렀다.

‘시벌, 못 해 먹겠다.’

차라리 예쁜 여자와의 소개팅이면 말도 안 하지.

하루에도 열 명이 넘게 찾아오는 아재와 할배들을 상대하다 보니 혼이 빠져나가는 기분이었다.

이제는 냄새만 맡아도 구역질이 올라오는 찻잔을 사이에 두고 나누는 이야기들도 대부분 엇비슷했다.

“오오, 자네가 말로만 듣던 바로 그 열화신룡이군!”

[진태경 대화 공략집].

뭐 그런 제목의 책이라도 한 권씩 읽고 오시는지 첫 마디가 하나같이 똑같다.

하지만 말 잘 듣는 어린애도 삐딱해지는 순간이 있는 법.

처음에는 애써 웃으며 의미 없는 말을 주고받던 나도 점점 솔직해졌다.

“자네에 관한 소문은 익히 들었다네.”

“저도 저에 관한 이야기는 익히 들었습니다.”

“무림에 젊은 영웅이 나타났구먼. 참으로 기쁜 일이야. 허허허.”

“제가 가장 기쁘네요. 하하하.”

“그나저나 내게 과년한 딸이 하나 있는데…….”

“제게는 과년한 형이 둘이나 있습니다.”

“어허, 이 사람! 이 자리에서 다짜고짜 딸을 들이밀다니, 제정신인가! 진 소협. 저 친구 말은 너무 귀담아듣지 마시게나.”

“괜찮습니다. 어차피 귀담아듣지 않아서요.”

“그러니 저 친구 말고, 내 얘기를 들어 보게.”

“이야, 전개가 이렇게 되네.”

“사실 내게도 딸이 하나 있다네. 자네 마음에도 쏙 들 거야.”

“마음에 안 든다는 것에 혁무진의 불알을 걸겠습니다.”

“무슨 소리! 불알, 아니 미녀를 마다하는 사내가 세상 어디에 있단 말인가!”

“미녀라면…… 혹시 따님이 많이 예쁩니까?”

“그걸 말이라고! 이미 복건 땅에서는 소문이 자자하지!”

“오. 오오.”

“모르는 사람이 없네! 지나가는 아무나 붙잡고 물어봐도 상관없어. 지금도 충분히 예쁘지만 오 년 후에는 필시 복건제일미가 될 게야!”

“오오오, 복건제일미…… 잠깐만요. 그런데 왜 오 년 후입니까?”

“열두 살일세.”

“나가.”

칠 주야라는 시간이 어떻게 흘러갔는지도 잘 기억이 나지 않을 정도다.

나를 방문하는 이들 중에는 이미 일면식이 있거나 그저 호기심에 찾아온 사람도 있었지만, 어떻게든 나나 태원진가와의 연결고리를 만들고자 하는 이들이 대부분이었다.

물론 그중에는 무림인이 아닌 이들도 포함되어 있었다.

“조장님. 중원상회라는 곳에서 뵙고자 청하는데요?”

“모셔, 가 아니라. 상회가 왜 날 찾아와? 큰형이면 몰라도.”

“글쎄요. 이유는 잘 몰라도 제 안목으로 봤을 때는 그리 나쁜 사람들 같지는 않습니다. 한번 만나 보시는 것도 괜찮으실 것 같은데요.”

“야.”

“예, 예?”

“너 이 새끼 중원상회에서 뒷돈 받았지.”

“헉! 그, 그걸 어떻게.”

“받은 거 싹 다 뱉어 내고 돌려보내라. 좋은 말로 할 때.”

이제는 하다 하다 혁무진에게 뇌물까지 찔러 주는 놈들까지 생겨났다.

지금까지 온 손님 중 대부분은 어지간하면 진위경을 통해 약속을 잡은 거라 울며 겨자 먹기로 만났었다.

나를 만날 수 있는 유일한 창구가 진위경이라는 것을 분명히 알고 있음에도 다이렉트로 찾아왔다는 건 보통 두 가지 경우를 의미했다.

‘이미 진위경 선에서 까일 만한 결격 사유가 있거나, 언제 찾아와도 될 만큼 신분이 대단하거나.’

물론 전자의 경우가 압도적으로 많았고, 그런 이들은 얕은 수작을 부리다가 내 얼굴도 못 보고 돌아가기 일쑤였다.

그들이 왜 이렇게까지 하냐. 물론 나는 갑자기 엄청난 관심이 내게로 쏟아지는 이유를 이미 짐작하고 있었다.

‘깃발 때문이지, 뭐.’

무림맹이 정식으로 선포되던 그 날, 나는 무림맹주로 취임한 매종학과 적천강, 그리고 청풍과 함께 무림맹의 깃발을 세웠다.

나로서도 상당히 감명 깊은 순간이긴 했지만 그다지 큰 의미를 두지는 않았었는데, 그 광경을 목격한 다른 사람들의 시선에는 엄청난 컬쳐 쇼크였던 모양이다.

‘하긴, 새파랗게 어린놈 두 명이 다른 어르신들을 다 제치고 스포트라이트를 받았으니 그럴 만도 한가?’

당시 단상 위에는 구파일방과 오대세가를 비롯한 명문 대파의 인물들이 즐비했다.

이놈의 무림은 21세기 두메산골처럼 인구 고령화가 극에 치달아서, 단상의 이름을 경로당이라고 붙여도 될 정도다.

어찌어찌 그 자리에 끼게 된 마흔 줄의 중년인들도 보이차 셔틀에 불과한데, 아직 약관을 벗어난 지 얼마 되지도 않은 나와 청풍이 무엄하게도 그 영광스럽고도 역사적인 순간에 끼어든 것이다.

그 놀라운 광경은 모두에게 신선한 충격을 준 것이 확실했다.

그리고 누군가는 저 어린놈들의 실력과 자격을 인정하며 고개를 끄덕인 반면, 어떤 누군가는 상당히 아니꼽게 받아들인 것 같았다.

‘예를 들면 종남파라든지.’

모르긴 몰라도 지금쯤 종남파는 배알이 잔뜩 뒤틀려 있을 거다.

가뜩이나 계속해서 악연을 맺어 왔던 나와 태원진가가 급부상을 시작했으니까.

종남파의 세 얼간이, 종남삼수로부터 시작된 악연은 태원진가의 원단 연회에 찾아와 깽판을 놓던 노호검객이 적천강에게 복날 개처럼 두들겨 맞으며 악화되었다.

그뿐인가. 장문인인 풍운검군과 함께 종남파 최고의 고수로 거론되는 태을무정검(太乙無情劍)이 내게 패배함으로써 아예 정점을 찍었다.

그토록 치욕을 당했으니 내가 주목받는 것을 보고 이가 갈렸을 것이다.

아마 지금쯤 어딘가에서 나와 태원진가, 그리고 적천강을 물고 뜯고 씹고 있을지도 모르지.

지금까지 봐 온 종남파의 인물들의 성격상, 설령 암천이랑 손을 잡는다고 해도 고개가 끄덕여질 정도다.

‘어이, 종남파.’

‘암천 어서 오고.’

‘무림맹도 탄생했는데 왜 이렇게 죽상이야.’

‘진태경이 꼴 받게 하잖아. 싯팔 어린놈의 새끼가.’

‘껄껄. 잠력단 한 대 할래?’

‘좋지. 한 대 말아 줘.’

상상이 간다. 상상이 가.

그래도 구파일방에 속한 유서 깊은 정파 문파인 만큼 미쳤다고 암천과 손을 잡겠냐 싶지만, 어떤 방식으로든 사사건건 태클을 걸어올 것이 분명했다.

‘아니, 근데 억울하네. 다들 왜 나한테만 몰려들어?’

갑자기 뇌리를 스치는 생각에, 나는 구석에서 미미쨩과 함께 꼼지락거리고 있는 쌀벌레, 아니 만두 벌레를 바라보았다.

“왜요, 은인?”

“세상에, 벌레가 말도 하네.”

“네?”

“아무것도 아냐. 그런데 청 소협. 왜 이렇게 한가해 보여? 사람들도 안 찾아오고.”

“저는 배부를 때는 다른 사람 안 만나요. 맛있는 거 안 가져와도 안 만나고요.”

잠시 생각하던 내가 재차 물었다.

“당신 항상 배부르잖아.”

“네, 그래서 아무도 안 만나요.”

“……어, 그래.”

넌 참 속 편해서 좋겠다.

어떻게 보면 천하 무림을 통틀어 가장 개썅마이웨이를 꼽으라면 청풍이 아닐까.

녀석은 숭산결의가 있던 날에도 무림맹 깃발 처음 세워 본다며 좋아서 방방 뛰었었다.

‘천재인가, 미친놈인가.’

아마 둘 다겠지. 음.

내심 그렇게 중얼거리고 있을 때, 청풍이 하품을 하며 입을 열었다.

“그리고 한가한 거 아닌데요. 지금 수련 중이에요.”

“아니 이건 또 무슨 참신한 개소리야.”

“진짠데. 보세요.”

어깨에 두르고 있던 천년독각사, 미미를 내려놓은 청풍이 앉은 채로 신형을 꿈틀거렸다.

“……그, 방해해서 미안한데. 혹시 벌레로 진화 중인 거야?”

“아뇨. 무공이에요.”

“무공?”

“네. 미미의 움직임을 보고 만들었어요.”

그런데 난 왜 전혀 무공처럼 안 보이지. 나는 진심을 담아 물었다.

“무공 이름이 혹시 꿈틀거리기나. 단단해지기. 뭐 그런 건 아니지?”

“아뇨. 보법인데요.”

“……그럼 일어나서 해야지. 이 인간아.”

“아, 그렇구나. 깜빡했어요.”

아니, 이걸 말해 줘야 안다고?

내가 잠시 할 말을 잃은 사이, 냉큼 자리에서 일어난 청풍이 걸음을 내디뎠다.

아니, 내디뎠다고 느낀 순간 녀석의 신형이 사라졌다.

솨아아악!

미세한 소음과 함께, 넓은 방의 끝에 도달한 청풍이 이를 드러내며 환하게 웃었다.

“짠. 어때요?”

“……!”

내가 방금 뭘 본 거지?

순간 등허리를 타고 소름이 쭉 솟구친다.

그야말로 유령 같은, 아니 한 마리의 뱀과 같은 움직임. 보법이 분명한데, 보법이 아니다.

청풍은 걷는 것이 아니라 미끄러졌다. 그것도 다른 누구도 아닌 내가 육안으로 간신히 확인할 정도의 빠른 속도로.

“미미의 움직임과 무공 이것저것을 섞어 봤어요. 이렇게 움직이면 저도 미미가 된 것 같아서 기분 좋아요!”

“……섞어?”

“이름은 미미보(美美步)예요! 은인도 한 번 배워 보실래요?”

진짜 미친놈이다. 여러 가지 의미로.

입을 벌린 채 청풍을 바라보던 나는 고개를 저었다.

“아니, 싫어.”

“아앗…….”

그리고 청풍이 시무룩해하던 그때, 문밖에서 혁무진의 목소리가 들려왔다.

“조장님. 손님이 찾아오셨는데요.”

손님? 더 찾아올 사람이 있었나?
```

## Final English reading copy

```markdown
# Chapter 527

Seven days and nights had passed since the day people called the Mount Song Resolution.

Amid the shouts of countless Murim heroes, the Murim Alliance’s flag had been raised once more. News that the Murim Alliance had officially been restored for the first time in decades spread beyond Henan in an instant, shaking the entire Murim world.

*Things have been moving at a frantic pace.*

At first, I had thought there was no reason for me to be particularly busy. But I realized how naïve that had been less than half a day after the Murim Alliance was formed.

“Captain. I hear there’s a visitor downstairs.”

“Why do you say ‘I hear he’s come to visit’ instead of just ‘he came to visit’?”

“Apparently Young Hero Cheong ran into him while he was out buying dumplings. He says he’s waiting downstairs.”

“I suddenly want dumplings. And I’m not meeting him.”

“I only caught a glimpse of him, but he looked like someone distinguished.”

“What, am I some lowborn bastard? Send our distinguished guest home with all due courtesy.”

“How could I do that? I hear he came after making an appointment.”

“What the hell are you talking about? I never made an appointment after coming here. And how many people do I even know?”

“That’s true. You don’t have any friends, Captain.”

“Really? Because it looks like you’re about to lose your head.”

“Hmm. Maybe they spoke with the Lesser Family Head?”

“This bastard doesn’t even flinch anymore.”

“Spend three years as Hyuk Mujin, and you wind up with about three lives.”

“Enough nonsense. Send him back. Ah, but exactly who is this important person?”

“Oh, wait a moment. I’ll go ask.”

“Go on.”

Hyuk Mujin went downstairs at a leisurely pace, then returned at a speed that could only be described as insane.

“K-K-Kongtong Sect! The Kongtong Sect Leader!”

“Bring him in at once! Bring him innnn!”

*No, seriously—why is hyung there?*

Starting with the Sect Leader of the Kongtong Sect, one of the Nine Sects and One Gang, a steady stream of those known as renowned masters of Murim came to visit.

The Family Head of the Nangong Family, whom I already knew, came in person. Then people from sects and families I had formed connections with while traveling across the Murim world began arriving one after another.

Of course, the vast majority were people coming to establish a new connection with me.

“Captain.”

“……Who is it this time?”

“The Shandong Yue Family. The Family Head came in person.”

“……Receive him with due courtesy.”

“A representative from the Murim world of Guizhou was sent as well……”

“……Bring him in too.”

“Oh, and Captain.”

“……Bring him in.”

I hadn’t realized I was this famous. No, to be precise, I hadn’t realized I was *this* famous.

As I continued meeting people who came rushing to see me, I reached a state of exhaustion after only three days.

*Fuck, I can’t keep doing this.*

I could understand if it were a blind date with a pretty woman.

But dealing with more than ten middle-aged and old men every day made me feel like my soul was leaking out through my ears.

The conversations we had over teacups that made me nauseous just from smelling them were mostly the same.

“Oh! So you’re the very Blazing Flame Divine Dragon I’ve heard so much about!”

*The Jin Taekyung Conversation Guide.*

I wondered if each of them had read a book with that title before coming, because their opening lines were exactly the same.

But even the most obedient child eventually has a moment when he starts acting up.

At first, I had smiled and exchanged meaningless pleasantries. But as time went on, I became more honest.

“I’ve heard many rumors about you.”

“I’ve heard plenty of stories about myself too.”

“A young hero has appeared in Murim. It’s truly wonderful. Ho ho ho.”

“I’m the happiest person of all. Ha ha ha.”

“Incidentally, I have a daughter of marriageable age……”

“I have two marriageable older brothers.”

“Good heavens, man! How dare you spring your daughter on someone out of nowhere like that? Are you in your right mind? Young Hero Jin, don’t take anything that fellow says too seriously.”

“It’s all right. I wasn’t listening closely anyway.”

“Then listen to me instead of him.”

“Wow. So this is how the conversation develops.”

“As a matter of fact, I have a daughter too. I’m sure you’ll like her.”

“I’ll stake Hyuk Mujin’s balls that I won’t.”

“What are you talking about? Balls—no, what man in the world would ever turn down a beauty?”

“If she’s beautiful…… Is your daughter very pretty?”

“Do you even have to ask? Her beauty is already famous throughout Fujian!”

“Oh. Ohhh.”

“There isn’t a single person who doesn’t know her! You could stop anyone passing by and ask them. She’s already pretty enough, but in five years, she’ll surely become the First Beauty of Fujian!”

“Wow, the First Beauty of Fujian…… Wait a moment. Why five years from now?”

“She’s twelve.”

“Get out.”

I could hardly remember how the seven days and nights had passed.

Some of the people who visited me already knew me, while others had come out of simple curiosity. But most of them were trying to form some kind of connection with either me or the Jin Family of Taiyuan.

And, of course, not all of them were martial artists.

“Captain. Someone from a place called Central Plains Commerce is asking to see you.”

“Bring them in—no, wait. Why is a trading company looking for me? Unless they’re after my eldest brother.”

“I’m not sure of the reason. But judging by my own eye for people, they don’t seem like bad people. It might be worth meeting them once.”

“Hey.”

“Yes, yes?”

“You bastard. You took a kickback from Central Plains Commerce, didn’t you?”

“Gasp! H-How did you know?”

“Spit back out every last bit of it and send them away. While I’m still asking nicely.”

Now there were even people slipping bribes to Hyuk Mujin.

Most of the visitors who had come so far had arranged their appointments through Jin Wikyung, and I had met them despite myself because turning them away would have been awkward.

The fact that they knew Jin Wikyung was the only way to meet me and still came directly meant one of two things.

*Either they had already been rejected by Jin Wikyung for some disqualifying reason, or their status was important enough that they could come whenever they pleased.*

The first case was overwhelmingly more common. Those people would try some shallow trick and often leave without even seeing my face.

Why were they going this far?

I already had a pretty good idea why all this sudden attention was being focused on me.

*It’s because of the flag, obviously.*

On the day the Murim Alliance was officially proclaimed, I had raised the Murim Alliance’s flag together with Mae Jonghak, who had taken office as Alliance Leader, Jeok Cheongang, and Cheongpung.

It had been a deeply moving moment for me as well, but I hadn’t attached that much meaning to it. To everyone else who had witnessed it, however, it seemed to have been an enormous culture shock.

*Well, I suppose it makes sense. Two fresh-faced young punks had stolen the spotlight from all the elders.*

At the time, the platform had been packed with people from prestigious great sects, including the Nine Sects and One Gang and the Five Great Families.

Murim had reached such an extreme level of population aging that I could have called the platform a senior center and no one would have objected.

Even the middle-aged men in their forties who had somehow managed to squeeze onto the platform were nothing more than pu'er tea runners. And yet Cheongpung and I, who had only recently passed the age of twenty, had audaciously inserted ourselves into that glorious, historic moment.

That astonishing sight had clearly given everyone a fresh shock.

Some people had nodded, acknowledging the ability and qualifications of those two young punks. Others seemed to have found it extremely irritating.

*The Zhongnan Sect, for example.*

I couldn’t be certain, but by now the Zhongnan Sect’s guts were probably twisted with resentment.

After all, the Jin Family of Taiyuan and I, who had been locked in a bad relationship with them for so long, had begun rising rapidly.

The bad blood had started with the Three Hands of Zhongnan, the three idiots of the Zhongnan Sect. It had worsened when the Roaring Fury Swordsman came to the Jin Family of Taiyuan’s New Year’s Day banquet and caused a scene, only to be beaten by Jeok Cheongang like a dog on the hottest day of summer.

And that wasn’t all. The feud had reached its peak when the Taeeul Merciless Sword, regarded alongside the Sect Leader Wind-and-Cloud Sword Lord as the Zhongnan Sect’s greatest master, was defeated by me.

After suffering such humiliation, they must have ground their teeth at the sight of me receiving attention.

For all I knew, they might be somewhere right now biting, tearing, and chewing on me, the Jin Family of Taiyuan, and Jeok Cheongang.

Given the personalities of the Zhongnan Sect’s people I had seen so far, I could almost believe it if they joined hands with Dark Heaven.

*Hey, Zhongnan Sect.*

*Dark Heaven, come on in.*

*The Murim Alliance was born. Why do you all look so miserable?*

*Jin Taekyung is pissing us off. That fucking brat.*

*Ho ho ho. Want a hit of a Temporary Strength Pill?*

*Sure. Roll me one.*

I could picture it perfectly. I really could.

Still, they belonged to one of the Nine Sects and One Gang and were a venerable orthodox sect. Surely they wouldn’t actually be insane enough to join hands with Dark Heaven.

But they were certain to interfere at every turn in one way or another.

*No, but this is unfair. Why is everyone swarming me?*

At that thought, I looked toward the freeloader—or rather, the dumpling grub—fidgeting in a corner with Mimi-chan.

“Why, Benefactor?”

“Good heavens, the bug talks.”

“Pardon?”

“Nothing. But Young Hero Cheong, why do you look so free? No one comes to see you.”

“I don’t meet people when I’m full. I don’t meet them if they don’t bring delicious food either.”

After thinking for a moment, I asked again.

“You’re always full.”

“Yes. So I don’t meet anyone.”

“……Right.”

*Must be nice to have such an easy life.*

If I had to pick the person in all Murim who gave the fewest fucks and did exactly as he pleased, wouldn’t it be Cheongpung?

Even on the day of the Mount Song Resolution, he had bounced around excitedly because it was his first time raising the Murim Alliance’s flag.

*Is he a genius or a lunatic?*

Probably both. Hmm.

I was muttering that to myself when Cheongpung yawned and opened his mouth.

“And I’m not free. I’m training right now.”

“What fresh bullshit is this?”

“I’m serious. Look.”

Cheongpung took the Thousand-Year Poison Horned Snake, Mimi, off his shoulder and began squirming while still seated.

“……Sorry to interrupt, but are you evolving into a bug?”

“No. It’s martial arts.”

“Martial arts?”

“Yes. I made it after watching Mimi’s movements.”

Then why did it look absolutely nothing like martial arts?

I asked with complete sincerity.

“Is the name of this martial art something like Squirming or Toughening Up?”

“No. It’s a footwork technique.”

“……Then you should stand up and do it, you idiot.”

“Oh, right. I forgot.”

Did I really have to tell him that?

While I was briefly rendered speechless, Cheongpung promptly rose from his seat and took a step.

Or rather, the moment I felt him take a step, his figure disappeared.

Whoosh!

With only the faintest sound, Cheongpung reached the far end of the spacious room. He showed his teeth in a bright grin.

“Ta-da. What do you think?”

“……!”

*What did I just see?*

Goose bumps raced up my back.

It was a ghostlike movement—or rather, the movement of a snake. It was clearly a footwork technique, but it was not like any footwork technique I had ever seen.

Cheongpung hadn’t walked. He had slid.

And he had done it at a speed so fast that even I could barely track him with my naked eyes.

“I mixed Mimi’s movements with bits and pieces of different martial arts. When I move like this, I feel as if I’ve become Mimi too, so it makes me happy!”

“……You mixed them?”

“Yes. The name is Mimi Step! Would you like to learn it too, Benefactor?”

*He really is insane.*

In more ways than one.

I stared at Cheongpung with my mouth hanging open, then shook my head.

“No. I don’t want to.”

“Aww……”

Just as Cheongpung’s shoulders drooped, Hyuk Mujin’s voice came from outside the door.

“Captain. There’s a visitor here.”

*A visitor? Was there anyone else left who could come see me?*
```
