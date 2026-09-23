<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0893.txt",
      "sha256": "4e112510e3d6cbdde6baf9e1e3ea6aa2f54b869b8f8f6f8b082cf3a236548b14",
      "bytes": 12995
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b773689e253032bb9c553f0f3fc99e0ffbf1f0fc39534b7b3134681f6ce9ca4b",
      "bytes": 1305
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "42391788f53c6c5ac3e1dcd23d6389823b2c8658da1a82bb5b05e797a4f8f5b6",
      "bytes": 230370
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8c20863d0ee8ec2cb57f3c23d27ebab8bbb1049036ec71491e5316a8fef2622f",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "b1068ecb4e99d541ce45555c92233ac1021db30f04a5517639dcf09c04c05926",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c966bc1b410fcefb825dadf0992766031df3f4d87740e96bfdeec4a84d0a7da2",
      "bytes": 1511
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "b63cae293b5846af0324ef34fba32eeac6c5bddde9a50af2350e219f5c5d8c32",
      "bytes": 973
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "7513f83caea363caac2323057c1382acffa45af7585494757356da04c4f2db19",
      "bytes": 815
    },
    {
      "path": "characters/Namho.md",
      "sha256": "730c2fba40977be95f7b62e668ef3bb264f4e0908c86fba1f3f7900370887c7c",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "94aa83b79e0a0a12cdcc1c06ffd0450aa5dc27d1d6d1b9e6ad329feb2ad000b9",
      "bytes": 936
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "83ce4126c15d02a7e80e27aae44dbb284ac184ca79974c93d39914f5e0cc48b8",
      "bytes": 641
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "9a3348b091a71357b456218896be3a2ecc0907a656a041ec9b24792423b90c87",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "3c8b1ac9664350f5c7c4218196bc6582b61f79161702590cb5c76bab23c2a3e7",
      "bytes": 1074
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "07d2c96fe62f432be5a034d5574601b58c9d99f2f513dfecfeddecaef8b5684a",
      "bytes": 260688
    }
  ],
  "estimated_tokens": 12147
}
-->

# Durable State Update — Chapter 893

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
1 and safe_through 893. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 893. Profile updates may replace only one
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
  "chapter": 893,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 893,
    "continuity_sources": [893],
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
    "The grand banquet is approaching, and the group expects a decisive conflict may occur there.",
    "The enemy sees a decisive battle as the quickest route to controlling the Great Nation, despite the risks of facing Jin and Jeok Cheongang.",
    "The enemy’s confidence and apparent willingness to disregard Jeok Cheongang remain unexplained.",
    "Jin intends to consult Ma Sanbao, whom he suspects may have personally recruited assassins.",
    "Namho says the Hidden Shadow Pavilion once sought an alliance with the imperial household during the Great Faction War; after the late Emperor refused, court surveillance of martial artists increased and Pavilion agents were barred from the imperial capital.",
    "The restoration army has spent more than a decade preparing for the coup."
  ],
  "continuity_sources": [
    892
  ],
  "open_questions": [
    "What accounts for the enemy’s confidence that the decisive battle’s outcome is assured?",
    "What does Ma Sanbao know about the current crisis, and did he recruit assassins?",
    "Who are the assassins Jin has in mind?",
    "What will happen at the approaching grand banquet?",
    "Who is So Gyo, and why did she release Jin?"
  ],
  "safe_through": 892,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 사마공    | **Sima Gong**      |
| 살성     | **Slaughter Saint**           | —              |
| 일신     | **One God**         |
| 십왕     | **Ten Kings**       |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장로     | **Elder**                                    |
| 몬스터     | **monster**           |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 살천문 | **Salcheonmun** | Vanished assassin sect once associated with Mungyeong. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 892
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 891
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 892
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 891
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 892
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading the Depot in place of its bedridden leader, Cang Gong.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 892
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 892
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 543
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly, cunning, and inscrutable, with a ruthless reputation for valuing talent above family ties.
- **Voice:** Not established.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters, and he is the father of the current Black Dragon Demon Gate Young Sect Leader.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 891
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 891
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

## Korean source

