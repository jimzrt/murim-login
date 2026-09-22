<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0704.txt",
      "sha256": "114b57f315eda6ad873c14acab25b99d217eb2a9d45101b6e92b5cae7a8d1b0c",
      "bytes": 13422
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9ef34f3ccab48cf621d318b236ea258b859a3621793c99a00816ac21e495df47",
      "bytes": 2138
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "377408edd6bffa87540301dadb4da6acf3c4b03a8a29b32bdd22758532ccb70f",
      "bytes": 206401
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "969ac62bf4357486db64b9b3b53a65f256f49b49c1a3c4c71ee00a64e7b7e9e5",
      "bytes": 919
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "2a95364a8095afcde06b1ab09343fd02d75fce2018db5c878d76654460119f69",
      "bytes": 781
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "19a4792b92bf41381ad4e7f69ede4cc88a3d81d8f94aef675be8c761958a8ccf",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "144a83f59689581318f941db677ff3338d23af4b04246a635c54eb33ab7486ee",
      "bytes": 1887
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d5007ee77d745b6bda282ae5ebbf899e403a7830b02e459244d2105191b5399f",
      "bytes": 622
    },
    {
      "path": "characters/Masked Man.md",
      "sha256": "ab7fb90a7a37ef052ba8beb33b7dad0bde8e437db2590faa2847fa7841b70888",
      "bytes": 686
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "ad51f4f548893a84056575cca65d9ea8f111e233e9d1d1645321688caaed2411",
      "bytes": 853
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "5f857415db202fae015ad328432b8ec068b87e26f21c4936ceaad05e740306ee",
      "bytes": 888
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "dfcda2d4107d69798ca0482a6a8cac5863c8d9865bd48d697fa5c40491356efe",
      "bytes": 603
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "77b5156e82066c2bb8a153cb165e8edb0c9180c65514451d882d7dfcc39728ca",
      "bytes": 899
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "39588518517f0306c0f8c6983a12c725399d58da9336fd2022f2fd66d620875e",
      "bytes": 216408
    }
  ],
  "estimated_tokens": 12896
}
-->

