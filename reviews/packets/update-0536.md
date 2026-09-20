<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0536.txt",
      "sha256": "69a06fe325f0c59b133574bfd988730a71fe2002731797e476b8a95038e9252c",
      "bytes": 12754
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "472e74877174a7868e370f0bfc91b2953d5b32a011397adb46e743bfacc62cac",
      "bytes": 3652
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "af90627d4052b7c6389b3a086fe0914e59e0c8829b8efd1996d99a876f749e42",
      "bytes": 170267
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "0dd13d78ccb3f4b64c44339ceaf6d04263eb214f9ef41102a47fea2d86848363",
      "bytes": 803
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "f3316416ec9c020da374506afdc5b601dadcd54f1d3ac56f96608fbd5e116158",
      "bytes": 1144
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a8088196f1a02d9fc4bf11b8964ec1b49c830db8f9136b6e9695e0c9fa401589",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "140e665156e56edaed82644a5dbec2a8bf0dd64888695020098fa4f18cec4821",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2c99ffffcb3d4899ab69c05f8076ec983926745b1e8ab1f8faed459601b74837",
      "bytes": 2021
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0470c4f708c4feb8dc2f83fe1589e6acf8efef8343f62cd6f6aea2f643174290",
      "bytes": 622
    },
    {
      "path": "characters/Jongni Chu.md",
      "sha256": "bad98e7a82506f7df40254040fd41365bd2c8aed6b43123229537197d10b561e",
      "bytes": 1451
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "86b1e4cf6e112d71ff1596ac12b91cb3f1ed49ff25085e6bd471ea4dd4de8a1d",
      "bytes": 985
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "037f524e958f910979c9d07fffe52e926e522ff285fea83a6b4474cc5f9e2953",
      "bytes": 726
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "05a8c4777018be7f302e4c2708fd677b8877ef126aef4f5dcb9e47fe488fbc28",
      "bytes": 758
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6953309b55894d95e3d101930af21fd5c4d5febe941387f6112a5143182c1a16",
      "bytes": 161288
    }
  ],
  "estimated_tokens": 13847
}
-->

# Durable State Update — Chapter 536

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 536. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 536. Profile updates may replace only one
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
  "chapter": 536,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 536,
    "continuity_sources": [536],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Jin Taekyung and Cheongpung's prominent role in raising the Murim Alliance flag made them objects of intense attention among Murim factions.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Cheongpung has recently lost his appetite while refining it.",
    "Mimi is now a large horned snake under Cheongpung's care, eats dumplings, sweets, and Blood Fish, and has recently had her condition examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Mae Jonghak has summoned Taekyung and Cheongpung to the Alliance Leader's Hall, where the leaders of the Nine Sects and One Gang, Five Great Families, and surviving legendary masters have gathered; the purpose remains unknown."
  ],
  "continuity_sources": [
    535,
    534
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Why has the Alliance Leader summoned Jin Taekyung and Cheongpung, and what is the purpose of the gathering?"
  ],
  "safe_through": 535,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, and 이룡각 as Two Dragons Pavilion; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, and monster-comparison humor.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진백양    | **Jin Baekyang**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 권왕     | **Fist King**                 | Yan Hwapyeong  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 진주언가   | **Jinzhou Yan Family**           |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 종리추 | **Jongni Chu** | Young Peak martial artist from Yunnan; conceals his sect. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 상승검 | **Always-Victorious Sword** | Jongni Chu's self-styled epithet, coined in this chapter. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 맹주부 | **Alliance Leader's Office** | Office directly serving the Alliance Leader. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 종리추 | 진태경 | new acquaintances | friend; you | casual and overly familiar | Jongni Chu immediately declares Taekyung his friend and persistently follows him. |
