<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0699.txt",
      "sha256": "d28b37d20d2253e26877c58ca36cedc1a3f8d65b05c9fb858d31e3780157e5f1",
      "bytes": 13644
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "795e567e5593be314ff0449789229eda76105ddedb59e5ecf8355a68144ad420",
      "bytes": 2382
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b692e6c1c95949375957ebd4a1696a83b8ec456ca92678c22b38b1d7d70fe36b",
      "bytes": 205908
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "f8aa0aaaee5fb6aa582fa9b1ee02b9391322a26db367dcf553a370bfd8e06fa5",
      "bytes": 895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "94c516a6fe84ffa9ebdbde9e5880a12c45266d5e4b9393676a89c7c871538f95",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "36053c9af88480892d216d7ff850b84ae4cec3502f18f4c6b218414641d39760",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "90401b314bdea7fac996584c8c99f714378e95cba9caa0efafb40865340d1d1e",
      "bytes": 1924
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "80bfc2b71c9e660443dc790a356b5e6a403069bc162ef7608038d39fc298c9b7",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "0df9d8d9ba91707b976be5ee9b516db82fe3f23f848dca03004012f2e10eb918",
      "bytes": 820
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "60c6e951630709679f53fd86cb02f66769a3b063ad19b7ba5c9da7f429945e89",
      "bytes": 888
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "0c7feed66b7434e5b2a4baab93f93f0bd73ae5b3a9f450c75a708c001832b2f1",
      "bytes": 616
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "84be2a61cd2476f6e24cb7de860f2fba88cd39fe97b7c26038d1f258180b867f",
      "bytes": 899
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4b3403de50af859addbc907f7846372532637cfea9d724960e3c49d9169efc09",
      "bytes": 215636
    }
  ],
  "estimated_tokens": 12612
}
-->

