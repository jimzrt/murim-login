<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0708.txt",
      "sha256": "78ec3fb2b2c39f9b1639bc120f72d47f00e21155c4728eec635c10288987f91c",
      "bytes": 13052
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b248ec149facaada8efb209998cbfa35bf4eb7f69e88ec1008aeef604f75a8cf",
      "bytes": 1775
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c1986676bc48fdff4fd48cf0f0b57f97ebad0bdfdd8467f01fb8d3155af76b6e",
      "bytes": 207119
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "1e9f7e3c1684ebc952a843eb694b6073158ea00b2ad24222a6096457e632c47a",
      "bytes": 959
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "2d842ccb0d4b00ba7a3b7e200cb2b6f2e044ca175f7dee19f534e3fd050f75ac",
      "bytes": 913
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f170e1b2715c26293728570eb51b1ce88d6fc5273ac31c1e5bf56ef0162a257a",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e7e3bd5792c2f175c5c425e598e3cc7f4294d2b5c84c3c82ac86b27a4ae18424",
      "bytes": 1920
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7245cdc942fdc34c3730446d0b28d6ba74b2cc4c93267a418dc1ef39b5cc7449",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "6e331e24d35f4adc302a88db062c6926dd3689af4d8503994ebe83565e6535ad",
      "bytes": 667
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "1d9bdc814347c8c80b2cea79e3729b54446b155ddd4e6c02c09e2602ed5d46fd",
      "bytes": 854
    },
    {
      "path": "characters/Wang Ho.md",
      "sha256": "095f9b22fa90cf954cb8f70cf3ad13f30b4662aa6d2420da055461499518b1a8",
      "bytes": 489
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "42b9ef3fd20fdea57c5abc716007013adf3178812be39e80fea9bfe9555594be",
      "bytes": 603
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "46634c3058e8caa3e27a8ba78c44c42aff24c33f97c44d4c2c394ac611ade854",
      "bytes": 899
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "42950db70eda092711a593f9c9aa4cb9b9033ef6021c552aa6f10c5e22ea2c95",
      "bytes": 621
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6f15dee36d5a032caa90af77c98394a0c535306a63b90c78ecec925d6c2845d1",
      "bytes": 217728
    }
  ],
  "estimated_tokens": 12817
}
-->

