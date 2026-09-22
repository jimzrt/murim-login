<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0644.txt",
      "sha256": "30ddd10817e9cf90f2d437996d3a76b96b036e7c95adabc463c9351efb0d8d98",
      "bytes": 14918
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b8ea37734ae97ab850bc49c72604146c722fc78c26a0d6fc6f7857c4b2459e7e",
      "bytes": 2054
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cc07716d8cf955921642a1cb60909f0a00a15f6e0f45a300b391b0e2befd9647",
      "bytes": 198320
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "f53130a3a7340324f58e291deaa3c97132bec85d33e518c7c51ca68db4ab3161",
      "bytes": 705
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "e95b254283ad756dc7af1cd3971e70e95e95677d5d89fcc1d38cf06ea43a83cc",
      "bytes": 560
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "7b9903d15397144f93082657bfb165f15988df8a8521a6285fdc524c575a4d8c",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "22afcf8b738d2bb21481a3f04830f62d0add0db580dd9092743d30e21dcefc9a",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "49618ada00062021d16a381a1d0e6b0785142603412b4e5c07238e823093bba4",
      "bytes": 623
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "546d131483445e6040bf016086641b17fdb3f9b0edbf828f8a75a7224eabca7b",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3a2f95c0b801f164fe6c82f55a296cb4b9b0ac84ac2ddcb52c61dc781b426bd0",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8f2bd622803d80781e7c5d9f5e162de756b52e967a07c90b7db116d9de3dd3f2",
      "bytes": 622
    },
    {
      "path": "characters/Qilian Three Fiends.md",
      "sha256": "e09a8c08f22465eeb5237810c6d77de7c144a4524207cd528c682d3182a7f030",
      "bytes": 637
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "84815df9d5aa1c7702b19f76b4ef8e95833d73cde592e272bffdc286ccc6cb62",
      "bytes": 888
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "8d6f54cd26fac1837156f6bbb1b91b6fa6b7629a1c6c3955d8ed93918d0bb1dd",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4794cdd387e34c919af6c0815be1f611eaec2400b5c875cfc21b325ce12e4055",
      "bytes": 203614
    }
  ],
  "estimated_tokens": 13580
}
-->

