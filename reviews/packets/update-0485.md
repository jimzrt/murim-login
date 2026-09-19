<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0485.txt",
      "sha256": "d92bd751adb282d6fe1fead3d7238992892de7350cc3c8a8f0c9c84539627550",
      "bytes": 13993
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "df6076f30b720ada7eb37809d12080ffe5f34083dab877648c0bb39e464fefde",
      "bytes": 3164
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fa7ceecaf5de1320b506d0c2daa93e0813f03bef34ce1bee5c98a161c0b80944",
      "bytes": 154981
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "aa9696866f2417a3087365360b92008207c7c711dfc4ece673d6e4b150988b45",
      "bytes": 803
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b2b7d74fa03705d76987bca102d41f1f14b1914b2c42a980e598b71df98d2a22",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1cfcdd791581691a84decc2db0ceda4ff01b67f34834bde80ee0bc862713ca8b",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f13761e4c74ea88d7de622c81652e5f6584bcfa82301890930e3467dc080c99a",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f043134623113cc5fd0eee8c2560e8c129f4c45973b1325b38de23b43b912cfe",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "9ee1fd2b93b8518ec1e069b7fe2b214e213f5b44755a4f523feca4efa69af717",
      "bytes": 786
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "7ebb63458a6478af12b10ab19267bb6fb669e2afc002123fe325b09e21f7e2f0",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4f9a2b6f44f23a401944cbb3ff87467abd5f25164948ba8ba22aebcefbbab70a",
      "bytes": 151253
    }
  ],
  "estimated_tokens": 12866
}
-->

# Durable State Update — Chapter 485

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 485. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 485. Profile updates may replace only one
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
  "chapter": 485,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 485,
    "continuity_sources": [485],
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
    "The Water God Dragon died after regaining its reason and giving Taekyung its purified Origin Essence, which humans call an inner core.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan can enthrall people by seizing their emotions and souls, and she can speak remotely through a controlled person's body.",
    "Honglan identifies herself as the Southern Heaven Demon Empress, serves Lord of Heaven, and confirms that Dark Heaven has many eyes and ears, including Blood Lord's reports.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "The Dongting Fisherman is alive but severely injured and may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "Gung Gibang traced the vessel connected to Honglan to Red Cliffs.",
    "Cheongpung reported that Zhuge Feng found the Gate site from the Water God Dragon's memories.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Hubei authorities concealed the Water God Dragon incident and suppressed local dark-path forces to redirect public anger toward Dark Heaven.",
    "The exposed fissure at the Water God Dragon's site triggered an ominous System notification when Taekyung touched it."
  ],
  "continuity_sources": [
    483,
    484
  ],
  "open_questions": [
    "What lies beyond the exposed fissure, and why did touching it trigger an ominous System notification?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who created or controlled the Gate that corrupted the Water God Dragon, what is its purpose, and how is that power related to Dark Heaven?"
  ],
  "safe_through": 484,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, established renderings of live-fish sashimi and bone-in sashimi, and gukbap with an explanatory footnote.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, 꽃뱀 as flower snake, 산재처리 as workers’ compensation, 거열형 as tearing apart by chariots, 섭혼술 as Soul-Seizing Technique, 남천마후 as Southern Heaven Demon Empress, 묘족 as Miao people, 페미비수타 as femibista, 대장군 as Great General, and 정관대전 as Great Government War."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 독왕     | **Poison King**               | Tang Taesang   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 괴공절학 | **monstrous martial arts and supreme techniques** | Bizarre arts associated with the Demonic Cult. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 천년마도 | **Thousand-Year Demonic Path** | Ancient demonic tradition associated with the Demonic Cult. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 문경 | 남천마후 | legendary_assassin_to_hostile_demon_empress | you | polite and grave | Warns her to stop the killing. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 482
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 484
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 484
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 481
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 481
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 484
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a former assassin who passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 483
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃485화



쿵. 쿵.

몸 안에서 울리는 심장박동 소리가 천둥처럼 크게 들린다.