# Durable State Update — Chapter 708

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 708. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 708. Profile updates may replace only one
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
  "chapter": 708,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 708,
    "continuity_sources": [708],
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
    "The Southern Heaven Demon Empress is severely injured and exhausted after Jin Taekyung's earlier attack and the Beast Miao King's assault.",
    "The Beast Miao King, Jin Taekyung, and the guardian spirit have surrounded the Southern Heaven Demon Empress and launched a coordinated final attack.",
    "The masked man is crushed beneath a boulder but remains capable of twitching and may still recover abnormally.",
    "The Southern Heaven Demon Empress has awakened her innate qi through the rift, twisting the surrounding space.",
    "An unidentified sword has stabbed the Southern Heaven Demon Empress from behind through the ruins.",
    "The Southern Heaven Demon Empress still wants to survive so she can resume her grand plan and revenge elsewhere.",
    "The Nanman battle appears to have ended, with the Southern Heaven Demon Empress's forces defeated or unable to reverse the situation."
  ],
  "continuity_sources": [
    707
  ],
  "open_questions": [
    "Who wielded the sword that stabbed the Southern Heaven Demon Empress?",
    "What effect will the awakened innate qi have after the sword strike?",
    "Will the Southern Heaven Demon Empress survive the combined attack and the sword wound?",
    "Will the masked man recover after being crushed beneath the boulder?"
  ],
  "safe_through": 707,
  "temporary_decisions": [
    "Retain One Annihilation, White Flame, Fist Force, Finger Qi, Internal Injury, demonic qi, innate qi, and mental strength.",
    "Render 천녀 as lowly woman in the Southern Heaven Demon Empress's prayerful internal monologue.",
    "Preserve the Southern Heaven Demon Empress's title as Southern Heaven Demon Empress and her devoted address to 천주 as Lord of Heaven."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 십왕     | **Ten Kings**       |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 왕호 | **Wang Ho** | Commander of the Baekcheon Unit who arrives leading white-armored reinforcements. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 백천대주 | **Commander of the Baekcheon Unit** | Title used for Wang Ho. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 요희 | 무야호 | human ally to intelligent spiritual beast | you | casual and familiar | Yohi asks Muyaho whether it wants her to ride on its back. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 진태경 | 무야호 | human ally to intelligent spiritual beast | Muyaho | quiet and familiar | Jin whispers that they should go as Muyaho advances with the guardian spirit. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 백상 | 중년인 | Nanman Palace Lord to civilian tribesman | you | controlled and grave | Baeksang orders the middle-aged man to flee with his mother and the other civilians through the East Gate. |
| 중년인 | 백상 | Nanman civilian to betrayed Palace Lord | you | hostile, fearful, and grieving | The middle-aged man confronts Baeksang while protecting his mother and condemns him for the deaths and destruction. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 왕호 | 야수묘왕 | Baekcheon Unit Commander to Nanman Beast Palace Palace Lord | Palace Lord | formal and deferential | Wang Ho bows and formally reports his arrival to the Beast Miao King. |
| 왕호 | 진태경 | baekcheon_unit_commander_to_allied_combatant | you | formal and concerned | Wang Ho catches Jin as he begins to fall and tells him to stop because the battle is over. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 705
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman; he secretly raised a three-hundred-warrior Bai unit in Wenshan, entrusted its mobilization token to Yayul Cheok, and left a final instruction to oppose Dark Heaven.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 707
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people; he has overwhelmed the Southern Heaven Demon Empress and now attacks her alongside Jin Taekyung and the guardian spirit.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 707
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 707
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license; despite severe injuries, he is advancing with the guardian spirit and the Beast Miao King to kill the Southern Heaven Demon Empress.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 707
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 700
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature advancing with Jin Taekyung, Yohi, and the beast army.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 707
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; after being overwhelmed by the Beast Miao King and surrounded by Jin Taekyung and the guardian spirit, she awakens her innate qi but is stabbed from behind by an unidentified sword.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Wang Ho.md

# Wang Ho (왕호)

- **Safe through:** Chapter 706
- **Aliases:** None
- **Role:** Wang Ho is the Commander of the Baekcheon Unit and leads its three hundred white-armored Bai warriors and beasts under Yayul Cheok.
- **Personality:** Not established.
- **Voice:** Formal and deferential when addressing the Palace Lord.
- **Relationships:** He commands the Baekcheon Unit and acknowledges Yayul Cheok as its Palace Lord.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 707
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone and leads the Sacred Land beasts, but both the stone's power and the White Tiger's strength are weakening under the rift's demonic qi.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 705
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty former Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 698
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people who has returned to the Nanman Beast Palace with Jin Taekyung and now stands against Baeksang.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃708화



푹!

귓가를 파고드는 선명한 파육음과 함께, 남천마후를 둘러싼 세상이 멈췄다.

등허리를 깊숙이 파고든 서늘한 날붙이의 감촉만이 생생했다.

왜. 누가. 어떻게.

아득한 고통 속, 뇌리를 가득 채운 수많은 의문들.

동시에 이성보다 앞선 본능이 몸을 움직인다. 섬전과도 같은 속도로 돌아선 남천마후가 일장(一掌)을 뻗었다.

후웅!

선천지기(先天地氣). 손에 담겨 있던 미증유의 공력 중 일부가 허물어진 잔해더미를 후려친 순간.

콰아아앙!

거대한 굉음과 함께 수천, 수만 근에 달하는 잔해가 폭발하듯 터져 나갔다.

그리고 그 무수한 파편들 사이에, 앞서 남천마후가 떠올렸던 의문에 대한 답이 숨어 있었다.

“커헉!”

폭발의 여파에 휩쓸려 힘없이 튕겨 나가는 한 사람의 신형.

피와 먼지로 더럽혀진 백의(白衣)의 한쪽 소매는 텅 비어 있었고, 회생불능의 상처를 입은 가슴의 상흔에서는 핏물이 울컥거리며 쏟아졌다.

그러나…… 차갑게 가라앉은 눈빛은 끝까지 남천마후를 노려보고 있었다.

가늠키 힘든 분노와 후회로 점철된 눈동자가 그녀에게 속삭이는 듯했다.

아주 오랫동안, 이 순간만을 기다려 왔다고.

“백상……!”

비명처럼 튀어나온 한 사람의 이름. 그와 동시에 남천마후는 등 뒤로 덮쳐 오는 바람을 느끼며 눈을 부릅떴다.

슈화아아악!

예기치 못한 일격으로 소모된 시간은 한순간에 불과했다.

하지만 눈 한번 깜빡거릴 그 찰나의 순간은, 다른 누군가에게는 득이 되었고 남천마후에게는 독이 되었다.

으득.

끈적한 핏물을 삼킨 남천마후는 섬광과도 같은 속도로 등허리에 박힌 검을 뽑아내며 돌아섰다.

돌풍처럼 불어닥친 세 존재가 그곳에 있었다.

야수묘왕, 수호령. 그리고 진태경.

그들의 모습을 본 순간 백상의 일격으로 진탕된 내부의 기혈(氣穴)이 몸부림쳤다.

생명을 장작 삼아 피워올린 동귀어진(同歸於盡)의 불꽃이 바람 앞의 촛불처럼 흔들리는 것이 느껴진다.

재차 엄습해 오는 통증과 흐릿해진 시야.

그러나 멈출 수 없다. 멈춰서도 안 된다.

필살(必殺).

오직 그 일념 하나로, 남천마후는 이를 악문 채 손을 뻗었다.

어느덧 눈앞까지 들이닥친 세 개의 신형을 향해, 감히 존귀하신 천주(天主)께서 이루시고자 하는 대업에 걸림돌이 될 적들을 향해.

고오오오옹.

느려진 세상 속, 미증유의 기운이 피에 젖은 손아귀를 타고 검신으로 흘러들었다. 주인을 바꾼 검이 비스듬히 내리그어진다.

쏴아아악!

그리고 남천마후는 볼 수 있었다.

일그러지는 공간 너머에서 서서히 커지는 세 쌍의 눈동자와, 모두를 보호하듯 철벽처럼 솟구치는 녹색의 강기를.

하지만…….

‘끝이다.’

들리지 않을 남천마후의 뇌까림과 함께, 아득한 섬광이 모든 것을 집어삼켰다.

화아아악!



* * *



그것은 이 땅의 누구도 본 적 없는, 거대한 폭발이었다.

화악, 구구구궁!

수많은 맹수와 함께 살아남은 이들을 대피시키던 요희와 무야호도.

한껏 피를 머금은 병장기를 곧추세운 채 어둠이 드리워진 내궁을 포위하고 있던 수천의 전사도.

그리고 숨을 헐떡이며 외궁 밖 언덕을 향해 내달리던 부족민들도 그 광경을 보았고, 어떤 단어를 떠올렸다.

경천동지(驚天動地).

그렇게밖에 표현할 수 없었다. 아득한 섬광과 거센 진동은 내궁을 넘어 멀리, 끝없이 전해졌고 그 힘을 느낀 모두는 얼어붙었다.

아니, 영혼까지 옭아매는 두려움에 몸을 떨었다.

“아, 아아……!”

곳곳에서 흘러나온 신음은 오직 한 방향. 그들이 떠나온 남만야수궁을 향하고 있었다.

쿠궁. 쿠구궁.

무너진다.

오랜 세월 선조들이 피땀 흘려 쌓아 올린 전각과 가옥이, 그들이 일평생을 나고 자란 삶의 터전이 눈앞에서 무너지려 하고 있었다.

더 이상 무슨 말이 필요할까.

수천, 수만 쌍의 넋 나간 시선이 남만야수궁을 향했다.

정든 고향의, 이제는 돌아갈 수 없을 그곳의 마지막 모습을 눈에 담기 위해서.

그러나 그들의 눈앞에 드리워진 짙은 절망은, 얼마 지나지 않아 희망으로 바뀌었다.

드드드득…….

서서히 잦아드는 진동. 남만야수궁을 통째로 집어삼킬 것처럼 붕괴하던 지면도 움직임을 멈추었고, 금방이라도 쓰러질 듯 휘청이던 가옥과 전각은 단지 기우는 것에 그쳤다.

상상할 수 없던 재앙. 그리고 뒤이어 찾아온 기적.

이 믿을 수 없는 광경을 지켜본 사람들은 안도와 기쁨에 젖었고, 한낱 인간의 몸으로 재앙을 일으킨 누군가는 고통과 분노로 몸을 떨어야 했다.

“이, 이건 말도…… 쿠에에엑!”

투두둑.

입가를 타고 검붉은 핏물이 흘러넘친다.

반경 오십 장 안의 모든 것을 산산조각 내어 저 멀리 날려 버린 공허한 공간 속. 남천마후는 혈광(血光)이 가득한 눈으로 주위를 둘러보았다.

단 일격이었고, 한 번뿐인 확실한 기회였다.

설령 자신이 죽는다 해도 상관없었다. 이미 살아서는 돌아갈 수 없고, 살아간다 해도 이 늙고 추악한 모습으로 남은 생을 살아야 했을 테니까.

그런데…… 살아남았다.

모든 것을 집어삼키며 폭사(爆死)해야 했을 자신이. 이토록 치욕스럽게 살아남았다.

“백상! 네놈이. 네놈이 감히!”

드드득!

끔찍한 분노가 담긴 포효와 함께 터져 나온 기파(氣波)가 공간을 뒤흔들었다.

예기치 못했던 백상의 일격.

아마도 남은 힘을 쥐어 짜내어 뻗었을 그 검 한 자루가 모든 것을 뒤틀었다.

순간 뒤엉킨 기혈로 인해 남천마후는 자신의 모든 선천지기를 일격에 담지 못했고, 덕분에 폭사를 면했으나 그것은 ‘놈들’ 역시 마찬가지였다.

“쿨럭.”

쿵.

수십 장 밖, 반백의 거한이 내장 조각이 섞인 핏물을 토해 내며 한쪽 무릎을 꿇는다.

전신에 무수한 파편을 박아 넣은 그의 넓은 등 뒤로, 핏물을 흠뻑 머금은 채 쓰러져 있는 거대한 백호와 한 청년의 모습이 남천마후의 눈에 비쳤다.

“야율척, 네놈……!”

피 가래가 끓어오르는 목소리와 함께, 남천마후의 눈앞에 마지막 순간 보았던 야수묘왕의 모습이 스쳐 지나갔다.

마지막 순간. 한 치의 망설임도 없이 진태경의 앞을 막아섰던 그의 모습이.

‘도대체 왜?’

이해할 수 없었다. 야수묘왕 야율척. 머나먼 중원 땅에서 십왕(十王)이라는 위명을 얻은 그가 어째서 그런 선택을 했는지.

그리고 그것은 저 노린내 나는 짐승 역시 마찬가지였다.

‘하나뿐인 목숨을 걸어? 그것도 한낱 애새끼를 위해서?’

의문과 동시에 한 가지 확신이 남천마후를 사로잡았다.

진태경. 저놈만큼은 무슨 수를 써서라도 죽여야 한다.

일국(一國)의 왕이나 다름없는 남만야수궁의 궁주가, 신물을 지닌 백호가 놈을 위해 목숨을 걸었다는 것은 이 자리에서 가장 위험한 가능성을 품은 존재라는 뜻이니까.

그리고 남천마후에게는, 아직 미처 쏟아 내지 못한 선천지기가 남아 있었다.

생명을 불태워 얻은 마지막 힘이.

‘천주시여. 감히 당신의 뜻을 거스르려 하는 이 불충한 종복을, 부디 용서하소서.’

저벅.

마음속으로 낮게 읊조린 남천마후가 무겁게 걸음을 뗀 그 순간, 날카로운 파공성이 울려 퍼졌다.

쉭, 콰득!

어디선가 날아온 한 자루의 창이 남천마후의 손아귀에서 파르르 몸을 떨었다.

강철로 이루어진 창날을 맨손으로 부수어 버린 그녀가 혈광을 빛냈다.

“모조리 죽고 싶으냐?”

스산한 목소리가 향한 곳에는, 갈기갈기 찢어지다시피 한 갑주를 걸친 한 중년인이 우뚝 서 있었다.

아니, 그는 혼자가 아니었다.

투둑. 툭.

이미 초토화된 공간 속, 비틀거리며 몸을 일으킨 백여 명의 전사들이 검과 창을 굳게 말아쥐고 중년인의 뒤에 결집했다.

비교적 뒤에 있었음에도 하나 같이 크고 작은 상처를 입은 그들은, 자신들에게 주어진 사명을 다하기 위해 남천마후를 가로막았다.

철벅.

피 웅덩이에 처박힌 무언가를 들어 올려 이마에 질끈 동여맨 중년인이 담담한 눈빛으로 남천마후를 응시한다.

낡은 비단에는 핏물로도 감출 수 없는 세 글자가 적혀 있었다.

백천대(白天隊).

그것이 앞서 들려 온 물음에 대한 중년인의, 백천대주 왕호의 대답이었고 살아남은 백천대원 모두의 의지였다.

그리고 다음 순간.

쐐애애애액! 콰앙!

남천마후라 불리는 악귀(惡鬼)가, 그들을 향해 달려들었다.



* * *



섬광. 그리고 폭발.

그것이 내 머릿속에 남아 있는 마지막 기억이었고, 다음에 눈을 떴을 때는 모든 것이 끝나 있을 거라고 생각했다.

살았거나. 혹은 죽었거나.

전투의 결과는 언제나 그 두 가지뿐이다.

하지만 짧은 어둠을 지나 불현듯 눈을 뜬 순간, 나는 그 생각이 절반만 맞았음을 깨달았다.

나는 살아남았지만, 전투는 아직 끝나지 않았다.

콰드드드득!

“끄아아아!”

“어서 막……!”

서걱!

“안 돼애!”

잠시 멀어졌던 감각이 돌아옴과 동시에, 나는 볼 수 있었다.

하늘 위로 흩뿌려지는 핏물과 솟구치는 사지. 그리고 거대한 힘에 짓눌려 피곤죽이 된 채 튕겨 나오는 누군가의 몸뚱어리를.

후우웅, 쾅!

투둑.

불과 몇 걸음 옆에서 터져 나온 핏물이 얼굴에 튀었다.

가슴 한복판이 뻥 뚫린 채 숨이 끊긴 전사를 멍하니 바라보던 그때, 힘없는 목소리가 귓가에 닿았다.

아니, 그것은 누군가의 의념(意念)이었다.

- 인간.

그제야 깨달았다. 지금 내 등을 받치고 있는 것이 무엇인지. 그리고 이 따스한 온기가 누구의 것인지.

그리고 다음 순간. 콧속 깊숙이 스며드는 짙은 혈향(血香)을 느끼며 고개를 돌린 나는 할 말을 잃었다.

“……!”

깊은 피 웅덩이 속에서 간헐적으로 떨리는 거대한 동체.

신비롭게까지 느껴지던 은빛 털은 핏물에 흠뻑 젖어 있었고, 청백색의 눈동자는 나를 향해 힘겹게 깜빡이고 있었다.

- 오래도 자는군.

“……이게 무슨.”

- 후회하지 않는다. 나도, 그도.

불현듯 한 가지 기억이 떠올랐다. 아득한 섬광이 시야를 물들이던 그 순간, 눈 앞을 가리던 녹색 강기와 은빛 갈기가.

‘설마.’

언제나 그렇듯, 불길한 예상은 빗나가지 않았다.

고개를 돌리기 무섭게 한 사람의 커다란 등이 보인다.

혈인(血人)이나 다름없는 모습으로 한쪽 무릎을 꿇은 그는, 야수묘왕 야율척은 이미 의식을 잃은 상태였다.

전신에 빼곡히 틀어막힌 검신의 파편은, 아마도 누군가를 대신하여 막아 낸 것이리라.

“이런 미친. 도대체 왜……!”

- 가라.

“뭐?”

- 어서 떠나라. 시간이 없다.

말문이 막힌 나를 향해, 힘겹게 고개를 움직인 수호령이 무언가를 뱉어 냈다.

스아아아.

어느새 어린아이 주먹만큼이나 작아진 신석(神石)이 희미한 빛을 내뿜는다.

수호령의 뜻을 알아차린 내가 이를 악물었다.

“개소리……하지 마.”

- 저들마저 쓰러진다면 그 다음은 너다. 그러나 도망친다면 충분히 살 수 있어.

드드드득!

“끄아아아악!”

지축이 흔들림과 동시에 또 다른 누군가의 비명이 뒤를 잇는다.

전신의 핏줄이 도드라진 채, 마지막 생명을 불태우며 일백이 넘는 백천대를 찢어발기는 남천마후의 모습이 시야에 들어왔다.

“……!”

그 압도적인 힘 앞에 오한이 엄습한다. 순간 얼어붙은 나를 향해, 수호령이 힘주어 속삭였다.

- 가라. 어서!

안다. 수호령의 말이 옳다는 것 정도는.

남천마후에게는 남은 시간이 그리 많지 않고, 혼자서라도 도망친다면 충분히 살아남을 수 있을 것이다.

하지만…….

‘평생을 후회하겠지.’

멍하니 중얼거린 나는 신석을 잡았다. 그리고 몸을 일으켜, 달려 나갔다.

외궁이 아닌, 남천마후를 향해.
```

## Final English reading copy

```markdown
# Chapter 708

Thwack!

Along with the clear sound of flesh being pierced that bored into her ears, the world surrounding the Southern Heaven Demon Empress came to a halt.

The only thing she could vividly feel was the cold blade driven deep into her back.

Why? Who? How?

Countless questions filled her mind amid the distant agony.

At the same time, instinct moved her body before reason could. The Southern Heaven Demon Empress spun around at lightning speed and thrust out a palm.

Whoosh!

Innate qi. The moment some of the unprecedented internal energy held in her hand struck the collapsed ruins—

Kraaaaaaash!

With a tremendous roar, tons upon tons of rubble exploded outward.

And hidden among those countless fragments was the answer to the questions the Southern Heaven Demon Empress had just asked herself.

“Kugh!”

A figure was helplessly flung away in the aftermath of the explosion.

One sleeve of the white robe, stained with blood and dust, hung empty. Blood gushed from the wound in his chest, an injury beyond recovery.

But his cold, steady gaze remained fixed on the Southern Heaven Demon Empress until the very end.

His eyes, filled with an immeasurable mixture of rage and regret, seemed to whisper to her.

*I’ve been waiting for this moment for a very long time.*

“Baeksang…!”

A single name burst from her lips like a scream.

At the same time, the Southern Heaven Demon Empress’s eyes widened as she felt the wind sweeping toward her from behind.

Shwaaaaaak!

The time lost to the unexpected attack had been no more than an instant.

But that brief moment—the span of a single blink—had benefited someone else and become poison to the Southern Heaven Demon Empress.

Crack.

Swallowing the sticky blood in her mouth, the Southern Heaven Demon Empress spun around while pulling the sword embedded in her back free at lightning speed.

Three beings swept toward her like a sudden gale.

The Beast Miao King, the guardian spirit, and Jin Taekyung.

The moment she saw them, the qi and blood within her, already thrown into turmoil by Baeksang’s attack, convulsed.

She could feel the flame of mutual destruction, kindled by burning her own life as fuel, flickering like a candle in the wind.

Pain surged through her again, and her vision blurred.

But she could not stop. She must not stop.

*Kill.*

With that single thought, the Southern Heaven Demon Empress gritted her teeth and reached out.

Toward the three figures already rushing into view.

Toward the enemies who dared stand in the way of the grand undertaking the most noble Lord of Heaven wished to accomplish.

Gooooooooong.

In the slowed-down world, an unprecedented energy flowed through her bloodstained hand and into the blade.

The sword, whose master had changed, slashed down diagonally.

Shwaaaaaak!

And the Southern Heaven Demon Empress saw it.

Three pairs of eyes slowly widening beyond the warped space.

And the green Force surging up like an iron wall, as though to protect them all.

But…

*It’s over.*

Along with the Southern Heaven Demon Empress’s inaudible mutter, a distant flash of light swallowed everything.

Fwoooooosh!

* * *

It was a massive explosion, unlike anything anyone in this land had ever seen.

Fwoom! Ruuuuumble!

Yohi and Muyaho, who had been evacuating the survivors along with countless wild beasts.

The thousands of warriors who had surrounded the darkened Inner Palace with blood-soaked weapons held upright.

And the tribespeople running toward the hills outside the Outer Palace, gasping for breath.

They all saw it, and one word came to mind.

*A cataclysm.*

There was no other way to describe it. The distant flash and violent tremors spread far beyond the Inner Palace, traveling endlessly into the distance, and everyone who felt that power froze in place.

No—they trembled beneath a fear that seemed to bind even their souls.

“A-Aah…!”

The groans rising from every direction all turned toward one place: the Nanman Beast Palace they had left behind.

Boom. Rumble.

It was collapsing.

The pavilions and homes their ancestors had spent long years building with blood and sweat—the place where they had been born and raised—were on the verge of collapsing before their eyes.

What more needed to be said?

Thousands upon thousands of vacant eyes turned toward the Nanman Beast Palace.

They wanted to take in one last sight of their beloved homeland—a place they could never return to now.

But the deep despair hanging before their eyes soon changed into hope.

Ruuuuumble…

The tremors gradually subsided. The ground, which had been collapsing as though it would swallow the Nanman Beast Palace whole, stopped moving, and the houses and pavilions that had swayed as though they might topple at any moment were left merely leaning.

An unimaginable disaster.

And then, a miracle.

Those who watched the unbelievable scene were overcome with relief and joy.

Meanwhile, someone who had caused a disaster despite possessing nothing more than a human body trembled with pain and rage.

“T-This is impossible… Kweh-heeeeeck!”

Drip. Drip.

Dark-red blood spilled down from the corner of her mouth.

In the empty space where everything within a radius of fifty jang had been shattered and hurled far away, the Southern Heaven Demon Empress looked around with eyes filled with a crimson glare.

It had been a single strike. One certain opportunity.

She would not have cared even if she had died.

She could no longer return alive, and even if she went on living, she would have to spend the rest of her days in this old, hideous form.

And yet…

She had survived.

She, who should have been blown apart and killed after swallowing everything in the explosion, had survived in this humiliating state.

“Baeksang! You bastard. How dare you!”

Rumble!

The qi wave that erupted along with her terrible roar of rage shook the surrounding space.

Baeksang’s unexpected attack.

That single sword, which he had probably thrust forward by squeezing out every last bit of his remaining strength, had twisted everything.

In that instant, the tangled qi and blood had prevented the Southern Heaven Demon Empress from putting all her innate qi into the strike. That was why she had avoided being killed in the explosion.

But the same was true of *them*.

“Cough.”

Thud.

Several dozen jang away, a graying giant dropped to one knee, vomiting blood mixed with pieces of his internal organs.

Countless fragments were embedded throughout his body. Behind his broad back, the Southern Heaven Demon Empress saw the massive White Tiger and a young man lying motionless, drenched in blood.

“Yayul Cheok, you bastard…!”

As blood-filled phlegm boiled in her throat, the image of the Beast Miao King she had seen at the final moment flashed before her eyes.

At the last moment, he had stepped in front of Jin Taekyung without a moment’s hesitation.

*Why?*

She could not understand.

Why had the Beast Miao King, Yayul Cheok, who had earned the great title of one of the Ten Kings in the distant Central Plains, made such a choice?

And that foul-smelling beast had done the same.

*Risk their only lives? For a mere brat?*

Along with her question, one certainty seized the Southern Heaven Demon Empress.

*Jin Taekyung. No matter what it takes, I have to kill that one.*

The Palace Lord of the Nanman Beast Palace, a man no different from a king of a nation, and the White Tiger possessing a divine artifact had risked their lives for him.

That meant he was the most dangerous possibility in this place.

And the Southern Heaven Demon Empress still had innate qi that she had not yet poured out.

The last strength she had gained by burning her life.

*Lord of Heaven. Please forgive this disloyal servant who dares attempt to defy your will.*

Step.

The Southern Heaven Demon Empress muttered the words quietly in her mind and took a heavy step forward.

At that moment, a sharp sound of splitting air rang out.

Shk! Crack!

A spear that had flown from somewhere trembled in the Southern Heaven Demon Empress’s grasp.

She crushed the steel spearhead with her bare hand and let her eyes glow with blood-colored light.

“Do you all want to die?”

A middle-aged man stood upright where her chilling voice was directed. He wore armor that had been torn almost to shreds.

No, he was not alone.

Drip. Thud.

In the already devastated space, more than a hundred warriors staggered to their feet and gathered behind the middle-aged man, gripping their swords and spears tightly.

Though they had been relatively far from the center, every one of them had suffered injuries both large and small. Still, they stood in the Southern Heaven Demon Empress’s way to fulfill the mission entrusted to them.

Splash.

The middle-aged man picked up something half-submerged in a pool of blood and tied it tightly around his forehead.

Three characters were written on the old silk, still impossible to hide beneath the blood.

**Baekcheon Unit.**

That was the middle-aged man’s answer to the question asked moments earlier.

It was the answer of Wang Ho, Commander of the Baekcheon Unit—and the will of every surviving member of the unit.

And then, the next moment—

Screeeeeech! Boom!

The Fiend known as the Southern Heaven Demon Empress charged toward them.

* * *

A flash of light.

And an explosion.

That was the last memory remaining in my mind, and when I opened my eyes again, I thought everything would be over.

I would either be alive.

Or dead.

The result of a battle was always one of those two things.

But when I suddenly opened my eyes after passing through a brief darkness, I realized that I had only been half right.

I had survived, but the battle was not over yet.

Kraaaaaack!

“Gaaaaah!”

“Stop it—!”

Slice!

“Noooo!”

As the senses that had briefly faded returned, I could see.

Blood spraying into the sky and limbs flying upward.

Someone’s body, crushed into a bloody mess beneath overwhelming power, being flung away.

Whoom! Boom!

Drip.

Blood that had burst only a few steps away splashed across my face.

As I stared blankly at the warrior whose life had ended with a hole blown through the center of his chest, a weak voice reached my ears.

No—it was someone’s mental voice.

—Human.

Only then did I realize what was supporting my back.

And whose warmth I could feel.

Then, as I turned my head after sensing the thick scent of blood seeping deep into my nose, I lost the ability to speak.

“……!”

A massive body trembled intermittently in a deep pool of blood.

Its silver fur, which had seemed almost mystical, was soaked through with blood. Its pale blue eyes struggled to blink in my direction.

—You’ve slept a long time.

“……What is this?”

—I have no regrets. Neither does he.

Suddenly, a memory came back to me.

At the moment that distant flash had filled my vision, there had been green Force and a silver mane blocking my eyes.

*No way.*

As always, my ominous prediction turned out to be right.

The moment I turned my head, I saw a large back.

The man kneeling on one knee, looking no different from a bloody corpse, was the Beast Miao King, Yayul Cheok.

He had already lost consciousness.

The fragments of sword blades embedded all over his body must have come from shielding someone else from the attack.

“This is insane. Why the hell…?”

—Go.

“What?”

—Leave. Hurry. There’s no time.

As I stood speechless, the guardian spirit weakly moved its head and spat something out.

Fwoooooosh.

The sacred stone, now no larger than a child’s fist, emitted a faint light.

Realizing what the guardian spirit meant, I gritted my teeth.

“Don’t give me that bullshit.”

—If even those people fall, you’re next. But if you run, you can live.

Kraaaaaack!

“Gaaaaaaaah!”

As the earth shook, another person’s scream followed.

The Southern Heaven Demon Empress entered my field of vision, her veins standing out across her entire body as she burned through the last of her life and tore apart more than a hundred members of the Baekcheon Unit.

“……!”

A chill swept over me before that overwhelming power.

As I froze in place, the guardian spirit whispered with all its strength.

—Go. Now!

I knew.

At least, I knew that the guardian spirit was right.

The Southern Heaven Demon Empress did not have much time left, and if I escaped alone, I would be able to survive.

But…

“I’d regret it for the rest of my life.”

I muttered dazedly and grabbed the sacred stone.

Then I rose and ran.

Not toward the Outer Palace.

Toward the Southern Heaven Demon Empress.
```