# Durable State Update — Chapter 699

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 699. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 699. Profile updates may replace only one
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
  "chapter": 699,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 699,
    "continuity_sources": [699],
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
    "Jin Taekyung and the beast army are inside the Nanman Beast Palace confronting the Southern Heaven Demon Empress.",
    "Yohi is with Jin and has been ordered to evacuate the Outer Palace tribespeople.",
    "The guardian spirit is accompanying Jin and resisting the Southern Heaven Demon Empress.",
    "The Southern Heaven Demon Empress is Honglan, the former Lower District Sect singing courtesan who deliberately approached Jin at Dongting Lake.",
    "The Southern Heaven Demon Empress created the massive rift behind the Inner Palace and regards its demonic qi and transformation as a blessing from the Lord of Heaven.",
    "The Beast King Stone has manifested and its radiance is blocking the demonic qi from the rift.",
    "The Southern Heaven Demon Empress searched Nanman for the Beast King Stone for more than ten years and demands it for the Lord of Heaven.",
    "Jin Taekyung and the White Tiger have attacked the Southern Heaven Demon Empress, beginning an unresolved clash of light and darkness.",
    "The Outer Palace has been devastated, and its civilians are fleeing amid deaths and injuries.",
    "Baeksang has saved and healed a former palace attendant, directed her family toward the East Gate, and continued toward the Inner Palace.",
    "Baeksang is approaching the moment he has envisioned for decades."
  ],
  "continuity_sources": [
    698
  ],
  "open_questions": [
    "What will be the outcome of the clash between Jin, the White Tiger, and the Southern Heaven Demon Empress?",
    "Can the Beast King Stone continue blocking the rift and allow the rift to be closed?",
    "What does the Lord of Heaven intend to do with the Beast King Stone?",
    "What purpose has Baeksang pursued for decades, and what will happen when he reaches the Inner Palace?",
    "How many Nanman civilians will survive the devastation of the Outer Palace?"
  ],
  "safe_through": 698,
  "temporary_decisions": [
    "Use Whitey for Jin's nickname 흰둥아.",
    "Use civil war for 내전 and fighting spirit for 전의.",
    "Use the quoted paraphrase “Do everything in your power, then leave the result to Heaven and wait” for 진인사대천명.",
    "Use rift for 균열 and evolution for 진화.",
    "Retain Guardian spirit for 수호령, Benefactor for 은인, and Great Chieftain for 대족장."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 내가고수 | **I'm a Master** | System Title granted to Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 백상 | 중년인 | Nanman Palace Lord to civilian tribesman | you | controlled and grave | Baeksang orders the middle-aged man to flee with his mother and the other civilians through the East Gate. |
| 중년인 | 백상 | Nanman civilian to betrayed Palace Lord | you | hostile, fearful, and grieving | The middle-aged man confronts Baeksang while protecting his mother and condemns him for the deaths and destruction. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 698
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he has publicly admitted betraying all Nanman people to pursue a purpose maintained for decades.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 698
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 698
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 698
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and the leader of the beast-army assault confronting Baeksang and the revealed Southern Heaven Demon Empress inside the Nanman Beast Palace.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 698
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 698
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the former Lower District Sect singing courtesan, the creator of the massive rift behind Nanman's Inner Palace, and the enemy seeking to seize the Beast King Stone for the Lord of Heaven.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 698
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 698
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone, restored to its former silver-white tiger form and using the Beast King Stone's radiance to oppose the rift and the Southern Heaven Demon Empress.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 695
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty former Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃699화



구구구궁! 쿵!

거센 진동을 이기지 못한 내궁의 석벽이 힘없이 허물어지고, 둔중한 소음을 떨어져 나간 철문이 지면을 후려친다.

흡사 작은 동산이 무너지는 듯한 광경.

그러나 미끄러지듯 잔해를 피한 백상의 신형은 쾌속하게 쏘아졌다.

쉬이이익!

전신을 스치는 바람. 곤두선 오감으로부터 비릿한 혈향(血香)과 곳곳에서 울려 퍼지는 비명이 전해진다.

백상은 자신의 내부에서 요동치는 공력을 느끼며 심호흡했다.

‘휩쓸려서는 안 된다.’

마치 병풍처럼 내궁의 뒤에 우뚝 선 거대한 절벽.

이제는 ‘균열’이라 불려야 할 절벽의 틈새에서 흘러나오고 있는 마기(魔氣)는 백상으로서도 쉽게 생각할 수 없었다.

아니, 초절정 고수였기에 이렇게 내궁을 활보할 수 있다.

마도(魔道)를 걷는 자가 아니라면, 어지간한 내가고수(內家高手)조차 저 마기의 영역에 들어선 순간 공력이 진탕되고 평정심을 잃었을 것이다.

지금 이 순간, 비틀거리며 그를 막아선 한 중년인처럼.

“구, 궁주? 궁주님이십니까?”

모를 수 없는 얼굴이다.

아비를 닮아 탐욕스럽고, 별다른 능력도 없이 부족장의 자리를 물려받아 호의호식하던 자.

그렇기에 누구보다 열성적으로 백상을 지지했던 이였으니까.

그러나 언제나 기름 낀 얼굴로 백상에게 아부로 가득한 미소를 건네던 그는, 지금 칠공(七空)에서 피를 흘리며 부르짖고 있었다.

“제발, 제발 살려 주십시오! 전 아직 죽기 싫습……!”

허우적거리며 뻗은 손이 새하얀 옷깃을 스친다. 중심을 잃고 쓰러진 부족장을 가만히 내려다보던 백상이 입을 열었다.

“내가 왜 그래야 하지?”

“구, 궁주?”

“이미 알고 있었을 텐데. 내가 하려는 일이 남만에 크나큰 해가 된다는 것을.”

“……!”

“서로의 목적을 위해 합당한 대가를 주고받았으니, 부디 억울해하지는 말게.”

나 역시 그러할 테니.

입 밖으로 흘러나오지 않은 뒷말과 함께, 백상의 손가락 끝에서 지풍(指風)이 쏘아졌다.

푸푹!

천령개(天靈蓋)를 관통당한 부족장의 신형이 그대로 허물어진다.

믿을 수 없다는 듯 눈을 부릅뜬 그의 눈빛은 죽어서도 백상에게 질문을 던지는 것 같았다.

왜. 어째서.

이 지옥도 앞에서도 당신은 그리 당당할 수 있느냐고.

그리고 망자(亡者)의 물음에, 백상은 마음속으로 답했다.

‘이미 각오했으니까.’

그럼에도 입술 사이로 흘러나오는 숨결은 파르르 떨렸다.

설령 저자가 제 목숨이 아니라 부족민들을 살려 달라 애걸했다면 살려 주었을까?

아니, 어쩌면 편안한 죽음을 맞이했으니 형편없는 무공을 지닌 그에게는 오히려 자비였을지도 모른다.

일만.

무려 일만이다. 그 수많은 전사와 맹수가, 마기에 휩싸여 피를 흘리며 몸부림치고 있었다.

그들이 내지르는 비명이 심장을 쥐어짜고, 칼날처럼 머릿속을 후비는 듯했다.

하지만 백상은 걸음을 멈추지 않았다.

쐐애애액!

거침없이 쏘아진 신형이 비명이 깔린 드넓은 연무장을 가로질렀다.

어릴 적 야율척과 함께 사고를 칠 때마다 숨어들었던 마구간도, 과실주를 훔치려 드나들었던 곳간도 한 줄기 바람이 되어 스쳐 지나갔다.

복수심. 분노. 후회.

보보(步步)마다 켜켜이 쌓여 온 감정들이 휘몰아친다.

하나뿐인 아들을 전장으로 데려가지 않았더라면. 남천마후가 찾아온 그 날, 손을 맞잡는 대신 검을 뽑았더라면.

누구보다, 심지어 백상 자신보다 그를 믿었던 하나뿐인 의형(義兄)에게만큼은 모든 진실을 털어놨더라면.

혹은…….

‘차라리 나 홀로 모든 것을 안고 자결했더라면.’

저벅.

어느 순간 쉼 없이 나아가던 발걸음이 멈췄다. 굳게 닫힌 문을 응시하는 눈은 어느새 붉게 충혈된 지 오래다.

지금 백상의 뇌리에는 지난 밤 들었던 남천마후의 목소리가 울려 퍼지고 있었다.



‘정오. 내일 정오야. 궁에 있는 모든 전사를 내궁으로 소집해.’

‘내일…… 정오입니까.’

‘그래. 당신이 맡은 역할은 거기까지야. 그 후의 일은 우리가 알아서…….’

‘약조.’

‘응?’

‘약조를 지켜 주십시오. 오래전, 저와 했던 약조를.’

‘너, 제법 건방지구나? 감히 어른이 말씀하시는데 말도 끊을 줄 알고.’



남천마후는 웃었고, 백상은 한 치의 망설임도 없이 무릎을 꿇었다.

그리고 그녀는 남만야수궁의 새로운 주인이 바닥에 머리를 찧는 것을 한참이나 지켜본 후에야 그가 간절히 원했던 대답을 들려주었다.



‘예의 바른 아이에게는 상을 줘야겠지. 좋아, 대계가 시작되면 네 집무실로 돌아가.’

‘……집무실이라면.’

‘그래, 바로 이곳이지. 내가 한 약조는 그때 이루어질 거야.’



웃음기 섞인 목소리가 귓가에서 흩어진다. 천천히, 아주 느리게 문을 향해 뻗어지는 백상의 하나뿐인 손이 파르르 떨렸다.

‘어떻게?’라는 의문은 처음부터 들지 않았다.

남천마후가, 암천이 그렇다면 그런 것이다.

지금껏 그들이 보여 준 괴력난신(怪力亂神)과도 같은 일들을 생각하면 더더욱 그러했다.

제아무리 많은 이목이 내궁에 깔려 있다 해도 약조는 지켜질 것이다.

‘드디어.’

드디어 이곳까지 왔다. 지그시 눈을 감자 아득한 기억의 파도가 밀려와 몸과 마음을 잠식한다.

기나긴 인고(忍苦)의 세월.

하지만 이 쓸쓸한 이야기에도 마지막 장은 존재했다. 잠에서 깬 듯 눈을 뜬 백상은 힘주어 문을 열었다.

드륵.

활짝 열어젖힌 문.

그와 동시에 넓은 집무실이 백상의 시야에 들어왔다.

옛 주인의 온기가 남아 있는 간소하면서도 투박한 집기와 오랜 세월을 간직한 탁자.

더불어 이와 같은 집무실 풍경에 어울리지 않게 한 자리를 차지하고 있는 커다란 면경(面鏡).

그리고. 그리고…….

그것이 전부였다.

‘없다. 아무것도.’

믿을 수 없는 현실이 만근의 바위가 되어 한 사람을 짓눌렀다.

텅 빈 공허한 눈빛으로 집무실을 바라보던 백상이 문득 실소를 흘렸다.

“허. 허허. 허허허.”

울지 못해 웃었고, 웃지 않을 수 없어 웃었다.

남천마후는 약조를 지키지 않았다. 수십 년의 세월도. 그간 자신이 저지른 모든 일도 잿가루가 되어 흩날렸다.

그 모든 것이, 결국 이렇게 끝난 것이다.

“으하하하하!”

백상은 파안대소(破顔大笑)했다. 마치 소년 시절로 돌아간 것처럼. 배를 움켜잡고 바닥을 데굴데굴 구르고, 눈물을 줄줄 흘리면서 웃었다.

아니, 울었다.

“으하, 으하하! 으아아아아!”

웃음소리 대신 터져 나온 절규. 백상은 한 줌의 공력조차 실려있지 않은 주먹으로 바닥과 벽면을 후려쳤다.

쾅! 쾅! 콰아앙!

쉴 새 없이 쏘아지는 주먹.

굉음과 함께 박살 난 것은 집무실뿐만이 아니었다.

굳은살로 뒤덮인 손등이 터져 나가고, 주먹을 뒤덮은 핏물 사이로는 언뜻 새하얀 뼈가 내비쳤다.

아프다. 그 어느 때보다.

툭. 투두둑.

점점이 떨어진 핏물이 거미줄처럼 갈라진 바닥에 고인다. 비틀거리며 자리에서 일어난 백상은 창가로 다가갔다.

세상이 멈추었다고 생각한 그와는 달리, 활짝 열린 창밖 너머에서는 모든 것은 지금 이 순간에도 가파르게 돌아가고 있었다.

“크아아악!”

“제, 제발 죽여……!”

- 커륵, 크르륵!

몸과 마음을 잠식하는 마기에 저항하여 몸부림치는 인간과 짐승들.

그리고 끔찍한 비명을 토해 내는 그들을 향해 달려나가는 크고 작은 그림자들.

두두두두!

지축을 울리며 무너진 석벽을 타 넘은 수많은 맹수의 무리가 그들을 덮쳤지만, 그 목적은 살육이 아닌 구조다.

- 크아아앙!

선두에 선 낯익은 백호의 포효와 함께 일사불란하게 움직인 맹수들이 가장 가까운 이들의 팔과 다리, 혹은 목덜미를 물고 외궁을 향해 내달렸다.

이 끔찍한 마기에서 벗어나기 위해.

한 걸음이라도 더, 이들을 빛으로 인도하기 위해.

꾸국.

한껏 말아쥔 주먹. 살갗 깊숙이 파고드는 손톱 끝에 핏방울이 비친다.

고개를 들어 먼 곳을 응시하는 백상의 시선 끝에는 쉼 없이 뒤섞이는 빛과 어둠이 있었다.

구구구궁!

느껴진다. 상상할 수도 없는 거대한 힘의 파동이.

그리고 격돌이 이어질 때마다 조금씩 사그라지는 빛과 계속해서 추락을 거듭하는 한 사람의 모습이.

콰앙! 드드득!

굉음과 함께 튕겨져 나온 신형이 유성처럼 지상으로 내리꽂힌다. 두 개의 전각이 무너지고 땅이 흔들린다.

그러나 그것도 잠시. 푸른 화염은 허공을 딛고 짙은 어둠을 향해 쏘아졌다.

단 한 순간도 쉴 새 없이. 곧 다가올 죽음조차 불태워 버릴 것처럼.

‘진태경.’

왜 그렇게까지 하는 것이냐, 왜.

새어 나오지 않는 물음이 입안에 맴돈다.

가까운 과거, 어두컴컴한 뇌옥의 한 귀퉁이에서 들었던 한 마디는 백상의 귓가에 울려 퍼지고 있었다.



‘얼마나 더 많은 피를 흘릴 셈이냐, 백상.’



백상은 넋 나간 눈빛으로 창밖을 바라보며 뒤늦은 대답을 건넸다.

“모르겠구나. 나도.”

누구에게도 말하지 못한 비밀이다.

그는 아들을 잃은 뒤 복수를 꿈꾸었고, 남천마후를 만나 희망을 보았으며, 어느 순간 돌아올 수 없는 강을 건넌 스스로를 발견하고 절망했다.

그리고…… 그렇게 걸어온 가시밭길의 끝에서 텅 빈 무(無)를 마주하게 되었다.

저벅.

백상은 비틀거리는 걸음으로 창가에서 뒷걸음질 쳤다.

자신의 손으로 직접 그려 낸 지옥도(地獄道)를, 그 지옥도의 완성을 목숨을 바쳐 막으려는 젊은 이방인의 모습을 차마 더 이상 지켜볼 수 없었다.

‘그 모든 것은, 무엇을 위해서였나.’

영원히 답을 찾지 못할 의문과 함께, 창가에서 고개를 돌린 백상의 전신이 순간 석상처럼 굳었다.

“……!”

백상의 시선이 멈춘 곳에는 피와 먼지로 뒤덮인 한 사람이 그를 바라보고 있었다.

모든 것을 잃고 텅 빈 껍데기가 되어 버린. 그저 높은 무위로 세월을 억누르며 괴물로 연명해 온 어느 노인의 모습을, 집무실 한구석을 차지한 커다란 면경(面鏡)이 비추고 있었다.

하지만 백상이 본 것은 그뿐만이 아니었다.

“아.”

휘(輝)아야.

닿지 않을 부름과 함께 그는 손을 뻗었다. 아니, 뻗으려 했다.

적어도 투명하고 매끄럽던 면경의 표면이, 물결처럼 일렁이기 전까지는.

스르르륵.

그 순간. 백상은 비로소 깨달았다.

이 면경을 자신에게 선물한 것이 누구인지.

남천마후가 왜 이곳에서 약조가 이루어질 것이라 했는지.

‘허언(虛言)이…… 아니었다.’

차갑게 식었던 마음속, 사라졌다고 생각한 희망의 불씨가 다시 타오르기 시작한다.

그리고 파르르 떨리는 백상의 눈동자에, 어느덧 혼탁한 어둠으로 물든 면경이 검게 물든 인영(人影)을 토해 냈다.

강기를 머금은 서늘한 검신도 함께.

푸욱!



* * *



팟.

남천마후가 발을 뻗었다. 소년의 손바닥보다도 작은 발.

그러나 창날의 옆면과 맞닿은 순간, 거인의 그것보다 강대한 힘이 전신으로 밀려든다.

드득, 쾅!

- 인간!

수호령의 외침을 들으며, 지상으로 추락한 나는 지면 깊숙이 처박혔다.

등을 통해 전해지는 충격에 저절로 입술이 벌어진다.

쿨럭.

입가를 타고 흐르는 붉은 선혈.

이미 적지 않은 내상(內傷)을 입었고, 금이 간 뼈는 움직일 때마다 삐걱거리며 통증을 호소한다.

‘괴물.’

남천마후는 희대의 썅년이지만, 희대의 괴물이기도 했다. 지금껏 상대한 누구보다, 심지어 서천마군 보다도 더한 무위를 지닌 괴물.

하지만…….

‘일어나야지. 몇 번이라도.’

설령 몇 번이 아니라 몇십 번이라 해도 마찬가지다.

더 이상 물러설 곳은 없다. 단 한 번이라도 뒷걸음질 친다면 그곳이 바로 지옥이다.

나뿐만이 아니라 남만에 존재하는 모든 생명체. 그리고 중원까지 불길에 휩싸일 것이 틀림없다.

‘막아야 해.’

나는 소매로 입가를 문지르며 일어섰다.

그리고 재차 공력을 일으키기도 전에, 지금 내가 처한 이 상황이 아직 최악이라 부르기에는 부족함이 있었다는 사실을 깨달았다.

구구구구궁!

본능적으로 고개를 돌린 나는 볼 수 있었다.

“……이런 시발.”

무너지는 내궁(內宮)의 위로, 짙게 드리워지는 어둠을.
```

## Final English reading copy

```markdown
# Chapter 699

Rumble! Crash!

Unable to withstand the fierce vibrations, the stone walls of the Inner Palace crumbled helplessly, and the iron gate that had broken free slammed into the ground with a heavy roar.

It looked as though a small hill had collapsed.

But Baeksang’s figure slipped past the falling debris and shot forward at tremendous speed.

Whoooosh!

Wind brushed across his entire body. His sharpened senses caught the metallic scent of blood and the screams echoing from every direction.

Feeling the internal energy churning inside him, Baeksang took a deep breath.

*I must not be swept away.*

A massive cliff stood tall behind the Inner Palace like a folding screen.

The demonic qi flowing from the gap in that cliff—a gap that now had to be called a rift—was not something even Baeksang could take lightly.

No. It was precisely because he was a Supreme Peak master that he could move freely through the Inner Palace.

Unless one walked the Demonic Path, even a fairly skilled internal-energy master would have had his internal energy thrown into disarray and lost his composure the moment he entered the demonic qi’s domain.

Just like the middle-aged man now staggering into his path to block him.

“P-Palace Lord? Is that you, Palace Lord?”

It was a face he could never mistake.

A man as greedy as his father, who had inherited the position of tribal chieftain without possessing any particular ability and had lived in comfort and luxury.

That was why he had supported Baeksang more enthusiastically than anyone else.

But the man who had always offered Baeksang oily smiles filled with flattery was now crying out with blood pouring from his seven apertures.

“Please, please save me! I don’t want to die ye—!”

The hand he thrust out desperately brushed against Baeksang’s snow-white collar.

Baeksang quietly looked down at the fallen tribal chieftain, who had lost his balance, and opened his mouth.

“Why should I?”

“P-Palace Lord?”

“You must have known already. That what I intended to do would bring great harm to Nanman.”

“……!”

“We exchanged fair payment for the sake of our respective goals, so please do not consider yourself wronged.”

*I will do the same.*

Along with the words that never escaped his lips, Finger Qi shot from Baeksang’s fingertips.

Puhk!

The tribal chieftain collapsed as the attack pierced the crown of his skull.

His eyes were wide with disbelief. Even in death, his gaze seemed to ask Baeksang a question.

*Why? How could you?*

*How can you still stand so proudly even in the face of this hellscape?*

And Baeksang answered the dead man’s question in his heart.

*Because I had already made up my mind.*

Even so, the breath escaping between his lips trembled.

If that man had begged him to save the tribespeople instead of his own life, would Baeksang have saved them?

No. Perhaps meeting such a peaceful death was actually an act of mercy for a man with such poor martial arts.

Ten thousand.

A full ten thousand. So many warriors and beasts were bleeding and writhing as they were swallowed by the demonic qi.

Their screams seemed to squeeze his heart and claw through his mind like blades.

But Baeksang did not stop walking.

Whoooosh!

His figure shot forward without hesitation and crossed the vast training ground blanketed in screams.

The stable where he and Yayul Cheok had hidden whenever they got into trouble as children, and the storehouse they had entered to steal fruit wine, both slipped past like gusts of wind.

Vengeance. Rage. Regret.

The emotions that had piled up layer after layer with every step whipped around him.

*If only I had not taken my only son to the battlefield. If only I had drawn my sword instead of clasping hands with the Southern Heaven Demon Empress on the day she came.*

*If only I had told the one sworn elder brother who trusted me more than anyone—even more than Baeksang himself—the whole truth.*

*Or perhaps……*

*If only I had carried everything alone and taken my own life.*

Step.

At some point, the footsteps that had advanced without pause came to a stop.

His eyes, fixed on the tightly closed door, had long since become bloodshot.

At that moment, the voice of the Southern Heaven Demon Empress from the previous night echoed through Baeksang’s mind.

“*Noon. Tomorrow at noon. Gather every warrior in the palace in the Inner Palace.*”

“*Tomorrow…… at noon?*”

“*Yes. That is as far as your role extends. After that, we will take care of the rest……*”

“*Our promise.*”

“*Hm?*”

“*Please keep our promise. The promise you made to me long ago.*”

“*You’re rather impudent, aren’t you? You even dare interrupt an adult while she’s speaking.*”

The Southern Heaven Demon Empress had laughed, and Baeksang had knelt without a moment’s hesitation.

Only after watching the new lord of the Nanman Beast Palace repeatedly strike his head against the floor for quite some time did she finally give him the answer he had so desperately wanted.

“*A polite child deserves a reward, doesn’t he? Fine. Once the grand plan begins, return to your office.*”

“*……My office?*”

“*Yes, this very place. The promise I made will be fulfilled then.*”

Her laughter-filled voice scattered beside his ears.

Baeksang’s only hand trembled as he slowly—so very slowly—reached toward the door.

He had never wondered *How?*

If the Southern Heaven Demon Empress and Dark Heaven said it was so, then it was so.

Considering the supernatural powers they had displayed until now, there was even less reason to doubt it.

No matter how many eyes had been placed throughout the Inner Palace, the promise would be kept.

*At last.*

He had finally reached this place.

When he gently closed his eyes, waves of distant memories surged over him and swallowed his body and mind.

Long years of suffering.

But even this lonely story had a final chapter.

As though awakening from sleep, Baeksang opened his eyes and pushed the door open with all his strength.

Creak.

The door swung wide.

At the same time, the spacious office came into view.

Simple, crude furnishings that still held the warmth of their former owner. A table that had preserved the traces of many long years.

And, entirely out of place in such an office, a large mirror occupying one corner.

And then. And then……

That was all.

*It’s gone. There’s nothing.*

The unbelievable reality became a rock weighing ten thousand measures and crushed one man beneath it.

Baeksang stared at the office with hollow, empty eyes, then suddenly let out a hollow laugh.

“Heh. Heh heh. Heh heh heh.”

He laughed because he could not cry, and he laughed because he had no choice but to laugh.

The Southern Heaven Demon Empress had not kept her promise.

Decades of time. Everything he had done during that time.

All of it turned to ash and scattered in the wind.

In the end, everything had ended like this.

“Ha-ha-ha-ha-ha!”

Baeksang burst into uproarious laughter.

As though he had returned to his boyhood, he clutched his stomach, rolled across the floor, and laughed with tears streaming down his face.

No.

He was crying.

“Ha—ha-ha! Aaaaaah!”

A scream burst out instead of laughter.

Baeksang struck the floor and walls with a fist that held not even a trace of internal energy.

Bang! Bang! Krrr-boom!

His fist shot out without pause.

The office was not the only thing shattered by the thunderous impacts.

The callused back of his hand split open, and white bone showed faintly through the blood covering his fist.

*It hurts.*

More than ever before.

Drip. Drip-drip.

Drops of blood fell and pooled in the spiderweb cracks spreading across the floor.

Baeksang staggered to his feet and approached the window.

Unlike him, who thought the world had stopped, everything beyond the wide-open window was still turning rapidly at that very moment.

“Graaah!”

“P-Please, just kill me……!”

—Grrk, grrrk!

Humans and beasts struggled as they resisted the demonic qi devouring their bodies and minds.

And large and small shadows raced toward them as they released horrifying screams.

Thud-thud-thud-thud!

Countless beasts thundered across the ground, climbed over the collapsed stone walls, and descended upon them.

But their purpose was not slaughter.

It was rescue.

—Graaaar!

With the roar of a familiar White Tiger at the head of the group, the beasts moved in perfect formation. They bit the arms, legs, or scruffs of the nearest people and beasts, then raced toward the Outer Palace.

To escape this terrible demonic qi.

To guide them toward the light, even if only one step farther.

Crkk.

Baeksang clenched his fist tightly.

Blood welled at the tips of his nails as they dug deep into his flesh.

He raised his head and stared into the distance.

At the end of his gaze, light and darkness continued to twist together without pause.

Rumble!

He could feel it.

The waves of an unimaginably immense power.

And, each time the clashes continued, the light gradually fading—and the figure of one person continuing to fall.

Boom! Crack!

A figure was blasted away with a deafening roar and plunged toward the ground like a meteor.

Two pavilions collapsed, and the earth trembled.

But only for a moment.

Blue flames stepped on empty air and shot toward the thick darkness.

Without resting for even a single moment.

As though it intended to burn away even the death that would soon arrive.

*Jin Taekyung.*

*Why are you going this far? Why?*

The question that could not escape lingered inside his mouth.

A single sentence he had heard in a corner of a dark underground prison in the recent past echoed beside Baeksang’s ears.

“*How much more blood are you planning to spill, Baeksang?*”

Baeksang stared blankly out the window and finally gave his answer.

“I don’t know. I don’t either.”

It was a secret he had been unable to tell anyone.

After losing his son, he had dreamed of revenge.

After meeting the Southern Heaven Demon Empress, he had seen hope.

Then, at some point, he had discovered himself standing on the other side of a river he could never cross back over, and despaired.

And…… at the end of the thorny path he had walked, he had come face-to-face with an empty nothingness.

Step.

Baeksang staggered backward from the window.

He could no longer bear to watch the hellscape he had drawn with his own hands—or the young outsider who was trying to stop its completion with his life.

*What had it all been for?*

Along with a question he would never find an answer to, Baeksang turned his head away from the window.

His entire body suddenly stiffened like a statue.

“……!”

A blood- and dust-covered person stood where his gaze had stopped, looking back at him.

A man who had lost everything and become an empty shell.

An old man who had merely suppressed the years with his formidable martial arts and survived as a monster.

The large mirror occupying one corner of the office reflected his figure.

But that was not all Baeksang saw.

“Ah.”

*Hwi.*

With a call that could never reach its destination, he extended his hand.

No—he tried to extend it.

At least, until the surface of the transparent, smooth mirror began to ripple like water.

Ssssrrrk.

At that moment, Baeksang finally understood.

Who had given him this mirror.

Why the Southern Heaven Demon Empress had said the promise would be fulfilled here.

*It wasn’t a lie.*

In the heart that had gone cold, the ember of hope he had thought extinguished began to burn once more.

And in Baeksang’s trembling eyes, the mirror, now stained with murky darkness, turned black and spat out a shadowy human figure.

Along with a cold sword blade imbued with Force.

Puhk!

* * *

Flash.

The Southern Heaven Demon Empress thrust out her foot.

It was smaller than a boy’s palm.

But the moment it touched the side of the spearhead, a force more powerful than that of a giant surged through my entire body.

Crack—bang!

—Human!

Hearing the guardian spirit’s cry, I plummeted to the ground and was driven deep into the earth.

The impact traveled through my back, forcing my lips open.

Cough.

A line of red blood ran from the corner of my mouth.

I had already suffered no small amount of Internal Injury, and the cracked bones complained with pain, creaking whenever I moved.

*Monster.*

The Southern Heaven Demon Empress was one of the greatest fucking bitches in history, but she was also one of the greatest monsters in history.

A monster with martial arts more formidable than anyone I had faced until now—even the Western Heaven Demon Lord.

But……

*I have to get up. No matter how many times.*

Even if it was not a few times but dozens of times, it made no difference.

There was nowhere left to retreat.

If I took even one step backward, that place would become hell.

Not only me, but every living thing in Nanman—and even the Central Plains—would inevitably be swallowed by the flames.

*I have to stop her.*

I wiped the blood from the corner of my mouth with my sleeve and stood.

And before I could even summon my internal energy again, I realized that the situation I was in still did not qualify as the worst.

Rumble, rumble, rumble!

I instinctively turned my head.

And I saw it.

“……For fuck’s sake.”

Darkness descending thickly over the collapsing Inner Palace.
```