한 걸음, 그리고 다시 한 걸음. ‘그것’에 가까워질수록 가슴이 거세게 뛰었다.

모래를 한 움큼 넣고 씹은 것처럼 입안이 까끌거렸고, 나도 모르게 크게 뜨인 눈동자는 뻑뻑했다.

그리고 마침내 내 손이 절벽의 틈새에 닿은 그 순간. 나는 이 불길함의 실체를 확인할 수 있었다.

삐빅.



- 해당 게이트는 이미 대부분의 기능을 상실하였습니다!

- 게이트의 입장이 불가능합니다!

- [게이트 공략] 퀘스트가 생성되지 않습니다!



귓가를 파고드는 알림과 눈앞을 가득 메운 홀로그램 창, 나를 바라보는 사람들의 시선들…….

그 모든 것들의 앞에서, 나는 천천히 한마디를 내뱉었다.

“……씨발.”

콰드득.

나도 모르는 사이 힘이 들어간 손아귀가 절벽을 파고든다.

절벽의 틈새, 아니 게이트로부터 흘러나오는 아주 미약한 마기에 눈앞이 아득해졌다.

‘마지막까지 아니길 바랐는데.’

빌어먹을 게이트. 정말 게이트였다니.

도대체, 어떻게, 왜?

그 후로도 오랫동안, 답을 찾을 수 없는 의문들은 머릿속을 떠나지 않았다.



* * *



머릿속이 복잡하다. [기억의 파편]을 통해 보았을 때부터 설마 하는 생각은 했지만, 막상 믿기 힘든 현실을 마주하자 쉽게 말이 나오지 않았다.

‘무림에, 그것도 게이트라니.’

이건 거대한 균열이다. 이 세계를 둘러싼 법칙이 무너지고 있다는 신호였고, 재앙의 첫걸음이었다.

‘암천(暗天).’

놈들의 정체는 내 예상을 아득히 뛰어넘을 정도로 깊고, 어두운 것이었다.

사람들에게서 홀로 떨어진 채로 검게 물든 동정호의 강물을 바라보던 나는, 바닥에 굴러다니는 돌멩이 하나를 집어 강물을 향해 던졌다.

퐁당.

‘소림에서 벌어진 혈사는 사천으로 이어졌고, 결국 여기까지 왔다.’

지난 몇 달의 시간은 그야말로 시산혈해(尸山血海)의 연속이었다.

하남에서 성라대연이 벌어지는 와중에 정파 무림의 태산북두라 불리는 소림이 습격당했고, 암천이라는 불길은 사천으로 번졌다.

중요한 것은 그 과정에서 이해할 수 없는 현상들이 있었다는 것이다.

‘혈주, 서천마군, 그리고 이동진의 존재.’

아직도 생생하게 떠오른다. 죽음을 담보로 한 적천강의 화신귀무(火神鬼舞)에 당하고도 회복하던 혈주의 모습이.

‘아니, 그건 회복이라고 부를 수 없을 정도였지.’

맞다. 당시 혈주가 보여 주었던 능력은 회복이 아닌 재생에 가까웠다.

시간을 역행한 것처럼 돋아나던 새 살과 제 자리를 찾는 뼈마디. 잿더미처럼 새카맣게 타들어 간 모든 것이 순식간에 재생되던 모습.

그리고 그 믿을 수 없는 광경을 바라보던 나는, 더할 나위 없이 익숙한 존재를 머릿속에 떠올렸었다.

‘트롤(Troll). 그래, 마치 트롤 같았어.’

아니면 포션이거나……. 젠장, 트롤에 포션이라니. 내가 떠올린 거지만 미친 생각이다.

더 미칠 것 같은 건 그게 정말 사실일지도 모른다는 거고.

재차 돌멩이를 집어 든 나는 더 멀리 날려보냈다.

퐁당.

혈주가 보여 준 기이한 현상은 거기에서 끝이 아니었다. 검성의 등장과 함께 수세에 몰리자 천주를 부르짖으며 씻은 듯이 사라져 버리지 않았나.