```text
＃893화



애초에 나를 비롯한 모두의 시선이 사마표와 신의를 향한 이유는 간단했다.

살수와 아주 밀접할 수밖에 없는, 그쪽 업계 관련자니까.

“왜, 왜 그런 눈으로 날 보는 거요. 나는 착한 사마외도요.”

“저는 이미 오래전에 그 바닥에서 손 뗐습니다. 아, 아니 제가 아니라 스승님께서…….”

물론 당사자들은 억울해했지만, 그래도 저 두 사람이 살수라는 부류와 상당한 연관성이 있다는 건 부정할 수 없는 사실이다.

더군다나 살성(殺星)이라는 무시무시한 과거를 가진 스승을 둔 누군가라면 특히나.

“자자. 그냥 여쭤보는 거니까 진정하시고, 뭐 아시는 거 없습니까? 예를 들자면…… 황궁에 기어들어 올 만큼 간 크고 실력 좋은 살수 집단이라든지.”

흔들리는 동공으로 사람들을 바라보던 신의가 어쩔 수 없다는 듯 입을 열었다.

“그런 것까지 제가 어찌 알겠습니까. 제 스승님께서 한때 그쪽에 몸담으셨던 건 사실이지만…….”

“몸담은 수준이 아니라, 헤엄을 쳤지 아주.”

적천강의 중얼거림에 나도 모르게 고개를 끄덕였다.

“어후, 그분이야 뭐 날아다니셨죠.”

“그렇지. 얼마나 날아다녔는지 결국 별이 됐어.”

“누가 들으면 돌아가신 줄 알겠습니다. 그 바닥에서는 아직 살아 있는 전설이신데.”

“아무렴. 역사를 새로 썼지, 피로.”

“그래도 아무 이유 없이 함부로 살생하진 않으셨잖아요.”

“그거야 나중 일이었지. 그 인간도 소싯적에는 주위 놈들이랑 엇비슷했을 게다. 뭐 어릴 때니 까라면 까야지.”

나와 적천강의 티키타카를 듣고 있던 신의의 눈이 짜게 식었다.

“이렇게 나오실 거면 그냥 아무 말도 안 하겠습니다.”

“어허, 왜 이러세요. 말이 그렇다는 거지 제가 얼마나 존경하는 분인데.”

“거 참, 나이도 먹을 만큼 먹은 놈이 삐치기는. 무슨 말이라도 좀 해 봐라. 네놈 스승에게서 몇 마디라도 주워들은 것이 있을 것 아니냐.”

살살 달래자 잠시 머뭇거리던 신의가 이내 한숨을 푹 내쉬었다.

“스승님은 늘 당신의 과거에 대해 말씀하시길 꺼리셨습니다.”

충분히 이해한다. 내가 아는 살성은 피로 점철된 자신의 과거를 후회하고 있었으니까.

정마대전이 종결된 직후, 모든 것을 내려놓고 의원의 길을 걷기 시작한 것도 바로 그 때문이었다.

더는 누군가를 죽이고 싶지 않아서.

아무리 씻고 또 씻어도 사라지지 않는 그 피비린내를, 살인이 아닌 활인(活人)으로 지워 내고 싶어서.

그렇게 고금제일의 살수는 신의(神醫)가 되었다.

“그러나…….”

문득 말꼬리를 흐린 신의가, 잠시 참았던 숨을 토해 냈다.

“그런 스승님께서도 간혹, 아니 매우 드물게 과거의 이야기를 하실 때가 있었습니다. 대부분이 후회 가득한 넋두리였지만 다른 살수들에 대한 것들도 있었지요.”

“그럼 혹시?”

“스승님과 동시대에 활약했던 살수들이라면, 저도 한 번쯤은 들어 봤을 겁니다. 물론 살수라는 부류의 특성상 지금까지 현역으로 있을 가능성은 거의 없겠…….”

“역시 어르신께 제일 먼저 물어보길 잘했네요.”

“네? 그게 무슨.”

“제가 오늘 본 그 살수가, 지금 말씀하신 조건에 딱 부합되는 것 같거든요.”

“……!”

나는 놀라움에 눈을 부릅뜬 신의에게, 아니 뒷말을 기다리는 모두에게 내가 보고 느낀 것을 처음부터 끝까지 말해 주었다.

혹시 모를 인피면구나 역용술을 감안해도 족히 칠순은 넘어 보였던 그의 나이와 일신의 무위. 그리고 스스로 마삼보와의 연관성을 밝혔던 것까지.

그리고 모든 이야기가 끝나자, 주화란이 휘둥그레진 눈으로 입을 열었다.

“그 노인이, 초절정 고수였다고요?”

“예. 확실합니다.”

“하지만 살수가 어떻게…… 아, 죄송합니다. 그런 의미로 말한 건 아니에요.”

주화란의 사과에 신의가 손을 내저었다.

“아닙니다. 제가 비록 무림과는 거리가 먼 삶을 살아왔지만, 살수가 초절정의 경지에 올랐다는 것이 어떤 의미인지는 익히 알고 있으니까요.”

살수가 높은 경지에 다다르지 못한다는 것은 이미 널리 알려진, 동시에 이해하기 쉬운 무림의 상식이다.

정결한 몸과 마음으로 일로정진(一路精進) 해도 초절정의 영역에 발을 들여놓기란 하늘의 별 따기인데, 생존과 암살을 위해 온갖 기술을 익혀야 하는 살수들은 어떻겠나.

‘현대로 따지면 전공과목 하나만 죽어라 파도 힘든 상황에서, 교양과목 수십 개를 추가로 들어야 하는 꼴이지.’

그렇기에 순수한 무공 자체만 보자면 사마외도(邪魔外道)에 속한 부류 중에서도 가장 약체로 평가받는 것이 바로 살수다.

살성이 고금제일의 살수라 불리는 이유도 비슷한 맥락이고.

하지만 오늘 내가 마주친 그 노인은 틀림없는 초절정 고수였다.

약간의 신체적 결함이 있긴 했지만.

“절름발이라 하셨습니까?”

나는 신의의 물음에 고개를 끄덕였다.

“예. 혹시 몰라서 자세히 살펴봤는데, 아무리 봐도 꾸며 낸 것 같진 않더라고요. 게다가 짐 나르는 인부로 위장할 거라면, 굳이 그럴 이유도 없었을 테고.”

“진 소협께서 그렇다면 그렇겠지요. 이유도 타당하고. 그나저나 절름발이, 절름발이라.”

“생각나는 사람 없으십니까?”

고민하던 신의가 반신반의하는 얼굴로 대답했다.

“정확하진 않지만 스승님께 들은 이야기 중에 그와 비슷한 사람이 한 명 있긴 합니다. 한때 청해성(靑海省)을 주름 잡았던 살수인데 별호가 아마…….”

“독각귀살(獨脚鬼殺)?”

불쑥 끼어든 누군가의 목소리와 함께 돌아가는 고개.

나를 비롯한 모두의 시선이 갑작스럽게 자신을 향해 쏠리자, 잠시 움찔하던 사마표가 입을 열었다.

“익히 들어 본 바가 있소. 살수면서도 일신의 무공이 고강하여 종종 암습이 아닌 생사결로도 표적을 처치했었다고.”

“네가 그런 것까지 어떻게 알아?”

“어찌 알긴. 들어서 알지.”

“누구한테…… 아.”

쓸데없는 물음이었다.

사마표가 누군가. 내 밑에서 개처럼 구르고 있어서 그렇지, 이 녀석은 사파 제일의 후기지수이자 곤륜파와 함께 청해성의 패권을 틀어쥔 흑룡마문(黑龍魔門)의 소문주다.

‘게다가 아버지는 바로 그 흑야왕(黑夜王) 사마공이고.’

사마외도를 대표하는 초절정 고수 중 한 사람인 흑야왕 사마공은 별호와 달리 십왕(十王)의 반열에는 들지 못했지만, 정마대전에서 무림맹의 편에서 싸워 지금의 흑룡마문을 일구어 낸 거물.

그리고 그런 흑룡마문의 본진이 바로 청해성이니, 소문주인 사마표가 주워들은 풍월이 없다면 그게 더 이상하다.

그나저나 독각귀살이라.

“별호부터 끝내주네. 언뜻 추측해 봐도 썩 좋은 사람일 것 같진 않은데, 안 그래?”

내 말에 사마표가 고개를 끄덕였다.

“그야 살수니까.”

“뭘 자꾸 차별해. 어차피 너도 같은 사마외도 아니냐?”

“아무리 각주라지만 말이 심하군. 나는 그래도 양심 있고 착한 사마외도다.”

“뭔 시벌. 양심 있고 착한 사마외도가 어디 있어. 밝은 암천. 뭐 그런 거냐?”

“……진짜 너무하는군.”

“그래, 알겠어. 너 괜찮은 놈인 건 알겠으니까 그렇다 치고, 계속 씨부려 봐.”

지금까지 줄곧 입을 다물고 있다가, 갈굼과 동시에 미친놈처럼 실실 쪼개기 시작한 송일섬을 노려보던 사마표가 입을 열었다.

“정마대전 이전부터 청해성 일대에 흉명(凶名)이 자자했다더군. 일신의 무위 자체도 뛰어나지만, 살수로서의 기량은 그 이상이라 당시 초절정의 고수였던 곤륜파(崑崙波)의 장로도 죽였을 정도라고 했다.”

“그 정도야?”

“적어도 내가 들은 바로는.”

“그렇단 말이지. 그래, 좋아. 그래서?”

“그래서라니?”

“계속해 보라고.”

“이게 끝이다. 정마대전 이후로는 그냥…… 행적이 묘연해졌다고 들었는데.”

“…….”

한창 잘 싸다가 도중에 일이 생겨서 급하게 끊은 기분. 지금 내 기분이 딱 그렇다.

하지만 다행히도, 지금 내 주위에는 걸어 다니는 무림 대백과 사전이 있었다.

“네가 봤다던 그 늙은이가, 독각살귀가 확실한 게냐?”

불쑥 끼어든 남호가 허리를 두드리며 말을 이었다.

“은영각이 입수했던 정보에 의하면 독각살귀는 한쪽 다리가 없다. 물론 평소에는 정교하게 만들어진 의족(義足)을 차고 다녀서 어지간한 눈썰미로는 파악할 수 없었지만.”

“그 말씀은…….”

“다른 인물을 오인했을 가능성도 충분하다는 뜻이다. 설령 네가 봤다던 그자가 바로 그 독각살귀가 맞다 해도…… 지금으로서는 어쩔 수 없는 아군이고.”

남호가 마지막에 덧붙인 말이 유난히도 크게 울려 퍼졌다.

‘아군. 아군이라.’

고작 그 두 글자만으로도 느껴지는 불쾌함.

동시에 유독 그 늙은 살수의 존재가 목에 걸린 가시처럼 느껴졌던 이유를, 이제야 알 것 같았다.

‘거부감이 드는 거겠지. 그런 부류와 얽히는 것이.’

누군가 내게 스스로를 착한 사람이라 생각하느냐고 묻는다면, 나는 쉽사리 대답할 수 없을 것이다.

나 역시 숱한 살업(殺業)을 쌓았으니까.

‘몬스터가 아닌, 진짜 사람을 죽였지.’

그저 적이라고 생각되면 가차 없이 죽였다. 빠르게 강해지는 만큼 살인도 쉬워졌다. 단전을 폐(廢)하고 사지의 근맥을 잘라 불구로 만들 수도 있었으나 굳이 그럴 이유를 찾지 못했다.

아니, 찾지 않았다.

조금의 후환(後患)조차 남겨 두기 싫었으니까.

그런 것에 대해 고민할수록, 어느새 서서히 변해 버린 내 모습을 돌아볼수록 내면의 고통이 커진다는 것을 알아 버렸으니까.

진정으로 선한 이들은 무림에 없다.

각자의 목적과 가치관에 따라 누군가의 목숨을 거두고, 자신의 목숨을 내놓는 이들만이 있을 뿐.

그렇기에 나 역시 스스로를 선한 사람이라 대답할 수 없다.

다만, 조금이라도 선해지기 위해 노력 중일 뿐이다.

어제도, 오늘도, 내일도.

그리고 바로 그것이, 내가 그 늙은 살수에게서 느끼는 가장 큰 거부감이었다.

‘아무런 이유도, 변명조차 없는 살인.’

살수가 임무에 나서는 이유와 목적이 있다면 오직 하나, 돈이다.

그 늙은 살수는 살성처럼 선해지기 위한 노력을 하지 않았을 것이다. 그저 전표에 적힌 숫자를 따라 사람을 죽였고, 죽이고, 죽일 것이다.

어제도, 오늘도, 내일도.

그리고 그런 그가, 오늘은 우리의 든든한 아군이자 얼마 남지 않은 미래에 함께 등을 맞대고 싸울 전우가 되었다.

‘이게…… 맞는 건가?’

나는 문득 혼란스러워졌다.

마삼보가 말했던 대업(大業)이라는 두 글자가 무겁게 가슴을 짓눌렀다. 화려하지만 차가운 옷을 걸친 채 건청궁에 억류되어 있을 어린 왕의 모습도 함께.

그리고 조용히 씁쓸한 입맛을 다시고 있던 그때, 한 사람이 차분한 목소리로 입을 열었다.

“언젠가 스승님께 여쭈어본 적이 있습니다. 왜 당신이 나고 자라신 사문(師門)이었던 살천문(殺川門) 명맥을 끊어 놓으셨는지.”

신의. 그다.

스승과는 달리 새하얀 백발을 지닌 늙은 의원이 천천히 말을 이었다.

“스승님께서 답하셨습니다. 자신이 한 일에 대해 후회도, 반성도 없는 자들은 죽어 마땅했다고. 그리하여 당신의 손에 피를 묻히셨노라고.”

“……!”

“사람들에게는 저마다의 가치관이 있기 마련이지요. 제 스승님이나, 진 소협처럼 말입니다.”

더 이상 듣고 있을 수 없었다.

나는 자리에서 일어나 밖으로 향했다.

마삼보를 봐야겠다. 그리고 해결해야겠다. 이 의문을, 왜 그들을 끌어들였는지.
```

