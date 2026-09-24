<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0998.txt",
      "sha256": "fc1f73f3469ff3c5e8099981bedd2464a84fedc5f5808ab9da44790dd5e94ff2",
      "bytes": 13419
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d9a425eb55391298fc00eebddf6a94a3d752eb26f313c3d6be9f379d2e85ca98",
      "bytes": 1042
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "621398c9438a3090504b275aed446f14ad5887e2758148be8b124c4bebd29e92",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4e492e091a1a2bc354ad8d7367103e9a0b7774360758b649c4d080ddbe0d27e2",
      "bytes": 1391
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "b5cec3945ae0fe9ffe9ccc4f59f843dd34fc5a43a77f2b08cabb091b5bcfae1e",
      "bytes": 1178
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "206a34f3d3d97184c1b962be0c733a22dcf625ea13e206ddb8249cd4644c3b40",
      "bytes": 699
    },
    {
      "path": "characters/Moon Beauty Saber.md",
      "sha256": "5ac09282519b007cbb682ed1be8519a92ac97970f7a0671ae042f708fb9036bb",
      "bytes": 637
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "fbcda8047b8c1e4e1071ccc3788ccc282ca17302feaac081f55dad60f331721c",
      "bytes": 936
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "92518639aff7f58a4de0b0404b3635b43fadea1f5f9a42239aa0950f1ac61d86",
      "bytes": 888
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "b8527f6e1136752ee621eee667e9bc38eaca739e7a98bb6e17d423ebcb2aa10e",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0cfb76de4496dfd84609e284fd61b787fe53be76130ba1752c7f0390185f35fd",
      "bytes": 274035
    }
  ],
  "estimated_tokens": 12299
}
-->

# Durable State Update — Chapter 998

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 998. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 998. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 998,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 998,
    "continuity_sources": [998],
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
    "Taekyung has left ahead of the Jin Family’s larger force; the family and its allies remain behind to move with the army.",
    "Mukyung intends to catch up with Taekyung and has urged him not to be defeated before then.",
    "The Zhuge Clan has completed all its assigned tasks; preparations are complete and the all-out war is beginning.",
    "Dark Heaven’s forces are advancing from Xinjiang; Qinghai and the Kunlun Sect are considered likely targets.",
    "Snow began falling months earlier than expected.",
    "Sama Pyo burned his father’s order to return immediately and left with the group."
  ],
  "continuity_sources": [
    997
  ],
  "open_questions": [
    "What is the objective behind Dark Heaven’s advance from Xinjiang, and where will its forces strike?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?"
  ],
  "safe_through": 997,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 체력               | **Stamina**                    |
| 게이트     | **Gate**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 월미도 | **Moon Beauty Saber** | Sobriquet of the Fang Family's top-tier wandering martial artist. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 군선 | **military vessel** | Vessel carrying the Hubei government troops and sailors. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 마봉진 | **Demon-Sealing Formation** | Zhuge Feng's formation for sealing the Gate's mana. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 한혈마 | **sweat-blood horse** | A famed breed said to descend from sweat-blood horses. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 진위경 | Zhuge Clan Family Head to Jin Family Lesser Family Head | Lesser Family Head | formal and conciliatory | Uses 소가주 while trying to secure Jin Wikyung's support during the settlement. |
| 진위경 | 제갈풍 | Jin Family Lesser Family Head to Zhuge Clan Family Head | Sir Zhuge | formal with deliberate comic deference | Uses 제갈 대협 while theatrically scolding Taekyung to force Zhuge Feng to concede. |
| 사마표 | 정호 | Black Dragon Demon Gate Young Sect Leader addressing a Shaolin Master | Master Jung Ho | Polite and ingratiating | Uses 정호대사 and 대사 while flattering Jung Ho and negotiating responsibility for the killing. |
| 정호 | 사마표 | Shaolin martial monk addressing the Black Dragon Demon Gate Young Sect Leader | Benefactor | Formal and admonitory | Uses 시주 while questioning Sama Pyo and demanding accountability. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 996
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 995
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 997
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 983
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Moon Beauty Saber.md

# Moon Beauty Saber (월미도)