당시에는 모두가 사마외도의 괴공절학 중 하나라고 단정 지었으나, 게이트라는 사실을 확인한 지금은 달랐다.

‘텔레포트(Teleport).’

비록 내가 매직 존슨을 통해 경험했던 텔레포트와는 미세한 차이가 있다지만 그게 텔레포트가 아니면 혁무진 손에 장을 지진다.

‘다시 생각해 보면 서천마군도 석연치 않은 구석이 한 두 가지가 아니었지.’

사천혈사 당시 서천마군은 독왕을 처치하는 대가로 한쪽 팔을 내놓아야 했다.

하지만 정작 사천당문의 지하 뇌옥에서 대면했을 때, 놈은 새로운 팔을 얻은 상태였다.

그리고 아무리 여러 방면으로, 생각할 수 있는 모든 경우의 수를 따져 봐도 그걸 가능하게 하는 것은 딱 두 가지밖에 없다.

서천마군의 정체가 생체 프라모델이거나, 아니면 알 수 없는 힘이 작용했거나.

당연하게도 전자일 가능성은 없다. 물론, 나로서는 그랬으면 좋겠지만.

‘이동진의 존재도 마찬가지.’

이동진. 수백에 달하는 암천의 흑의인을 한 번에 옮길 수 있는 신묘한 진법.

마교의 후신이라 불리는 암천이니, 마교에 그런 게 있었다면 진작 오십여 년 전에 써먹고도 남았을 거다.

그랬다면 정마대전은 마교의 승리로 막을 내렸을 테고, 나도 태원진가가 아니라 흑룡방, 뭐 그런 흑도 문파의 삼공자가 되었겠지.

‘왜 몰랐을까.’

무림이라는 세상에서 유일한 이방인이었던 나조차도 예측하지 못한 실체.

드문드문 머릿속에 스쳤던 한 줄기 의심은 천년마도의 괴공절학이라는 말에 묻혔고, 서천마군이 괴력난신(怪力亂神)라 부르는 힘에 의해 지워졌었다.

하지만 지금은 다르다.

나는 게이트의 존재를 확인했고, 어느덧 내게도 익숙해진 무림의 상식과 법칙이 무너져 내리고 있다는 사실을 깨달았다.

그리고 무림인들이 괴공절학과 괴력난신이라 부르는 암천의 기이한 능력을 단 두 글자로 설명할 수 있다는 사실도.

‘마법.’

머릿속을 가득 채운 한 단어에, 눈앞이 밝아지고 뜨겁게 달궈졌던 이마가 차갑게 식는다.

더불어 아직 모습을 드러내지 않은 한 존재를 뜻하는 말이 입술 사이로 흘러나왔다.

“……천주(天主).”

암천의 정점에 군림하는 자.

혈주와 서천마군, 남천마후와 같은 이들이 스스로 하찮은 종이라 칭할 만큼 압도적인 존재.

‘도대체, 네 정체는 뭐냐.’

천주에 대해 생각하는 것만으로도 온몸의 피가 싸늘하게 식는 기분이다.

만약, 아주 만약에 천주라는 놈이 지금 이 순간 내가 무의식중에 떠올린 바로 그 존재라면…….

풍덩!

“……!”

높이 솟구치는 물보라와 출렁이는 강물.

나는 찬물을 뒤집어쓴 사람처럼 화들짝 놀라며 상념에서 깨어났다. 고개를 돌리자 언제 다가왔는지조차 모를 익숙한 얼굴이 시야에 들어왔다.

“뭘 그렇게 넋이 나가 있어?”

퉁명스러운 목소리. 하지만 자글자글한 얼굴 주름 사이로 보이는 눈동자에 담긴 감정은 우려와 걱정이다.

그런 적천강의 모습에 피식 실소를 흘린 내가 입을 열었다.

“깜짝 놀랐네. 뭡니까?”

옆자리에 털썩 주저앉은 적천강이 대답했다.

“그냥 하도 안 보이길래 와 봤다.”

