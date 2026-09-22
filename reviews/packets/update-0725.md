<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0725.txt",
      "sha256": "43320165f327d52408e502a7e860f1dbf4af911188e102a215fa4f8b4b54a810",
      "bytes": 13367
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "429a2cd691189a2ca7511a5beb94b3a0f506447625103c94b6a031967ccd1003",
      "bytes": 1771
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d14607f7a804dd19f78b60c7f6d3f243ac00867b933108b57b2ff6879b51f418",
      "bytes": 209672
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "8913cb8d0e3c55b644ce0a0c71056e669f58668f6695bc765550ae9d2a68d84d",
      "bytes": 788
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "82a7afe0d9cb0840f87547cbbde676715ab8af8155554d33392992614cd60eae",
      "bytes": 830
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "fa9da1114ad55a3ff81565ba8f2e16aa4cb883d80b64e5d8f92b926a9437e40d",
      "bytes": 898
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "02a9e967a62ba2471f55e181b940d8023b849f078eb555018a7cf38d1fa87398",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0c8db303e3dc9840540aa555685ae9216fcecb0ae8e953f01454ce5272eb9ec5",
      "bytes": 1824
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e891df195177649bf4bd0dc6726fe0fcec2ff88f63fd36a043bee558052800c2",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "5cca2912520c101c68bc9817a0bb72075a9a9de5339665d81c868deeda7bbaf0",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "0d16172e1adb166faccbcca076590771e47dd750ba6723813a35305ea83a9a2a",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "95e261ef3ab69c55a03ba0f95afd878718640c247d7e8025ee159b1738b306b7",
      "bytes": 219687
    }
  ],
  "estimated_tokens": 12367
}
-->