- **Safe through:** Chapter 519
- **Aliases:** None
- **Role:** Moon Beauty Saber is a top-tier wandering martial artist of the Fang Family who has long since reached the level of injuring others with Sword Energy.
- **Personality:** Dignified, condescending, status-conscious, and quick to assert his superiority.
- **Voice:** Formal, self-assured, and patronizing toward people he considers beneath him.
- **Relationships:** He identifies himself as a member of the Fang Family and treats lower-status martial artists condescendingly.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 996
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 987
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 997
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃998화



진위경도 이미 말한 바 있듯이, 암천과의 대규모 일전이 벌어질 가능성이 가장 높은 곳은 곤륜파가 위치한 청해(靑海)였다.

적들이 중원으로 향하기 위해서는 반드시 무너트려야 할 교두보이자, 정파 무림으로서는 목숨 걸고 지켜 내야 하는 전략적 요충지.

그리고 바로 그렇기에, 나는 어떤 방식으로 청해성까지 가느냐는 혁무진의 물음에 망설임 없이 대답할 수 있었다.

“뛰어야지. 존나게.”

“그건 당연히 알죠. 그런데 제가 여쭙고 싶은 건…….”

“존나게 뛰는 건 좋은데 언제까지 뛰냐, 그거겠지.”

“크으, 역시 조장님. 정확하십니다.”

“계속.”

“……예?”

“계속이라고. 쭉.”

“잠깐, 이대로 쭉 청해성까지요?”

나는 힘차게 내달리는 말의 고삐를 늦추지 않으며 되물었다.

“그렇지 않으면?”

“저로서는 수로(水路)를 이용하는 게 나아 보이는데요. 우선은 조장님 말씀대로 육로로 이동하되, 섬서에서 장강의 지류를 타고 청해성까지 직행하는 겁니다. 그편이 반나절 정도는 더 빠르고 힘도 훨씬 덜 들걸요?”

언뜻 듣기에는 제법 타당한 의견이었다.

비록 반나절에 불과하지만 시간도 단축되는 데다, 중요한 전투를 앞두고 체력까지 비축할 수 있으니까.

심지어 역사와 전통이 있는 장강의 전국구 깡패, 장강수로맹조차 무림맹의 일원이니 운이 좋다면 쾌조선을 강탈…… 아니 빌려 탈 수 있을지도 모른다.

하다못해 대국의 군선(軍船)이라도.

그러나 나는 단번에 고개를 내저었다.

“육로가 더 나아.”

“왜요, 혹시 배 멀미 있으세요?”

“…….”

“있어도 좀 참고 가시죠. 제가 등 두드려 드릴게요.”

이 새끼는 초절정 고수가 죠스로 보이나.

심지어 나는 이제 막 초입에 접어든 초절정 고수도 아니다.

이제는 등봉조극의 경지에 환골탈태까지 완성한, 그야말로 초인 중의 초인.

배가 아니라 월미도 디스코 팡팡을 타고 이동해도 흔들리지 않는 편안함을 느낄 마당에 배멀미라니.

순간 할 말을 잃은 내가 어이없는 눈빛으로 혁무진을 바라보던 그때, 녀석의 뒤통수를 향해 한 줄기 맹렬한 바람이 불어닥쳤다.

쐐액, 빡!

“억!”

듣기만 해도 속이 시원해지는 타격음.

숙련된 솜씨로 혁무진의 뒤통수를 후려갈긴 적천강이 작게 혀를 찼다.

그는 말안장이 불편하다는 이유로, 좌우에 끝없이 늘어선 나뭇가지를 밟으며 이동하던 중이었다.

“멍청한 놈 같으니. 무슨 말이 그리도 많으냐. 상관이 까라면 깔 것이지.”

내가 아닌 다른 누군가에게 뒤통수를 맞았다면 눈에 쌍심지를 켰겠지만, 그 누군가가 바로 화왕 적천강이라면 이야기가 달라진다.

차마 뭐라 말도 못 하고, 아픈 뒤통수만 만지작거리던 혁무진이 눈치를 살피며 입을 열었다.

“아니, 저는 그냥 더 좋은 의견을 제시한 것뿐인데 왜 이러시는지.”

“더 좋은 의견? 정말 그리 생각하느냐?”

“아닙……니까?”

“제법 그럴듯한 의견이었던 건 인정해 주마. 하지만 네놈은 가장 중요한 한 가지 사실을 간과했다.”

혁무진이 뭐라 대답하기도 전에, 적천강의 나직한 목소리가 바람 사이로 울려 퍼졌다.