“올 거면 조용히 오시지. 난데없이 바위를 던지시네.”

“일곱 살 난 어린애마냥 돌멩이나 깔짝깔짝 던지고 있는 꼴을 보고 있자니 답답해서 그랬다. 불만 있느냐?”

“있으면요?”

후웅!

말이 끝나기도 전에 고개를 숙이자, 심상치 않은 파공성이 머리카락을 스치며 허공을 강타한다.

뒤통수 어택에 실패한 적천강이 입맛을 다셨다.

“눈치 하나는 기똥찬 놈이로고.”

“이런 거 한두 번 합니까. 이제는 눈 감고도 피하죠.”

“감아 봐.”

“……싫은데요.”

“건방진 녀석 같으니. 한데 그런 놈이 아까는 왜 그렇게 넋을 놓고 있었느냐? 무림에서 그러고 있다가는 골로 가기 딱 좋다.”

“그래서, 저를 골로 보내시려고요?”

“오냐. 네 녀석이 원한다면 못 할 것도 없지.”

“그럼 제자를 다시 찾으셔야 할 텐데요. 아, 제자가 아니라서 별 상관없나?”

“커흠. 커흐흐흠!”

나오지도 않은 헛기침을 억지로 뱉어 내던 적천강이 불쑥 입을 열었다.

“그래서, 머리에 똥만 차 있는 놈이 뭐가 그리 고민이냐?”

“똥 어디서 쌀까 고민했는데요.”

빡!

아, 이번에는 못 피했다. 금나수까지 써 가며 기어코 뒤통수를 후려치는 데 성공한 적천강이 눈을 치켜떴다.

“피똥 싸고 싶으냐?”

“어후, 왜요. 머릿속에 똥만 차 있는 놈이 똥 생각했다는데 뭐가 문젭니까.”

“주둥이와 궁둥이 위치를 바꿔 놓기 전에 성심성의껏 대답해라.”

“아, 예.”

얼얼한 뒤통수를 쓰다듬으며 잠시 생각하던 내가 입을 열었다.

“사실 제가 이 세상 사람이 아닌데, 제가 원래 있던 세상에 존재하는 나쁜 힘이 암천과 깊은 연관이 있는 것 같거든요. 이번에 미쳐 날뛴 이무기 있죠? 그게 다 그놈들 짓이에요. 절벽에 있는 균열은 게이트라는 건데, 그게 제대로 터지면 막, 어? 괴물이 아주 그냥 쏟아져 나옵니다.”

“…….”

“그때가 되면 전부 끝장이에요, 끝장. 그리고 아마 아니겠지만 마왕 아스모데우스라는 놈이 있거든요. 만약 그놈이 아직 살아서 무림을 노리는 거면 진짜 전부 좆 되는…….”

“알겠다.”

어차피 아무도 믿지도 않을 허무맹랑한 이야기. 대놓고 속 시원하게 떠들어 대던 나는 적천강의 반응에 이어지려던 말을 삼켰다.

“예?”

“알겠다고 했다.”

“…….”

“네 녀석이 한 말. 모두 충분히 알아들었으니 더 말할 필요 없느니라.”

아니, 이거 반응 왜 이래.

당황스럽다 못해 혼란스러울 지경이다. 동시에 말로 형용키 어려운 어떤 감정이 가슴 깊숙한 곳으로부터 불쑥 솟구쳤다.

‘믿어 준다고? 이런 허무맹랑한 이야기를? 아니, 나를?’

말없이 나를 응시하는 적천강의 눈빛에, 문득 가슴이 벅차오르고 목이 콱 막힌다.

짧다면 짧고 길다면 길다 할 수 있는 일 년 남짓한 시간.

누구보다 많은 일을 겪으며 동고동락했던 노인의 눈동자에 서린 감정은 절대적인 신뢰라고 부를 만한 무언가였다.

‘……그만큼 믿고 있었구나. 나를.’

