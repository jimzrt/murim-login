<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0614.txt",
      "sha256": "f6fdbd77688349571aae98e27dc1c8d8dab0fc4b9b64ddb5291ab332187dcaaa",
      "bytes": 13721
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "deff27302ef38aac4e749f6b0cd5a439ba0029fd31bc01a814c8c1577367d0fc",
      "bytes": 2796
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "da4ddc5a415839d9fe26fbd9ae4790c8da7a6c1784f917dc973a6606dfe1e279",
      "bytes": 190794
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "2baa9e7c8574a66301cfb2740d8e60c446ddc10b76df49132f07d60647f637b0",
      "bytes": 803
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "750239958fde168052410e7e3f2d1a7efa1d123aefd8e760480c45b73f2247af",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "4c3ebb803ccc80637763ceabf9c9f170ca51571b4c2f03fad8535366240ad9f9",
      "bytes": 1147
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "51dea74617c55b2a5c23753fb8ee917f810a18cf4e5354165b6315b8caa7d61d",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "879e1adff31b42d4a0b512dbd4083b14e1121838c30a77e44f9b83f0ae7ebc67",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "2dbe0968d6552816797df71930b96f43530e06158363aa5e063911be6699d243",
      "bytes": 959
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "aae984a63b6aa0911bf9c3cb7359d8fff023a14f6c58725910202b47740bc7ea",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "d4539dcc76ae97c9fb1a83d7100fae87c59b38bc4c45630f066e90b3a294ec1c",
      "bytes": 811
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "72c6b0bd55235a21593394a68d69e17e116e5e7c272b6c81ed172e33e18c4881",
      "bytes": 528
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "036777e18b8d1bbb0c267898a33041b1f3a89a131c59381df8a40df78d15b7b7",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c1b539560d50fbfeedc338e100f34afcea9d0704ce2a11d5d3fbb935d9ca9f38",
      "bytes": 192674
    }
  ],
  "estimated_tokens": 12859
}
-->