“암천. 그 간악하기 짝이 없는 놈들이 진정 청해성을 노리고 있는 것인지.”

“……!”

“아직 확실하게 알려진 것은 아무것도 없다. 사막 너머로 진군하고 있다는 암천의 대군이 어디로 향할지는 그 누구도 모른다. 중원으로 향하는 길은 비단 청해성뿐이 아니니까.”

정확히 지금의 상황을 꿰뚫고 있는 적천강의 말에, 나는 고개를 끄덕여 동의를 표했다.

맞다.

길은 하나가 아니다. 셋, 혹은 그 이상이다.

당장 청해와 감숙, 마지막으로 변방을 넘어 새외(塞外)로 분류되는 서장까지.

청해성은 전략적 요충지이기에 주 표적이 될 확률이 높은 것일 뿐, 침공 가능성은 감숙과 서장 역시 충분하다.

더군다나…….

‘놈들에게는 워프 게이트, 아니 이동진(移動陳)이 있지.’

그리고 이동진의 존재는 적들에게 더 많은 선택지를 쥐여 주는 동시에, 아군에게 있어서는 더할 나위 없이 치명적인 비수다.

당장 확인된 바로만 일천에 달하는 머릿수를 이동진으로 중원 어딘가로 보내 버릴 수 있으니 오죽하겠나.

물론 이를 해결할 방법이 없는 것은 아니었다.

기관진식에 한해서만큼은 천하제일로 불리는 제갈세가에는 마봉진(魔封陳)이라는 진법이 존재했고, 마봉진은 그 명칭에 담긴 뜻 그대로 마력을 억제하고 봉인하는 효력을 지녔으니까.

동정호에서 ‘균열’이 발생했을 당시, 더 큰 피해 없이 사태를 마무리 지을 수 있었던 이유도 가주인 제갈풍을 필두로 한 제갈세가의 식솔들이 마봉진으로 균열을 틀어막았기 때문이었다.

‘균열을 막을 정도라면 이동진의 무력화도 충분히 가능할 테고, 직접 봤던 만큼 마봉진의 효력은 확실해. 문제는 시간과 인력이지.’

천하는 실로 광활하다.

그리고 암천이 천하라는 드넓은 모래사장 어딘가에 몇 개나 되는 이동진을 만들어 두었는지는 누구도 모른다.

이동진의 해결법을 찾은 지 반년이 훌쩍 넘었음에도, 산서성 인근의 여러 문파가 잠시나마 지원군을 보내는 것을 망설였던 것이 바로 그 반증이다.

만약 단 한 개의 이동진만 남아 있더라도, 그것은 곧 날카로운 유리 조각이 되어 안심한 채 모래사장을 걷던 누군가의 발바닥을 깊숙이 파고들 테니까.

‘그렇기에, 더더욱 육로로 이동해야 해.’

오랜 세월 동안 외침(外侵)이 있었을 때마다 격전지가 되었던 청해성인 만큼, 무림맹은 할 수 있는 최선의 대책을 마련해두었을 터.

고작 반나절, 혹은 하루의 시간 차이로 무너질 만큼 그 방비는 허술하지 않을 것이다.

‘서장도 충분히 안심할 수 있는 수준은 돼. 만약 서장의 포달랍궁이 암천과 손을 잡았다 하더라도, 사천에 머무르고 있는 전력이라면 충분히 버틸 수 있다.’

서천마군이 직접 노렸던 사천당문은 엄청난 피해를 입었으나, 청성과 아미는 아직 건재한 상황.

그리고 거기에 더해, 현재 사천에는 생각지도 못한 손님들이 머무르고 있었다.

‘남만야수궁(南蠻野獸宮).’

비록 갈 길이 멀어 바삐 떠났지만, 그들에 대한 소식은 틈틈이 전해 들어 알고 있었다.

유례없는 대이주를 감행한 열대의 전사들이 마침내 밀림을 떠났고, 무림맹의 요청을 흔쾌히 받아들여 사천을 지키고 있다는 것을.

“이미 서쪽 전선(前線)은 어느 정도의 대비책을 세워 놨을 거야. 단 한 곳만 빼고.”

비단 혁무진 한 사람에게만 하는 말이 아니다.

상념을 끝마치고 불현듯 입을 연 나는, 나란히 말을 몰아 내달리는 화룡각 대원들의 얼굴을 차례차례 바라보다 나직이 덧붙였다.