가끔 그럴 때가 있다. 알 수 없는 감정에 사로잡혀, 아무런 말도 나오지 않을 때. 나조차도 무슨 말을 해야 하는지 알 수 없는 그런 때가.

하지만 지금 이 순간, 나는 깨달았다. 언제부터인가 마음속에서 만지작거리고 있던 그 말을 해야 할 때라는 걸.

“노야. 아니…….”

오랜 망설임 끝에 꺼낸 한마디.

그리고 떨리는 마음으로 입을 연 나를 향해, 적천강은 인자하게 웃으며 고개를 끄덕였다.

“잘 알아들었다. 죽고 싶다는 말을 길게도 하는구나.”

“스, 예?”

“예는 무슨 개 같은 놈의 예.”

빠바박!

뭐여, 시벌.

갑자기 찾아온 뇌정지 타임. 멍하니 입을 벌린 채 뒤통수를 감싸 안은 내게, 분노에 찬 목소리가 날아들었다.

“노부가 머저리로 보이느냐? 뭐? 이 세상 사람이 아니야? 이세계에서 양민이었던 내가 무림에서는 초절정 고수. 뭐 그런 거냐!”

“제목 생각보다 트렌디하고 괜찮은, 아니, 그게 아니라 제 말을 좀 들어 보세요.”

“이미 들었다. 유언.”

“어어, 어. 잠깐만!”

“잠깐만? 그렇게 맞아도 정신을 못 차리고 또 반말을 쓰다니, 이런 개호로……!”

퍼버버버벅!

눈앞을 가득 메운 수십여 개의 장영(掌影)이 전신을 두드린다.

몸 안을 파고드는 뜨거운 열기를 느끼며, 나는 생각했다.

‘스승님은 무슨. 시부럴.’

잠시나마 감동에 젖었던 내가 병신이다.



* * *



“다음에 또 그런 헛소리를 지껄였다가는 반으로 찢어 죽인다. 알겠느냐?”

적천강의 살벌한 살인 예고에, 일각이나 무차별 폭행당한 진태경이 앓는 소리를 냈다.

“어우, 잠깐만요. 저 지금 진짜 죽을 것 같은데요.”

“시끄럽다. 노부의 조모보다 느려 터진 놈 같으니!”

“……저기, 노야. 기왕 말이 나왔으니 하는 말인데, 혹시 소피 보러 가실 때 몰래 스마트폰 꺼내서 쓰시는 건 아니죠?”

빡!

또 다시 알아들을 수 없는 소리를 지껄이는 진태경에게 마지막 일격을 먹인 적천강은 혀를 차며 자리를 떴다.

전신에서 흘러나오는 흉흉한 분위기에 사람들이 헛숨을 삼키며 길을 비켰다.

저벅, 저벅.

어디론가 향하는 발걸음.

어느덧 혼자가 된 적천강의 얼굴 위에는, 도무지 의미를 알 수 없는 복잡미묘한 감정이 떠올라 있었다.

‘……놈. 그런 알 수 없는 소리나 해 대다니.’

하지만 글쎄, 모르겠다. 일평생 소문이나 미신을 쥐똥만큼도 믿지 않았던 적천강이었지만, 진태경이 하는 말이라면 달랐다.

그 어떤 허무맹랑한 이야기라 할지라도, 그 녀석은 자신에게 있어 누구보다 특별한 존재였으니까.

‘그러고 보니 스, 뭐라고 하려 했던 것 같은데.’

설마? 아니, 아니겠지.

한숨을 내쉰 적천강은 절벽 위에 걸린 달을 바라보았다.

휘영청한 달빛 아래, 얼마 떨어지지 않은 곳에 자신과 같은 처지인 한 사람이 강물을 바라보며 서 있는 것이 보였다.

“잠깐 이야기 좀 할까?”

적천강이 건넨 한마디에, 문경이 대답했다.

“싫다, 꺼져라.”
```

## Final English reading copy

```markdown
# Chapter 485

Boom. Boom.

The sound of my heartbeat echoing inside my body was as loud as thunder.