# Durable State Update — Chapter 704

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 704. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 704. Profile updates may replace only one
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
  "chapter": 704,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 704,
    "continuity_sources": [704],
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
    "Jin Taekyung is barely able to stand after One Annihilation and must circulate his qi or die.",
    "One Annihilation erased the surrounding section of ground and killed the mutants that interfered with its execution, but it did not kill the Southern Heaven Demon Empress.",
    "The Southern Heaven Demon Empress has reverted to her aged original appearance and lost an arm, part of her side, and half her face, yet the rift's demonic qi is stabilizing and strengthening her.",
    "The Masked Man has been killed by the guardian spirit four times, but repeatedly rises again, recovering faster and becoming stronger under the demonic qi.",
    "The guardian spirit is heavily wounded, while the sacred stone's power and the White Tiger's strength are diminishing as the demonic qi spreads.",
    "Nearly one thousand mutants under the demonic qi's influence surround Jin and the guardian spirit, and the influence has begun spreading from the Inner Palace into the Outer Palace.",
    "Jin has ordered the guardian spirit to abandon him and rescue the people before the situation worsens.",
    "The Southern Heaven Demon Empress intends to keep Jin alive long enough to tear him apart and bring his divine artifact to the Lord of Heaven; she also wants the White Tiger's pelt."
  ],
  "continuity_sources": [
    703
  ],
  "open_questions": [
    "What caused the tremendous rumble that swept across the Nanman Beast Palace?",
    "Can the guardian spirit escape with the people while leaving Jin behind?",
    "Will the Southern Heaven Demon Empress capture Jin for the Lord of Heaven or kill him herself?",
    "Will the Masked Man rise again and become even stronger?",
    "Can the sacred stone, the guardian spirit, and the White Tiger resist the demonic qi long enough to stop the mutation?"
  ],
  "safe_through": 703,
  "temporary_decisions": [
    "Use jiazi for 갑자.",
    "Use vital essence for 정혈.",
    "Use grand art for 대공.",
    "Use practitioner for 술사.",
    "Retain One Annihilation, demonic qi, Force, and Finger Qi as established terminology."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 십왕     | **Ten Kings**       |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 복면인 | **Masked Man** | The Southern Heaven Demon Empress's trained hunting dog; identity remains unknown. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 권강 | **Fist Force** | Qi force projected through the Western Heaven Demon Lord's fist. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 일다경 | **the time it takes to drink a cup of tea** | Duration in the progression of Jeok's lost time. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 진태경 | 복면인 | hostile combatant to unknown hostile combatant | you | blunt, hostile, and incredulous | Jin directly questions the masked man about his identity and his relationship with the Great Snow Fiend. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 699
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and after betraying Nanman to pursue a decades-old promise, he witnesses a dark figure emerge from the mirror in his office.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 701
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace and a Supreme Peak master who secretly lived for decades under Heugung's identity through the Bone-Shrinking Technique.
- **Personality:** The Beast Miao King is calculating, patient, ruthless, and willing to endanger Nanman's people to advance Dark Heaven's grand plan.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He maintained his public bond with Baeksang while secretly monitoring Baeksang and Yohi for the Southern Heaven Demon Empress, but he has now been branded a traitor, fled the Nanman Beast Palace, and disappeared.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 703
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 703
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license; he is now severely injured after One Annihilation failed to kill the Southern Heaven Demon Empress.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 703
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Masked Man.md

# Masked Man (복면인)

- **Safe through:** Chapter 703
- **Aliases:** None
- **Role:** The Masked Man is the Southern Heaven Demon Empress's trained hunting dog; the guardian spirit has killed him four times, but he repeatedly rises again, recovering faster and growing stronger under the rift's demonic qi.
- **Personality:** The Masked Man is emotionless, silent, and indifferent to extreme bodily damage.
- **Voice:** No spoken voice has been established.
- **Relationships:** He serves the Southern Heaven Demon Empress as her hunting dog; his identity and relationship with the Great Snow Fiend remain unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 703
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; One Annihilation shattered her cultivated youth, leaving her aged, maimed, and scarred, but the rift's demonic qi is restoring her strength as she continues attacking Jin Taekyung.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 702
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 703
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone and leads the Sacred Land beasts, but both the stone's power and the White Tiger's strength are weakening under the rift's demonic qi.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 699
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty former Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃704화



남천마후는 확신하고 있었다.

앞으로 일다경(一茶頃). 고작해야 차 한잔 마실 시간만 있으면 이 지긋지긋한 전투를 끝낼 수 있다고.

그것이 저 찢어 죽여도 시원치 않을 애새끼와 짐승이 살아 숨쉴 수 있는 마지막 시간이 될 것이라고.

하지만 그토록 굳건하던 확신은, 일장(一掌)을 발출하려던 그 순간 균열을 일으켰다.

구웅-!

어디선가 시작된 거대한 울림.

그와 동시에 공기가 출렁이고 바람이 멈춘다. 짙은 어둠 너머에서 전해지는 강대한 기파(氣波)를 느낀 남천마후가 이를 악물었다.

‘이건……!’

강자다. 그것도 마기의 영향에서 자유로울 정도의 강자!

뇌리를 스치는 생각도, 그에 따른 대응도 찰나였다.

일이 틀어졌음을 깨달은 남천마후는 하나뿐인 손에 실린 공력을 발출하며 외쳤다.

기파가 느껴지는 방향이 아닌, 더 늦기 전에 숨통을 끊어야 할 누군가를 향하여.

“놈을 죽여!”

콰아아아아!

그 순간, 공간을 가르며 쏘아진 것은 혼탁한 빛을 띤 막대한 장력(掌力)만이 아니었다.

무려 일천에 달하는 인간과 짐승. 마기에 의해 더욱 악하고 강해진 변이체들이 일제히 괴성을 토해 내며 신형을 날렸다.

파팟. 쉬쉬쉬쉭!

- 크륵, 크아아아!

강철보다 단단하고 날카로운 이빨이 어둠 속에서 빛난다.

본래 지녔던 신체능력을 훌쩍 웃도는 힘과 속도로 달려드는 그들의 머리 위로, 거대한 기운을 품은 장력이 유성처럼 쏘아졌다.

짙은 어둠 속, 흐릿한 빛무리를 받으며 서 있는 두 존재를 향해.

아니, 남천마후에게 씻을 수 없는 모욕을 안겨 준 한 인간을 산산조각 내기 위해.

그러나 자신을 향해 덮쳐 오는 그 모든 것들을 바라보며, 진태경은 피곤에 젖은 입꼬리를 비틀었다.

“어쩌나. 이미 늦었는데.”

“……!”

불과 한 시진 전, 남천마후의 입술 사이로 흘러나왔던 그 짤막한 한 마디가 비웃음 가득한 목소리로 돌아온 그 순간.

퍼엉! 화아악!

사방에 드리워진 짙은 어둠이, 마기가 폭발하듯 양옆으로 터져 나갔다.

동시에 그 사이로 뛰쳐 나온, 숲과 초목(草木)을 닮은 녹색 강기가 가로막는 모든 것을 부수었다.

아니, 맹렬하게 물어뜯고 집어삼켰다.

마치…… 한 마리의 맹수처럼.

콰드드드득!

지축이 흔들린다. 압축된 공기가 터져 나가고, 쓰디쓴 마기가 뒤섞인 바람이 지워진다.

사방에서 달려들던 변이체의 사지를 찢어발긴 녹색 강기가 거대한 장력를 향해 아가리를 벌렸다.

꽈앙! 구구궁!

격돌과 함께 뒤섞이는 빛.

하늘이 갈라지는 듯한 굉음에 이어 무시무시한 충격파가 공간을 뒤흔들었다.

그 너머에서 힘없이 사그라지는 자신의 장력을 바라본 남천마후가 실핏줄이 터져 나간 눈동자를 부릅떴다.

‘공멸(共滅)?’

자신이 누구인가.

하늘과 땅을 통틀어 가장 위대하며 존귀한 존재. 천주의 명을 받드는 가장 충실한 종복 중 한 사람이자, 그중에서도 남천(南天)을 위임받을 만큼 신뢰받는 강자다.

제아무리 진태경에 의해 상당한 힘을 잃은 상태라 해도, 어지간한 초절정 고수 정도는 촌각 안에 찢어발길 수 있다.

한데 공멸이라니.

믿을 수 없고 믿고 싶지도 않은 결과였지만, 남천마후는 눈앞에서 벌어진 현실을 부정할 만큼 멍청하지 않았다.

더불어 갑작스럽게 나타난 상대의 정체를 유추할 만큼의 판단력도 지니고 있었다.

‘틀림없다.’

이 정도의 권강(拳罡). 그리고 서서히 가라앉고 있는 먼지구름 사이로 보이는 저 커다란 인영.

남천마후의 입술 사이로 차갑게 식은 목소리가 흘러나왔다.

“……야수묘왕(野獸苗王) 야율척.”

퍼엉!

남천마후가 내저은 소매 끝에서 터져 나간 바람이 시야를 밝힌다.

흩어지는 먼지구름 사이, 늙은 대호처럼 반백(半白)의 수염을 갈기처럼 늘어트린 거한의 얼굴이 드러났다.

철탑처럼 우뚝 선 그의 등 뒤로, 거대한 백호의 몸뚱어리에 몸을 기대고 있는 어느 청년의 모습도 함께.

“늦으셨네요. 많이.”

흐릿한 진태경의 목소리에, 야수묘왕이 담담한 얼굴로 입을 열었다.

“미안하구나. 늦어서.”

“하마터면 객사(客死)할 뻔했습니다.”

“그럴 일은 없을 것이다.”

나직하게 대답한 야수묘왕이 섬전처럼 손을 뻗었다.

펑.

북이 터지는 듯한 소리와 함께 진태경의 신형이 들썩인다.

무너지려는 그의 신형을 황급히 감싸 안은 수호령이 본능적으로 이빨을 드러낸 그때, 고개를 내저은 진태경이 입을 벌렸다.

“우욱. 우에에엑!”

촤아아악.

넓은 등허리를 적시는 검붉은 핏물. 마치 토사물처럼 쏟아지는 사혈(死血)의 뜨끈한 감촉을 느낀 수호령이 중얼거렸다.

- 기분 한번 끝내주는군.

“……!”

- 그런 눈으로 쳐다볼 것 없다. 몸집 큰 인간이여. 나는…….

눈을 크게 뜬 야수묘왕을 향해 수호령이 말을 이으려던 그때, 죽은 피를 토해 낸 진태경이 몸을 일으키며 입을 열었다. 전보다 훨씬 생기 있는 목소리로.

“통성명을 나누기에는 썩 좋은 분위기는 아닌데, 우선 인사하세요. 이쪽은 흰둥이. 제가 새로 입양했어요.”

- 입양이라니, 감히!

“오. 그럼 흰둥이는 인정?”

- 노옴!

상황도 잊고 털을 바짝 세우며 화를 내는 수호령을 보며 진태경이 씩 웃은 그 순간. 야수묘왕이 불현듯 양손을 떨쳤다.

퍼엉!

녹색 권강과 혼탁한 장력이 허공에서 부딪친다. 동시에 힘없이 축 늘어져 있던 투명한 창날이 움직였다.

서걱!

틈을 노려 달려들었던 변이체 십여 마리가 비명도 지르지 못하고 쪼개진다.

그리고 순간 비틀거리는 진태경의 등 뒤를 향해 쇄도하던 또 다른 변이체들은, 자신들은 기다리고 있던 거대한 앞발을 볼 수 있었다.

후웅, 콰득!

핏물이 분수처럼 솟구치고, 몸뚱어리에서 분리된 사지가 나뒹굴었다.

크르릉. 낮은 울음소리를 흘린 수호령과 등을 맞댄 진태경이 백염(白炎)의 창날을 들어 한 방향을 가리켰다.

“그리고 다른 사람이 말하는 와중에 끼어든 저 썅년은…… 아시죠?”

야수묘왕이 고개를 끄덕였다. 깊게 가라앉은 눈동자에는 추악한 모습을 한 노파가 비치고 있었다.

“그래, 남천마후.”

끓어오르는 듯한 목소리에는 숨길 수 없는 분노가 담겨 있었다.

아직도 주위를 둘러싼 수많은 변이체. 마기에 잠식당하여 본래의 모습을 잃어버린 그들은, 한때 야수묘왕이 누구보다 아끼고 사랑하던 이 땅의 부족민들이었다.

아니, 그 사실은 지금도 변하지 않는다.

변이체들을 본 그 순간부터 욱신거리기 시작한 가슴 한구석이 바로 그 증거였다.

‘늦지 않길 바랐는데.’

숨이 턱에 차도록 달렸다. 온 힘을 쥐어 짜내어 이곳까지 왔다.

그리고 저 멀리에서 어둠과 불길에 휩싸인 남만야수궁의 전경을 확인한 순간, 깨달았다.

이미 늦어 버렸음을.

야수묘왕이 지금 이 자리에 오기까지 지나쳐야 했던 것은 산과 들. 강과 계곡뿐만이 아니었다.

지옥도(地獄道).

그는 지옥도를 보았다. 수십여 년 전, 정마대전이라 명명된 그 끔찍했던 기억의 파편이 떠올라 마음을 난도질했다.

미처 피신하지 못한 부족민들의 시신 위에는 무너진 건물의 잔해가 짓누르고 있었고, 불과 얼마 전까지만 하더라도 풍악과 웃음소리가 가득하던 거리는 넘실거리는 어둠과 화마(火魔)가 차지했다.

그리고 지금 이 순간, 이 지옥도를 만들어 낸 가장 큰 원흉이 야수묘왕의 시선 끝에 서 있었다.

“남만야수궁의 궁주로서 맹세하건대.”

붉어진 두 눈동자에서 화염이 줄기줄기 쏟아진다.

술과 사람을 좋아하고, 거나하게 취하여 껄껄 웃던 평소의 모습은 이제 어디에서도 찾아볼 수 없다.

과거 일만의 전사를 이끌고 북상. 마교의 십만마도(十萬魔徒)에 맞서 십왕(十王)이라는 위명을 얻은 거인이 서늘한 목소리로 말을 이었다.

“네년의 사지를 갈기갈기 찢어 주마.”

야수묘왕의 커다란 등 뒤에서 고개를 쏙 내민 진태경이 덧붙였다.

“혹시 힘에 부치실까 봐, 팔 하나는 이미 제가 잘랐습니다.”

여전히 창백하지만, 빠르게 돌아오고 있는 혈색. 애병을 움켜쥔 손은 더 이상 떨리지 않는다.

크게 심호흡한 진태경은 앞으로 걸음을 내디뎠다.

저벅.

단 한 걸음.

그러나 아직도 사방을 가득 메우고 있는 변이체들은 몸을 움찔거리기만 할 뿐, 섣불리 달려들지 못했다.

비록 이성은 마비되었지만, 변이와 함께 더욱 극대화된 본능이 알아차렸기 때문이다.

공기의 흐름이 바뀌었다는 것을. 또 자신들에게 명령을 내려야 할 주인이 무슨 이유에선지 침묵하고 있다는 것을.

그리고 이러한 변이체들의 본능은 진실에 가까웠다.

남천마후는 남만에 온 이래, 두 번째로 위기감을 느끼고 있었다.

‘이대로라면…… 좋지 않아.’

평소라면 코웃음을 쳤을 것이다. 제아무리 십왕 중 한 자리를 차지한 야수묘왕이라 해도, 자신과의 간극을 메우기에는 역부족일 테니까.

하지만 지금은 달랐다.

진태경의 일격은 찰나의 순간 남천마후마저 공포에 얼어붙게 할 만큼 강력했고, 그로 인해 한쪽 팔과 함께 상당한 힘을 잃어버렸다.

이런 상황에서 나타난 야수묘왕은 충분히 위협적이다.

야수묘왕의 도움으로 약간의 힘을 회복한 진태경과 상당한 기운을 품은 수호령 역시 변이체 따위가 어찌할 수준은 되지 못한다.

그러나 마음속 불안감이 조금씩 커져만 가는 이유는 그뿐만이 아니었다.

‘왜. 왜 나타나지 않는 거지?’

몇 달 전 사천에서 죽음을 맞이한 서천마군이 그러했듯, 남천마후 역시 적지 않은 수하들을 휘하에 거느리고 있었다.

머릿수는 약 오백.

일군(一群)이라 칭하기에는 부족한 숫자일지는 모르나, 남만인들의 눈을 피해 은거하며, 혹시 모를 상황을 대비하기에는 충분한 정예들이다.

그런데…….

‘오지 않았어. 아직도.’

균열이 열린 지 어언 반 시진이 넘은 시점. 하지만 때맞춰 모습을 드러낸 것은 복면인 하나뿐이었다.

본래대로라면 백상에게 선물한 거울에 새겨진 이동진(異動陣)을 타고 절반이 넘어오고, 남은 절반은 외부에서 외궁의 성문을 봉쇄해야 했다.

‘설령 이동진에 문제가 생겼더라도, 지금쯤이면 어떤 식으로든 나타나야 인지상정이거늘.’

남천마후가 지그시 입술을 깨문 그때, 그녀가 딛고 선 지면이 조금씩 흔들리기 시작했다.

드득. 드드드득.

뒤늦게나마 수하들이 도착했음을 깨달은 남천마후는 희미한 미소를 머금었다.

지금 오고 있는 오백의 병력은 그녀가 직접 가려 뽑은 이들이다.

마공(魔功)을 익힌 그들은 마기의 영향으로 평소보다 더욱 강해질 테니, 아무리 많은 맹수가 외궁에 남아 있다 한들 앞길을 막아설 수는 없다.

“사지를 갈기갈기 찢어 죽여? 너 따위가 날?”

남천마후는 피식 실소를 흘렸다. 어느새 굳어 있는 진태경과 야수묘왕의 얼굴을 보자 흘러나오는 웃음을 참을 수 없었다.

“인정하지. 너희는 내가 생각했던 것 이상으로 잘 싸웠어. 아니, 누구도 이렇게까지 되리라고는 생각하지 못했을 거야.”

하지만 그것도 이제는 끝이지.

뒷말을 삼킨 남천마후는, 언제 그랬냐는 듯 사뿐하게 걸음을 옮겼다. 그리고 팽팽하던 긴장감이 느슨해진 그때, 야수묘왕이 불쑥 입을 열었다.

“있다.”

“뭐?”

“이렇게 되리라고 예견했던 사람이. 돌이킬 수 없는 길을 걸으면서도, 자책감에 몸부림치면서도 마지막까지 희망을 놓지 않았던 한 사람이.”

도무지 이해할 수 없는 말.

남천마후는 눈을 깜빡이던 그때, 야수묘왕이 섬전처럼 돌아서며 일권(一拳)을 뻗었다.

콰아아아!

가파르게 쏘아진 녹색 강기가 어둠을 뚫고 길을 만든다.

그리고 그 길을 따라, 이 전투의 마지막 향방을 가를 지원군이 도착했다.

두두두두!

새하얀 옷과 갑주로 무장한 일단의 무리.

그 선두에 선 사내가, 야수묘왕을 향해 고개를 숙였다.

“백천대주 왕호가…… 궁주를 뵙습니다.”
```

## Final English reading copy

```markdown
# Chapter 704

The Southern Heaven Demon Empress was certain.

She needed no more than *the time it takes to drink a cup of tea* to end this tiresome battle.

It would be the last stretch of time that brat she wanted to tear apart and that beast could remain alive and breathing.

But that unshakable certainty began to crack at the very moment she was about to unleash a palm strike.

Kwoooong—!

A tremendous rumble that had begun somewhere.

At the same time, the air rippled and the wind stopped. Sensing the powerful wave of qi coming from beyond the thick darkness, the Southern Heaven Demon Empress clenched her teeth.

*This is…!*

A master. And one powerful enough to remain free from the demonic qi’s influence.

The thought that flashed through her mind and the response that followed were both instantaneous.

Realizing that something had gone wrong, the Southern Heaven Demon Empress released the internal energy gathered in her only hand and shouted.

Not toward the direction from which she sensed the wave of qi, but toward the person whose throat she needed to cut before it was too late.

“Kill him!”

Kwooooooosh!

At that moment, it was not only an enormous palm force, tinged with murky light, that shot through the air and tore across space.

Nearly a thousand humans and beasts—mutants made even more vicious and powerful by the demonic qi—threw themselves forward in unison, shrieking.

Pap-pap. Shhhhhk!

—Krrk, kraaaah!

Teeth harder and sharper than steel glinted in the darkness.

Above the heads of the mutants charging forward with strength and speed far beyond their original physical abilities, a palm force filled with tremendous energy shot through the air like a meteor.

Toward the two figures standing amid the dense darkness beneath a hazy halo of light.

No—to tear apart the human who had inflicted an insult on the Southern Heaven Demon Empress that could never be washed away.

Yet as Jin Taekyung watched everything rushing toward him, he twisted the corner of his exhaustion-laden mouth.

“Too bad. You’re already too late.”

“……!”

That brief sentence, which had slipped from the Southern Heaven Demon Empress’s lips only one shichen earlier, came back to her in a voice full of mockery.

Boom! Fwoosh!

The dense darkness spread in every direction exploded sideways as though the demonic qi itself had detonated.

At the same time, a green Force resembling forest and vegetation burst through the gap and smashed apart everything in its path.

No.

It tore into them and devoured them with ferocity.

Like a wild beast.

Krrrunch!

The earth shook. Compressed air burst outward, and the wind mixed with bitter demonic qi was erased.

The green Force tore apart the limbs of the mutants charging in from every direction before opening its jaws toward the enormous palm force.

Kwaaang! Rumble!

Light intertwined in the collision.

After a deafening roar that made it seem as though the sky itself had split apart, a terrifying shock wave shook the surrounding space.

Beyond it, the Southern Heaven Demon Empress stared wide-eyed at her palm force as it faded away helplessly.

The capillaries in her eyes had burst.

*Mutual annihilation?*

Who was she?

She was the greatest and most exalted existence beneath heaven and earth. One of the most loyal servants who served the will of the Lord of Heaven—and a powerful figure trusted enough to be entrusted with South Heaven itself.

Even after losing a considerable amount of strength because of Jin Taekyung, she could still tear apart an ordinary Supreme Peak master in moments.

And yet mutual annihilation?

It was an unbelievable result—one she did not even want to believe—but the Southern Heaven Demon Empress was not foolish enough to deny the reality unfolding before her eyes.

Nor did she lack the judgment to infer the identity of the opponent who had appeared so suddenly.

*No doubt about it.*

That level of Fist Force. And the enormous silhouette visible through the dust cloud as it slowly settled.

A voice, cold as ice, escaped the Southern Heaven Demon Empress’s lips.

“……Yayul Cheok, the Beast Miao King.”

Boom!

The wind bursting from the sleeve the Southern Heaven Demon Empress swung aside cleared the air before her.

Amid the dispersing dust cloud, the face of a giant appeared. A half-gray beard hung from his chin like the mane of an old great tiger.

Behind his iron-tower-like frame, a young man leaned against the massive body of a White Tiger.

“You’re late. Very late.”

At Jin Taekyung’s hazy voice, the Beast Miao King opened his mouth with a calm expression.

“I am sorry. For being late.”

“I almost died out here.”

“That will not happen.”

The Beast Miao King answered quietly and thrust out his hand like a flash of lightning.

Bang.

With a sound like a drum exploding, Jin Taekyung’s body jerked.

As the guardian spirit hurriedly caught his collapsing body, instinctively baring its teeth, Jin Taekyung shook his head and opened his mouth.

“Urk. Ueeecch!”

Shwaaaaaak!

Dark red blood soaked the guardian spirit’s broad back.

Feeling the hot sensation of the stagnant blood pouring out like vomit, the guardian spirit muttered.

—What a wonderful feeling.

“……!”

—There is no need to look at me like that, large human. I—

The guardian spirit was about to continue, addressing the wide-eyed Beast Miao King, when Jin Taekyung, having vomited up the dead blood, raised himself and spoke.

His voice was far more lively than before.

“It’s not exactly the best atmosphere for introductions, but say hello first. This is Whitey. I just adopted him.”

—Adopted me? How dare you!

“Oh. So you’re okay with Whitey?”

—You bastard!

Jin Taekyung grinned as the guardian spirit forgot the situation and bristled furiously.

At that moment, the Beast Miao King abruptly swept both hands outward.

Boom!

Green Fist Force and the murky palm force collided in midair.

At the same time, the transparent spearhead that had been hanging limp moved.

Slash!

Around ten mutants that had rushed forward, seeking an opening, were sliced apart without even having time to scream.

Then another group of mutants charged toward Jin Taekyung’s back as he staggered for an instant.

They saw the enormous forepaw waiting for them.

Whoosh! Crunch!

Blood spurted like a fountain, and limbs severed from their bodies rolled across the ground.

With a low growl rumbling from its throat, the guardian spirit stood back-to-back with Jin Taekyung.

Jin raised the spearhead of White Flame and pointed in one direction.

“And that fucking bitch who interrupted while someone else was talking… You know who I mean, right?”

The Beast Miao King nodded.

His deeply sunken eyes reflected an old woman with an ugly appearance.

“Yes. The Southern Heaven Demon Empress.”

His voice seemed to boil with anger that could not be hidden.

Countless mutants still surrounded them.

Consumed by the demonic qi and stripped of their original forms, they were the tribespeople of this land whom the Beast Miao King had once cherished and loved more than anyone.

No.

Even now, his feelings for them had not changed.

The aching in one corner of his chest, which had begun the instant he saw the mutants, was proof of that.

*I had hoped I wouldn’t be too late.*

He had run until he could barely breathe. He had squeezed every last bit of strength from his body to reach this place.

And the moment he saw the Nanman Beast Palace in the distance, engulfed in darkness and flames, he had realized it.

He was already too late.

To reach this place, the Beast Miao King had crossed more than mountains and plains, rivers and valleys.

He had seen a hellscape.

The sight had brought back fragments of the horrific memories from several decades ago—the memories of the war that had been named the Great Faction War—and torn his heart apart.

The corpses of tribespeople who had been unable to evacuate were crushed beneath the debris of collapsed buildings, while the streets that had been filled with music and laughter until not long ago had been claimed by surging darkness and flames.

And at this very moment, the greatest cause of the hellscape stood at the end of the Beast Miao King’s gaze.

“I swear this as the Palace Lord of the Nanman Beast Palace.”

Flames streamed from his reddened eyes.

The man’s usual appearance—fond of alcohol and people, laughing loudly after getting thoroughly drunk—could no longer be found anywhere.

In the past, he had led ten thousand warriors north and faced the Demonic Cult’s hundred thousand demonic followers, earning the fearsome name of one of the Ten Kings.

Now, that giant continued in a chilling voice.

“I will tear your limbs apart piece by piece.”

Jin Taekyung poked his head out from behind the Beast Miao King’s broad back and added,

“Just in case it’s too much for you, I already cut off one of her arms.”

His complexion was still pale, but color was returning quickly. The hand gripping his favored weapon no longer trembled.

Jin Taekyung took a deep breath and stepped forward.

Scuff.

One step.

Yet the mutants still filling the surrounding area merely twitched. They could not bring themselves to charge recklessly.

Though their reason had been paralyzed, their instincts—heightened even further by the mutation—had noticed it.

The flow of the air had changed.

And for some reason, the master who should have been giving them orders had fallen silent.

The mutants’ instincts were close to the truth.

The Southern Heaven Demon Empress had felt a sense of crisis for the second time since coming to Nanman.

*This isn’t good…*

Under normal circumstances, she would have snorted.

Even if the Beast Miao King was one of the Ten Kings, he was still nowhere near strong enough to close the gap between them.

But this time was different.

Jin Taekyung’s One Strike had been powerful enough to freeze even the Southern Heaven Demon Empress with fear for an instant, and she had lost a considerable amount of strength along with one arm because of it.

The Beast Miao King’s appearance in such a situation was a genuine threat.

Jin Taekyung had recovered a small amount of strength with the Beast Miao King’s help, and the guardian spirit also possessed a considerable amount of qi. Neither of them was an opponent the mutants could handle.

But that was not the only reason the unease in her heart continued to grow.

*Why? Why haven’t they appeared?*

Just as the Western Heaven Demon Lord had done when he met his death in Sichuan several months earlier, the Southern Heaven Demon Empress had a considerable number of subordinates under her command.

Approximately five hundred.

It might not have been enough to call them a full unit, but they were elite soldiers who had lived in seclusion, hidden from the eyes of Nanman’s people, and were more than sufficient to prepare for any possible situation.

And yet…

*They haven’t come. Still.*

More than half a shichen had passed since the rift opened.

But the only one to appear at the appointed time had been the Masked Man.

Normally, more than half of them should have crossed over through the Moving Formation engraved on the mirror she had given Baeksang, while the remaining half should have sealed the Outer Palace’s gates from outside.

*Even if something had gone wrong with the Moving Formation, it would only make sense for them to appear somehow by now.*

At the moment the Southern Heaven Demon Empress bit down on her lips, the ground beneath her feet began to shake.

Creak. Creak-creak.

Realizing that her subordinates had finally arrived, the Southern Heaven Demon Empress wore a faint smile.

The five hundred soldiers approaching now were ones she had personally selected.

They had mastered demonic martial arts, and the demonic qi would make them even stronger than usual. No matter how many beasts remained in the Outer Palace, they would be unable to block their path.

“Tear my limbs apart piece by piece? You?”

The Southern Heaven Demon Empress let out a quiet laugh.

When she saw the now-stiff faces of Jin Taekyung and the Beast Miao King, she could not hold back her laughter.

“I admit it. You fought better than I expected. No—no one could have imagined things would turn out like this.”

*But it ends here.*

Swallowing the rest of her words, the Southern Heaven Demon Empress began walking lightly, as though nothing had happened.

And just as the taut tension began to loosen, the Beast Miao King abruptly spoke.

“There is.”

“What?”

“There is someone who foresaw that this would happen. Someone who did not let go of hope until the very end, even while walking down an irreversible path and writhing in guilt.”

Words she could not understand at all.

As the Southern Heaven Demon Empress blinked, the Beast Miao King spun around like a flash of lightning and thrust out one fist.

Kwoooooosh!

Green Force shot sharply forward, piercing the darkness and carving out a path.

And along that path came the reinforcements who would decide the ultimate outcome of the battle.

Thud-thud-thud-thud!

A group of people armed in pure white clothing and armor.

The man at their head bowed toward the Beast Miao King.

“Wang Ho, Commander of the Baekcheon Unit… pays his respects to the Palace Lord.”
```