| 진태경 | 종리추 | new acquaintances | you; Jongni Chu; punk | blunt and dismissive | Taekyung rejects Jongni Chu's forced friendship and repeatedly tells him to leave. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 종리추 | 청풍 | newly met fellow finalist | friend | casual and overly familiar | Jongni Chu immediately calls the disguised Cheongpung friend after learning his false identity. |
| 청풍 | 종리추 | newly met fellow martial artist | friend | casual and exuberant | Cheongpung enthusiastically accepts Jongni Chu's offer of friendship while still using his disguise. |
| 적천강 | 종리추 | legendary_master_to_suspicious_rival | you / tongue-cut bastard | grave and threatening | Questions Jongni Chu about Tianshan and threatens him over harm to Taekyung or Cheongpung. |
| 종리추 | 적천강 | suspicious_rival_to_legendary_master | you | polite and taunting | Refuses to answer Jeok Cheongang directly and hints at the danger to his Disciple. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 혈주 | 종리추 | hostile_opponents | you; fearless bastard | hostile and suspicious | The Blood Lord questions Jongni Chu's identity and calls him the fearless man who interfered with his attack on Hong Dao. |
| 종리추 | 혈주 | opponents | you | calm and admonishing | Jongni Chu addresses the Blood Lord as 자네 while explaining that he must stop him by force. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 종리추 | 송호 | old_acquaintances; former_savior_and_survivor | Thousand-Faced Fox Song Ho; you | casual-familiar | Mae Jonghak addresses Song Ho informally, asks about his prosthetic leg, and recalls that Song would be the first to recognize him. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 문가 | hostile_interlocutors | Mun | blunt and threatening | Jeok Cheongang addresses the Slaughter Saint as Mun while defending Jin Taekyung. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 486
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 535
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, and the creator of the snake-inspired Mimi Step footwork technique.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Mungyeong recently examined her condition.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 535
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 535
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 534
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 534
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jongni Chu.md

# Jongni Chu (종리추)

- **Safe through:** Chapter 520
- **Aliases:** Always-Victorious Sword; Life-Sustaining Sword
- **Role:** Sword Saint Mae Jonghak, Cheongpung's grandfather, who traveled for a year under the young identity Jongni Chu after Returning to Youth; while using Jongni Chu's identity, he concealed his Supreme Peak realm through Returning to Simplicity, coined Always-Victorious Sword, fought through the Star-Array Grand Banquet, attacked Cheongpung in the semifinal, and left the final after forcing Jin Taekyung out of bounds; he revealed himself at Mount Song, protected Cheongpung from the Blood Lord with the divine Thirty-Six Plum Blossom Swords, treated Jeok Cheongang and Cheongpung after the Blood Lord escaped, and confirmed his identity to Jin Taekyung and Song Ho.
- **Personality:** Approachable, eccentric, relentlessly positive, and unusually eager to form friendships; treats even severe verbal abuse as proof of genuine friendship.
- **Voice:** Friendly, casually familiar, cheerful, and shamelessly persistent.
- **Relationships:** Immediately declares Jin Taekyung his friend after meeting him, follows him through Henan, and travels with Taekyung and the other finalists toward Luoyang after passing the preliminaries; he also immediately befriends the disguised Cheongpung and overwhelms a masked Hidden Shadow Pavilion agent who attacks him.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 535
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 525
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 525
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded in the Three-Gate Bloodbath and recovering under medical care.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, and Mimi is his cherished old friend and companion, currently entrusted temporarily to Cheongpung while the clan's future is uncertain.

## Korean source