One step, then another. The closer I got to *it*, the harder my heart pounded.

My mouth felt gritty, as though I had shoveled in a handful of sand and chewed it. My eyes, opened wide without me realizing it, felt dry and stiff.

And the moment my hand finally touched the fissure in the cliff, I was able to confirm the true nature of this foreboding.

*Beep.*

> **System**
>
> - This Gate has already lost most of its functions!
>
> - Entry into the Gate is impossible!
>
> - The **Gate Conquest** Quest cannot be generated!

The notification drilling into my ears, the holographic window filling my vision, the gazes of everyone watching me…

In the face of all of it, I slowly uttered a single word.

“...Fuck.”

Crunch.

Before I realized it, my clenched hand dug into the cliff.

The faintest trace of demonic qi flowing from the fissure—or rather, from the Gate—made my vision swim.

*I’d hoped it wouldn’t be this until the very end.*

That damn Gate. It really was a Gate.

How? Why?

Even long afterward, those questions with no answers continued to haunt my mind.

* * *

My thoughts were a mess. I had suspected it might be possible ever since I saw it through the *Memory Fragment*, but when I came face-to-face with a reality this difficult to believe, I couldn’t speak easily.

*A Gate in the Murim.*

This was a gigantic rift. A sign that the laws surrounding this world were collapsing—and the first step toward a disaster.

*Dark Heaven.*

Their true nature was far deeper and darker than I had ever imagined.

Separated from the others, I gazed at the blackened waters of Dongting Lake. Then I picked up a loose stone from the ground and tossed it into the lake.

Splash.

*The bloodshed at Shaolin led to Sichuan, and eventually reached this place.*

The past several months had been one continuous sea of corpses and blood.

While the Star-Array Grand Banquet was taking place in Henan, Shaolin—the Mount Tai and Northern Dipper of the orthodox Murim—was attacked, and the flames of Dark Heaven spread to Sichuan.

The important thing was that inexplicable phenomena had occurred along the way.

*The Blood Lord, the Western Heaven Demon Lord, and the Moving Formation.*

I could still vividly recall the sight of the Blood Lord recovering even after being struck by Jeok Cheongang’s Dance of the Fire God and Demon—a technique that staked his life itself.

*No. It wasn’t even accurate to call that recovery.*

That was right. What the Blood Lord had shown was closer to regeneration than recovery.

New flesh sprouting as if time were reversing. Bones sliding back into place. Everything burned pitch-black like ash regenerating in an instant.

As I watched that unbelievable sight, I had thought of something more familiar than anything else.

*Trolls. Yeah, he was just like a troll.*

Or maybe a potion…

*Damn it. A troll and a potion? What the hell was I thinking?*

What was even crazier was that it might actually have been true.

I picked up another stone and threw it farther.

Splash.

The strange phenomenon the Blood Lord had displayed hadn’t ended there. When the arrival of the Sword Saint put him on the defensive, hadn’t he cried out for the Lord of Heaven before vanishing without a trace?

At the time, everyone had concluded that it was one of the demonic, heterodox arts known as monstrous martial arts and supreme techniques. But now that I knew about the Gate, things looked different.

*Teleport.*

It might have differed slightly from the teleportation I had experienced through Magic Johnson, but if that wasn’t teleportation, I’d burn Hyuk Mujin’s palm myself.

*Come to think of it, there had been more than one thing that didn’t add up about the Western Heaven Demon Lord.*

During the Sichuan Blood Tragedy, the Western Heaven Demon Lord had sacrificed one arm to defeat the Poison King.

But when I confronted him in the underground prison beneath the Sichuan Tang Clan, he already had a new arm.

And no matter how many angles I considered or how many possibilities I went through, there were only two things that could have made that possible.

Either the Western Heaven Demon Lord was a living plastic model, or some unknown power had been at work.

Naturally, the former was impossible.

Though, personally, I wouldn’t have minded if it were true.

*The existence of the Moving Formation was the same.*

The Moving Formation. A wondrous formation capable of transporting hundreds of Dark Heaven’s black-robed men at once.