## Final English reading copy

```markdown
# Chapter 893

The reason everyone’s eyes had turned to Sama Pyo and the Divine Physician—including mine—was simple.

They were both connected to the assassin business.

“Wh-Why are you looking at me like that? I’m one of the good practitioners of demonic, heterodox arts.”

“I left that line of work a long time ago. I—No, I mean my Master…”

Of course, the two of them protested that it was unfair. Even so, there was no denying they had considerable ties to the world of assassins.

Especially someone whose Master had once been known as the terrifying Slaughter Saint.

“Now, now. I’m only asking, so calm down. Do you know anything? For example… an assassin group skilled and bold enough to sneak into the imperial palace.”

The Divine Physician looked around at us with darting eyes, then spoke as if he had no choice.

“How would I know something like that? It’s true my Master was involved with that world once, but…”

“Involved? He was swimming in it.”

At Jeok Cheongang’s mutter, I nodded without thinking.

“Whew. He was practically flying around back then.”

“Right. He flew around so much he eventually became a star.”

“You say that, and people will think he’s dead. He’s still a living legend in that world.”

“Of course. He rewrote history—with blood.”

“Still, he didn’t kill people for no reason.”

“That came later. When he was young, he was probably no different from the rest of those bastards. You know how it is when you’re young—you do what you’re told.”

The Divine Physician, who’d been listening to Jeok Cheongang and me go back and forth, gave us a look as cold as brine.

“If you’re going to put it that way, I won’t say another word.”

“Come on, don’t be like that. I’m only speaking loosely. You know how much I respect him.”

“Honestly, you’re old enough to know better. Don’t sulk. Say something. Surely you picked up a thing or two from your Master.”

After I tried to coax him, the Divine Physician hesitated for a moment, then let out a deep sigh.

“My Master was always reluctant to speak about his past.”

I could understand that. The Slaughter Saint I knew regretted the bloodshed that stained his past.

That was why, right after the Great Faction War ended, he’d put everything behind him and started walking the path of a physician.

Because he didn’t want to kill anyone anymore.

He wanted to wash away the stench of blood that no amount of scrubbing could remove—not by killing, but by saving lives.

And so the greatest assassin of all time became the Divine Physician.

“However…”

The Divine Physician trailed off, then let out the breath he’d been holding.

“Even my Master would sometimes speak of his past. Very rarely, though. Most of what he said was regretful rambling, but he did talk about other assassins, too.”

“Then, could it be…?”

“If they were assassins active in my Master’s time, I’ve probably heard of them at least once. Of course, given what assassins are like, it’s unlikely any of them are still active—”

“I’m glad we asked you first, sir.”

“Pardon? What do you mean?”

“The assassin I saw today seems to fit those conditions perfectly.”

“…”

The Divine Physician’s eyes widened with surprise. I told him—and everyone else waiting for me to continue—everything I’d seen and sensed, from beginning to end.

Even allowing for a human-skin mask or a disguise technique, the man had looked well over seventy. His martial prowess had been formidable, and he’d revealed his connection to Ma Sanbao himself.

When I finished, Ju Hwaran spoke, her eyes wide.

“That old man was a Supreme Peak master?”

“Yes. I’m sure of it.”

“But how could an assassin… Ah, I’m sorry. I didn’t mean it that way.”

At Ju Hwaran’s apology, the Divine Physician waved a hand.

“No, it’s all right. Though I’ve lived far removed from Murim, I know very well what it means for an assassin to reach the Supreme Peak realm.”

It was common knowledge in Murim, and easy enough to understand, that assassins rarely reached the higher realms.

Even if you devoted yourself to a single path with a pure body and mind, setting foot in the Supreme Peak realm was like trying to pluck a star from the sky. What chance did assassins have, when they had to learn all kinds of techniques just to survive and kill?

*It’s like trying to master your major while having to take dozens of extra electives.*

That was why, if you judged them purely by their martial arts, assassins were considered the weakest among the groups that practiced demonic, heterodox arts.

The Slaughter Saint’s title as the greatest assassin of all time came from the same principle.

But the old man I’d encountered today had been a Supreme Peak master. There was no doubt about it.

He did have a slight physical disability, though.

“You said he was lame?”

I nodded at the Divine Physician’s question.

“Yes. I took a close look just in case, but it didn’t seem faked. Besides, if he was going to disguise himself as a laborer carrying supplies, there’d be no reason to pretend.”

“If Young Hero Jin says so, then so it must be. Your reasoning makes sense. Still… lame, you say.”

“Does anyone come to mind?”

The Divine Physician thought for a moment, then answered with a doubtful look.

“I can’t say for certain, but I did hear of someone like that from my Master. He was an assassin who once dominated Qinghai Province. His epithet was, if I remember right…”

“The One-Legged Ghost Killer?”

Someone’s voice cut in, and we all turned.

When everyone’s gaze suddenly swung toward him, Sama Pyo flinched for a moment before speaking.

“I’ve heard of him. Though he was an assassin, his personal martial arts were so formidable that he sometimes killed his targets in life-and-death duels rather than through ambush.”

“How do you know that?”

“How do you think? I heard about it.”

“From who—Ah.”

That was a pointless question.

Who was Sama Pyo? He might be getting worked like a dog under me, but he was the foremost young prodigy of the unorthodox factions and the Young Sect Leader of the Black Dragon Demon Gate, which held sway over Qinghai alongside the Kunlun Sect.

*And his father was none other than the Black Night King, Sima Gong.*

The Black Night King Sima Gong was one of the Supreme Peak masters representing the demonic, heterodox arts. Despite his epithet, he wasn’t one of the Ten Kings. But he’d fought on the Murim Alliance’s side during the Great Faction War and built the Black Dragon Demon Gate into the formidable power it was today.

And since the Black Dragon Demon Gate’s stronghold was in Qinghai, it would’ve been stranger if its Young Sect Leader hadn’t heard a thing or two.

So, the One-Legged Ghost Killer.

“His epithet’s incredible. Just hearing it, he doesn’t sound like a good guy, does he?”

Sama Pyo nodded.

“He’s an assassin.”

“Why do you keep discriminating against them? Aren’t you demonic, heterodox arts yourself?”

“Even if you are the Pavilion Master, that’s harsh. I’m still one of the good, decent practitioners of demonic, heterodox arts.”

“What the fuck? Where have you ever seen a decent practitioner of demonic, heterodox arts? What are you, bright Dark Heaven or something?”

“...You really are something.”

“Fine, I get it. You’re a decent guy. Whatever. Keep talking.”

Sama Pyo glared at Song Ilseom, who’d kept quiet until now but had started grinning like a lunatic the moment I laid into Sama Pyo, then spoke.

“They say the One-Legged Ghost Killer had a fearsome reputation throughout Qinghai even before the Great Faction War. His martial prowess was impressive, but his skill as an assassin was even greater. He was said to have killed an Elder of the Kunlun Sect, who was a Supreme Peak master at the time.”

“He was that good?”

“At least, that’s what I’ve heard.”

“I see. All right. So?”

“So what?”

“Keep going.”

“That’s all. After the Great Faction War, I heard… his whereabouts became unknown.”

“…”

It felt like we’d been having a good fight, only for something to come up and cut it short. That was exactly how I felt.

Fortunately, though, I had a walking encyclopedia of Murim beside me.

“Are you certain the old man you saw was the One-Legged Killing Ghost?”

Namho spoke up, rubbing his lower back.

“According to the information the Hidden Shadow Pavilion obtained, the One-Legged Killing Ghost had only one leg. Of course, he wore a finely crafted prosthetic leg, so it was hard to tell unless you had a keen eye.”

“You mean…”

“It means there’s a good chance you mistook him for someone else. Even if the man you saw really was the One-Legged Killing Ghost… for now, he’s an ally whether we like it or not.”

Namho’s last words rang louder than the rest.

*An ally. An ally.*

Just those two words left a bad taste in my mouth.

At the same time, I finally understood why the old assassin’s presence had felt like a thorn in my throat.

*I must be repulsed by the thought of getting mixed up with people like him.*

If someone asked me whether I thought I was a good person, I wouldn’t be able to answer easily.

I’d taken countless lives myself.

*Not monsters. Real people.*

If I thought someone was an enemy, I killed them without hesitation. The faster I grew stronger, the easier killing became. I could have crippled them by destroying their dantian and severing the Sinews and Meridians in their limbs, but I couldn’t find a reason to bother.

No. I didn’t look for one.

I didn’t want to leave even the slightest chance of future trouble.

And I’d learned that the more I thought about it, the more I looked back at how I’d slowly changed, the greater the pain inside me became.

There were no truly good people in Murim.

Only people who took someone else’s life and risked their own, according to their own goals and values.

That was why I couldn’t call myself a good person, either.

I was only trying to become a little better.

Yesterday, today, and tomorrow.

And that, more than anything, was why I felt repulsed by the old assassin.

*Killing without a reason. Without even an excuse.*

An assassin had only one reason to take a job, one purpose: money.

The old assassin wouldn’t have tried to become a better person like the Slaughter Saint. He would have killed, would kill, and would keep killing people for the numbers written on a bank draft.

Yesterday, today, and tomorrow.

And now, today, he’d become our dependable ally—a comrade who would fight back-to-back with us in the not-too-distant future.

*Is this… right?*

I found myself confused.

The two words Ma Sanbao had used—*the great undertaking*—weighed heavily on my heart. So did the image of the young king held captive in Qianqing Palace, dressed in splendid but cold clothes.

Just as I quietly smacked my lips at the bitter taste in my mouth, someone spoke in a calm voice.

“I once asked my Master why he’d cut off the lineage of Salcheonmun, the sect where he was born and raised.”

It was the Divine Physician.

The old doctor, whose hair was white as snow unlike his Master’s, continued slowly.

“My Master replied that people who felt neither regret nor remorse for what they’d done deserved to die. And so he stained his hands with blood.”

“...!”

“Everyone has their own values, after all. My Master had his, and so does Young Hero Jin.”

I couldn’t listen any longer.

I stood and headed outside.

I needed to see Ma Sanbao. And I needed to get to the bottom of it—to understand why he’d brought them in.
```