```text
＃536화



이룡각(二龍閣).

귓가에 닿은 단어는 처음 듣는 것이었고, 그만큼 낯설었다. 하지만 동시에 알 수 있었다.

‘이룡각의 주인들.’

그것이 나와 청풍을 가리키는 것이라는 사실을.

그리고 다음 순간, 매종학의 입술 사이로 차분하면서도 힘 있는 목소리가 흘러나왔다.

“열화신룡 진태경. 가까이 오라.”

말투도, 분위기도 다르다.

평소 친구라 부르며 내게 장난을 걸었던 모습은 더 이상 어디에도 없다.

지금 눈앞에 있는 자는 상승검 종리추도, 검성 매종학도 아니다.

저벅.

크게 심호흡하며 한 걸음 앞으로 다가간 나는 무림맹의 맹주를 향해 정중히 포권을 취했다.

“태원진가의 진태경, 맹주님을 뵙습니다.”

나를 응시하는 매종학의 눈동자에 빛이 서렸다.

“태원진가는 오랜 세월 의기(意氣)의 표상이었다. 굶는 이를 배불리 먹였고, 병든 이는 보살폈으며 중원이 위험에 처할 때면 언제나 목숨을 아끼지 않고 맞서 싸웠지.”

삼백 년. 자그마치 삼백 년이다.

태원진가의 뿌리는 명문가라 불릴 만큼 깊고 단단했다. 흔들릴지언정 뽑히지 않았고, 걸음이 휘청일지언정 정도(正道)를 벗어나는 법이 없었다고 했다.

“그대는 이 년 전 겨울. 한 핏줄이자 가문의 대장로였던 화양검 진백양을 직접 베었다. 은영각주. 그 이유가 무엇인가?”

조용히 시립해 있던 은영각의 수장, 천면호리 송호가 굳은 표정으로 입을 열었다.

“배반자였기 때문입니다. 이미 오래전부터 암천의 뜻에 따라 움직인 그는 태원진가뿐만 아니라 무림의 배반자였습니다.”

“확실한가?”

“속하의 목숨을 걸지요.”

목숨을 걸 필요도 없다.

그 사실을 모르는 사람은 이 자리에 아무도 없으니까.

아니, 무림의 소식에 조금이라도 귀가 밝다면 누구라도 그에 관해 알고 있다.

그렇다면 모두가 알고 있는 이런 이야기에 왜 아까운 시간을 쓰는가.

나는 그 이유를 이미 짐작하고 있었다.

‘다시 한번 알려 주기 위해서. 동시에 납득시키기 위해서.’

지금도 계속해서 이어지고 있는 매종학의 목소리는 오롯이 나를 향한 것이 아니다.

진짜 목표는 바로 이 드넓은 대회의실에 자리한 이십여 명의 거인들이다.

“일 년 전. 바로 이곳 하남에서 성라대연이 열렸고, 암천의 습격에 의해 소림의 경내가 피로 물들었지. 그대는 무엇을 했는가?”

매종학의 물음에, 나는 망설임 없이 대답했다.

“싸웠습니다.”

“이유는?”

“그건…….”

나는 문득 입을 다물었다.

‘이유가 뭐냐고?’

순간적으로 찾아온 당황에 말문이 막혔다.

몰라서가 아니다. 단 한 번도 생각해 보지 않았던 문제였기 때문이었다.

‘글쎄. 왜였을까.’

나는 오랫동안 스스로를 이기주의자에 속물이라고 생각해 왔지만, 그렇다고 해서 피도 눈물도 없는 냉혈한은 아니었다. 눈앞에서 사람이 죽어 나가는데 실익을 따질 틈이 어디 있겠나.

소림사가 피로 물들던 그 날, 내 머릿속에 물음표는 없었다. 오직 느낌표만이 가득한 채로 달려갔고, 그렇게 싸웠을 뿐이다.

나는 후련한 목소리로 대답했다.

“생각해 본 적 없습니다.”

“어째서인가?”

“사람이라면 당연히 해야 하는 일이었으니까요.”

“사람이라면 당연히 해야 할 일이라…….”

내가 한 대답을 작게 뇌까린 매종학이, 미소 띤 눈으로 자신의 제자이자 의손주를 응시했다.

“풍아. 너는 어떠했느냐.”

“네?”

“죽음이 두렵지 않았더냐?”

맑은 눈동자로 멍하니 매종학을 바라보던 청풍이 우물쭈물 대답했다.

“두려웠어요. 단 한 번도 죽음이라는 것을 생각해 본 적 없었거든요.”

“하지만 너는 소림으로 향했지. 그 이유가 무엇이냐?”

“……후회요.”

“음?”

“평생 후회했을 것 같아요. 그때 도망쳤다면.”

그때였다. 작게 웅얼거리던 청풍의 목소리가 또렷해진 것은.

“제 목숨보다, 더 큰 무언가를 잃게 될 것 같았어요.”

맞다. 혈주와 싸우던 그때에도 녀석은 그리 말했었다.

베이고, 찢기고, 엄청난 피를 흘리며 고통에 몸부림치면서도 물러서지 않았다. 상대가 되지 않는다는 것을 알면서도 끊임없이 달려들었다.



‘뭐냐? 왜 이렇게까지 먼저 죽지 못해서 지랄들이냐는 말이다!’



그리고 의문과 분노를 담아 묻는 혈주를 향해, 청풍은 맑게 웃으며 대답했었다.



‘물러나면…… 평생 후회할 것 같아서.’



그 후회. 뭔지 안다.

어쩌면 나는 죽음에 대한 두려움보다, 홀로 겪어야 할 후회의 시간에 대한 두려움이 더 컸을지도 모르겠다.

“후회. 후회라…….”

작게 중얼거린 매종학이 내게 시선을 돌렸다.

“그대는 어떤가?”

“저 말씀이십니까?”

이미 그 질문에 대한 답은 처음 헌터 일을 시작하던 그때부터 변함이 없다.

피식 실소를 흘린 내가 대답했다.

“죽음은 항상 두렵죠. 저 죽는 거 무서워합니다.”

내가 너무 솔직했나?

크흠. 큼. 잠자코 상황을 주시하던 이들 중 몇몇이 불편한 기색이 담긴 헛기침을 토해 낸다.

하지만 어느새 매종학의 입가에 맺힌 웃음은 더욱더 짙어져 있었다.

“죽음에 대한 두려움을 이기고 곤경에 처한 다른 이를 돕는 것. 그것이 바로 협(俠)이다.”

“……!”

흘러나오던 헛기침이 뚝 멎었다. 삽시간에 고요해진 사방.

삐딱한 자세로 의자에 앉아 있던 한 사람이 불쑥 입을 열었다.

“사람이라면 당연히 해야 할 일. 허나 그리 생각하는 것과 행하는 것은 천지 차이지. 그리고 너희 두 녀석은 망설임 없이 행하였다.”

목소리에 따뜻한 온기가 느껴진다. 나를 바라보는 화왕 적천강의 눈은 분명히 웃고 있었다.

“그것이 바로 인의(人意)니라.”

“……!”

인의와 협. 협과 인의.

한편으로는 같지만 다르고, 짧지만 무거운 의미가 담긴 두 단어가 좌중을 짓눌렀다.

사람들은 말한다. 죽음을 두려워하지 않는 자가 진짜 무림인이라고.

하지만 죽음의 두려움 앞에서도 굴복하지 않고 인의와 협을 행하는 이를, 세상은 다른 이름으로 부른다.

“협객(俠客)…….”

누군가의 입술 사이로 새어 나온 중얼거림이 유난히도 크게 울려 퍼진 그때. 희미한 미소를 띤 반백의 장년인이 입을 열었다.

“협객이라. 그것참, 썩 마음에 드는 단어로군.”

그리 크지 않은 체구에 비해 이상하리만치 크고 두꺼운 손. 나는 그제야 장년인의 정체를 깨달았다.

‘권왕(拳王) 언화평.’

이제는 낡고 케케묵은 까마득한 과거. 정파 간의 세력 다툼으로 처참히 몰락한 진주언가의 마지막 후손.

이름 없는 험산의 봉우리에서 세상을 등진 채 살아가던 그는 십만의 마병이 중원을 침공했다는 소식에 망설임 없이 무림맹에 합류했다고 했다.



‘권왕이 왜 대단한 놈인 줄 알아?’

‘저야 모르죠.’

‘한때 노부가 물었었지. 정파 놈들 때문에 태어나기도 전에 가문이 몰락했는데 배알도 없냐고. 여기 모인 놈 중에 인의와 협을 아는 놈들이 몇이나 되겠냐고.’

‘진짜 눈치가 없으시네요.’

‘닥치고 들어라. 이다음에 그놈이 한 대답이 걸작이니까.’

‘뭐랬는데요?’

‘상관없다더군.’

‘네?’

‘노부가 한 말 그대로다. 아무것도 상관없고, 자신은 그저 돕기 위해 왔다는 거야. 그리고 정마대전이 끝나자마자 허깨비처럼 사라져 버렸지. 아무리 생각해도 그놈은 진짜였어. 으허허.’



바로 그 권왕 언화평이 지금 이쪽을 바라보며 웃고 있다. 따뜻한 온기가 느껴지는 웃음이었다.

“당연한 것을 당연하게 행하는 것. 두려움을 이겨 내고 나아가는 것. 그게 바로 협객이지. 그렇고말고.”

흡족한 표정으로 고개를 끄덕이는 사람은 권왕뿐만이 아니다.

곳곳에서 부드러운 시선으로 나와 청풍을 바라보고 있었다.

특히 그중 낯익은 몇몇 인물이 보내는 시선에는 숨길 수 없는 고마움이 담겨 있었다.

‘만독수라(萬毒修羅) 당사독.’

아직 몸이 완전히 회복되지 않았는지, 파리한 안색을 하고 있었음에도 자세는 꼿꼿하고 눈동자에 서린 녹광은 또렷했다.

시선이 마주치자 주름진 입꼬리를 슬쩍 끌어당긴 그가 돌연 입을 열었다.

“이 늙은이가 사천당가의 가주로서 한 말씀 올릴까 합니다.”

갑작스러운 발언에 시선이 집중된다. 매종학이 작게 고개를 끄덕이자 쉭쉭거리는 목소리가 이어졌다.

“무림맹의 각주는 막중한 무게를 지닌 중책입니다. 뛰어난 무공은 물론 그에 따른 경륜도 필요하다 생각됩니다. 불혹은커녕 이립도 되지 않은 젊은이들이 맡기에는 무리지요.”

생각지도 못한 말에 순간 작은 동요가 퍼져 나갔다. 동시에 몇몇 사람의 안색이 가볍게 바뀌었다.

누군가는 기쁨, 누군가는 불쾌함 따위의 감정이 낯빛을 스쳐 지나간다.

하지만…….

‘끝까지 들어 봐야 하는 건 한국말에만 해당하는 게 아니지.’

그리고 다음 순간 이어진 당사독의 말은 내 짐작을 확신으로 바꿔 주었다.

“허나, 열화신룡 진태경과 화산신룡 청풍. 이 두 사람만은 논외입니다. 그들은 산서에서, 하남과 사천에서, 호북에서 암천과 싸웠고 인의와 협이 무엇인지 보여 주었습니다. 이 늙은이와 가문 역시 감히 갚을 수 없는 빚을 졌지요.”

그 말에 곳곳에서 동의하는 목소리가 흘러나온다.

무림을 종횡하며 개인적으로, 혹은 적천강이나 태원진가를 통해 인연을 맺은 문파와 가문의 수장들이다.

아무런 접점이 없음에도 불구하고 당연하다는 듯 고개를 끄덕이는 이 또한 있었다.

그리고 이와 같은 반응에 힘입은 만독수라 당사독이 또렷한 목소리로 말을 이었다.

“이들이 무림맹의 중책을 맡는다고 하여 그 누가! 감히 자격을 의심할 것이며 맹주의 명에 토를 달겠습니까.”

유난히 강한 힘이 실린 부분에, 몇몇 사람의 미간이 찌푸려졌다. 종남파의 장문인인 풍운검군 역시 그중 하나였다.

녹광이 어린 눈빛으로 천천히 훑어본 당사독이 포권을 취했다.

“보시다시피 아무런 잡음도 일지 않을 터이니, 맹주께서는 괘념치 마시고 명하시면 될 것입니다.”

누군가 불만을 표하기도 전에 논란을 종식시켜 버리는 화술.

심지어 상대는 무림의 대표적인 노빠꾸 종족인 사천당가의 가주다.

비록 사천혈사로 인해 엄청난 피해를 입었지만, 사천당가가 오대세가의 일원이며 무시하지 못할 저력을 지녔다는 사실은 변하지 않는 사실이다.

“으음…….”

누군가가 흘린 무거운 침음성.

그리고 짧은 침묵을 깨트리는 목소리가 있었다.

“열화신룡 진태경. 그리고 화산신룡 청풍.”

따뜻한 눈빛으로 나와 청풍을 응시하던 매종학이 말을 이었다.

“정작 그대들에게는 묻지 않았구나. 이룡각에 속할 뜻이 있는가?”

그 순간이었다.

띠링.



무림맹에 입맹(入盟)하시겠습니까?



눈 앞에 펼쳐진 알림.

나도, 청풍도. 고민은 길지 않았다. 시선을 마주친 우리가 한 목소리처럼 대답했다.

“그리하겠습니다.”

“하면 정식으로 명한다. 지금 이 시간 부로 두 사람은 무림맹주의 명만을 받드는 맹주부 직속 이룡각(二龍閣)에 속할 것이며, 각각 한 사람의 각주가 되어 필요한 인원을 선별할 수 있는…….”

이어지는 말은 제대로 들리지 않았다. 아니, 제대로 들을 수 없었다.

띠링. 띠링. 띠링, 띠링!

쉴 새 없이 울려 퍼지는 종소리가 귓가를 가득 메웠다.
```