Dark Heaven was called the successor to the Demonic Cult. If the Demonic Cult had possessed something like that, they would have used it more than fifty years ago.

If they had, the Great Faction War would have ended in victory for the Demonic Cult, and instead of becoming the Third Young Master of the Jin Family of Taiyuan, I would have become the Third Young Master of the Black Dragon Gang—or some other dark-path sect.

*Why hadn’t I realized it?*

Even I, the only outsider in the world known as the Murim, had failed to predict the truth.

The faint suspicion that had occasionally brushed across my mind had been buried beneath the claim that these were monstrous martial arts and supreme techniques from the Thousand-Year Demonic Path. Then it had been erased by the power the Western Heaven Demon Lord called supernatural powers.

But things were different now.

I had confirmed the existence of the Gate. I had realized that the common sense and laws of the Murim, which had gradually become familiar to me, were collapsing.

And I had realized that the strange abilities of Dark Heaven—which martial artists called monstrous martial arts and supernatural powers—could be explained with just one word.

*Magic.*

At the single word filling my mind, my vision brightened, and my forehead, which had been burning hot, slowly cooled.

Along with it, another word referring to an existence that had yet to reveal itself slipped between my lips.

“...Lord of Heaven.”

The one who reigned at the summit of Dark Heaven.

An overwhelming existence whom people like the Blood Lord, the Western Heaven Demon Lord, and the Southern Heaven Demon Empress called themselves lowly servants before.

*What the hell are you?*

Just thinking about the Lord of Heaven made the blood throughout my body feel cold.

If—just if—that bastard called the Lord of Heaven was the very existence I had unconsciously thought of at this moment…

Splash!

“...!”

A spray of water shot high into the air, and the lake rippled.

I snapped out of my thoughts with a start, like someone who had been doused in cold water. When I turned my head, a familiar face had appeared in my vision. I had no idea when he had approached.

“What are you spacing out for?”

His voice was gruff. But the emotion in his eyes, visible between the deep wrinkles on his face, was concern and worry.

I let out a quiet laugh at Jeok Cheongang’s expression and opened my mouth.

“You startled me. What brings you here?”

“You’d been gone for so long, I came to see what you were doing.”

“If you were coming, you could have come quietly. Why did you suddenly throw a rock?”

“Watching you fiddle around with pebbles like a seven-year-old child was making this old man frustrated. Do you have a problem with that?”

“What if I do?”

Whoosh!

Before the words had even left my mouth, I ducked. A vicious sound split the air where my head had been, brushing past my hair.

Jeok Cheongang smacked his lips in disappointment after his attack on the back of my head failed.

“You’ve got remarkably sharp instincts.”

“Do you think this is the first time? I can dodge it with my eyes closed now.”

“Close them.”

“...I’d rather not.”

“You insolent brat. Then why were you so distracted earlier? In the Murim, spacing out like that is a good way to get yourself killed.”

“So you were planning to kill me?”

“Of course. If that’s what you want, this old man can certainly oblige.”

“Then you’ll have to find another Disciple. Oh, wait. Since I’m not actually your Disciple, I guess it doesn’t matter.”

“Ahem. Ahem-ahem!”

Jeok Cheongang forced out several fake coughs before suddenly opening his mouth.

“So what has the idiot with nothing but shit in his head so troubled?”

“I was wondering where to take a shit.”

Smack!

Damn it. I couldn’t dodge that one.

Jeok Cheongang finally succeeded in smacking the back of my head, even using a grappling technique to do it, and glared at me.

“Do you want to shit blood?”

“Why? You said my head was full of shit, and I said I was thinking about shit. What’s the problem?”

“Answer properly before I switch your mouth and ass around.”

“Ah. Yes, sir.”

Rubbing my throbbing head, I thought for a moment before speaking.

“The truth is, I’m not from this world. And I think the evil force that exists in the world I originally came from is deeply connected to Dark Heaven. You know that imugi that went berserk this time? It was all their doing. The rift in the cliff is a Gate. If it ever fully breaks open, monsters will come pouring out.”