# Durable State Update — Chapter 725

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 725. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 725. Profile updates may replace only one
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
  "chapter": 725,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 725,
    "continuity_sources": [725],
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
    "Nanman is unified under the Beast Miao King's authority, with the Great Chieftain system abolished and the Nanman Beast Palace operating as a Murim Alliance ally.",
    "The Nanman Beast Palace has formally joined the Murim Alliance and pledged to send more troops against Dark Heaven than during the Great Faction War.",
    "Yayul Mok learned humanity from Jin Taekyung and is committed to defending Nanman and its allies with his life.",
    "The Sacred Rain is fading but has healed Jin Taekyung's companions from their injuries.",
    "The prelude to the Great War has begun with Nanman's beasts and people mobilizing.",
    "The White Tiger is present above Nanman's assembled forces and answers the Beast Miao King's war cry.",
    "Dark Heaven's full strength remains unrevealed despite its previous interventions.",
    "The Lord of Heaven has taken an unexplained personal interest in Jin Taekyung.",
    "Jeok Cheongang has requested a private conversation with Jin Taekyung during the journey from Nanman."
  ],
  "continuity_sources": [
    724
  ],
  "open_questions": [
    "Why is the Lord of Heaven interested in Jin Taekyung, and what does the Lord of Heaven intend?",
    "Why has Dark Heaven withheld its full strength, and what is its larger plan?",
    "How will the Great War unfold now that Nanman has joined the Murim Alliance?",
    "What will happen to Nanman and the Sacred Rain after the rain ends?"
  ],
  "safe_through": 724,
  "temporary_decisions": [
    "Render 전고 as war drums.",
    "Render 신강 as Xinjiang.",
    "Retain God wills it! for 신께서 원하신다!.",
    "Preserve the established Lord of Heaven rendering for 천주 and the chapter's profane comic banter."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 법왕     | **Dharma King**               | Hong Dao       |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |
| 흑수권마 | 대설귀 | junior hostile subordinate to senior ally | Senior | deferential but urgent and protesting | Black Hand protests the Great Snow Fiend's order to capture Jin. |
| 대설귀 | 흑수권마 | senior hostile commander to junior subordinate | you | blunt, commanding, and threatening | The Great Snow Fiend orders Black Hand to stop questioning him. |
| 진태경 | 대설귀 | hostile_martial_opponents | old man | mocking, casual, and profane | Jin taunts the Great Snow Fiend while preparing to continue the fight. |
| 대설귀 | 진태경 | hostile_martial_opponent | Jin Taekyung | cold, incredulous, and confrontational | The Great Snow Fiend addresses Jin while demanding an explanation for his survival. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |

## Listed compact profiles

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 692
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand was a sadistic Dark Heaven agent and Supreme Peak master who acted under orders associated with the Southern Heaven Demon Empress before his death.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand was the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; the Great Snow Fiend was his senior and could overrule him under the Southern Heaven Demon Empress's orders.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 703
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 713
- **Aliases:** Hanbaek (한백)
- **Role:** The Great Snow Fiend was the former ruler of Great Snow Mountain and a Supreme Peak fiend who killed Baekhwi and Venerable Wusang during the Great Faction War before Jin Taekyung killed him.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend was an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he was senior to Black Hand and served under the Southern Heaven Demon Empress before Jin Taekyung killed him.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 724
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 723
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 723
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 724
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 714
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃725화



― 이야기 좀 하자.

귓가를 파고드는 전음에 작게 고개를 끄덕인 나는 고삐를 느슨하게 잡았다.

그 행동의 뜻을 알아차린 맹수가 서서히 발걸음을 늦췄고, 함께 나란히 이동하게 된 적천강의 입술이 열렸다.

“천주가 네놈에게 유독 관심을 보인다는 말, 사실이냐?”

“네.”

“거, 희한하군. 노부는 처음 듣는 이야기인데.”

“그럴걸요. 저도 처음 하는 얘기니까.”

“왜 말하지 않았느냐?”

“안 물어보셨잖아요.”

솔직히, 이렇게 대답하면서도 한 대 정도는 얻어맞을 줄 알았다.

하지만 적천강은 번개처럼 방어 자세를 취한 나를 물끄러미 바라보다가, 담담한 목소리로 혼잣말처럼 뇌까렸다.

“물어보지 않았으니 말하지도 않는다……. 그래, 영 틀린 말은 아니로군.”

이 양반이 갑자기 왜 이래.

“저기, 노야?”

“왜.”

“그, 혹시 삐치셨어요?”

“뭐라? 삐쳐? 노부가?”

“예.”

적천강이 대단한 농담을 들은 것처럼 껄껄 웃었다.

“노부가 다섯 살 난 어린아이도 아닌데 삐칠 일이 뭐가 있겠느냐. 물론 지난 사흘 동안 그것에 관하여 말할 시간은 얼마든지 있었고 네 녀석을 생각해서 노부 역시 묻지 않았지만, 그거야 쥐뿔도 상관없는 일이니 신경 쓰지 말거라. 결국 안 물어본 놈이 등신 아니겠느냐. 으허허.”

“…….”

“강호인들은 말한다. 사제지간(師弟之間)에는 숨기는 것이 없어야 한다고. 하지만 우리 사이에는 해당하지 않는 경우이니 넌 개의치 말거라. 뭐, 따지고 보면 노부는 열화문의 명맥을 이을 후인이 필요했고 네놈은 무공이 필요하여 상부상조했으니 그것으로 된 거지. 사실 요즘 같은 세상에 사제지간의 정 운운하는 것도 우습다.”

“…….”

“혹여나 네놈에게 무슨 일이라도 생길까 싶어 뭐 빠지게 남만까지 달려오고, 정체를 숨기기 위해 멀쩡한 머리털까지 다 뽑았지만, 노부는 괜찮다. 결과적으로는 그것도 안 빠졌고 머리털은 금방 자랄 테니까. 아무렴, 그렇고말고.”

“…….”

“그까짓 염병할 얘기 좀 안 들었다고 노부가 삐칠 게 뭐가 있겠느냐. 애초에 목마른 놈이 우물을 파야 하는 게지. 때가 되면 어련히 말하겠거니, 하고 기다렸다가는 노부처럼 말라 뒈지는 것 아니겠느냐. 허허허.”

신선처럼 웃는 적천강을 보며 나는 생각했다.

‘진짜 오지게 삐쳤네.’

사람이 이 정도로 삐칠 수가 있나.

이 정도면 포브스 지가 선정한 ‘세상에서 가장 삐친 인물 1위’에 뽑혀도 손색이 없을 정도다.

“네 녀석을 처음 만났던 날이 생각나는구나. 그때는 노환으로 제정신이 아니었는데. 이래서 늙으면 죽어야 한다는 말이…….”

숨이 턱턱 막혀 오는 듯한 압박감.

나는 폭주 기관차처럼 질주하는 적천강을 향해 간신히 입술을 뗐다.

“아까 드린 말씀은 농담이고, 저도 정신이 없어서 말씀을 못 드린 겁니다. 나름대로 생각 정리는 해야 할 것 아닙니까.”

“흠.”

적천강의 눈이 게슴츠레해진다. 평소의 모습을 약간이나마 되찾은 그가 퉁명스럽게 물었다.

“그래서, 천주에 관한 것도 농담이냐?”

“그건 사실인데요. 안타깝게도.”

“근거는?”

나는 적천강에게 대략적인 이야기를 들려주었다.

우리가 남만야수궁에 머무를 당시 그도 이미 한 번 들었던 내용이지만, 간단히 축약했던 그때와는 달리 훨씬 더 상세하게.

그리고 이야기를 모두 들은 적천강이 미간을 좁혔다.

“그 연놈들이 널 사로잡으려 했다?”

“예. 그런데 하다 보니 안 되겠다 싶었는지, 죽이려 하더라고요. 독혈지에서 싸웠던 대설귀와 흑수권마도, 또 남천마후도.”

“널 생포하고자 한 것이 천주의 명령 때문이었을까?”

“그건…….”

적천강의 물음에 잠시 기억을 떠올린 나는, 이윽고 고개를 저었다.

“아무래도 아닌 것 같습니다.”

“그렇게 생각하는 이유는?”

“만약 정말 천주가 그런 명령을 내렸다면, 남천마후는 설령 홀로 최후를 맞이하더라도 절 죽이려 들지는 않았을 테니까요.”

“목숨보다 앞서는 충심(忠心)이라……. 믿기 힘들 정도군.”

“단순한 충성심이 아닙니다.”

나직이 대답한 나는 기억 속에 남은 남천마후의 모든 것을 떠올렸다.

그때의 눈빛. 그 순간의 표정. 환희로 들뜬 목소리와 그녀가 했던 모든 언행들.

그날, 내가 남천마후로부터 느낀 감정은 고작 충성심이라는 단어로 표현할 수 있는 것이 아니었다.

그것은…….

“광신(狂信)이었습니다. 남천마후에게. 아니, 암천에게 있어 천주는 살아 있는 신이나 다름없어요.”

“……!”

“암천의 모두가 천주를 두려워하고 경애합니다. 놈이 어떻게든 저를 생포하라는 명령을 내렸다면, 그건 누구도 거스를 수 없는 신명(神命)이에요.”

그토록 강하던 혈주도, 서천마군도.

이번에 최후를 맞이한 남천마후 역시 천주의 이름 앞에서는 종복을 자처하며 엎드렸다.

그들 한 사람 한 사람이 어지간한 초절정 고수쯤은 맨손으로 찢어발길 수 있는 괴물들.

천주는 바로 그 괴물들이 받들어 모시는 왕이요, 신인 것이다.

“확신할 수는 없지만…… 남천마후는 천주가 관심을 보였다는 이유 하나만으로 절 생포하려 한 것 같습니다.”

“단지 천주의 총애를 얻기 위해서?”

내가 조용히 고개를 끄덕이자, 적천강이 신음처럼 중얼거렸다.

“광신도라…….”

흐려진 말꼬리가 바람에 파묻힌다.

호랑이의 등에 올라탄 채, 지금 이 순간에도 스쳐 지나가는 주위 풍경을 말없이 바라보던 적천강이 불쑥 입을 열었다.

“마교도(魔敎徒)를 본 적이 있느냐?”

“혹시 제가 환갑 정도로 보이세요?”

“그래, 네 녀석 정도의 나이라면 보지 못한 것이 당연하지. 정마대전이 끝나고서도 한참 후에야 태어났으니.”

“다 아시는 분이 갑자기 그건 왜.”

“문득 그런 생각이 들었다. 차라리 그 시절의 마교와 다시 한번 싸우는 것이 나을지도 모르겠다는 생각이.”

“……!”

“물론 놈들 역시 광신도였다. 허나 그 수괴인 천마(天魔)는 결국 한낱 인간이었고, 천마의 휘하에 있던 십만 마도 역시 그 사실을 알고 있었지. 그들에게 천마란 단지 자신들을 이끄는 교주(敎主)일 뿐, 신이 아니었던 게야.”

나는 적천강이 무슨 말을 하려 하는지 깨달았다.

마교도에게 있어 천마는 피륙(皮肉)으로 이루어진 인간이었지만, 암천의 모두에게 천주는 신이다.

그렇기에 그들은 자신들의 신을 위해 싸울 것이다.

죽음에 대한 두려움 없이 싸울 것이고, 몸에 무수한 창칼이 박혀도 웃으며 숨을 거둘 것이다.

“그 어느 때보다 끔찍한 전쟁이 될 것이다.”

적천강이 무거운 눈빛으로 나를 응시하며 말을 이었다.

“너에게는 더더욱.”

“천주가…… 절 주시하고 있기 때문입니까.”

“원했든, 원치 않았든 네 녀석은 이미 필요 이상으로 많은 주목을 받았다. 지금 이 순간조차도 천하 어딘가에서는 네 이름이 울려 퍼지고 있겠지.”

“…….”

“삼성(三星)과 십왕(十王)은 낡은 이름이다. 허나 네 녀석은 달라. 고금을 통틀어 유례를 찾아볼 수 없는 재능을 지녔고, 천하의 누구도 이제 고작 약관을 넘긴 네가 강자라는 사실을 부인하지 못한다.”

나를 바라보는 적천강의 눈빛은 숨길 수 없는 대견함과, 불안함이 서려 있었다.

“그렇기에 천주 역시 주시하는 것이다. 더군다나 놈은 이미 한 번 너를, 네 안에 숨어 있는 무한한 가능성과 진면목을 확인했었으니까.”

“……사천당문의 뇌옥.”

“그래. 알 수 없는 괴력난신(怪力亂神)의 힘을 이용해서, 서천마군의 눈으로 너를 보았지.”

어찌 잊을 수 있을까.

머리 위로 쏟아져 내리는 돌가루와 피가 흩뿌려진 석벽.

그리고 우뚝 선 채 나를 바라보던 서천마군의. 아니, 잠시나마 종복의 몸을 빌린 천주의 한마디를.



‘재미있군. 재미있어.’



그때, 놈은 분명 웃고 있었다.

전신이 한 줌의 재가 되어 흩날리면서도, 나를 향한 마지막 인사를 잊지 않았다.



‘다음에 또 보도록 하지.’



떠올리는 것만으로 가슴이 덜컥 내려앉는 그날의 기억.

작게 심호흡하는 내 모습을 말없이 바라보던 적천강이 문득 입을 열었다.

“어쩌면…… 천주는 어렴풋이 짐작하고 있을지도 모른다. 네가 지금껏 누구에게도 말한 적 없던 그 비밀들을.”

“……!”

“그렇기에, 이제는 나 역시 묻지 않을 수 없구나.”

누군가 일시 정지 버튼을 누른 것처럼 멈춰 버린 세상 속, 적천강이 천천히 입술을 뗐다.

“네가 숨겨 왔던 모든 것을, 노부에게 말해 줄 수 있겠느냐?”



* * *



적천강은 고개를 들어 하늘을 바라봤다.

지난 사흘간 쉼 없이 빗줄기를 쏟아 낸 하늘은, 한없이 어지러운 그의 마음과는 달리 푸르고 맑았다.

‘선계(仙界)라…….’

미처 흘러나오지 못한 목소리가 마음속에서 흩어진다. 더 이상 무슨 말을 해야 할까. 도대체 어떻게 이해해야 할까.

참으로 긴 시간을 살아왔음에도, 그 모든 것이 부질없게 느껴졌다.

‘만약 자네가 곁에 있었다면, 이 어지러운 마음도 금세 다잡을 수 있었을 텐데.’

적천강은 몇 달 전 세상을 떠난 벗을 떠올렸다.

술과 고기를 좋아해서 땡중이었고, 누구보다 인의(人意)를 사랑했기에 법왕(法王)이라 불리었던 한 사람을.

하지만 이내 고개를 저었다.

법왕은 이제 이 세상 사람이 아니고, 설령 그가 살아 있었다 하더라도 저 푸른 하늘을 올려다보며 천기(天氣)를 읽을 수는 없었을 것이다.

‘이미 천기가 어그러졌다고 했지. 더 이상 저 하늘은 누구에게도 어떤 답을 해 주지 않는다고. 분명 그리 말했었어.’

동시에 법왕은 거대한 전란(戰亂)을 예고했다.

하늘마저 어지럽히는 기운이 온 천하에 미칠 것이라고. 불길이 되어 사방을 휩쓸 것이라고.

하지만 법왕의 예견은 그뿐만이 아니었다.

‘신성(新星)의 주인.’

어지러운 하늘을 밝히며 떠오른 새로운 별.

법왕은 그 신성의 주인으로 한 청년을 점찍었고, 이후 구화산으로 향한 적천강은 열화문의 명맥을 그 청년에게 잇도록 했다.

“……허. 그저 헛소리 좋아하는 땡중인 줄 알았건만.”

헛웃음 섞인 중얼거림이 공허하게 흩어진다. 전신을 휩쓰는 시원한 바람을 말없이 맞고 있던 적천강의 시선이 문득 옆을 향했다.

지금 이 순간에도 거침없이 내달리고 있는 한 마리 맹수.

그리고 튼튼한 가죽끈으로 전신을 고정한 채 안장 위에 엎드린 한 사람.

아니, 적천강의 하나뿐인 제자.

‘괘씸한 놈 같으니. 이 사달을 일으켜 놓고 잘도 자는구먼.’

한편으로는 어이가 없었지만, 진태경으로부터 대략적인 이야기를 들은 적천강에게는 더 이상 놀랄 힘도 남아 있지 않았다.

무림과는 완전히 동떨어진 또 다른 세상. 그리고 선계와 같은 그곳과 무림을 오가는 한 청년.

‘괘씸한 놈 같으니. 이 사달을 일으켜 놓고 잘도 자는구먼.’

한편으로는 어이가 없었지만, 진태경으로부터 대략적인 이야기를 들은 적천강에게는 더 이상 놀랄 힘도 남아 있지 않았다.

무림과는 완전히 동떨어진 또 다른 세상. 그리고 선계와 같은 그곳과 무림을 오가는 한 청년.

비록 그 모든 것을 이해할 수는 없었지만, 적천강은 자신이 들었던 이 믿지 못할 이야기가 모두 진실이라는 것을 받아들인 후였다.

‘그럼 설마, 이놈이 소신선(小神仙)이라도 되는 건가.’

마음속으로 중얼거린 그때. 진태경의 입가에서 죽 늘어진 침이 적천강의 뺨에 척, 하고 달라붙었다.

철퍽.

“…….”

주먹에 절로 힘이 들어간다.

하지만 적천강은 곤히 잠든 제자의 이마를 쥐어박는 대신, 한숨을 내쉬며 흐트러진 자세를 잡아 주었다.

‘그래, 그간 고생했으니 푹 자거라.’

아니, 아니지.

적천강은 오직 한 사람에게만 들릴 만큼 작은 목소리로 중얼거렸다.

“잘 다녀오너라.”
```

## Final English reading copy

```markdown
# Chapter 725

“Let’s talk.”

At the Sound Transmission that pierced my ear, I gave a small nod and loosened my grip on the reins.

The beast noticed and gradually slowed its pace. Jeok Cheongang, who had been traveling alongside me, parted his lips.

“Is it true that the Lord of Heaven has taken an unusual interest in you?”

“Yes.”

“Huh. Strange. This old man is hearing about it for the first time.”

“I suppose so. It’s the first time I’ve mentioned it, too.”

“Why didn’t you tell me?”

“You never asked.”

Honestly, even as I answered, I expected to get hit at least once.

But Jeok Cheongang merely stared at me as I instinctively assumed a defensive stance like lightning. Then he muttered in a calm voice, as though speaking to himself.

“You don’t tell me because I didn’t ask… Hm. That isn’t entirely wrong.”

What was wrong with this old man all of a sudden?

“Um, Old Master?”

“What.”

“Are you… sulking?”

“What? Sulking? Me?”

“Yes.”

Jeok Cheongang burst into laughter, as if he had just heard an incredible joke.

“Why would this old man sulk? I’m not a five-year-old child. Of course, we had more than enough time to discuss it over the past three days, and this old man didn’t ask because he was thinking of you, but that has nothing whatsoever to do with anything, so don’t worry about it. In the end, the idiot is the one who didn’t ask, isn’t he? Hahaha.”

“……”

“People of the martial world say that a Master and Disciple should have no secrets between them. But that doesn’t apply to us, so don’t concern yourself with it. Come to think of it, this old man needed someone to carry on the Fire Gate Clan’s lineage, and you needed martial arts, so we helped each other out. That should be enough. Besides, talking about the bonds between Master and Disciple in a world like this is laughable.”

“……”

“This old man ran all the way to Nanman until something nearly fell off because I was afraid something might happen to you. I even plucked out all my perfectly good hair to hide my identity, but I’m fine. In the end, that didn’t fall off either, and my hair will grow back soon enough. Of course. Naturally.”

“……”

“Why would this old man sulk just because he didn’t hear some goddamn story? A thirsty man should dig his own well. If I waited for you to tell me when the time was right, wouldn’t I end up dried out and dead just like this old man? Hahahaha.”

Looking at Jeok Cheongang, who was laughing like an immortal, I thought:

*He’s really, really sulking.*

Could a person sulk this much?

At this point, he could have been named Forbes’ Most Sulky Person in the World and no one would have objected.

“I remember the day I first met you. Back then, this old man wasn’t in his right mind because of the infirmities of old age. That’s why they say that once you get old, you should just die…”

A suffocating pressure began to bear down on me.

As Jeok Cheongang charged ahead like a runaway locomotive, I finally managed to part my lips.

“What I said earlier was a joke. I couldn’t tell you because I was out of it, too. I needed some time to sort out my thoughts.”

“Hm.”

Jeok Cheongang’s eyes narrowed. Having recovered at least a little of his usual self, he asked gruffly,

“So the part about the Lord of Heaven was a joke, too?”

“That part is true. Unfortunately.”

“What proof do you have?”

I gave Jeok Cheongang a rough account of what had happened.

He had already heard a brief version of it when we were staying at the Nanman Beast Palace, but this time I went into far greater detail.

When I finished, Jeok Cheongang furrowed his brow.

“Those bastards tried to capture you?”

“Yes. But at some point, they must have decided that wouldn’t work, because they tried to kill me instead. The Great Snow Fiend and Black Hand Fist Demon, whom I fought at the Poisonblood Grounds, and the Southern Heaven Demon Empress, too.”

“Was their attempt to capture you an order from the Lord of Heaven?”

“That…”

I recalled what had happened for a moment before shaking my head.

“I don’t think so.”

“Why?”

“If the Lord of Heaven had truly given such an order, the Southern Heaven Demon Empress wouldn’t have tried to kill me, even if it meant meeting her end alone.”

“Loyalty that comes before one’s life… It’s almost impossible to believe.”

“It wasn’t simple loyalty.”

I answered quietly as I recalled everything about the Southern Heaven Demon Empress.

Her eyes at that moment. Her expression. Her voice buoyant with ecstasy, and everything she had said and done.

The emotion I had felt from her that day could not be expressed with the simple word *loyalty*.

It was…

“Fanaticism. To the Southern Heaven Demon Empress—or rather, to all of Dark Heaven—the Lord of Heaven is no different from a living god.”

“……!”

“Every member of Dark Heaven fears and reveres the Lord of Heaven. If he ordered them to capture me by any means necessary, then that order would be a divine command no one could disobey.”

The Blood Lord, who had been so powerful. The Western Heaven Demon Lord.

Even the Southern Heaven Demon Empress, who had met her end this time, had prostrated herself before the Lord of Heaven and claimed to be his servant.

Each of them was a monster capable of tearing apart an ordinary Supreme Peak master with their bare hands.

And the Lord of Heaven was the king and god whom those very monsters worshiped.

“I can’t be certain, but I think the Southern Heaven Demon Empress tried to capture me for one reason alone: because the Lord of Heaven had taken an interest in me.”

“Simply to earn the Lord of Heaven’s favor?”

I quietly nodded, and Jeok Cheongang muttered like a groan.

“A fanatic…”

His fading voice was swallowed by the wind.

Mounted on the back of the tiger, Jeok Cheongang silently watched the scenery rushing past us. Then he suddenly spoke.

“Have you ever seen a member of the Demonic Cult?”

“Do I look about sixty years old to you?”

“Yes. At your age, it would be natural that you hadn’t seen one. You were born long after the Great Faction War ended.”

“Why are you asking that when you already know?”

“I suddenly had a thought. Perhaps it would be better to fight the Demonic Cult of that era once more.”

“……!”

“Of course, they were fanatics, too. But the Heavenly Demon, their leader, was ultimately nothing more than a human being. The hundred thousand Demonic Path warriors beneath him knew that as well. To them, the Heavenly Demon was merely the Cult Leader guiding them—not a god.”

I understood what Jeok Cheongang was trying to say.

To the members of the Demonic Cult, the Heavenly Demon had been a human made of flesh and blood. But to every member of Dark Heaven, the Lord of Heaven was a god.

That was why they would fight for their god.

They would fight without fear of death. Even with countless blades and spears buried in their bodies, they would smile as they breathed their last.

“It will be the most terrible war in history.”

Jeok Cheongang continued, watching me with heavy eyes.

“Especially for you.”

“Because the Lord of Heaven is watching me?”

“Whether you wanted it or not, you have already drawn more attention than necessary. Even at this very moment, your name is probably echoing somewhere across the land.”

“……”

“The Three Saints and Ten Kings are old names. But you are different. You possess a talent without precedent throughout history, and no one in the world can deny that you became a master despite having only just passed the age of twenty.”

There was unmistakable pride in Jeok Cheongang’s gaze as he looked at me, along with a trace of unease.

“That is why the Lord of Heaven is watching you, too. And more importantly, he has already seen you once—your true nature and the infinite potential hidden within you.”

“……The underground prison of the Sichuan Tang Clan.”

“Yes. Using some unknown supernatural power, he saw you through the Western Heaven Demon Lord’s eyes.”

How could I forget?

The stone wall sprayed with blood, with stone dust raining down over my head.

And the words spoken by the Western Heaven Demon Lord as he stood tall and looked at me.

No—the words spoken by the Lord of Heaven, who had briefly borrowed the body of his servant.



*“Interesting. Very interesting.”*



He had definitely been smiling then.

Even as his entire body turned into a handful of ashes and scattered away, he had not forgotten to offer me one final greeting.



*“I’ll see you again.”*



Just remembering that day made my heart sink.

Jeok Cheongang silently watched me take a small, deep breath before speaking.

“Perhaps… the Lord of Heaven has an inkling of the secrets you have never told anyone.”

“……!”

“That is why I can no longer avoid asking you, either.”

In a world that had stopped as if someone had pressed a pause button, Jeok Cheongang slowly parted his lips.

“Can you tell this old man everything you’ve been hiding?”



* * *



Jeok Cheongang raised his head and looked at the sky.

The sky had poured down rain without pause for the past three days, but unlike his endlessly confused heart, it was blue and clear.

*The realm of immortals…*

The voice that had failed to escape scattered inside his mind. What else could he say? How was he supposed to understand it?

Despite having lived for an extraordinarily long time, all of it suddenly felt meaningless.

*If you were here, I could have steadied this confused heart in no time.*

Jeok Cheongang thought of the friend who had died several months earlier.

A man who loved alcohol and meat and was a sorry excuse for a monk, yet was called the Dharma King because he cared more deeply about people’s hearts than anyone.

But he soon shook his head.

The Dharma King was no longer of this world. And even if he had been alive, he would not have been able to look up at that blue sky and read the heavenly patterns.

*You said the heavenly patterns had already gone awry. That the sky no longer gave anyone any answers. You definitely said that.*

At the same time, the Dharma King had foretold a massive war.

He had said that a force capable of throwing even the heavens into confusion would spread across the world, becoming a blaze that swept in every direction.

But that was not all the Dharma King had foreseen.

*The Master of the Morning Star.*

A new star rising to illuminate the confused heavens.

The Dharma King had identified a young man as the Master of that Morning Star, and afterward Jeok Cheongang had gone to Mount Jiuhua and made that young man the successor to the Fire Gate Clan’s lineage.

“Hah… I thought he was nothing more than a drunken monk who enjoyed spouting nonsense.”

His mutter, mixed with a hollow laugh, scattered into the empty air. Jeok Cheongang stood silently as the cool breeze swept over his entire body, then suddenly shifted his gaze to the side.

A single beast was charging forward without pause.

And one person, strapped securely in place with thick leather straps, was sprawled facedown across the saddle.

No, not just any person.

Jeok Cheongang’s one and only Disciple.

*What an infuriating brat. He caused all this trouble, and now he’s sleeping like a baby.*

On the one hand, it was absurd. But after hearing a rough account from Jin Taekyung, Jeok Cheongang no longer had the strength to be surprised.

A completely different world, utterly removed from Murim. And a young man traveling back and forth between that place—one like the realm of immortals—and Murim.

*What an infuriating brat. He caused all this trouble, and now he’s sleeping like a baby.*

On the one hand, it was absurd. But after hearing a rough account from Jin Taekyung, Jeok Cheongang no longer had the strength to be surprised.

A completely different world, utterly removed from Murim. And a young man traveling back and forth between that place—one like the realm of immortals—and Murim.

Jeok Cheongang could not understand all of it, but he had already accepted that the unbelievable story he had heard was entirely true.

*Could this brat actually be some kind of Little Immortal?*

Just as he muttered the thought to himself, a long strand of drool hanging from Jin Taekyung’s mouth landed squarely on Jeok Cheongang’s cheek.

With a wet smack.

“……”

His fist tightened of its own accord.

But instead of punching his sleeping Disciple in the forehead, Jeok Cheongang sighed and adjusted the young man’s disordered posture.

*Yes. Sleep soundly. You’ve been through a lot.*

No. No, that wasn’t right.

Jeok Cheongang muttered in a voice quiet enough for only one person to hear.

“Have a safe journey.”
```