“감숙(甘肅).”

“……!”

“……!”

“만약 암천이 모두의 예상을 비틀어 감숙을 노린다면, 그곳이야말로 이번 전쟁의 최대 격전지다.”

그리고 이는 결코 과장된 생각이 아니다.

암천은 늘 허를 찌르는 행보를 보여 왔다.

비록 나를 비롯한 수많은 이들이 피똥을 지려 가며 노력한 덕분에 놈들이 벌인 흉계는 번번이 가로막혔지만, 그렇다고 무림맹이 이 전쟁에서 승기(勝氣)를 잡은 것은 아니었다.

아니, 오히려 암천에게 농락당했다는 것이 정확한 표현일 것이다.

‘소 잃고 외양간 고친 격이지.’

처음부터 외양간을 노리는 방화범을 잡았다면 아군의 승리다.

하지만 외양간은 매번 불에 탔고, 수많은 이들이 가축처럼 도살당해야 했다.

가는 곳마다 활활 타오르는 외양간에 물을 뿌렸던 나로서는, 이 모든 것이 전부 지긋지긋하면서도 신물이 날 지경이었다.

그러니…….

‘이번만큼은 막아야 한다. 반드시.’

다시 한번 불이 붙기 전에, 또 다른 큰 희생이 있기 전에.

신중에 또 신중을 기해야 한다.

돌다리도 두드려 보고 건너듯이, 감숙의 상황을 두 눈으로 똑똑히 확인하고 청해로 건너가야 한다.

그것이 내가 굳이 조금 더 빠르고 편한 수로를 버리고 육로를 택한 가장 큰 이유였다.

‘그리고 이 선택이, 저 녀석에게도 훨씬 위안이 될 테고.’

나는 힐끗 고개를 돌려 한 사람을 바라보았다.

태원진가를 나선 지 한나절이 지난 지금까지도 말 한마디 없이 묵묵하게 말고삐만 쥐고 있는 그, 사마표를.

물론 평소에도 과묵한 편인 녀석이지만, 근래 들어서는 그 정도가 조금씩 심해지는 것을 느끼고 있었다.

‘그럴 수밖에 없겠지. 당장 암천의 대군이 신강의 사막을 가로지른다면, 가문이 위태로워질 상황이니까.’

구파일방의 일익인 공동파와 함께 감숙성을 양분하는 또 하나의 패자, 흑룡마문(黑龍魔門).

바로 그 흑룡마문의 소문주인 사마표로서는 당연히 심경이 복잡해질 수밖에 없을 것이다.

나와 적천강이 한 말을 듣고 난 직후인 만큼 더더욱.

그러나 구태여 위로하지는 않았다.

지금 같은 상황에서는 위로도 사치다. 눈을 마주치자 말없이 살짝 고개를 끄덕여 보이는 사마표에게서 시선을 뗀 나는, 말고삐를 강하게 움켜쥐었다.

“이럇!”

두두두두!

지구력 하나만큼은 한혈마조차 따라갈 수 없다는 초원마(草原馬)는 지친 기색 하나 없이 내달렸다.

밤낮이 또 한 번 교차하고, 달과 해가 서로를 스쳐 지날 때까지.

그렇게 사흘이라는 시간이 바람처럼 흘렀을 때, 산서성을 벗어난 우리는 섬서와 감숙의 경계선에 다다를 수 있었다.



* * *



“그만. 현 위치에서 반 시진 휴식한다.”

환갑쯤 되었을까.

불쑥 입을 열어 모두의 발걸음을 멈추게 한 것은, 호리호리한 키에 가늘게 찢어진 눈매가 인상적인 노인이었다.

물론 노인의 뒤를 따라가던 수백여 명의 사람들은 알고 있었다.

당장 눈으로 보이는 것이 전부가 아니듯, 노인이 살아온 세월은 그보다도 훨씬 길며 이를 가능케 하는 것은 고강한 무위라는 것을.

까마득한 연배와 드높은 무위.

두 가지를 동시에 지닌 노인의 명령을 거부할 수 있는 것은, 이 자리에 단 한 명뿐이었다.

“난데없이 휴식이라니. 대관절 그게 무슨 말씀이십니까. 대사형.”

깨끗한 도포(道袍)를 걸친 반백의 도사가 당황한 얼굴로 다가왔음에도, 노인은 아무렇지 않게 대답했다.