“...”

“When that happens, everything is over. Completely over. And there’s probably no way it’s true, but there’s a bastard called Demon King Asmodeus. If he’s still alive and has his sights set on the Murim, then we’re all completely fucked—”

“I understand.”

I swallowed the rest of my words at Jeok Cheongang’s response.

It was a ridiculous story that no one would believe anyway. I had been laying it all out without restraint, but his reaction left me speechless.

“Excuse me?”

“I said I understand.”

“...”

“I understood everything you said well enough. There is no need to say anything more.”

What was with that reaction?

I was so confused that I could hardly think straight. At the same time, an emotion too difficult to describe suddenly surged up from deep within my chest.

*He believes me? He believes this ridiculous story? No… he believes me?*

As I stared silently into Jeok Cheongang’s eyes, my chest suddenly felt full, and my throat tightened.

A little over a year—a period that could be called short or long.

In the old man’s eyes, after we had experienced and endured more together than anyone else, there was something that could be called absolute trust.

*...He trusted me that much.*

Sometimes that happened. I would be seized by some inexplicable emotion, unable to say a word. Unable even to figure out what I should say.

But at that moment, I realized that it was time to say the words I had been turning over in my heart for some time.

“Old Master. No…”

It was the first word I had managed to draw out after a long hesitation.

And as I opened my mouth with a trembling heart, Jeok Cheongang smiled kindly and nodded.

“I understood you perfectly. You sure take a long time to say that you want to die.”

“M—yes?”

“What do you mean, ‘yes,’ you damn bastard.”

Whap-whap-whap!

What the fuck?

My brain ground to a halt. I stared blankly, mouth hanging open, clutching the back of my head as his furious voice rang out.

“Do you take this old man for an idiot? What? You’re not from this world? ‘I Was a Mere Civilian in Another World, but Now I’m a Supreme Peak Master in the Murim.’ Is that it?”

“That title’s surprisingly trendy and pretty good—no, that’s not the point. Just hear me out.”

“I already did. Your last words.”

“Whoa, whoa. Hold on!”

“‘Hold on’? After all the times I’ve beaten you, you still haven’t come to your senses, and now you’re talking to me like an equal again, you insolent little…!”

Whap-whap-whap!

Dozens of palm shadows filled my vision and hammered every inch of my body.

As I felt the searing heat digging into my body, I thought,

*Master, my ass. Fuck.*

I was an idiot for getting moved, even for a moment.

* * *

“If you spout that kind of bullshit again, I’ll tear you in half and kill you. Understood?”

At Jeok Cheongang’s grim death threat, Jin Taekyung—who had been beaten indiscriminately for fifteen minutes—let out a groan.

“Ugh, hold on. I think I’m actually going to die.”

“Quiet. You’re slower than this old man’s grandmother!”

“...Old Master, since we’re on the subject, you don’t happen to sneak your smartphone out and use it whenever you go take a leak, do you?”

Smack!

After delivering one final blow to Jin Taekyung, who had once again spouted something incomprehensible, Jeok Cheongang clicked his tongue and left.

The murderous aura radiating from his entire body made everyone swallow hard and clear a path.

Step. Step.

He walked toward somewhere.

Now alone, Jeok Cheongang wore a complicated expression that was impossible to decipher.

*...That brat. Spouting such incomprehensible nonsense.*

Still, who knew? Jeok Cheongang had never believed in rumors or superstitions—not even a little—in his entire life. But if Jin Taekyung was the one saying it, things were different.

That brat was more special to him than anyone else.

*Come to think of it, he seemed to be about to say something starting with “M—.”*

Could it be? No. Of course not.

Jeok Cheongang sighed and looked up at the moon hanging over the cliff.

Beneath the bright moonlight, he saw someone in the same predicament standing nearby and gazing at the lake.

“Can we talk for a moment?”

At Jeok Cheongang’s words, Mungyeong answered,

“No. Get lost.”
```