# Durable State Update — Chapter 614

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 614. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 614. Profile updates may replace only one
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
  "chapter": 614,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 614,
    "continuity_sources": [614],
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
    "Al Diab Jawahiri, the leader of Al-Qaeda, remains in the Skeleton King's custody.",
    "The Skeleton King is an undead named monster who has fought alongside Jin Taekyung and is accepted by Chuck Hagel as an ally.",
    "Al-Qaeda possesses a large Magic Gem research laboratory that appears to have operated for at least ten years.",
    "Choi and Magic Johnson are investigating the Al-Qaeda laboratory and its research results.",
    "Restricted supplies found among the terrorists indicate that someone is supporting or supplying them from within established military, political, or smuggling networks.",
    "The masked group has destroyed terrorist leadership and headquarters while concealing its identities, creating a significant deterrent against further terrorist action.",
    "Middle Eastern terrorist groups and Afghan rebels have issued a joint statement promising restraint after the masked group's campaign.",
    "Jin-ho, now a civil servant in the Hunter and Gate Management Department, has inferred Jin Taekyung's involvement in the masked group's campaign and agreed to keep it secret.",
    "Jin Taekyung intends to return to the Murim after recognizing that his reunion with Jin-ho provided the comfort and clarity he needed.",
    "Jin Taekyung has completed an unnamed cultivation technique intended to be stable for even the lowest-rank Hunter while retaining moderate power that evil people cannot easily abuse.",
    "Jin Taekyung has entrusted the Skeleton King with the completed martial art and a letter for Choi Minwoo.",
    "Choi Minwoo is serving as Guild Master of the Peace Guild and Vice Guild Master of Ares Guild while grieving his grandfather Kim Hwajong."
  ],
  "continuity_sources": [
    613,
    612
  ],
  "open_questions": [
    "Who supplied Al-Qaeda with the restricted equipment, weapons, artifacts, and military goods?",
    "What results, if any, did Al-Qaeda obtain from its long-running Magic Gem experiments?",
    "What fate will the Skeleton King ultimately assign to Al Diab and the remaining terrorists?",
    "Will the terrorist groups' apparent surrender and restraint last beyond the immediate pressure of the masked group's campaign?",
    "How will Choi Minwoo respond after receiving Jin Taekyung's martial art and letter?"
  ],
  "safe_through": 613,
  "temporary_decisions": [
    "Use Al Diab Jawahiri as the full English rendering of 알 디아브 자와히리.",
    "Retain Crazy Korean as Chuck Hagel's address for the masked protagonist.",
    "Preserve Jin-ho hyung as Jin-ho's familiar address.",
    "Render 심마 as heart demon, 심법 as cultivation technique, and 무공 as martial arts.",
    "Keep Magic Gem laboratory for 마정석 관련 비밀 실험실."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 십왕     | **Ten Kings**       |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 칭호               | **Title**                      |
| 로그인              | **Login**                      |
| 동기화              | **Synchronization** / **Sync** |
| 헌터      | **Hunter**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 은자 | **silver nyang** | Silver currency unit. |
| 수문위사 | **gate guard** | Jin Family guard stationed at the gate. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 원정 | **Origin Essence** | The Water God Dragon's purified energy core, which humans call an inner core. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 화룡각주 | **Fire Dragon Pavilion Master** | Unique Title awarded to Jin Taekyung. |
| 대별산 | **Mount Daebyeol** | Secondary meeting point for the departing party. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 545
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 610
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 603
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 613
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 613
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 551
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 551
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 551
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 595
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 539
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃614화



띠링.



- [동기화]를 시작합니다. 10, 9, 8, 7…… 1, 0.

- [동기화]가 성공적으로 완료되었습니다. 갱신된 능력치가 신체에 적용되며, 특정 칭호에 한하여 사용이 제한됩니다.

- [로그인]을 완료했습니다.



익숙한 시스템 알림이 끝나기도 전에, 까슬까슬한 촉감과 젖은 풀잎 냄새가 피부와 코를 타고 전해져 온다.

나는 입술에 붙어 있는 볏짚을 뱉어 내며 내심 중얼거렸다.

‘돌아왔구나.’

무림으로의 귀환.

현대에서는 고작 한 달 남짓한 시간을 보냈을 뿐인데, 먼 과거의 일처럼 느껴지는 것은 결코 착각이 아니다.

‘일이 하도 많았어야지.’

무림. 그리고 현대.

나와 두 세상을 둘러싼 모든 상황이 급변하고 있었다. 연이어 벌어지는 사건 속에서 몸이 두 개라도 부족할 지경이다.

“…….”

다시 생각해 보니까 두 개는 맞구나. 그걸 번갈아 가며 컨트롤해야 하는 거라 더럽게 피곤한 거지.

그나저나…….

‘아. 일어나기 싫다.’

전신을 감싼 볏짚은 생각 이상으로 따뜻하면서 푹신했다.

이대로 늘어지게 한숨 자고 싶은 마음이 간절하다. 보급형 무공을 만드느라 근 일주일 동안 잠도 제대로 자지 못했기 때문이다.

다음 순간 두런두런 들려온 대화 소리만 아니었다면, 정말 그대로 잠들었을지도 몰랐다.

“음. 조장님이 어떤 사람이냐고요?”

“네, 예전부터 궁금했거든요. 아직 다른 두 사람도 안 와서 심심한 것도 있고. 송 호위도 그렇죠?”

익숙한 목소리다. 혁무진과 주화란의 대화에 이어, 추혼객(抽魂客) 송일섬이 퉁명스럽게 대답했다.

“난 별로 안 궁금하오.”

“들었죠? 송 호위도 궁금하대요.”

“아니, 안 궁금하다니까.”

“은자 두 냥 더 드릴게요.”

“……살짝 궁금해지는군.”

저 돈에 미친 새끼.

큰손 회장님의 은자 도네이션 한 방에 무릎을 꿇은 송일섬까지 가세하자, 혁무진의 머뭇거리는 목소리가 들려왔다.

“음, 이거 대답하기 어려운데. 조장님은 아직 주무시는 거 확실하죠?”

“네. 네.”

“확실히 잠들어 있다. 호흡이 안정되어 있어.”

“하긴 그렇겠네요. 한 번 잠들면 귀신이 업어 가도 모를 정도니까.”

안정된 것 같은 소리 하고 있네.

그건 내가 호흡을 조절해서 그런 거다. 개인적으로도 은근히 어떤 대답이 들려올지 궁금했으니까.

그리고 나의 충실한 오른쪽 새끼발가락은 기대를 배신하지 않았다.

“저희 조장님은 아주 그 유명한 그, 아주 유명한 어 뭐랄까…….”

“잘생기고 헌앙한 후기지수?”

맑고 고운 영창 피아노 같은 주화란의 물음에, 혁무진이 세상 단호한 어조로 대답했다.

“씹새끼였죠.”

“……아.”

“……어.”

“요즘에서야 열화신룡이니 뭐니 하지. 일이 년 전만 해도 그만한 씹새끼 찾는 것도 힘들었습니다. 매일같이 기루 가서 술 처먹고, 공금 훔쳐서 도박장에 뿌리고. 오죽하면 그때 당시 조장님 별호가…….”

“야.”

“맞습니다. 야왕(夜王)이었어요. 그쪽 분야에서는 십왕(十王)이 떼로 덤벼도 상대가 안 된다니까요. 밤마다 옆구리에 전낭 떡 하니 차고 위풍당당한 걸음으로 기루로 향할 때면 저랑 동료 수문위사들이 그랬습니다. 저 씹새끼 오늘도 천마군림보 쓴다고. 그나저나 송 대협께서는 견문이 넓어서 들어 보셨구나. 역시.”

혁무진의 너스레에 송일섬이 떨떠름한 목소리로 대꾸했다.

“그게 무슨 소리냐. 난 아무 말도 안 했는데.”

“예?”

“아무 말도 안 했다고.”

“에이. 무슨 소리세요. 조금 전에 야라고 하셨잖아요.”

“아니라니까.”

“틀림없이 사내 목소리였는데요. 농담도, 참. 그럼 도대체 누가…….”

길게 늘어지던 말꼬리가 뚝 끊겼다.

짧지만 무거운 침묵이 흐른 뒤, 누군가의 손길이 내 얼굴을 덮은 볏짚을 조심스럽게 걷어냈다.

부스럭. 스윽.

시야를 가리고 있던 볏짚이 치워지고, 희미하게 비추는 달빛 아래로 두 개의 시선이 부딪친다.

나는 사람 좋아 보이는 푸근한 웃음과 함께, 오랜만에 마주한 혁무진을 향해 인사를 건넸다.

“야.”

“…….”

말없이 깊게 가라앉은 시선으로 나를 내려다보던 혁무진이 손에 든 볏짚을 다시 내 얼굴에 덮었다.

마치 아무 일도 없던 것처럼, 아주 조심스럽게.

“치워.”

“달이 밝아서 그런가. 웬 환청이…….”

“안 치우면 네 인생이 어두워진다. 치워.”

“옙.”

볏짚에서 느꼈던 훈훈한 온기는 이미 사라진 지 오래다.

나는 엑소시스트에 의해 봉인되었다가 수백 년 만에 깨어난 흡혈귀처럼, 마차 짐칸에서 부스스 몸을 일으켰다.

휘우우우.

스산한 바람이 옷자락에 들러붙은 볏짚을 날려 보낸다.

나와 시선이 마주친 주화란이 황급히 고개를 돌리고, 언제 피웠는지 모를 모닥불 근처에서 불을 쬐고 있던 송일섬은 갑자기 말에게 건초를 먹여야겠다는 혼잣말과 함께 엉덩이를 뗐다.

그리고 일렁이는 불길을 받아 커진 내 그림자가, 한 사람을 향해 드리워졌다.

“마지막으로 남길 말은?”

나직한 내 물음에 혁무진이 침착하게 대답했다.

“조장님, 이러지 마시고 제 말을 좀 들어 보십시오.”

“그래서 물었잖아.”

“마지막이라면서요. 마치 유언 같잖아요.”

“유언 맞을걸.”

“……아.”

“아주 신이 났더라. 수하의 그런 모습에 조장으로서 참을 수 없는 기쁨을 느낀다.”

반쯤은 사실이다. 정말 참을 수가 없었다.

무림에서 개고생, 현대에서 개고생하고 잠도 못 잔 상태로 돌아왔는데 직속 수하가 뒷담화를 까고 있던 건에 대하여.

그리고 이 라노벨 제목 같은 상황에 뒤따라온 감정의 이름은 분노였다.

“얼굴, 팔, 다리, 복부, 등. 이 중 하나만 골라.”

“혹시 그거, 제 사인(死因)입니까?”

“죽이진 않고, 죽도록 때릴 거야.”

잠깐 고민하던 혁무진이 대답했다.

“복부로 하겠습니다.”

“이유는?”

“등의 상처는…… 무림인의 수치니까.”

나는 녀석의 기개에 탄성을 내뱉었다.

“지랄 염병을 떠는군.”

“잘못한 건 사실이니 벌은 달게 받겠습니다. 오십시오.”

“그럼 네가 복부를 골랐으니, 난 나머지를 고르겠다.”

“예?”

“뭐가 ‘예?’야. 너만 고르면 불공평하잖아. 나도 골라야 공평한 거지.”

“아니, 잠깐만요. 도대체 그게 왜 공평…….”

빡!

강렬한 타격음.

천천히 타들어가는 모닥불 위, 코피를 뿌리며 솟구친 한 사람의 그림자가 짙게 드리워진다.

‘오자마자 주먹을 쓰게 되다니.’

이곳은 안휘(安徽)와 호북(湖北). 하남(河南)으로 이어지는 접경지인 대별산(大別山).

그리고 BGM처럼 잔잔하게 깔리는 혁무진의 비명을 듣고 저 멀리에서 다가오는 두 그림자는, 근본 없는 사파 나부랭이이자 화룡각의 마지막 구성원들이다.

“……저자는 왜 맞고 있는 거지?”

“태산이! 왔다!”

마침내 한자리에 모인 화룡각 남만원정대에게, 나는 짧지만 강렬한 훈시를 남기고 돌아섰다.

“자자, 이 새끼만 마저 패고 출발합시다.”

반발은 없었다.

지금의 나는 S급 헌터 진태경이 아니라, 정파 무림 제일의 후기지수인 열화신룡이자 저들의 직속 상관인 화룡각주 진태경이니까.

뻐억!

“억! 어어억!”

난 무림이 참 좋다. 물론 개 같은 암천은 빼고.



* * *



그곳은 빛 한점 들어오지 않는 칠흑(漆黑)의 공간이었다.

어떤 소리도, 생기도 느껴지지 않는 어둠 속에서 죽은 듯이 엎드린 인영(人影)들이 잘게 몸을 떨었다.

그리고 다음 순간.

“천상천하(天上天下)!”

“만마앙복(萬魔仰服)!”

하나의 목소리로 터져 나온 벼락같은 외침과 함께, 어둠 속에서 검붉은 불꽃이 솟구쳤다.

화아아악!

거세게 타오른 불의 고리.

틀림없는 불꽃임에도 불구하고, 뼈마디에 사무칠 만한 한기를 뿜어내는 불길 너머로 누군가의 그림자가 일렁였다.

- 오랜만이구나.

사내인지, 여인인지. 혹은 젊은이인지, 늙은이인지. 그도 아니라면 그 목소리가 낮은지 높은지조차 구분할 수 없었다.

그것은 실로 기이한 음성이었고, 큰 울림을 낳으며 사방에서 울려 퍼져 바닥에 엎드리고 있던 인영들을 옥죄었다.

- 나의 종들아.

그 짧은 한마디에 담긴 미증유의 거력(巨力) 앞에 모두가 몸을 떨었다.

절대자에 대한 두려움으로, 혹은 자신들이 모시는 존재를 마주했다는 감격과 환희로.

그렇기에 그들은 한목소리로 부르짖었다.

“이 어리석고 미천한 종들이, 위대하신 천주(天主)를 배알하옵니다!”

천주. 하늘의 주인.

그 존재를 설명할 수 있는 단어는 오직 그것밖에는 없었다.

누구보다 존엄하고 위대한 절대자. 구름 위 하늘은 그의 궁전이며, 하늘 아래 땅에 살아가는 모든 하찮은 것들은 천주의 종이요, 백성이었다.

아니, 반드시 그렇게 만들어야 했다.

- 얼마나 흘렀는가.

살아 있는 신의 물음을 이해하지 못하는 자는 아무도 없었다.

이 자리에 엎드린 이들은 감히 이루 말할 수 없을 만큼 헌신적이며, 충성스러운 천주의 종복들이었으니까.

바닥 깊숙이 엎드려 있던 한 청년도 마찬가지였다.

“위대하신 천주께서 마지막으로 깨어나신 그날로부터, 꼭 일백하고도 삼십육 일이 흘렀사옵니다!”

청년의 힘찬 대답에, 거세게 타오르던 불길이 일렁였다.

- 그래. 떠오르는구나. 서천(西天). 그 아이가 떠난 날이었지.

“망극하옵니다!”

청년을 필두로 다시 한번 거대한 외침이 터져 나왔다.

처음과는 달리 부끄러움과 자책이 실린 외침이었다.

서천마군과 그가 이끌던 암천의 일군(一群)이 사천당가에서 전멸했을 때, 그들은 그 예상치 못한 결과에 당황했고 깊이 잠들어 있던 주인을 깨워야 했다.

“위대하신 천주시여. 두 번 다시…… 그런 일은 없을 것이옵니다.”

청년의 악문 잇새 사이로 흘러나온 목소리에 다시 한번 불길이 흔들렸다.

- 아니다. 부족한 너희를 믿은 내 과오일 뿐.

“……!”

- 혈주(血主). 부족한 것은 너도 마찬가지 아니더냐.

그 어떤 것보다 뼈아픈 질책에 청년, 혈주의 눈동자가 파르르 떨렸다.

자신이 숭배해 마지않는 주인이 지금 무엇을 말하는지, 누구보다 잘 알기 때문이었다.

‘하남.’

정파 무림이 소림혈사(少林血史)라 명명한 그 날은, 혈주의 인생에 있어 가장 뼈아픈 기억 중 하나였다.

계획되었던 것에 비해 한참이나 부족한 성과를 이루었을뿐더러, 팔 한쪽을 놓고 오는 치욕까지 겪어야 했으니까.

만약 소림의 신물인 녹옥불장마저 가져오지 못했다면…… 생각하기도 싫다.

‘검성. 그리고 진태경.’

산 채로 찢어 죽여도 시원치 않을 두 놈을 떠올리자 살심(殺心)이 절로 일어난다.

그러나 충성스러운 종복은 주인의 앞에서 삿된 감정을 보여선 안 되는 법. 혈주는 솟구치는 살심을 가까스로 억누르며 입을 열었다.

“부, 부디 용서해 주시옵소서.”

후우웅.

대답 대신 한 줄기 서늘한 바람이 휘몰아쳤다.

혈주를 비롯한 모두가 더더욱 몸을 움츠린 그때. 나직한 음성이 그들의 귓가를 파고들었다.

- 부족한 것은 채우면 그만.

공기가 무겁게 가라앉았다. 바람이 멎고 살아 있는 것들이 숨을 죽였다.

모든 것이 멈춘 공간 속에서 천주의 목소리가 이어졌다.

- 부족한 너희를, 내가 채워 주리니.

그것은 명령이었고, 거부할 수 없는 힘이었다.

솨아아아아.

어둠이, 그림자가 일렁였다.

보이지 않는 어디에선가 흘러나온 막대한 기운이 몸에 깃드는 것을 깨달은 혈주가 환희로 눈을 부릅떴다.

“처, 천주시여!”

혈주는, 모두는 다시 한번 깨달았다.

자신들이 모시는 주인이야말로 살아 있는 신이자 하늘과 땅 전체를 아우르는 절대자임을.

그리고 주인께서 친히 나누어 주신 이 힘이, 무엇을 의미하는지.

- 남천(南天)과 북천(北天)에게 전하라.

구구구구궁!

땅이, 세상이 뒤흔들렸다.

모든 것을 일그러트리는 그 미증유의 기운 너머로 천둥 같은 울림이 터져나왔다.

- 이제…… 대전(大戰)을 시작한다.

천상천하. 만마앙복.

환희와 광기에 가득 찬 충복들의 부르짖음 속에서, 보이지 않는 그림자는 손을 내저었다.

칠흑 같은 공간을 물들이던 검붉은 불길이 사라지고, 또다시 어둠이 찾아왔다.
```

## Final English reading copy

```markdown
# Chapter 614

> **System**
>
> **Synchronization** begins. 10, 9, 8, 7…… 1, 0.
>
> **Synchronization** completed successfully. The updated stats have been applied to the body, and the use of certain **Titles** is restricted.
>
> **Login** complete.

Before the familiar System notifications had even finished, the rough texture of straw and the smell of wet grass reached me through my skin and nose.

I spat out the piece of rice straw stuck to my lips and muttered inwardly.

*I’m back.*

My return to the Murim.

I had spent barely over a month in the modern world, yet it felt like something that had happened in the distant past. That was no illusion.

*I’ve had way too much going on.*

The Murim. And the modern world.

Everything surrounding me and the two worlds was changing at a frightening pace. There had been so many incidents one after another that even two bodies would hardly have been enough.

“……”

Come to think of it, I really did have two. It was having to control them by turns that made it so damn exhausting.

Anyway…

*Ah. I don’t want to get up.*

The rice straw wrapped around my entire body was warmer and softer than I had expected.

I desperately wanted to stay sprawled out like this and sleep for a while. I had barely slept for nearly a week while developing a martial art for widespread use.

If I hadn’t heard the low murmur of conversation nearby the next moment, I might really have fallen asleep.

“Hmm. You’re asking what kind of person Captain is?”

“Yes. I’ve been curious for a while. The other two haven’t arrived yet, so I’m bored, too. Escort Song, you’re curious as well, right?”

It was a familiar voice. After Hyuk Mujin and Ju Hwaran’s conversation, Song Ilseom, the Soul-Chasing Guest, answered gruffly.

“I’m not particularly curious.”

“Did you hear that? Escort Song is curious, too.”

“I said I’m not curious.”

“I’ll give you two more silver nyang.”

“……I’m becoming slightly curious.”

That bastard was obsessed with money.

Once Song Ilseom had joined in after kneeling before the big spender’s silver donation, Hyuk Mujin’s hesitant voice reached me.

“Hmm. This is difficult to answer. Captain is definitely still asleep, right?”

“Yes. Yes.”

“He is certainly asleep. His breathing is steady.”

“Well, I suppose that makes sense. Once he falls asleep, he wouldn’t know if a ghost carried him away.”

What do you mean, steady?

That was because I was controlling my breathing. Personally, I was rather curious about what kind of answer I would hear, too.

And my loyal right pinky toe did not betray my expectations.

“Our captain is that very famous, uh, that extremely famous… What should I call it…?”

“A handsome and heroic rising martial artist?”

At Ju Hwaran’s question, delivered in a voice as clear and lovely as a Young Chang piano, Hyuk Mujin answered in the most decisive tone imaginable.

“He was a fucking bastard.”

“……Ah.”

“……Uh.”

“These days, people call him the Blazing Flame Divine Dragon and all that. But just a year or two ago, you’d have been hard-pressed to find a bigger fucking bastard. Every day, he’d hit a pleasure house, get shit-faced, steal public funds, and blow the money at gambling dens. He was so bad that his sobriquet back then was…”

“Hey.”

“That’s right. He was the Night King. In that field, even if all Ten Kings came at him together, they wouldn’t have been a match. Whenever he strapped a money pouch to his side and headed proudly toward a pleasure house every night, my fellow gate guards and I would say, ‘That fucking bastard is using the Heavenly Demon Reign Step again today.’ Come to think of it, Great Hero Song, you’ve heard of him because you’re so well traveled. As expected.”

At Hyuk Mujin’s rambling, Song Ilseom answered in a displeased voice.

“What are you talking about? I didn’t say anything.”

“What?”

“I didn’t say anything.”

“Come on. What are you talking about? You said ‘hey’ a moment ago.”

“I didn’t.”

“It was definitely a man’s voice. Don’t joke around. Then who on earth was it…?”

His drawn-out sentence abruptly broke off.

A short but heavy silence passed. Then someone carefully brushed away the rice straw covering my face.

Rustle. Ssshh.

The straw blocking my vision was removed, and beneath the faint moonlight, two gazes collided.

With a warm, friendly smile, I greeted Hyuk Mujin, whom I had not seen in a long time.

“Hey.”

“……”

Hyuk Mujin stared down at me in silence, his gaze sinking deeply. Then he covered my face with the straw in his hand again.

Very carefully, as if nothing had happened.

“Move it.”

“Perhaps the moon is bright. I seem to be hearing things….”

“If you don’t move it, your life is going to get dark. Move it.”

“Yes, sir.”

The pleasant warmth I had felt from the straw had long since vanished.

Like a vampire sealed away by an exorcist and awakened after several hundred years, I slowly rose from the wagon’s cargo bed.

Whoooosh.

A chilly wind blew away the pieces of straw clinging to my clothes.

Ju Hwaran met my gaze, then hurriedly turned her head away. Song Ilseom, who had been warming himself by the campfire—when had he even lit it?—suddenly stood up with a mutter about needing to feed the horses hay.

And my shadow, enlarged by the dancing firelight, fell over one person.

“What are your last words?”

At my quiet question, Hyuk Mujin answered calmly.

“Captain, please don’t do this. Hear me out.”

“That’s why I asked.”

“You said they were my last words. It sounds like a will.”

“It probably is.”

“……Ah.”

“You were having a great time. As your squad leader, I feel an indescribable joy at seeing my subordinate like that.”

That was half true. I really couldn’t contain myself.

After busting my ass in the Murim, busting my ass in the modern world, and returning without getting any sleep, I found my direct subordinate badmouthing me behind my back.

And the name of the emotion that followed this situation straight out of a light novel was rage.

“Face, arms, legs, abdomen, or back. Pick one.”

“Is that perhaps my cause of death?”

“I’m not going to kill you. I’m just going to beat you within an inch of your life.”

After a brief moment of thought, Hyuk Mujin answered.

“I’ll choose my abdomen.”

“Why?”

“Wounds on the back are… a martial artist’s shame.”

I let out an exclamation at his spirit.

“What a load of bullshit.”

“I did do wrong, so I’ll gladly accept my punishment. Come at me.”

“Since you chose your abdomen, I’ll choose the rest.”

“What?”

“What do you mean, ‘what?’ It would be unfair if only you got to choose. I have to choose, too, for it to be fair.”

“No, wait a minute. How is that fair at all…?”

Wham!

A violent impact rang out.

Above the slowly burning campfire, the dark shadow of a man who had leaped into the air while spraying blood from his nose loomed large.

*I’m already using my fists the moment I get back.*

This was Mount Daebyeol, the border region connecting Anhui and Hubei to Henan.

And the two shadows approaching from the distance to the accompaniment of Hyuk Mujin’s quiet screams were the Fire Dragon Pavilion’s final members, a bunch of rootless unorthodox faction trash.

“……Why is that person being beaten?”

“Taishan! Is here!”

At last, the Fire Dragon Pavilion’s Nanman expedition party had gathered in one place. I left them with a short but powerful lecture, then turned away.

“All right, let’s finish beating this bastard and get going.”

There was no objection.

Right now, I wasn’t the S-rank Hunter Jin Taekyung. I was the Blazing Flame Divine Dragon, the greatest young prodigy of the orthodox Murim, and the Fire Dragon Pavilion Master—their direct superior.

Crack!

“Urgh! Aaaagh!”

I really did love the Murim.

Of course, that excluded the damned Dark Heaven.

* * *

It was a pitch-black space where not a single ray of light entered.

In the darkness, where no sound or sign of life could be felt, figures lying facedown trembled faintly.

Then, the next moment—

“Heaven above, earth below!”

“All demons bow in submission!”

With those thunderous cries bursting forth in a single voice, crimson-black flames rose from the darkness.

Fwoosh!

A ring of fire blazed fiercely.

Though it was unmistakably a flame, the fire beyond it radiated a chill deep enough to seep into the bones. Beyond that flame, someone’s shadow wavered.

—It has been a long time.

It was impossible to tell whether the voice belonged to a man or woman, a young person or an old one. It was impossible even to distinguish whether the voice was low or high.

It was a truly strange voice. It reverberated loudly, echoing from every direction and constricting the figures prostrate on the floor.

—My servants.

Everyone trembled before the unprecedented power contained in those few words.

Perhaps from fear of the absolute being. Or perhaps from the joy and rapture of standing before the one they served.

That was why they cried out in unison.

“These foolish and lowly servants humbly pay their respects to the great Lord of Heaven!”

Lord of Heaven. The master of the heavens.

That was the only phrase capable of describing the being.

A supreme entity more dignified and magnificent than anyone else. The heavens above the clouds were his palace, and every lowly thing living on the earth beneath the sky was the Lord of Heaven’s servant and subject.

No. They had to make it so.

—How much time has passed?

No one failed to understand the question of the living god.

Those prostrate in this place were the Lord of Heaven’s devoted and loyal servants, devoted beyond anything that could be put into words.

The young man bowed low against the floor was no different.

“Exactly one hundred and thirty-six days have passed since the day the great Lord of Heaven last awoke!”

At the young man’s vigorous answer, the fiercely burning flames wavered.

—Yes. I remember now. Western Heaven. That was the day the child left.

“We are deeply ashamed!”

Led by the young man, another enormous cry burst forth.

Unlike the first, this cry was filled with shame and self-reproach.

When the Western Heaven Demon Lord and the forces of Dark Heaven under his command had been annihilated at the Sichuan Tang Clan, they had been thrown into confusion by the unexpected result and had been forced to awaken their master, who had been sleeping deeply.

“Great Lord of Heaven. Never again… will such a thing happen.”

The flames shook once more at the voice that slipped through the young man’s clenched teeth.

—No. It was my mistake for trusting you, who were inadequate.

“……!”

—Blood Lord. You are no different, are you?

At the most painful reprimand of all, the pupils of the young man—Blood Lord—trembled.

He knew better than anyone what the master he worshiped so fervently was saying.

*Henan.*

The day the orthodox Murim had named the Shaolin Bloodshed was one of the most painful memories of Blood Lord’s life.

Not only had the results fallen far short of what had been planned, but he had also suffered the humiliation of leaving one of his arms behind.

If he had failed to bring back Shaolin’s sacred treasure, the Green Jade Buddha Staff, as well… He did not even want to think about it.

*The Sword Saint. And Jin Taekyung.*

The thought of those two bastards—whom even tearing apart alive would not satisfy him—made murderous intent rise within him.

But a loyal servant must never display wicked emotions before his master. Blood Lord barely suppressed the murderous intent surging within him and opened his mouth.

“P-Please forgive me.”

Whoooong.

Instead of an answer, a chilly wind swept through the darkness.

Just as Blood Lord and everyone else shrank back even further, a quiet voice pierced their ears.

—What is lacking can simply be filled.

The air sank heavily. The wind stopped, and every living thing held its breath.

In that space where everything had come to a halt, the Lord of Heaven’s voice continued.

—I shall fill what you lack.

It was a command, backed by an irresistible force.

Fwoooooosh.

The darkness and shadows wavered.

Blood Lord’s eyes widened with rapture as he realized that an immense surge of qi from somewhere unseen was settling into his body.

“L-Lord of Heaven!”

Blood Lord—and everyone else—understood once more.

Their master was a living god, an absolute being who encompassed the entirety of heaven and earth.

And they understood what this power, personally bestowed upon them by their master, meant.

—Deliver this message to South Heaven and North Heaven.

Rumble, rumble, rumble!

The earth trembled. The world shook.

Beyond that unprecedented power that warped everything, a thunderous resonance burst forth.

—Now… we begin the Great War.

Heaven above, earth below. All demons bow in submission.

Amid the cries of the loyal servants, filled with rapture and madness, the invisible shadow waved a hand.

The crimson-black flames that had colored the pitch-black space disappeared, and darkness descended once more.
```