“이 늙은이의 몸이 불편하여 더는 움직이지 못하겠네. 하여 반 시진 정도만 쉬어 가려 하는데, 무슨 문제라도 있나?”

“대사형!”

“목소리 낮추게, 장문 사제. 대사형께 이 무슨 무례인가.”

불쑥 끼어든 누군가의 음성.

질책이 담긴 목소리를 따라 고개를 돌린 반백의 도사가 한숨을 내쉬었다.

“이 사형까지 왜 그러시는 겁니까. 본산(本山)을 떠난 지 벌써 이틀이 지났는데, 아직도 감숙에 닿지 못했다는 걸 아시는 분들께서…….”

“그만.”

이 사형이라 불린 그, 풍성한 백염(白髥)으로 신선처럼 보이는 노도사가 손을 들어 말을 끊었다.

“어쩌겠나. 육신이 쇠한 탓에 이동에 한계가 있는 것을. 나와 대사형은 오히려 장문 사제에게 섭섭하군.”

“그게 무슨.”

“한동안 요양에만 몰두하던 두 사형이 이제야 겨우 거동을 할 수 있게 되었거늘, 어찌 그리 재촉하는가?”

반백의 도사는 뭐라 말하려는 듯이 입술을 달싹였지만, 별다른 말을 잇지 못하고 고개를 돌렸다.

아니, 설령 마음속의 말을 소리 내어 뱉었다 하더라도 결과는 크게 달라지지 않았을 것이다.

바로 다음 순간, 인적 드문 숲속에서 거센 말발굽 소리가 울려 퍼졌으니까.

두두두두!

뿌옇게 피어오르는 흙먼지를 뚫고 튀어나온 여러 필의 초원마가, 숲길 한가운데에 멈춰 있던 일단의 무리를 발견하고 속도를 줄이기 시작했다.

정확히는, 그들 사이에 우뚝 솟아올라 있던 깃발을 보고 멈췄다는 것이 옳았다.

대(大) 종남파(終南派).

숨을 헐떡이는 초원마의 말안장 위, 일필휘지로 수놓아진 글자를 읽은 선두의 청년이 작게 중얼거렸다.

“이거 오타 난 것 같은데…….”
```

## Final English reading copy

```markdown
# Chapter 998

As Jin Wikyung had already said, the most likely place for a major battle with Dark Heaven was Qinghai, where the Kunlun Sect was located.

It was a strategic foothold the enemy would have to take before advancing into the Central Plains—and one the orthodox Murim would have to defend with their lives.

And that was exactly why I could answer Hyuk Mujin’s question about how we would get to Qinghai without a moment’s hesitation.

“We run. Fucking hard.”

“I know that much, of course. But what I wanted to ask was…”

“You mean, running fucking hard is fine, but how long do we keep it up?”

“Ah, Captain. You really do know exactly what I’m thinking.”

“Keep going.”

“…Excuse me?”

“Keep going. All the way.”

“Wait, all the way to Qinghai?”

I asked as I kept the reins tight, urging my horse onward at full speed.

“Otherwise?”

“I think taking the water route would be better. We can travel overland as you said, then follow a tributary of the Yangtze from Shaanxi straight to Qinghai. It’d save us about half a day and take a lot less effort.”

At first glance, it was a pretty reasonable suggestion.

Even if it only saved half a day, we’d still get there sooner and conserve our Stamina before an important battle.

And the Yangtze River Channel League, the nationwide gangsters of the river with a long history and tradition, was part of the Murim Alliance. If we were lucky, we might even be able to hijack a swift ship… I mean, borrow one.

Or at the very least, a Great Nation military vessel.

But I immediately shook my head.

“The land route is better.”

“Why? Do you get seasick?”

“……”

“Even if you do, just bear with it. I’ll pat your back for you.”

Was this bastard looking down on a Supreme Peak master?

And I wasn’t some newly minted Supreme Peak master, either.

I’d reached the pinnacle of martial arts and even completed Bone Transformation. I was a superhuman among superhumans.

I could ride a Disco Pang Pang at Wolmido and still feel perfectly steady. And this guy was talking about seasickness?

I stared at Hyuk Mujin in disbelief, momentarily at a loss for words. Just then, a fierce gust of wind swept toward the back of his head.

Whoosh—smack!

“Gah!”