## Final English reading copy

```markdown
# Chapter 536

Two Dragons Pavilion.

The words reaching my ears were completely unfamiliar—just as unfamiliar as the name itself. And yet, at the same time, I understood.

*The masters of the Two Dragons Pavilion.*

That was referring to Cheongpung and me.

Then, a calm yet powerful voice flowed from between Mae Jonghak’s lips.

“Blazing Flame Divine Dragon Jin Taekyung. Come closer.”

His manner and the atmosphere were completely different.

There was no trace of the man who usually joked around with me and called me his friend.

The person standing before me was no longer Always-Victorious Sword Jongni Chu, nor was he Sword Saint Mae Jonghak.

Step.

After taking a deep breath, I walked forward and respectfully cupped my hands toward the Alliance Leader of the Murim Alliance.

“Jin Taekyung of the Jin Family of Taiyuan greets you, Alliance Leader.”

A light shone in Mae Jonghak’s eyes as he stared at me.

“For generations, the Jin Family of Taiyuan has stood as a symbol of righteous spirit. It fed the hungry, cared for the sick, and whenever the Central Plains was in danger, its members fought without regard for their own lives.”

Three hundred years.

No less than three hundred years.

The Jin Family of Taiyuan had roots deep and sturdy enough to be called an illustrious family. It might have swayed, but it was never uprooted. Its steps might have staggered, but it had never once strayed from the righteous path.

“Two years ago, in winter, you personally cut down Blade of Flowers Jin Baekyang, your own blood relative and the family’s Head Elder. Chief of the Hidden Shadow Pavilion. What was the reason?”

The leader of the Hidden Shadow Pavilion, Thousand-Faced Fox Song Ho, who had been standing silently at attention, opened his mouth with a stiff expression.

“Because he was a traitor. He had been acting in accordance with Dark Heaven’s will for a long time. He was a traitor not only to the Jin Family of Taiyuan, but to the entire Murim.”

“Are you certain?”

“I stake my life on it.”

There was no need to stake his life.

No one present was unaware of the truth.

No. Anyone with even the slightest ear for news from the Murim knew about it.

Then why waste precious time discussing something everyone already knew?

I already had a pretty good idea.

*To remind them once again. And to convince them at the same time.*

Mae Jonghak’s voice, which continued to ring out, was not directed solely at me.

His true targets were the more than twenty giants seated throughout this enormous conference hall.

“One year ago, the Star-Array Grand Banquet was held here in Henan, and Shaolin’s grounds were stained with blood during Dark Heaven’s attack. What did you do?”

I answered Mae Jonghak’s question without hesitation.

“I fought.”

“Why?”

“That was…”

I suddenly closed my mouth.

*Why?*

The question caught me off guard and left me speechless.

Not because I didn’t know.

Because I had never once thought about it.

*Well. Why had I?*

For a long time, I had considered myself a selfish materialist. But that didn’t mean I was a heartless, bloodless bastard. When people were dying right in front of me, where was the time to calculate whether there was anything in it for me?

On the day Shaolin was stained with blood, there had been no question mark in my head. It was filled with exclamation marks. I had run there and fought.

I answered in a relieved voice.

“I’ve never thought about it.”

“Why not?”

“Because it was something any person would naturally have to do.”

“Something any person would naturally have to do…”

Mae Jonghak murmured my answer under his breath, then turned his smiling eyes toward his Disciple and sworn grandson.

“Pung. What about you?”

“Me?”

“Were you not afraid of death?”

Cheongpung stared blankly at Mae Jonghak with clear eyes before answering hesitantly.

“I was afraid. I’d never thought about death even once before.”

“But you went to Shaolin. Why?”

“…Regret.”

“Hmm?”

“I think I would have regretted it for the rest of my life if I’d run away then.”

That was when Cheongpung’s softly murmuring voice grew clear.

“I felt like I would lose something greater than my life.”

That was right. He had said the same thing when we fought the Blood Lord.

Even as he was cut, torn open, and writhing in agony while bleeding an enormous amount of blood, he never retreated. Even knowing he was hopelessly outmatched, he kept charging forward.

*What the hell? Why are you acting like you’re so desperate to die first?*

And when the Blood Lord had asked him that with confusion and anger, Cheongpung had answered with a clear smile.

*If I retreat… I think I’d regret it for the rest of my life.*

That regret.

I knew what it was.

Perhaps I had been more afraid of the years of regret I would have had to endure alone than I was of death itself.

“Regret. So, regret…”

Mae Jonghak muttered quietly, then turned his gaze toward me.

“What about you?”

“Me, sir?”

The answer to that question had never changed—not since the moment I first began working as a Hunter.

I gave a short, quiet laugh and answered.

“Death is always scary. I’m afraid of dying.”

Had I been too honest?

“Ahem. Hm.”

Several of the people who had been silently watching the situation cleared their throats uncomfortably.

But by then, the smile at the corners of Mae Jonghak’s mouth had grown even deeper.

“Overcoming the fear of death and helping someone else in trouble. That is chivalry.”

“……!”

The throat-clearing stopped abruptly. Silence fell over every direction in an instant.

Then a man sitting crookedly in his chair suddenly spoke.

“Something any person should naturally do. But thinking that way and acting on it are worlds apart. And you two acted without hesitation.”

There was warm feeling in his voice. The eyes of Fire King Jeok Cheongang, gazing at me, were unmistakably smiling.

“That is humanity.”

“……!”

Humanity and chivalry.

Chivalry and humanity.

The two words were alike in one sense yet different in another. Brief as they were, their weight pressed down upon everyone in the room.

People say that someone who does not fear death is a true martial artist.

But the world has another name for those who refuse to yield to the fear of death and still act with humanity and chivalry.

“A knight-errant…”

The murmur that slipped between someone’s lips rang out unusually loudly.

That was when a graying middle-aged man with a faint smile opened his mouth.

“A knight-errant. Now that is a word I rather like.”

His hands were strangely large and thick for a man of his relatively modest build.

Only then did I realize who he was.

*Fist King Yan Hwapyeong.*

A distant, dusty past that had long since become old news.

The last descendant of the Jinzhou Yan Family, which had been utterly ruined by power struggles between orthodox factions.

He had turned his back on the world and lived atop an unnamed rugged mountain. But when he heard that a hundred thousand demonic soldiers had invaded the Central Plains, he had joined the Murim Alliance without hesitation.

*“Do you know why the Fist King is such an incredible man?”*

*“How would I know?”*

*“I once asked him whether he had no pride after the orthodox bastards caused his family to fall before he was even born. I asked him how many of the people gathered here even understood human righteousness and chivalry.”*

*“You really have no sense of timing.”*

*“Shut up and listen. What he said next was a masterpiece.”*

*“What did he say?”*

*“He said it didn’t matter.”*

*“What?”*

*“Exactly what I said. Nothing mattered, and he had simply come to help. Then, as soon as the Great Faction War ended, he disappeared like a phantom. No matter how I think about it, that man was the real thing. Ha ha ha.”*

That very Fist King Yan Hwapyeong was looking this way now, smiling.

It was a smile filled with warm feeling.

“Doing what is only natural. Overcoming fear and moving forward. That is what makes someone a knight-errant. Indeed.”

Yan Hwapyeong was not the only one nodding with a satisfied expression.

People throughout the room were looking at Cheongpung and me with gentle gazes.

Several familiar figures in particular were sending us looks that contained unmistakable gratitude.

*Myriad-Poison Asura Tang Sadok.*

Although his complexion was pale, as if he had yet to fully recover, his posture remained straight and the green light in his eyes was clear.

When our gazes met, he slightly tugged at the corner of his wrinkled mouth before suddenly speaking.

“As the Family Head of the Sichuan Tang Clan, I would like to say a few words.”

Everyone’s attention focused on him at his unexpected statement.

Mae Jonghak gave a small nod, and Tang Sadok continued in his hissing voice.

“Being a pavilion master of the Murim Alliance is a position of tremendous weight and responsibility. I believe it requires not only outstanding martial arts, but also the experience to match. It would be unreasonable to entrust it to young people who are not even thirty, let alone forty.”

A small stir spread through the room at his unexpected words. At the same time, several people’s expressions changed slightly.

Feelings such as joy and displeasure passed over various faces.

But…

*The rule about listening to the whole sentence before judging it doesn’t only apply to Korean.*

And Tang Sadok’s next words turned my suspicion into certainty.

“However, Blazing Flame Divine Dragon Jin Taekyung and Huashan Divine Dragon Cheongpung are the exceptions. These two have fought Dark Heaven in Shanxi, Henan, Sichuan, and Hubei, and shown us what humanity and chivalry truly are. This old man and my family have incurred a debt we dare not claim we can repay.”

Voices of agreement rose from various parts of the room.

They belonged to the heads of sects and families who had crossed paths with me personally throughout the Murim, or through Jeok Cheongang or the Jin Family of Taiyuan.

There were also people who nodded as though it were only natural, despite having no connection to me at all.

Encouraged by this response, Myriad-Poison Asura Tang Sadok continued in a clear voice.

“If these two take on important positions within the Murim Alliance, who would dare question their qualifications or object to the Alliance Leader’s command?”

Several people frowned at the unusually forceful emphasis in his words.

The Wind-and-Cloud Sword Lord, the Sect Leader of the Zhongnan Sect, was one of them.

Tang Sadok slowly swept his gaze across the room, his eyes glowing green, then cupped his hands.

“As you can see, there will be no objections whatsoever. Alliance Leader, you need only give the order without concern.”

It was a masterful bit of rhetoric that killed the controversy before anyone could voice a complaint.

Besides, anyone who did object would be taking on the Family Head of the Sichuan Tang Clan—the Murim’s quintessential no-brakes clan.

Although the Sichuan Blood Tragedy had inflicted tremendous damage on the Sichuan Tang Clan, the fact remained that it was one of the Five Great Families and possessed strength no one could afford to disregard.

“Hmm…”

Someone let out a heavy groan.

Then a voice broke the brief silence.

“Blazing Flame Divine Dragon Jin Taekyung. And Huashan Divine Dragon Cheongpung.”

Mae Jonghak continued, gazing at Cheongpung and me with warm eyes.

“I have not yet asked the two of you. Do you wish to join the Two Dragons Pavilion?”

That was when—

Ding.

> **System**
>
> Would you like to join the Murim Alliance?

Neither Cheongpung nor I needed long to think.

We met each other’s gaze and answered as one.

“We will.”

“Then I hereby formally decree this. From this moment onward, the two of you shall belong to the Two Dragons Pavilion, directly under the Alliance Leader’s Office and answerable only to the Alliance Leader’s commands. Each of you shall become a pavilion master, with the authority to select the personnel you require…”

I could no longer make out the words that followed.

No. I couldn’t hear them properly.

Ding. Ding. Ding, ding!

The bells rang without pause, filling my ears.
```
