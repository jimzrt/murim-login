<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0616.txt",
      "sha256": "ea24af09620d890c09d0411782ac88238710cdd087f0f20903389d63996c78e3",
      "bytes": 13531
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0f9676982dc301995f04538d98b3e4f92109201dd9ca263e43c61620fdd6f211",
      "bytes": 2556
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fabd1b9c7a8719ac19641d7c2a1e04d5e46bfa668fc5b780f0539f31e3dfa52c",
      "bytes": 191394
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "31b568c0895c99a9031c93bb06abcb1f1ecaf75c3d992ae6f439c88210513258",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "4ad0921f0f13ea15c7aab72b0200bf8499dde4d7c6f6c19bf7c530a46e06e5b0",
      "bytes": 1147
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c633fe74edd4eb4b34def3ef72de8c695c4443d575f254299ea7cb925d500b43",
      "bytes": 1702
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "aa0dfb74bc369a344b875e32b97ef11220ac8e3e3b60f8e95134ed34544dd4c8",
      "bytes": 959
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "bc198ae6e7e78fd7c40da189aea12d2d7248161b127a1b92277dc9a9c2e73265",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "528990785c6e6e4b6da550062266dbcbf4f2afd1c0f602225510247f50b81b5b",
      "bytes": 932
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "0dd50859ac55d5726abf5a285b9e14ff17c83b846eed0ac91ce2da6374969370",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "630eb81ce8d3238c11058f1c750a888d8cf1ef8aeee2234372cc58146cbea3ff",
      "bytes": 193961
    }
  ],
  "estimated_tokens": 11999
}
-->