It was the sort of impact that felt satisfying just to hear. Jeok Cheongang, who had expertly smacked the back of Hyuk Mujin’s head, clicked his tongue.

He was traveling by stepping on the branches that stretched endlessly along either side of the road, because he found the saddle uncomfortable.

“You stupid fool. Why do you have to talk so much? If your superior tells you to do something, you do it.”

If anyone but me had smacked Hyuk Mujin on the back of the head, he’d have been glaring daggers. But when that someone was the Fire King, Jeok Cheongang, it was a different story.

Hyuk Mujin gingerly rubbed the back of his aching head, glancing around before speaking up.

“I was just making a better suggestion. Why are you doing this to me?”

“A better suggestion? You really think so?”

“Wasn’t it…?”

“I’ll admit it was a fairly plausible suggestion. But you overlooked one very important fact.”

Before Hyuk Mujin could answer, Jeok Cheongang’s low voice carried through the wind.

“Dark Heaven. Whether those thoroughly devious bastards are truly targeting Qinghai.”

“……!”

“We know nothing for certain yet. No one knows where Dark Heaven’s army, said to be marching beyond the desert, is headed. Qinghai isn’t the only route into the Central Plains.”

I nodded in agreement with Jeok Cheongang’s assessment of the situation.

That was right.

There wasn’t just one route. There were three, maybe more.

Qinghai, Gansu, and even Tibet, beyond the borderlands and counted among the Outer Lands.

Qinghai was likely to be the main target because of its strategic importance, but Gansu and Tibet were also entirely possible targets for an invasion.

And besides…

*They have a Warp Gate—or rather, a Moving Formation.*

The Moving Formation gave the enemy more options, while serving as a painfully sharp dagger aimed at our backs.

They could send as many as a thousand people—at least, that was the number we’d confirmed so far—to somewhere in the Central Plains through a Moving Formation. How could we take that lightly?

Of course, it wasn’t impossible to deal with them.

The Zhuge Clan, known as the finest in the world at mechanisms and formations, possessed a formation called the Demon-Sealing Formation. Just as its name suggested, it could suppress and seal magical power.

When a “rift” had opened at Dongting Lake, the Zhuge Clan had managed to contain it with the Demon-Sealing Formation, led by their Family Head, Zhuge Feng. That was why the incident had been brought to an end without even greater losses.

*If they can stop a rift, they should be able to neutralize a Moving Formation, too. I’ve seen the Demon-Sealing Formation myself, so I know it works. The problem is time and manpower.*

The world was vast beyond measure.

And no one knew how many Moving Formations Dark Heaven had built somewhere in that boundless sea of sand.

Even though it had been well over half a year since we found a way to deal with the Moving Formations, several sects near Shanxi Province had still hesitated to send reinforcements, even temporarily. That alone proved the point.

Even if just one Moving Formation remained, it would be like a sharp shard of glass, digging deep into the sole of someone walking carelessly across the sand.

*That’s why we have to travel overland.*

Qinghai had been a battlefield whenever foreign invasions came over the centuries. The Murim Alliance would have prepared the best defenses it could.

Those defenses wouldn’t be so flimsy that a difference of half a day—or even a full day—could bring them down.

*Tibet should be reasonably safe, too. Even if the Potala Palace in Tibet has joined hands with Dark Heaven, the forces stationed in Sichuan should be able to hold them off.*

The Sichuan Tang Clan, which the Western Heaven Demon Lord had directly targeted, had suffered tremendous losses. But Qingcheng and Emei were still intact.

And on top of that, some unexpected guests were currently staying in Sichuan.

*The Nanman Beast Palace.*

We’d left in a hurry, with a long road still ahead of us, but I’d heard news about them from time to time.

The tropical warriors had finally left the jungle in an unprecedented mass migration. They’d readily accepted the Murim Alliance’s request and were now defending Sichuan.

“The western front will have prepared to some extent. There’s just one place that hasn’t.”

I wasn’t speaking to Hyuk Mujin alone.

After finishing my train of thought, I suddenly spoke. I looked around at the Fire Dragon Pavilion members riding alongside me, then added quietly,

“Gansu.”

“……!”

“……!”

“If Dark Heaven defies everyone’s expectations and targets Gansu, that will be the greatest battlefield of this war.”

That wasn’t an exaggeration.

Dark Heaven had always found ways to catch us off guard.