# Durable State Update — Chapter 644

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 644. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 644. Profile updates may replace only one
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
  "chapter": 644,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 644,
    "continuity_sources": [644],
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
    "Jin Taekyung has been admitted to the Nanman tribal grand council with majority support.",
    "Yayul Cheok formally authorized Jin's attendance as Palace Lord and great chieftain of the Miao people.",
    "Baeksang opposed Jin's admission but accepted the majority decision without blocking it.",
    "Chieftains support Jin because he saved their people at Ailao Mountain or because their tribes owe historical debts to the Fire King and Fire Gate Clan.",
    "The Quest [Tribal Grand Council] has been created.",
    "Approximately two hundred elite warriors of Ailao Mountain remain alive inside the Thousand-Year Spider webs and await evacuation.",
    "The Thousand-Year Spider webs appear to shield their victims from the Poison Mist.",
    "The missing ferocious beasts have not been found in the Poisonblood Grounds.",
    "Dark Heaven's involvement in the Thousand-Year Spider attack remains suspected but unconfirmed.",
    "The purpose of Ailao Mountain's Wraith remains unknown.",
    "The nature of the pure-white eggs in the Poisonblood Grounds remains unknown.",
    "An unidentified entity who knows Jin Taekyung has killed two informants after learning of his council attendance and implied a long-standing prior connection."
  ],
  "continuity_sources": [
    643
  ],
  "open_questions": [
    "Who is the hidden entity that recognizes Jin Taekyung, and what is the nature of their past connection?",
    "Where did the missing ferocious beasts go?",
    "Did Dark Heaven influence the Thousand-Year Spider attack, and why did it occur on the final day of the tribal competition?",
    "What does Ailao Mountain's Wraith intend to do?",
    "What are the pure-white eggs in the swamp, and what will emerge from them?"
  ],
  "safe_through": 643,
  "temporary_decisions": [
    "Use Tribal Grand Council for 부족 대회의.",
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사.",
    "Use black frog for 흑와.",
    "Use golden bee for 금봉."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 사천     | **Sichuan**            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 기련삼괴 | **Qilian Three Fiends** | Three identical brothers from the Qilian Mountains. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 음양 | **Yin and Yang** | Paired energies whose harmony has been disrupted in Jeok Cheongang. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 음양쌍귀 | **Yin-Yang Twin Ghosts** | Source spelling for the pair otherwise associated with the Yin Ghost and Yang Ghost. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 서천마군 | 기련삼괴 | commander_to_subordinates | Three Fiends; Three Old Men | mocking and superior | Calls them 삼괴 and then mockingly says they may now be called 삼노. |
| 기련삼괴 | 서천마군 | subordinates_to_commander | my lord | fearful and deferential | The brothers greet the Western Heaven Demon Lord as 마군. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 삼괴 | interrogator_to_captured_enemy | Three Fiends | threatening and coercive | Taekyung addresses the captured fiend by his collective sobriquet while demanding information about Dark Heaven, Hubei, and the Dongting Fisherman. |
| 삼괴 | 진태경 | captured_enemy_to_interrogator | you bastard | defiant and profane | The Three Fiends curses Taekyung, challenges him to remove the seal, and demands death rather than continued torture. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 643
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he opposes the Nanman Beast Palace joining the Murim Alliance and Jin Taekyung's attendance at the tribal grand council.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 643
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 614
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 643
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 642
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 643
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 643
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 643
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Qilian Three Fiends.md

# Qilian Three Fiends (기련삼괴)

- **Safe through:** Chapter 451
- **Aliases:** Three Fiends
- **Role:** First Fiend and at least one other brother are dead, the Third Fiend has been captured by Mungyeong, and the Second Fiend's fate remains unknown.
- **Personality:** Bloodthirsty and notorious throughout Qinghai, but fearful and submissive before the Western Heaven Demon Lord.
- **Voice:** The brothers speak in near-unison with frightened, deferential phrasing.
- **Relationships:** They serve the Western Heaven Demon Lord and address him as their superior.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 614
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 642
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃644화



띠링. 띠링. 띠링.



- 퀘스트, [부족 대회의]가 생성되었습니다!

퀘스트



[부족 대회의]



당신은 남만야수궁 역사 최초로 부족 대회의에 참석할 자격을 얻은 외지인이 되었습니다.

이는 과거 열화문의 오 대 문주조차 이루지 못했던 업적입니다.

왜냐하면 그는 대회의가 열리기도 전에 오독문을 멸문시키고 떠났거든요!

남만의 대소사가 결정되는 이 중대한 회의에서, 당신은 지금 할 수 있는 최선의 결과를 도출해 내야 합니다!



등급 : 초절정

제한 : 진태경

임무 : 남만야수궁의 입맹(入盟) (미완료)

보상 : ???

실패 : ???





나는 퀘스트 창을 바라보며 내심 한숨을 내쉬었다.

제아무리 나를 향한 여론이 호의적으로 변했다고는 하지만 남만야수궁을 입맹시키라니. 초절정이라는 퀘스트 등급만큼이나 빡센 임무다.

‘그 와중에 오 대 문주 무엇…….’

역시 열화문이라고 해야 하나?

일인전승(一人傳承)으로 수백 년간 이어져 내려온 유서 깊은 깡패 문파답다.

열화문의 역대 문주 중에서는 초야에 묻혀 장수한 이도, 무림에 나가 불꽃처럼 타오르고 단명한 이도 있었지만 늘 천하에서 다섯 손가락 안에 드는 신위를 지닌 괴물들이었다고 들었으니까.

‘아마 내가 이 자리에 앉을 수 있는 이유 중 하나겠지.’

무려 이백여 년 전의 일이라고는 해도 남만야수궁과 열화문은 제법 밀접한 관계가 있다.

K-무림식 해석으로는 단군 할아버지 절친이 세운 문파, 뭐 그쯤 되겠지.

문제는 내가 사람 패는 데에는 재주가 있어도, 설득하는 것에는 영 재능이 없다는 거다.

‘그래도 최선을 다해 봐야지.’

허리를 곧게 편 나는 탁자를 중심으로 자리한 서른두 명의 부족장들을 바라보았다.

가장 상석에는 야수묘왕. 그의 좌우로는 대족장인 백상과 요희, 흑웅이 차례대로 앉아 있었고 나머지 사람들은 세력 순에 상관없이 자리를 배정받은 듯했다.

비록 숫자는 적지만, 이들 한 사람 한 사람이 적게는 수백 이상, 많게는 수만의 부족민을 거느린 부족장이라는 것을 생각해 보면 오늘의 이 자리는 남만, 그 자체나 다름없다.

그리고 내가 그들의 면면을 훑던 그때, 상석에 자리한 야수묘왕이 짧은 침묵을 깨트렸다.

“자, 그럼.”

진중한 표정과 위엄 어린 눈빛. 마침내 입을 연 그의 모습에 장내의 공기가 활시위처럼 팽팽하게 당겨진다.

남만야수궁의 주인다운 카리스마를 흘린 야수묘왕이, 근엄한 목소리로 대회의를 시작을 알리는 역사적인 한 마디를 내뱉었다.

“다들 식사는 하고 왔나?”

“……?”

“요새 안 좋은 일들이 있었지만 그래도 끼니는 거르지 말아야지. 특히 장 족장은 작년에 비해 살이 좀 빠진 것 같은데?”

“……!”

역사적이긴 시부럴 거.

‘내가 지금 뭘 들은 거지.’

생각지도 못했던 첫 마디에 귀를 의심하고 있던 그때. 조금 전 내게 가장 먼저 포권을 취했던 장 족장이 대답했다.

“역시 궁주님 눈썰미는 못 속이겠군요. 사실 조금 빠졌습니다.”

아니. 이걸 받아 준다고?

“그럴 줄 알았네. 하지만 부족장이라는 사람이 그래서야 쓰나. 부족민들을 생각해서라도 스스로 몸을 보살펴야지. 그런데 자네 나이가 어떻게 되더라?”

“환갑입니다.”

“창창하군. 앞으로 더 먹게.”

“존명.”

이제는 환청까지 왔는지, 존명이 좆망으로 들린다.

‘남만 좆망.’

이게 내가 생각했던 부족 대회의가 맞나.

나는 아연한 표정으로 서른두 명의 부족장들을 바라봤다.

남만 전체를 대표하는 그들은, 야수묘왕의 첫 마디를 신호탄 삼아 듣는 것만으로도 가슴이 조촐해지는 대화를 곳곳에서 주고받는 중이었다.

“갈 족장, 소식 들었어. 여섯째가 성인식을 치렀다며?”

“일곱째일세.”

“내가 헷갈렸군. 자네가 자식을 한둘 낳았어야지. 아무리 기운이 좋아도 열다섯 명이나 낳는 게 말이 되나?”

“열일곱 명일세.”

“……작년 대회의 때는 분명히 열다섯이었는데?”

“둘 더 낳았네. 쌍둥이로.”

“아.”

한쪽에서는 남만 축구 리그 창설을 노리는 게 아닌가 의심되는 슈퍼 정자맨의 대화가.

“구 족장. 얼마 전에 훔쳐 간 가축 돌려놔.”

“뭔 놈의 가축?”

“목초지에서 감쪽같이 사라진 젖소 쉰두 마리. 자네 부족민들 짓인 거 모를 줄 알았나?”

“그런 적 없네.”

“네놈이야 당연히 그렇게 말하겠지. 지금 좋게 말할 때 돌려놔.”

“아, 진짜! 그런 적 없다니까!”

“좋게 말할 때 젖소 내놓으라고! 이 젖소 젖 같은 새끼야!”

다른 한쪽에서는 그 많던 젖소는 누가 다 훔쳐 갔을까에 관한 격렬한 고성이.

“마치 어제의 기억처럼 떠오르는군. 네놈들이 우리 부족의 영역을 침범하던 그 날이.”

“아, 이 인간은 매년 이 지랄이네. 아직 불혹밖에 안 된 주제에 팔십 년 전 일을 왜 자꾸 들먹여?”

“나는 선조들의 혼을 물려받았으니까. 그런 의미에서 땅 내놔.”

“그게 말이 되나? 선대에서 마무리된 일을 왜 자꾸 끌어오냐고!”

“땅 내놔.”

“아니 진짜…….”

“땅 내놔.”

또 다른 구석에서는 환생설을 주장하는 땅귀신의 밀고 당기기가 이어지는 중이다.

그리고 이 모든 상황을 황당하게 바라보던 내 귓가에 한 사람의 전음이 파고들었다.

- 웃긴 표정이네.

나는 슬쩍 고개를 돌려 전음의 주인을 찾았다. 동시에 이쪽을 바라보며 재밌다는 듯 웃고 있는 요희와 눈이 마주쳤다.

- 부족 대회의는 늘 이래. 뭐, 남만 곳곳에 흩어져 있다가 일 년에 단 한 번 모이니까 당연하기도 하지만.

잠시 고민하던 나는 솔직하게 대답했다.

- 그걸 감안해도 너무 개판인데.

- 부족 대회의는 남만 전체의 대소사(大小事)를 다루는 자리야. 말 그대로 작은 일 역시 회의 내용에 포함된다는 뜻이지.

- ……그 일이 작아도 너무 작은데?

- 서른두 개나 되는 부족이 어떻게 화합하며 살아가겠어? 모두가 모인 자리에서 하나씩 결정짓는 거지. 그렇게 앙금을 푸는 거고.

콰당!

“야, 이 개샛끼야!”

“아니, 이 새끼가 미쳤나…….”

“네가 그렇게 무공이 강해? 입 닥치고 따라 나와.”

젖소에 관해 격론을 벌이다가 마침내 멱살을 움켜잡은 두 족장을 바라본 요희가 덧붙였다.

- 물론 예외도 있지.

- …….

- 금방 정리될 거야. 진짜 대회의는 그때부터가 시작이지.

“아. 땅 줘. 땅 달라고.”

“허어어. 이 천년지주 같은 새끼.”

“그러고 보니까 천 년 전에 우리 조상님들께서…….”

“그만! 그마아아안!”

금방 정리된다라.

음. 아닐 것 같은데.

‘진짜 야만인 새끼들인가……?’

내가 차마 말하지 못한 진심을 마음속으로 중얼거리던 그때, 요희의 말처럼 혼란스럽던 주위 상황이 하나둘씩 빠르게 정리되더니 새로운 이야기가 흘러나오기 시작했다.

“이번 맹수 토벌에서 만족 전사 서른 명이 부상을 입고, 스물둘이 죽었습니다. 근래 들어 유난히 기승을 부리고 있는 듯하니 피해가 더 커지기 전에 내궁에서 나서 주시길 요청하는…….”

“갑작스럽게 내린 폭우로 홍수가 발생했습니다. 목초지를 비롯한 인근 가호(家戶) 오십여 채가 물에 잠겼고…….”

“황족과 둥족의 분쟁이 종결되었음을 이 자리에서 보고드립니다. 양 측은 합의에 따라 공식 서안을 작성했으며, 향후 십 년간 평화를…….”

맹수 토벌에 관한 상황. 재난 재해와 분쟁.

전채 요리가 끝나자 슬슬 메인 디쉬가 나오기 시작한다.

그리고 그렇게 흘러나오는 이야기들 중에는 제법 신경 써야 할 정보들 역시 포함되어 있었다.

“북동쪽에서 괴인(怪人)이 나타났다고 합니다.”

괴인?

내 의문과 동시에, 지금껏 짧은 대답과 함께 고개만 끄덕이던 야수묘왕이 자세를 바로 세우며 입을 열었다.

“괴인이라. 이 이야기는 처음 듣는 듯한데.”

“저어. 그것이…….”

맨 처음 괴인에 관한 이야기를 꺼낸 부족장이 반신반의하는 표정으로 대답했다.

“확실한 정보는 아니라 자신 있게 말씀드릴 수는 없습니다만…….”

“정보의 출처가 어딘가?”

“사흘 전, 북동쪽의 경계를 넘어온 한족 하나를 붙잡았는데 그자가 알려 주었습니다. 갑작스럽게 나타난 정체 모를 괴인이 귀주(貴州)에서 피바람을 일으키고 있다더군요.”

귀주성은 사천, 광서와 함께 남만과 맞닿아 있는 접경지다. 과장 조금 보태자면, 엎어지면 코 닿을 거리라고 해도 과언이 아닐 정도다.

‘그런데 귀주에서 괴인이 나타나? 이렇게 갑자기?’

찜찜하다. 아니, 찜찜하다 못해 거슬릴 정도다. 그리고 괴인의 정체만큼이나 알 수 없는 낌새를 알아차린 것은 나뿐만이 아니었다.

“더 자세히.”

눈살을 찌푸린 야수묘왕의 모습에 부족장이 마른침을 꿀꺽 삼켰다.

“괴인의 이름도, 나이도 밝혀진 바가 없습니다. 다만 중원의 승려들처럼 민머리에 한 자루 선장(禪杖)을 들고 다니며 지금껏 귀주성에서만 기백 명을 쳐 죽였다고 했는데, 그 때문인지 혈승(血僧)이라는 별호로 불린다고 합니다.”

“혈승?”

“예. 제가 붙잡은 그 한족도 제법 뛰어난 무림인으로 보였지만, 혈승에 관하여 이야기할 때에는 두려움을 금치 못했습니다.”

혈승이라는 살벌한 별호도 그렇지만, 실로 엄청난 무공의 소유자임이 틀림없다.

‘귀주도 엄연히 정파의 영역. 무림맹이 손 놓고 있을 리는 없었을 텐데.’

그럼에도 불구하고 기백 명을 쳐 죽이며 악명을 떨치다니. 최소 초절정의 무위가 뒷받침되지 않고서야 불가능한 일이다.

게다가 놈이 나타난 장소가 하필 남만과 인접한 귀주성이라는 것도 마음에 걸렸다.

‘혹시.’

기묘한 시기에 갑작스럽게 나타난 정체불명의 괴인. 정파의 영역인 귀주성을 단신으로 휩쓸 만큼의 무위.

나로서는 암천과의 연관성을 생각하지 않을 수 없었다. 설령 남천마후와 같은 급의 거물이 아니더라도 가능성은 충분하다.

혈주와 서천마군 역시 음양쌍귀(陰陽雙鬼)나 기련삼괴(祁連三怪)와 같은 초절정 고수들을 휘하에 두었으니까.

‘그리고 그 혈승이라는 놈의 목적이 남만이라면……?’

거기까지 생각이 다다른 내가 부족장을 향해 처음으로 입을 뗐다.

“그 혈승이라는 자가 어디로 향하는지 알 수 있습니까?”

“본인도 물어보고 싶었지만, 지금은 알 방도가 없소.”

“그게 무슨…….”

옅은 한숨과 함께 고개를 내저은 부족장이 대답했다.

“그가 죽었소.”

“예?”

“더 물어볼 것도 없이 죽어 버렸단 말이오. 애당초 상당한 부상을 입고 있었던데다가, 갑작스럽게 바뀐 환경에 적응하지 못했던 것 같소. 때마침 내린 폭우로 홍수가 나는 바람에 제대로 된 조치도 취하지 못했지.”

“……!”

혈승의 등장. 그리고 지금으로서는 유일했던 증인의 사망.

정적이 좌중에 내려앉은 그때. 대회의가 시작된 직후부터 계속해서 침묵을 지키던 한 사람이 불쑥 입을 열었다.

“부상과 풍토병. 그리고 죽음이라. 종종 있는 일이지.”

갑작스러운 누군가의 목소리에 사람들의 시선이 한 곳을 향해 쏠린다.

백상. 바로 그였다.

“중원에서 살성(殺星)이 나타난 것 역시 마찬가지요. 한족들은 늘 그랬지. 그들은 한 부족임에도 불구하고 서로를 죽고 죽이며 지금의 천하를 유지시켜 왔소. 한 마디로…….”

담담한 어조. 그리고 담담하기 그지없는 표정. 백상의 서늘한 목소리가 이어졌다.

“중원의 일에 하등 신경 쓸 이유가 없다는 뜻이오. 적어도 우리 남만은.”

지금 든 이 생각이 단순한 착각인지는 모르겠다.

하지만 한 가지 확실한 것은, 지금 이 이야기가 내게는 묘하면서도 이질적으로 느껴졌다는 것이다.

남만에서 둘째가는 세력과 부족민을 지닌 백족의 대족장이, 바로 옆에서 벌어지는 일조차 무시하려 하다니.

그리고 그런 백상을 말없이 응시하던 나는 문득 입을 열었다.

“만약 혈승이 남하하고 있다면 어쩌시겠습니까?”

내 말이 뜻하는 바를 알아챈 부족장들은 눈을 크게 떴고, 백상은 한 치의 흔들림도 없이 대답했다.

“귀주와 맞닿아 있는 것은 이곳 남만뿐이 아니다. 광서(廣西)를 지나면 드넓은 망망대해가 펼쳐져 있고, 순풍을 타고 바다로 열흘을 나아가면 해남(海南)에 이를 수 있지.”

“말인즉슨, 혈승이 남만을 침범할 가능성은 낮다?”

“놈이 구태여 이곳까지 올 이유가 무엇이겠느냐. 독물과 맹수, 그리고 수많은 남만의 전사들을 상대하느니 광서를 통해 바다로…….”

“있습니다. 단 한 가지 분명한 이유가. 그런데…….”

이어지려는 목소리를 힘주어 끊어 낸 나는, 가라앉은 눈빛으로 백상을 응시하며 말을 이었다.

“참 희한하게도, 혼자만 그 사실을 모르시는 것 같네요.”

“뭐라?”

“아니면…… 마치 처음부터 모르는 척하기로 누군가와 약속이라도 한 겁니까?”

그 순간.

화륵. 훅.

위태롭게 흔들리던 횃불이 사라진다.

그리고 드넓은 대전에 내려앉은 암전(暗轉) 속, 시리도록 차가운 한기를 내뿜는 한 쌍의 눈동자가 있었다.

“네놈이 기어이, 선을 넘는구나.”

솨아아아악!

“글쎄.”

사방에서 전신을 옥죄어 오는 거대한 기파를 느끼며, 나는 담담하게 뇌까렸다.

“선은 그쪽이 넘으시는 것 같은데?”
```

## Final English reading copy

```markdown
# Chapter 644

*Ding. Ding. Ding.*

> **System**
>
> - A new Quest, **Tribal Grand Council**, has been created!
>
> **Quest**
>
> **Tribal Grand Council**
>
> You have become the first outsider in the history of the Nanman Beast Palace to earn the right to attend the tribal grand council.
>
> This is an achievement that even the Fire Gate Clan’s fifth Sect Leader of the past failed to accomplish.
>
> Why? Because he destroyed the Five Poisons Sect and left before the grand council could even begin!
>
> At this momentous meeting, where the major and minor affairs of Nanman will be decided, you must achieve the best possible result!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Nanman Beast Palace’s entry into the alliance *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

I stared at the Quest window and inwardly sighed.

No matter how favorably public opinion had shifted toward me, getting the Nanman Beast Palace to join the alliance was no simple task. It was every bit as brutal as the Quest’s Supreme Peak Grade suggested.

*And what was that bit about the fifth Sect Leader…?*

The Fire Gate Clan really was something else.

They were a venerable sect of thugs that had continued for hundreds of years through one-person succession.

Among the successive Sect Leaders of the Fire Gate Clan, I had heard that some had lived long lives secluded from the world, while others had gone out into the Murim, burned like flames, and died young. But every one of them had been a monster whose might ranked among the top five in the world.

*That’s probably one of the reasons I’m allowed to sit here.*

Though it had happened more than two hundred years ago, the Nanman Beast Palace and the Fire Gate Clan had been fairly close.

By K-Murim logic, it was basically a sect founded by Grandfather Dangun’s best friend.[^1]

[^1]: Dangun is the legendary founder of Korea’s first kingdom; “Grandfather Dangun” is a familiar, joking way to invoke remote shared ancestry.

The problem was that while I had a talent for beating people up, I had absolutely no talent for persuasion.

*Still, I have to do my best.*

I straightened my back and looked at the thirty-two chieftains seated around the table.

The Beast Miao King occupied the highest seat. To his left and right sat the great chieftains Baeksang, Yohi, and Heugung, in that order, while the others appeared to have been assigned their seats without regard to the strength of their factions.

There might not have been many of them, but each and every one was a chieftain commanding anywhere from several hundred to tens of thousands of tribespeople.

When I considered that, this gathering was practically Nanman itself.

And just as I was studying their faces, the Beast Miao King, seated at the head of the table, broke the brief silence.

“Well, then.”

His expression was solemn, and his gaze was filled with dignity. At last, he opened his mouth, and the air in the room drew taut like a bowstring.

The Beast Miao King radiated the charisma befitting the master of the Nanman Beast Palace and uttered a historic first sentence in a grave voice.

“Did everyone eat before coming here?”

“……?”

“We’ve had some unpleasant things happen lately, but you still shouldn’t skip your meals. In particular, Chief Jang, you seem to have lost a little weight compared to last year.”

“……!”

*Historic, my ass.*

*What did I just hear?*

While I was still doubting my ears at that completely unexpected opening, Chief Jang—the first person to offer me a cupped-fist salute earlier—answered.

“As expected, nothing gets past the Palace Lord’s keen eyes. I have lost a little weight, in fact.”

*No. He’s actually going along with this?*

“I thought so. But a man who calls himself a chieftain cannot be neglecting himself like that. You should take care of your health for the sake of your tribespeople. Now, how old are you again?”

“I am sixty.”

“You’re still in the prime of life. Eat more from now on.”

“Jonmyeong.”[^2]

Now I was hearing things too, because *jonmyeong* sounded like *jonmang*—“fucked.”

*Nanman is fucked.*

[^2]: *Jonmyeong* is a formal acknowledgment meaning “As you command”; it differs by one vowel from *jonmang*, crude slang for being utterly ruined.

I looked at the thirty-two chieftains with a dazed expression.

Representing all of Nanman, they had taken the Beast Miao King’s first words as a starting signal and were now exchanging conversations in various corners that made my heart feel cramped just listening to them.

“Chief Gal, I heard the news. Your sixth child had their coming-of-age ceremony?”

“My seventh.”

“I got confused. If only you’d stopped at one or two. No matter how vigorous you are, how can you have fifteen?”

“Seventeen.”

“……At last year’s grand council, you definitely had fifteen.”

“I had two more. Twins.”

“Oh.”

On one side was a conversation with a super-sperm man who seemed intent on founding a Nanman soccer league.

“Chief Gu. Return the livestock you stole a while ago.”

“What livestock?”

“The fifty-two dairy cows that vanished from the pasture without a trace. Did you think I wouldn’t know your tribespeople did it?”

“I have never done such a thing.”

“Of course you’d say that. Return them while I’m still asking nicely.”

“Oh, for real! I said I never did that!”

“I said hand over the cows while I’m asking nicely! You cow-udder bastard!”

On the other side, a furious argument raged over the question of who had stolen all those cows.

“It comes back to me as clearly as yesterday—the day you bastards trespassed into our tribal territory.”

“Damn it, this guy does this every year. You’re barely forty, so why do you keep bringing up something that happened eighty years ago?”

“I inherited the spirits of my ancestors. In that sense, hand over the land.”

“How does that make any sense? Why do you keep dragging up something that was settled by the previous generation?”

“Hand over the land.”

“No, seriously……”

“Hand over the land.”

Elsewhere, a land ghost insisting he had been reincarnated continued his back-and-forth struggle.

And while I was watching this entire absurd situation, someone’s voice slipped into my ear through Sound Transmission.

—You have a funny expression.

I subtly turned my head to find the owner of the voice. At the same time, my eyes met Yohi’s as she looked in my direction and smiled as though she were enjoying herself.

—The tribal grand council is always like this. Well, everyone is scattered across Nanman and only gathers once a year, so I suppose it’s natural.

After thinking for a moment, I answered honestly.

—Even taking that into consideration, this is too much of a shitshow.

—The tribal grand council is where all the major and minor affairs of Nanman are discussed. Literally, that means even small matters are included in the meeting.

—……That matter is way too small, though.

—How else could thirty-two tribes live together in harmony? They settle things one by one when everyone is gathered. That is how they clear away old grudges.

*Crash!*

“You goddamn mutt!”

“Has this bastard lost his mind……?”

“You think your martial arts are that strong? Shut your mouth and come outside.”

I watched the two chieftains who had finally grabbed each other by the collars after their heated argument over the cows. Yohi added:

—Of course, there are exceptions.

—……

—It’ll be settled soon. The real grand council starts after that.

“Ah. Give me land. I said give me land.”

“Gaaah. You Thousand-Year Spider bastard.”

“Come to think of it, a thousand years ago, our ancestors……”

“Stop! Stoooop!”

*It’ll be settled soon,* she said.

Hmm. I didn’t think so.

*Are these people really just a bunch of barbarians……?*

I was muttering the thought I could not bring myself to say aloud when, just as Yohi had said, the chaotic situation around us began to settle one piece at a time, and new topics started flowing in.

“Thirty Man warriors were wounded and twenty-two were killed in this year’s ferocious-beast hunt. The beasts seem to have become especially rampant lately, so before the losses grow any larger, we request that the Inner Palace take action……”

“Sudden torrential rain caused a flood. The pasture and around fifty nearby homes were submerged……”

“I hereby report that the dispute between the Huang and Dong tribes has come to an end. In accordance with the agreement, both sides have drawn up an official document, and peace will be maintained for the next ten years……”

The situation surrounding the ferocious-beast hunt. Natural disasters and disputes.

Once the appetizers were finished, the main dishes began to arrive.

And among the stories being brought up, there was also information that demanded some serious attention.

“They say a strange figure has appeared in the northeast.”

*A strange figure?*

As the question arose in my mind, the Beast Miao King—who until then had merely nodded along with short replies—straightened his posture and spoke.

“A strange figure. This is the first I have heard of it.”

“W-well, the thing is……”

The chieftain who had first brought up the matter of the strange figure answered with an uncertain expression.

“I cannot speak with confidence because the information has not been confirmed……”

“Where did the information come from?”

“Three days ago, we captured a Han Chinese man who had crossed the northeastern border. He told us about it. Apparently, an unidentified strange man appeared out of nowhere and is stirring up a bloodbath in Guizhou.”

Guizhou was a border region touching Nanman, along with Sichuan and Guangxi. With a little exaggeration, it was practically close enough to trip and bump your nose against.

*But a strange man appeared in Guizhou? So suddenly?*

It felt wrong. No, it felt more than wrong—it grated on me.

And I was not the only one to sense that something was just as inscrutable as the strange man’s identity.

“More details.”

At the Beast Miao King’s furrowed brow, the chieftain swallowed nervously.

“Nothing is known about the strange man’s name or age. However, they say he is bald like the monks of the Central Plains and carries a single Zen staff. He has beaten several hundred people to death in Guizhou alone, and because of that, they say he is known by the sobriquet Blood Monk.”

“Blood Monk?”

“Yes. The Han Chinese man we captured appeared to be a fairly skilled martial artist himself, but he could not hide his fear whenever he spoke about the Blood Monk.”

The Blood Monk was frightening enough as a sobriquet, but there was no doubt that its owner possessed truly astonishing martial arts.

*Guizhou is unquestionably orthodox faction territory. The Murim Alliance couldn’t possibly have just stood by and done nothing.*

And yet the man had killed several hundred people and earned a notorious reputation. It would have been impossible without at least Supreme Peak-level martial prowess.

Besides, it bothered me that he had appeared in Guizhou—a region directly adjacent to Nanman.

*Could it be……?*

An unidentified strange man who had appeared out of nowhere at an unusual time. Martial prowess powerful enough to sweep through Guizhou, a land of the orthodox faction, single-handedly.

I could not help but consider a connection to Dark Heaven. Even if he was not a great figure on the level of the Southern Heaven Demon Empress, the possibility was more than sufficient.

The Blood Lord and the Western Heaven Demon Lord had also kept Supreme Peak masters such as the Yin-Yang Twin Ghosts and the Qilian Three Fiends under their command.

*And what if the Blood Monk’s target is Nanman……?*

When my thoughts reached that point, I spoke to the chieftain for the first time.

“Is it possible to know where the Blood Monk is headed?”

“I would have liked to ask him myself, but there is no way to know now.”

“What do you mean……”

The chieftain shook his head with a faint sigh and answered.

“He is dead.”

“What?”

“He died before I could ask him anything else. He was already suffering from serious injuries, to begin with, and it seems he was unable to adapt to the sudden change in environment. A torrential rain came down at just the wrong time and caused a flood, so we could not take proper measures.”

“……!”

The Blood Monk’s appearance.

And now, the death of the only witness we had.

As silence descended over the room, someone who had remained silent since the grand council began abruptly spoke.

“Injury, endemic disease, and death. Such things happen from time to time.”

At the sudden voice, everyone’s gaze turned toward the same place.

Baeksang.

It was him.

“The Slaughter Saint appearing in the Central Plains is no different. Han Chinese have always been that way. Despite being one people, they have maintained the present world by killing and being killed among themselves. In short……”

His tone was calm, and his expression was utterly composed. Baeksang’s cold voice continued.

“There is no reason to pay the slightest attention to affairs in the Central Plains. At least not for Nanman.”

I did not know whether the thought that came to me then was merely a misunderstanding.

But one thing was certain: this conversation felt strange and alien to me.

Baeksang was the great chieftain of the Bai people, who possessed Nanman’s second-largest faction and the second-largest population. And yet he was trying to ignore an event unfolding right beside him.

As I silently stared at Baeksang, I suddenly opened my mouth.

“What will you do if the Blood Monk is heading south?”

The chieftains who understood what I meant opened their eyes wide, while Baeksang answered without a hint of wavering.

“Nanman is not the only place bordering Guizhou. If he passes through Guangxi, a vast open sea spreads before him. With a favorable wind, he can reach Hainan after sailing for ten days.”

“Meaning that the possibility of the Blood Monk invading Nanman is low?”

“What reason would he have to come all the way here? Rather than face venomous beasts, ferocious beasts, and countless Nanman warriors, he could simply head to the sea through Guangxi……”

“There is one reason. A single, unmistakable reason. But……”

I forcefully cut him off before he could continue, fixing Baeksang with a grave, steady gaze as I went on.

“Strangely enough, you seem to be the only one who doesn’t know that.”

“What?”

“Or……”

I paused before continuing.

“Did you make some kind of agreement with someone to pretend from the very beginning that you didn’t know?”

At that moment—

*Fwoosh. Whoomph.*

The wavering torchlight went out.

And amid the darkness that descended over the enormous hall, there was a pair of eyes radiating a piercing, icy chill.

“You have finally crossed the line.”

*Whoosh!*

“Well.”

I felt the enormous martial aura squeezing my entire body from every direction and muttered calmly.

“It seems you’re the one crossing the line.”
```