# Durable State Update — Chapter 616

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 616. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 616. Profile updates may replace only one
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
  "chapter": 616,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 616,
    "continuity_sources": [616],
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
    "The Fire Dragon Pavilion's Nanman expedition is traveling from Mount Daebyeol toward Yunnan and has entered Hubei after four shichen of riding.",
    "The current expedition party includes Jin Taekyung, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, and Taishan.",
    "Ju Hwaran possesses a horse-caravan map obtained through her grandfather Ju Gongsan's friendship and can guide the party along secret routes and markers.",
    "Song Ilseom and Sama Pyo are openly hostile toward each other because of Song's hatred of the unorthodox faction; Jin Taekyung prevented their first attempted fight.",
    "Jin Taekyung gained a small martial insight while developing a mass-produced martial art for modern Hunters and is now stronger than before his latest sleep.",
    "Song Ilseom is the last descendant of the Guangdong Chen Family and deeply hates the unorthodox faction.",
    "The Skeleton King has received Jin Taekyung's completed martial art and letter for Choi Minwoo.",
    "Choi Minwoo remains Guild Master of the Peace Guild and Vice Guild Master of Ares Guild while grieving Kim Hwajong.",
    "Al Diab Jawahiri remains in the Skeleton King's custody.",
    "Al-Qaeda possesses a long-running Magic Gem laboratory, and restricted supplies indicate support from established military, political, or smuggling networks.",
    "Jin-ho has inferred Jin Taekyung's involvement in the masked group's campaign and agreed to keep it secret.",
    "The Lord of Heaven has awakened, empowered Dark Heaven's servants, and declared that the Great War is beginning."
  ],
  "continuity_sources": [
    615,
    614
  ],
  "open_questions": [
    "Will Song Ilseom and Sama Pyo's hostility threaten the Nanman expedition?",
    "Who supplied Al-Qaeda with the restricted equipment, weapons, artifacts, and military goods?",
    "What results, if any, did Al-Qaeda obtain from its long-running Magic Gem experiments?",
    "What fate will the Skeleton King ultimately assign to Al Diab and the remaining terrorists?",
    "How will Choi Minwoo respond after receiving Jin Taekyung's martial art and letter?"
  ],
  "safe_through": 615,
  "temporary_decisions": [
    "Use horse caravans for 마방 and retain the established Yunnan, Nanman, and Fire Dragon Pavilion renderings.",
    "Use Pavilion Master for Ju Hwaran's address 각주님.",
    "Preserve Taishan's clipped third-person speech and simple vocabulary.",
    "Render 진일보 as a great advance and 반의 반 걸음 as a quarter of a step."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 신법     | **movement technique**                           |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 주화입마   | **qi deviation**                                 |                                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 은자 | **silver nyang** | Silver currency unit. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 검동 | **sword boy** | Young attendant hired by wandering martial artists to carry swords and perform dangerous errands. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 화룡각주 | **Fire Dragon Pavilion Master** | Unique Title awarded to Jin Taekyung. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 문가 | hostile_interlocutors | Mun | blunt and threatening | Jeok Cheongang addresses the Slaughter Saint as Mun while defending Jin Taekyung. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 614
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 615
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 585
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 615
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 615
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 615
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War; he is openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo because of his hatred of the unorthodox faction.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 615
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃616화



무림에서 성공한 장사치가 되었다는 것은, 치열한 경쟁에서 살아남았다는 뜻이다.

그런 의미에서 마방(馬幇)들이 새외와 중원을 오가며 제작했다는 지도는 그들이 왜 막대한 부를 축적할 수 있었는지에 대한 근거가 되기에 충분했다.

“여기가 맞네요. 희미하지만 틀림없는 마방의 표식이에요.”

“허, 이런 곳에 길이 있었을 줄이야.”

신속 정확 하면서도 중원 곳곳에 숨겨져 있는 은밀한 지름길.

비록 흐른 세월이 적지 않아 완전히 사라져 버린 길도 있었고, 숨겨진 만큼 극도로 험난하기도 했으나 우리에게는 그다지 큰 애로사항이 아니었다.

“조장님, 여긴 경사가 너무 가파른데요?”

“그러네. 길도 좁고. 그래도 가야지, 뭐.”

“그럼 어쩔 수 없이 말을 버려야 할 것 같습니다.”

“버리긴 뭘 버려. 짊어지고 가면 되지.”

“예?”

정정한다. ‘우리에게는’이 아니라, ‘내게는’이다.

그리고 내 말을 들은 사람들은 하나같이 눈을 동그랗게 떴다.

“뭐라고요?”

“덩치 큰 전마(戰馬)도 아니고, 초원에서 공수해 온 녀석들이니까 무게도 가볍지 않나?”

“……아무리 가벼워도 말인데. 그게 돼요?”

되더라. 그것도 생각 이상으로 쉽게.

이미 인간의 한계를 훌쩍 뛰어넘은 근력의 소유자인 나는 두 마리를 짊어지고 성큼성큼 걸었고, 나보다는 못하지만 타고난 역사(力士)인 데다 덩치까지 큰 태산은 세 마리까지 감당할 수 있었다.

“각주. 태산이. 무겁다. 어쩔 수 없이 한 마리는 여기에서 먹. 아니, 놓고 가자.”

“……침이나 삼키고 다시 말해 봐.”

사실 무게보다는 저놈의 식탐이 더 문제였다.

그리고 확연히 줄어든 시간과 거리만큼, 더 큰 장애물들이 우리를 기다리고 있었다.

“지도에 따르면 이 앞에 분명히 길이 있었어야 해요. 그런데…….”

“길이 사라졌구려. 정확히는 막혔다고 봐야겠지만.”

“송 호위의 말이 맞아요. 한두 달 전에 인근에서 산사태가 일어났다는 이야기를 들었는데, 그때 막힌 모양이네요.”

“이번에는 별수 없이 돌아가야 할 것 같소. 지도에 따르면 이 길로 족히 십 리는 이동해야 하는데, 수십 장 거리라면 모를까 이렇게 매몰된 길을 뚫는 건 어불성설……. 각주, 지금 뭐 하는 거지?”

“길 뚫을 준비.”

“어?”

“뭐 아예 산을 뚫는 것도 아니고. 흙 좀 걷어 내고 돌이나 바위 치우면 지나갈 만할 것 같은데? 몇 달 안 됐다며?”

“아니, 그렇긴 한데.”

“자고로 몸이 나쁘면 머리가 고생하는 법.”

“……듣다 보니 이상한데. 보통 그 반대 아닌가?”

“그렇지, 보통은.”

말을 짊어진 채 산을 오르고, 매몰된 길을 파헤치며 걷고 또 달리기를 며칠.

우리는 미친 듯한 속도로 호북을 넘어 사천에 당도할 수 있었다.

이 모든 것이 소수의 옛 마방들만이 공유하던 지름길, 그리고 표왕(漂王)이라 불리던 외조부가 남긴 자료를 모두 기억하고 있던 주화란 덕분이었다.

‘이렇게 빨리 올 줄이야.’

수로(水路)를 이용하지 않았음에도 이 정도의 속도라니.

물론 안 되는 것도 되게 만든 내 활약도 적지 않았지만, 주화란은 화룡각에 들어오기 전 스스로 했던 말처럼 자신의 역할을 톡톡히 해냈다.

아니, 이 정도의 성과라면 생각했던 것 이상이다.

‘확실히 무공이 전부는 아니네.’

내가 제아무리 초절정 고수라고 해도 이만한 재주는 없다. 나는 주화란을 향해 진심 어린 탄성을 내뱉었다.

“대단하십니다. 역시 주 소저밖에 없어요.”

“말, 말한테 건초 먹이고 올게요.”

“예? 아니 무슨 말들이 태산이도 아니고. 건초 먹은 지 얼마나 지났다고…… 주 소저. 주 소저?”

진짜 뭐지, 이거.

이쯤 되면 내 말이 안 들리는 건지. 안 듣기로 작정을 한 건지 모르겠다.

경신법까지 써 가며 후다닥 사라지는 주화란의 모습을 바라보던 나는 옆에서 느껴지는 시선에 고개를 돌렸다.

쉬쉭!

전광석화 같은 움직임이었지만, 내 눈썰미를 피할 수는 없다. 나는 미심쩍은 눈빛으로 범인을 바라보았다.

“마.”

움찔.

“다 봤어. 어딜 모른 척이야.”

확신에 찬 내 한마디에, 물가에 앉아 있던 송일섬이 어색한 표정으로 주위를 둘러보았다.

“음. 혹시 지금 나한테 한 말인가?”

“미안한데 근처에 너밖에 없거든. 그리고 표정 되게 어색한 거 모르지?”

“……뭘 말하는 건지 도무지 모르겠군.”

“보고 있었으면 보고 있던 거지, 뭘 그렇게 숨겨? 그리고 그놈의 유엽도는 틈만 나면 갈고 있냐. 남만 도착하면 바늘이 되어 있겠네.”

촤아악.

얼마나 정성껏 손질했는지, 거울처럼 반질거리는 도신(刀身)에 물을 끼얹은 송일섬이 짐짓 얼굴을 굳히며 대답했다.

“말 함부로 하지 마라. 내게는 남다른 의미가 있는 무기다.”

원래도 표정이 풍부한 녀석은 아니지만, 이렇게 정색하는 걸 보니 뭐가 있긴 한 모양이다.

‘하긴, 워낙 사연 많은 놈이니까.’

다른 사람의 마음에 아픈 상처를 내는 것은 못 할 짓이다.

무심코 실수를 했다는 생각에 멈칫했던 나는, 미안한 마음을 담아 조심스럽게 입을 열었다.

“음. 가문 대대로 내려온 보도, 뭐 그런 거냐?”

“그럴 리가. 가문에서는 무공 비급 하나도 빼 오지 못했다고 들었다. 조모께서는 일평생 무공을 익히지 않으셨던 분이셨어. 그 전란에서 살아남으신 것만으로도 기적이었지.”

“하긴, 보도인 것 치고는 많이 낡아 보이더라. 그럼 아버지의 유품?”

“그것도 아니야.”

좋은 시절을 추억하듯, 아련한 미소를 입가에 떠올린 송일섬이 도신을 쓸어내리며 말을 이었다.

“이 유엽도는 어릴 적 삼류 낭인의 검동(劍童) 노릇을 할 때 받았던 거다. 이것으로 난생처음 사람을 베었지. 아마 열두 살 때였을 거야.”

“……아, 그래.”

마음의 상처는 니미.

슬그머니 고개를 들던 미안함이 봄 눈 녹듯이 사라진다.

애초에 태생부터 무림인으로 태어난 놈이다. 첫 살인의 추억을 소중히 간직하고 있는 송일섬의 모습이 참…… 미친놈 같았다.

‘음. 확실히 이놈도 제정신은 아니야.’

무림에는 여러 종류의 인간군상이 있지만, 대체로 미친놈들이 득실거렸다.

애초에 무림이라는 곳이 미친놈이 아니고서야 버틸 수 없는 곳이라 더욱 그런 것일지도 모른다.

밥 먹다가 죽고. 싸우다가 죽고. 겨우겨우 살아남았어도 상처가 악화되어 죽고.

고생 끝에 고수가 되었어도 수련 중 주화입마로 죽기도 하는 곳이 무림이다.

‘제목이 뭐였더라. 전에 봤던 무협 소설에서는 금분세수(金盆洗手)로 평화롭게 은퇴하는 장면도 나왔었는데.’

무림에 오고 나서야 깨달았다. 소설은 역시 소설에 불과하다는 걸.

적천강 역시 금분세수에 관하여 묻는 내게 이렇게 말한 적이 있었다.



‘금분세수? 간단하지.’

‘오. 쉬워요?’

‘그래. 우선 금으로 된 대야를 사라. 친한 지인들도 잔뜩 부르고.’

‘처음부터 인싸와 자본주의의 냄새가 진동하긴 하는데 뭐 일단 알겠습니다. 그다음은요?’

‘마음 편히 손을 씻거라. 물론 무기에서 손을 뗀 순간, 지인들 사이에 숨어 있던 살수가 암기를 날리겠지만 말이다.’

‘아…….’

‘그리고 하나 더. 네가 지인이라고 생각했던 그놈이 살수일 수도 있다. 어떠냐. 참 쉽지 않으냐?’



친애하는 불밥 할아버지의 명언처럼, 무림이 시발 이렇다.

금분세수고 지랄이고 간에, 대다수의 무림인은 아침에 눈 뜨고 얼음물에 세수한다는 것만으로도 감사해야 한다.

어쩌면 다음 날에는 얼음물 대신 삼도천(三途川) 강물에 목욕재계할 수도 있으니까.

물론 그 상황까지 가면 은퇴한다는 의미에서는 금분세수와 비슷하긴 하다. 숨이 붙어 있느냐, 멈췄느냐의 차이지만.

‘무슨 무림 탈출 넘버원도 아니고.’

이미 폐지된 고전 프로그램이지만 무림 오면 초대박 확정이다.

TV가 보급되었다는 전제하라면 러시아 대선 투표율처럼 시청률 107% 정도 찍을지도 모르겠다.

실험 전문가로 섭외한 사마외도의 고수가 사람 좋은 웃음을 지으며 직접 실험을 진행하겠지.

‘자. 무림 동도 여러분. 이 초식에서는 이렇게 피하면 어떻게 될까요?’

푹.

‘보세요. 죽었죠? 허허.’

실험맨들의 목숨이 남아나질 않겠구만…….

전부 상상에 불과하지만, TV만 들어온다면 현실로 뒤바뀔 수 있는 곳이 무림이다.

난 이런 미친 세상에서, 미친놈들을 데리고, 미친놈들과 싸워야 하는 거고.

“……후.”

새삼 스스로가 짠해져 말없이 강물만 바라보던 그때, 송일섬이 불쑥 입을 열었다.

“사실 보고 있던 게 맞다.”

“음? 뭐가?”

“조금 전에 있었던 일 말이다. 대답을 안 한 것 같아서.”

갑자기 무슨 소린가 했네. 나는 어깨를 으쓱하며 대답했다.

“말 안 해도 알고 있었어. 그런데 왜 쳐다봤냐?”

“그냥. 소리가 들리기에 봤을 뿐이다.”

“더 솔직하게.”

“네놈의 언행이 너무 멍청해 보여서 쳐다보지 않을 수 없었다.”

“……오, 너무 솔직한데.”

“하지만 사실이지. 자꾸 그런 말을 하니까 주 소저가 자리를 피하는 것이 아니냐.”

나는 왠지 모르게 억울해진 심정이 되어 대답했다.

“아니 내가 뭘 했다고. 그냥 진심으로 감탄해서 칭찬한 것뿐인데.”

“지나가던 개도 안 믿을 소리를 하는군.”

“사실인데.”

“그만해라. 재미없다.”

“난 아까부터 재미없었어.”

“좋아. 그렇다고 치지.”

농담이라도 들은 것처럼 피식 웃던 송일섬이 내 표정을 바라보더니 떨떠름한 목소리로 물었다.

“사실이냐?”

“사실이라니까.”

“한 점의 거짓도 없이, 네가 하는 말과 행동이 어떤 의미인지. 왜 그럴 때마다 주 소저가 자리를 피하는지 전혀 모른다고?”

“하늘에 맹세코, 내 불알을 걸지.”

“허. 네가 혁무진이 아닌 본인의 불알을 걸다니…… 틀림없는 사실이군.”

뭔가 검증 절차가 이상하긴 한데, 일단 진심이 전해졌으니 넘어가도록 하자.

이제 내 말을 완전히 믿게 된 송일섬은 유니콘이라도 본 듯한 눈빛으로 나를 바라보고 있었다.

“어떻게 사람이 이럴 수가 있지?”

“뭐?”

“옛 별호가 야왕(夜王)이었다고 하지 않았나? 그럼 최소한 기본 정도는 알아야 하는 것이 인지상정인데.”

“…….”

나는 언제까지 방탕한 전임자가 싸지른 똥을 치워야 하는가. 야동왕이라면 양심상 어느 정도는 인정을 하겠지만 야왕이라니.

“……말하자면 길다.”

내 한숨 섞인 대답에 송일섬이 고개를 끄덕였다.

“당연히 그렇겠지. 매번 긴 밤을 보냈을 테니.”

“야, 이 새끼야. 칼 뽑아. 넌 오늘 뒈졌다.”

“안타깝지만 그건 나중으로 미뤄야 할 것 같군. 네놈 덕분에 일각이 지나도 나타나지 않는 고용주를 찾아야 하거든.”

“잊었나 본데, 나 화룡각주야. 네 직속 상관.”

“하지만 내게 은자를 주는 건 고용주지. 내 임무는 바로 그 고용주를 호위하는 것이고.”

잘 닦은 유엽도를 허리춤에 갈무리한 송일섬이 물가에서 일어났다.

저벅. 저벅. 한마디의 인사도 없이 모래와 자갈을 밟으며 돌아 걷던 그의 신형이, 어느 순간 우뚝 멈춘다.

“주 소저가 왜 그러는지 모르겠다면, 그 없는 눈치로 곰곰이 생각해봐라. 답은 스스로 찾아야지.”

“뭐?”

“강인해 보여도 아픔이 많은 여인이다. 상처 입을 일도, 헛되이 죽음을 맞이하는 일도 없었으면 좋겠군.”

그게 마지막이었다.

아무 일도 없었다는 듯 다시 걸음을 옮기는 송일섬의 뒷모습을 바라보던 나는, 문득 그런 생각이 들었다.

저 녀석이 아직까지 주화란의 곁에 머무는 것이 정말 은자 때문일까, 하는 생각이.

그리고 의문에 대한 답을 찾기도 전, 넘실거리는 사천의 장강(長江)을 가득 채우는 울림이 있었다.

둥. 두둥. 둥!

힘찬 북소리와 강하고 빠르게 물살을 가르는 뱃머리.

어느덧 안개를 해치며 나타난 십여 척의 쾌조선(快調船)과 그 위에 나부끼는 수룡채의 깃발을 확인한 내가 중얼거렸다.

“콜택시 왔네.”
```

## Final English reading copy

```markdown
# Chapter 616

To become a successful merchant in Murim meant surviving fierce competition.

In that sense, the map said to have been made by the horse caravans as they traveled between the Outer Lands and the Central Plains was more than enough proof of how they had managed to accumulate such immense wealth.

“This is the right place. It’s faint, but there’s no mistaking it—it’s a horse caravan marker.”

“Huh. I never knew there was a road through a place like this.”

Secret shortcuts hidden throughout the Central Plains, swift and accurate despite their concealment.

Some had vanished completely over the years, while others were so treacherous precisely because they were hidden, but neither posed much of a problem for us.

“Captain, isn’t the slope too steep here?”

“It is. And the road’s narrow, too. But we have to go, so what else can we do?”

“Then I’m afraid we’ll have no choice but to abandon the horses.”

“Abandon what? We can carry them.”

“Pardon?”

Correction. It wasn’t *us* who had no problem with it. It was *me*.

Everyone who heard my words opened their eyes wide.

“What did you say?”

“They aren’t even big warhorses. They were brought in from the grasslands, so they shouldn’t be that heavy, right?”

“……Even if they’re light, they’re still horses. Can you really do that?”

As it turned out, I could. And far more easily than I had expected.

I was already the possessor of physical strength that had far surpassed human limits, so I slung two horses over my shoulders and strode up the mountain. Taishan, who was not as strong as I was but was a natural strongman with a massive build, could manage as many as three.

“Pavilion Master. Taishan heavy. Cannot help it. One horse eat here. No, leave it here.”

“……Swallow your saliva and say that again.”

In truth, that guy’s appetite was a bigger problem than the horses’ weight.

And in proportion to the time and distance we had saved, even greater obstacles were waiting for us.

“According to the map, there should definitely have been a road ahead. But…”

“The road has vanished. More precisely, it appears to have been blocked.”

“Escort Song is right. I heard there was a landslide in the area a month or two ago. It seems the road was blocked then.”

“This time, I’m afraid we have no choice but to turn back. According to the map, we would have to travel at least ten li along this road. Unless it were a distance of a few dozen *jang*, clearing a road buried like this would be absurd…… Pavilion Master, what are you doing?”

“Preparing to clear the road.”

“What?”

“We aren’t exactly going to dig through the entire mountain. If we clear away some dirt and move the rocks and boulders, it looks like we can pass through. You said it happened only a few months ago, right?”

“No, that’s true, but…”

“As they say, when the body is weak, the head has to suffer.”

“……That sounds strange. Isn’t it usually the other way around?”

“Usually, yes.”

For several days, we carried horses up mountains, dug through buried roads, and alternated between walking and running.

At an insane speed, we crossed Hubei and reached Sichuan.

All of it was thanks to Ju Hwaran, who knew the shortcuts shared only among a handful of old horse caravans and remembered all the information left behind by her maternal grandfather, the Escort King.

*I can’t believe we got here this quickly.*

Even without using the waterways, we had traveled at an astonishing speed.

Of course, I had played no small part in making the impossible possible, but Ju Hwaran had fulfilled her role exactly as she had claimed she would before joining the Fire Dragon Pavilion.

No, given the results, she had exceeded my expectations.

*Martial arts really aren’t everything.*

No matter how much of a Supreme Peak master I became, I couldn’t do anything like this. I gave Ju Hwaran a heartfelt exclamation of admiration.

“You’re incredible. There’s no one like you, Young Lady Ju.”

“I’m going to feed the horses some hay.”

“What? Why? They aren’t Taishan. How long has it even been since they ate hay…… Young Lady Ju? Young Lady Ju?”

What the hell was this?

At this point, I couldn’t tell whether she couldn’t hear me or had simply decided not to.

As I watched Ju Hwaran hurry away using a movement technique, I turned my head at the gaze I felt from beside me.

*Swish!*

The movement had been as swift as lightning, but it couldn’t escape my sharp eyes. I stared suspiciously at the culprit.

“Hey.”

The man flinched.

“I saw everything. Don’t pretend you don’t know what I mean.”

At my certain accusation, Song Ilseom, who had been sitting by the water, awkwardly looked around.

“Hmm. Were you perhaps speaking to me?”

“Sorry, but you’re the only one nearby. And you do realize your expression is incredibly awkward, right?”

“……I have no idea what you’re talking about.”

“If you were watching, then you were watching. Why are you trying so hard to hide it? And do you sharpen that willow-leaf saber whenever you get the chance? By the time we reach Nanman, it’ll have turned into a needle.”

*Splash.*

Song Ilseom poured water over the blade, which gleamed like a mirror after being polished with extraordinary care. He deliberately hardened his expression before answering.

“Watch your mouth. This weapon has a special meaning to me.”

He had never been particularly expressive, but seeing him turn so sternly made it seem as though there really was a story behind it.

*Then again, that guy has quite a history.*

Hurting someone else’s feelings was a terrible thing to do.

I had paused, thinking that I might have made an inconsiderate mistake, then carefully opened my mouth with an apologetic expression.

“Hmm. Is it a treasured blade passed down through your family or something?”

“Impossible. I heard that my family could not bring out even a single martial arts manual. My grandmother never learned martial arts in her entire life. It was a miracle that she survived that war at all.”

“Well, it did look pretty worn for a treasured blade. Then is it a keepsake from your father?”

“That isn’t it either.”

As if reminiscing about happier days, Song Ilseom raised a wistful smile to his lips. He ran his hand along the blade as he continued.

“I received this willow-leaf saber when I was young, while serving as a sword boy for a Third Rate wandering martial artist. I cut a person with it for the first time in my life. I was probably twelve.”

“……Oh. I see.”

*Emotional scars, my ass.*

The guilt that had cautiously begun to rise within me melted away like snow in spring.

He had been born a martial artist from the start. Song Ilseom, who cherished the memory of his first killing, looked completely insane.

*Yeah. This guy isn’t right in the head either.*

There were all kinds of people in Murim, but most of them were, by and large, lunatics.

Perhaps that was because Murim was a place no one could survive without being insane.

You could die while eating. You could die while fighting. Even if you somehow survived all the hardship, your wounds could worsen and kill you.

Even after becoming a master through years of suffering, you could die from qi deviation while training.

*What was the title again? In that martial-arts novel I read before, there was even a scene where someone retired peacefully through golden-basin handwashing.[^1]*

Only after coming to Murim did I realize that novels really were nothing more than novels.

When I once asked Jeok Cheongang about golden-basin handwashing, he had answered me like this.

“Golden-basin handwashing? Easy.”

“Oh. It’s easy?”

“Of course. First, buy a basin made of gold. Then invite a whole crowd of close acquaintances.”

“It already reeks of social butterflies and capitalism, but all right. What comes next?”

“Wash your hands in peace. Of course, the moment you take your hands off your weapon, an assassin hiding among your acquaintances will throw a hidden weapon at you.”

“Ah….”

“And one more thing. The person you thought was an acquaintance might be an assassin, too. What do you think? Isn’t it easy?”

Just as my dear Fire-Rice Grandpa’s famous words suggested, this was how fucking Murim was.

Forget golden-basin handwashing or any other bullshit. Most martial artists ought to be grateful simply for waking up in the morning and washing their faces with ice water.

After all, the next day they might have to bathe and purify themselves in the waters of the Sanzu River instead of ice water.[^2]

Of course, if things went that far, it was similar to golden-basin handwashing in the sense that it meant retiring.

The only difference was whether you were still breathing.

*This isn’t Murim Escape Number One.*

It was an old program that had already been canceled, but if it came to Murim, it would be an instant smash hit.

Assuming television had been introduced, it might even reach a 107 percent viewership rating—like the turnout in a Russian presidential election.

A master of demonic, heterodox arts hired as an experiment expert would give everyone a friendly smile and conduct the experiment himself.

“All right, fellow martial artists. What do you think will happen if you dodge like this in this form?”

*Stab.*

“See? Dead. Heh heh.”

The experimenters wouldn’t survive for long……

It was all just my imagination, but Murim was the kind of place where it could become reality the moment television arrived.

In this insane world, I had to drag around a bunch of lunatics and fight other lunatics.

“……Hoo.”

Feeling sorry for myself, I silently stared at the river. That was when Song Ilseom suddenly spoke.

“I really was watching.”

“Hm? Watching what?”

“What happened a moment ago. I realized I never answered you.”

I had wondered what the hell he was talking about. I shrugged and answered.

“I knew you were watching. Why were you staring?”

“Because I heard a sound, so I looked.”

“Be more honest.”

“Your words and actions looked so stupid that I couldn’t help staring.”

“……Oh. That’s very honest.”

“But it’s the truth. Isn’t that why Young Lady Ju keeps leaving whenever you say things like that?”

For some reason, I felt wronged.

“What did I even do? I was just sincerely admiring her and complimenting her.”

“That is something not even a passing dog would believe.”

“But it’s true.”

“Stop. It isn’t funny.”

“I haven’t found it funny from the start.”

“Fine. Let’s say that’s so.”

Song Ilseom gave a quiet laugh as though he had just heard a joke. Then he looked at my expression and asked in a dubious voice,

“Is it true?”

“I’m telling you, it’s true.”

“You’re saying that, without a single lie, you have no idea what your words and actions mean? You truly don’t know why Young Lady Ju keeps leaving whenever you do that?”

“I swear to heaven, I’ll stake my balls.”

“Huh. You’re staking your own balls instead of Hyuk Mujin’s…… It must be the absolute truth.”

The verification process seemed a little strange, but since I had managed to get my sincerity across, I decided to let it go.

Now that Song Ilseom fully believed me, he stared at me as if he had seen a unicorn.

“How can a person be like this?”

“What?”

“You said your old sobriquet was the Night King, didn’t you? Then common sense dictates that you should at least know the basics.”

“……”

How long was I going to have to clean up the shit left behind by that promiscuous predecessor?

If it had been the Porn King, I could have admitted to it in good conscience to some extent. But the Night King?

“……It’s a long story.”

At my sighing answer, Song Ilseom nodded.

“Of course it is. You must have spent many long nights.”

“You son of a bitch. Draw your sword. You’re fucking dead today.”

“Unfortunately, we’ll have to put that off until later. Thanks to you, I have to find an employer who still hasn’t appeared even after fifteen minutes.”

“You seem to have forgotten, but I’m the Fire Dragon Pavilion Master. Your direct superior.”

“But the person who gives me silver nyang is my employer. And my mission is to protect that very employer.”

Song Ilseom secured the well-polished willow-leaf saber at his waist and rose from the water’s edge.

Step. Step.

Without even saying goodbye, he turned and walked away over the sand and gravel. Then, all at once, his figure came to a stop.

“If you don’t know why Young Lady Ju acts that way, think about it carefully with that nonexistent sense of tact you have. You have to find the answer yourself.”

“What?”

“She may look strong, but she’s a woman who has suffered a great deal. I hope she never has to be hurt or meet a pointless death.”

Those were his final words.

As I watched Song Ilseom’s back, he resumed walking as though nothing had happened. A thought suddenly occurred to me.

*Is that guy really staying by Ju Hwaran’s side because of silver nyang?*

Before I could find the answer to that question, a resonant sound filled the surging Yangtze in Sichuan.

*Boom. Boom-boom. Boom!*

Powerful drums. The prows of ships cutting strongly and swiftly through the current.

By then, a dozen or so swift ships had emerged through the fog, with the flags of the Water Dragon Stronghold fluttering above them.

I muttered,

“Our taxi’s here.”

[^1]: A ceremonial retirement ritual in which a martial artist washes their hands in a golden basin, symbolizing that they are giving up martial pursuits.

[^2]: The Sanzu River is a Buddhist river associated with the boundary between life and death.
```