Thanks to the efforts of countless people, myself included, who’d practically shit themselves trying to stop them, their plots had been thwarted time and again. But that didn’t mean the Murim Alliance had gained the upper hand in this war.

No—in fact, it would be more accurate to say Dark Heaven had been toying with us.

*Shutting the stable door after the horse has bolted.*

If we caught the arsonist targeting the stable before the fire started, that would be our victory.

But the stable had burned every time, and countless people had been slaughtered like livestock.

As the person who’d repeatedly run around dousing the stables wherever I went, I was sick and tired of all of it.

So…

*This time, we have to stop them. No matter what.*

Before another fire started. Before there were more terrible losses.

We had to be more cautious than ever.

Like tapping a stone bridge before crossing it, I had to see the situation in Gansu with my own eyes before moving on to Qinghai.

That was the biggest reason I’d chosen the land route over the slightly faster, more comfortable water route.

*And this choice should be a lot more reassuring for him, too.*

I glanced to the side at one man.

It had been half a day since we left the Jin Family of Taiyuan, and he still hadn’t said a word. He simply held the reins in silence: Sama Pyo.

He’d always been taciturn, but lately I’d felt it getting worse.

*He can’t help it. If Dark Heaven’s army is crossing the deserts of Xinjiang right now, his family could be in danger.*

Along with the Kongtong Sect, the Black Dragon Demon Gate was one of the two powers that divided Gansu Province between them. And Sama Pyo was the Black Dragon Demon Gate’s Young Sect Leader. Of course he’d have a lot on his mind.

Especially after hearing what Jeok Cheongang and I had just said.

But I didn’t bother trying to console him.

In a situation like this, comfort was a luxury. When our eyes met, Sama Pyo gave me a slight, silent nod. I looked away and tightened my grip on the reins.

“Hyah!”

Thud-thud-thud-thud!

The grassland horses, said to have more stamina than even sweat-blood horses, galloped on without a trace of fatigue.

Night and day passed each other once more, and the moon and sun crossed paths overhead.

Then, as three days swept by like the wind, we left Shanxi Province and reached the border between Shaanxi and Gansu.

* * *

“Stop. We’ll rest for half a shichen here.”

The one who suddenly spoke and brought everyone to a halt was an old man, perhaps around sixty, with a slender build and sharply slanted eyes.

Of course, the several hundred people following behind him knew better than to judge by appearances.

Just as what they saw with their eyes wasn’t all there was, the old man had lived far longer than he looked. Only his formidable martial prowess could account for it.

Great age and formidable skill.

Of all those present, there was only one person who could refuse the orders of an old man with both.

“Why are we stopping for a rest out of nowhere? What on earth do you mean, Eldest Senior Brother?”

A half-white-haired Daoist in a clean robe hurried over, looking confused. The old man answered without a care.

“My old body is uncomfortable, and I can’t go any farther. So I thought we’d rest for half a shichen. Is there a problem?”

“Senior Brother!”

“Lower your voice, Junior Brother Sect Leader. How can you be so rude to Eldest Senior Brother?”

Someone’s voice cut in abruptly.

The half-white-haired Daoist turned toward the scolding voice and sighed.

“Why are you doing this too, Senior Brother Lee? It’s been two days since we left the main sect, and we still haven’t reached Gansu. You know that…”

“Enough.”

The man he’d called Senior Brother Lee, an old Daoist with a luxuriant white beard who looked like an immortal, lifted a hand and cut him off.

“What can we do? Our bodies have grown weak, and there’s a limit to how far we can travel. Eldest Senior Brother and I are disappointed in you, Junior Brother Sect Leader.”

“What do you mean?”

“After devoting ourselves to recuperation for so long, your two Senior Brothers have only just become able to get around again. Why are you rushing us like this?”

The half-white-haired Daoist moved his lips as if he had something to say, but he couldn’t get another word out. He turned away.

And even if he’d spoken the words on his mind, the outcome would probably have been much the same.

Because at that very moment, the sound of pounding hooves rang through the deserted forest.

Thud-thud-thud-thud!

Several grassland horses burst through the rising cloud of dust. They spotted the group halted in the middle of the forest path and began to slow.

Or rather, it was more accurate to say they’d stopped after seeing the flag rising above the group.

**The Great Zhongnan Sect.**

From atop his panting grassland horse, the young man riding in front read the characters embroidered in a single flowing stroke and muttered under his breath,

“I think there’s a typo…”
```
