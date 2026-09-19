<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0490.txt",
      "sha256": "0cbecdfcc22ff4a2658e55e1f0f16867daaf6e378a09c9197b4af8c8a308916c",
      "bytes": 13163
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "47e17146a74271359340bdead39cbdca210652b1a323b7fee762c7c22ea06ff9",
      "bytes": 3773
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "793bb2b9346f14f9dde15ae3b1c79adc69481262021bff84b2e1319aaff00c78",
      "bytes": 156017
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6404ece7dbef1cd1a360f6813d1e76f2ef0d6a30d7ced3f8ac94e4b471727696",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "c9b7de79e60c9e7f2091927e21384d1ca9c3fc522d7a05f9f5f50979dac5db37",
      "bytes": 686
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2c741a686cd7c5841f190467f948950059b3e015aaa16e1fe7bcc06704de44d9",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e18ae09f3c6cecbe399a386e40957ae0c6cff7b5123be960253fe68181dec775",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0669874cd75b7c0c117a1a10afbebc3fd85ab5e47c3e087a97dd19676e23e860",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "46316a92304ec81bf37300968e808b4005c515389aa285daabdd8abcb9a01f67",
      "bytes": 975
    },
    {
      "path": "characters/Venerable Myoryeong.md",
      "sha256": "4596993e1fe6eea14b07b6324c729478b9bde3421e6b6f78fcbd0fd13973adde",
      "bytes": 553
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0d6cef49b0e30a240b8b7d8a8f091792176d3591c1c9e5c7e0fc265ebea7d898",
      "bytes": 152065
    }
  ],
  "estimated_tokens": 11856
}
-->

# Durable State Update — Chapter 490

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 490. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 490. Profile updates may replace only one
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
  "chapter": 490,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 490,
    "continuity_sources": [490],
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
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon has absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Dongting Lake is calm again after the Water God Dragon's mutated rampage nearly overturned it with thunder and waves.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Jeok trusts Taekyung more deeply than anyone else, despite interpreting Taekyung's attempted explanation of his origin as a drawn-out declaration that he wanted to die.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong has agreed to teach Taekyung his secret martial arts at Jeok's request, but will not form a formal Master-Disciple relationship; Taekyung accepted the Fake Murim Martial Artist Quest."
  ],
  "continuity_sources": [
    489,
    488
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What secret martial arts will Mungyeong teach Taekyung, and what training will make him a true Murim martial artist?"
  ],
  "safe_through": 489,
  "temporary_decisions": [
    "Render 독문 무공 as secret martial arts, 사승 as Master-Disciple relationship, 살귀 as Killing Ghost, and 가짜 무림인 as Fake Murim Martial Artist; preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, and 기막 as qi curtain."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 사숙     | **Martial Uncle**                            |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 묘령 | **Myoryeong** | Dharma name of the middle-aged Emei nun. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 은자 | **silver nyang** | Silver currency unit. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 혈어 | **Blood Fish** | Local name for the aggressive mutated fish in the Gate's waterways. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 489
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 484
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 489
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 488
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 488
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 489
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, Mungyeong has agreed to teach Taekyung secret martial arts without entering a formal Master-Disciple relationship, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Venerable Myoryeong.md

# Venerable Myoryeong (묘령)

- **Safe through:** Chapter 370
- **Aliases:** Myoryeong
- **Role:** Venerable Myoryeong is a middle-aged Emei Sect nun who survived an attack that killed the Emei Sect Leader and three Elders and bears the Black Hand Seal.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** She came from the Emei Sect to assist Taekyung's search and, after surviving the attack, identified the killer as a one-armed middle-aged man.

## Korean source

```text
＃490화



“그래, 이야기는 잘 끝냈소?”

무당파의 도사들은 앞서 말한 대로 정확히 한 식경 만에 돌아왔다.

아직 묻고 싶었던 게 많았던 나는 자리를 옮겨 계속 이야기를 나누고 싶었지만, 문경의 생각은 달랐다.

“할 말은 끝났다. 이만 돌아가라.”

“……예? 끝이요? 무슨 수련인지도 안 알려 줘 놓고 이대로?”

“내일이면 자연스럽게 알게 될 것이다.”

“어차피 이미 해시(亥時)인데요. 곧 있으면 자정인데, 그냥 속 시원하게 알려 주면 안 됩니까?”

“밤이 깊었군. 잊지 마라, 내일부터 시작이다.”

“아니, 저기요.”

“저기요?”

스윽.

소매 끝에서 슬쩍 솟구친 소검(小劍)과 문경을 번갈아 바라본 나는 굳은 얼굴로 어둠 너머를 가리켰다.

“저어기요. 저쪽으로 가시면 된다고요.”

“…….”

“저기로 쭉 가시다가 우회전하시면 됩니다.”

“말하려던 게 방향이 아니었던 것 같은데.”

“모르실 것 같아서 혹시나 하는 마음에. 헤헤.”

“알고 있으니 입 다물고 꺼져라.”

“옙. 그럼 편안한 밤 되십시오.”

잠시 후, 문경의 뒷모습이 시야에서 완전히 사라진 걸 확인한 나는 작게 중얼거렸다.

“시부럴…….”

산 넘어 산.

적천강의 방식에 겨우 익숙해졌나 싶었는데, 이제 살성 눈치까지 보게 생겼다.

앞으로 펼쳐질 고생길을 생각하면 벌써 눈앞이 깜깜했다.

‘아니, 차라리 노야가 훨씬 낫지.’

수련의 강도를 떠나, 적천강은 최소한 어떤 수련을 할 건지 알려 주기는 했다.

불같은 성미를 떠나 어느 정도의 커리큘럼은 갖춰져 있었다는 이야기다.

‘그런데 무슨 수련이길래 말도 안 해 줘.’

내가 이렇게까지 궁금해하는 이유는 간단했다. 엉겁결에 수락해 버린 퀘스트에도 어떤 정보도 나와 있지 않기 때문이었다.

‘퀘스트 창 오픈.’

띠링.



퀘스트



[가짜 무림인]



곧 천하에 드리워질 전운을 직감한 문경은 심사숙고 끝에 당신을 직접 가르치기로 결심했습니다.

그러나 모든 일에는 준비 과정이 필요한 법.

문경은 자신의 독문 무공을 전수하기에 앞서, 여러 가지 방법으로 당신을 시험할 것입니다.

그리고 이 첫 번째 시험이 언제 끝날지는, 당신에게 달렸습니다.



등급 : 無

제한 : 진태경

임무 : [문경] 에게 인정받기 (미완료)

보상 : ???

실패 : ???





두 번, 세 번을 다시 봐도 퀘스트 창은 그대로였다.

구화산에서 수련할 당시, 임무가 정확히 명시되어 있던 수련 퀘스트에 비하면 뜬구름 잡는 소리나 다름없다.

‘문경에게 인정받기라.’

이럴 바에야 철구를 주렁주렁 매달고 뛰어다니는 게 낫다. 최소한 정해진 목적이 있고 현재까지의 수치를 확인할 수 있으니까.

하지만 이건, 죄목으로 따지자면 괘씸죄와 비슷하다.

상대의 마음에 들 때까지 굴러야 한다는 소리 아닌가.

‘생각보다 오래 걸릴 느낌인데.’

문경의 수련 방식이 어떨지는 몰라도, 그에게 인정을 받기 위한 과정이 그리 쉽지 않을 거라는 사실은 확실하다.

더 객관적인 입장에서 냉정하게 말해 보자면 쉬운 게 이상한 거고.

‘빡셀 것 같긴 한데, 감수해야지.’

상대는 그저 그런 무림인이 아니라, 천하에서도 손꼽히는 초절정 고수인 살성이다. 그런 엄청난 고수에게 독문 무공을 사사하는 것 자체가 기연(奇緣)이라 할 수 있었다.

그리고 따지고 보면 나는 그런 기연을 이미 두 번이나 얻은 셈이다.

첫 번째는 두말할 것도 없이 시스템이고, 두 번째는…….

‘노야.’

역시 적천강을 빼놓을 수 없다.

아마 그와 만나지 않았더라면, 오직 대대로 한 사람에게만 전해지는 열화문의 무공을 익히지 않았더라면 시스템이 있었다 한들 지금 같은 힘과 위치에 오르지 못했을 테니까.

그렇게 꼬리에 꼬리를 물고 이어진 생각 끝에, 문득 떠오른 적천강의 얼굴이 눈앞을 스쳤다.

‘그래도, 뵈러 가야겠지.’

물론 나와 적천강은 정식으로 맺어진 사제지간이 아니다.

그러나 우리가 서로를 스승과 제자로 부르지 않는다고 해서, 단순히 필요에 의한 관계가 되는 것은 아니다.

말하지 않아도 아는 사이. 나와 적천강은 마음속에서 스승과 제자라는 단어를 만지작거리는 관계였다.

“…….”

아님 말고. 갑자기 자신 없어지네.

적천강의 생각은 다를 수도 있겠지만, 어쨌든 그렇다.

그리고 제자나 다름없는 나를 자존심까지 굽혀 가며 문경에게 부탁한 적천강의 마음이 심란하리라는 것은, 이미 짐작하고도 남음이었다.

‘지금쯤이면 또 어딘가에서 혼자 청승 떨고 계시겠지.’

다른 사람들은 적천강을 단지 성미가 불같고 괴팍하기 짝이 없는 늙은이라고 수군대지만, 내가 본 적천강은 심성이 여린 사람이다.

구박하고 툴툴거려도 내면에는 아끼는 사람에 대한 마음이 축축하게 젖어 있는, 그런 사람.

환한 달을 힐끗 올려다본 나는 걸음을 옮겼다.

‘금방 찾겠지. 주위에 사람도 많으니까.’

하지만 그런 속 편한 생각은, 불과 한 식경이 지나기도 전에 씻은 듯이 사라져 버렸다.

“못 봤다고?”

“예. 아까부터 통 안 보이시던데요?”

“만약 거짓말하는 거면…….”

“제가 왜 조장님한테 거짓말을 합니까. 맞아 죽기 싫으면 없던 사실도 지어내서 말할 텐데.”

“청 소협은? 청 소협도 못 봤어?”

“네, 은인. 왜요? 무슨 일 있어요?”

“그게…… 아니다. 별일 아니니까 하던 거나 마저 해.”

“앗. 별일 없으시면 미미 좀 보실래요? 혈어를 열 마리나 먹어서 그런지 배가 엄청 빵빵해요!”

“어. 그래, 굉장하네.”

그리 넓은 곳도 아닌데 도대체 어디로 사라진 건지.

나는 사라진 적천강을 찾아 이곳저곳을 찾아 헤맸다. 그러나 만나는 사람마다 붙잡고 물어봐도 결과는 영 신통치 않았다.

“어이, 거기 지나가는 거지. 이리와 봐.”

“싫다.”

“네가 요즘 덜 맞았구나.”

“제기랄. 나도 체면이라는 게 있다. 아무리 네놈이 초절정 고수라 해도 후개인 나를 저잣거리 똥개 부르듯이 대하면 방도(房徒)들이 어떻게 생각하겠나?”

“은자 두 냥.”

“이게 진짜 누굴 거지로 보나…….”

“열 냥.”

파팟!

“음. 친우의 부름을 무시할 수는 없는 법. 무슨 일이지?”

“우리 노, 아니 스승님. 어디 계신지 알아?”

“적 대협? 모른다. 이곳에 온 뒤에는 한 번도 못 뵈었으니까.”

“다른 개방도들한테 물어봐 줄 수 있냐?”

“글쎄, 우리도 각자 맡은 일이 있어서 바쁘긴 한데. 그래도 혹시 모르니 한 바퀴 돌아보고 귀띔 정도는 해 주지.”

“그래, 고맙다.”

“고맙긴 뭘. 우리 사이에.”

“그럼 수고하고.”

“……그런데 은자는?”

“후불제야. 단, 스승님 위치 알아 오면 두 배로 준다.”

“스, 스무 냥! 거지이잇!”

그러나 자본주의의 노예가 되어 신나게 달려간 궁기방도 결국 적천강의 위치를 알아내는 데는 실패하고 말았다.

녀석에게 은자 다섯 냥을 던져 준 나는 그 후에도 여러 곳을 돌아다녔지만, 돌아오는 대답은 늘 엇비슷했다.

“제갈 대협. 혹시 우리 스승님 못 보셨습니까?”

“오, 마침 잘 왔군. 본 가의 진법을 실험 중인데, 조금 더 보완하면 이 틈새에서 흘러나오는 기운을 억제할 수 있을 것 같…….”

“잘됐네요. 고생하세요.”

“진 대협, 제가 봤습니다!”

“정말입니까? 어디서요?”

“두 시진 전쯤에 저쪽 물가에서 누군가를 엄청나게 때리고 있었습니다.”

“그때 맞고 있던 게 전데요.”

“……아.”

“진 대협! 진 대협!”

“네. 거기 손드신 분은 어디서 보셨어요?”

“적 대협이라면 못 봤소.”

“아니, 그런데 왜.”

“이 무복에 서명 한 번만 부탁하오. 내 자식놈이 진 대협 같은 훌륭한 무인이 되는 게 꿈인데, 서명 한번 받으면 소원이 없겠다고…….”

“……자제분 성함이?”

“제갈소평이오. 무공 열심히 익히고, 편식하지 말라고 좀 써 주시오. 특히 대파.”

“잠깐. 그럼 저도 서명을 부탁드려도 되겠습니까?”

“내가 먼저 오지 않았나. 줄 서게!”

“네? 갑자기 줄을 왜 서세요. 거기 뒤로 빠지세요! 줄 서지 마세요! 아, 미치겠네.”

약 반 시진 뒤, 한바탕 순회공연을 마친 내가 임시로 세워진 개인 막사로 돌아왔을 때는 이미 자정이 넘은 시각이었다.

제갈소평을 시작으로 창우, 묘령이, 진수 등의 꿈나무들에게 교훈적인 메시지가 담긴 서명을 해 주고 나니 진이 쏙 빠진다.

“……그래서 노야는 어디에 계신 거야?”

여기가 요동벌판도 아닌데 이렇게 홀연히 사라질 수가 있나.

이 정도면 단단히 작정하고 숨은 것이 틀림없다. 아마도 내가 찾아올 것을 예측하고 모습을 감춘 거겠지.

‘어차피 금방 얼굴 보게 될 텐데, 이 정도로까지 피하시는 걸 보면…….’

아무래도 내가 짐작한 것 이상으로 심란한 모양이다.

작게 한숨을 내쉰 나는 막사 구석에 자리한 나무 탁자에서 물 주전자를 집어 벌컥벌컥 들이켰다.

하루 종일 돌아다니며 말을 했더니 목이 타서 안 되겠, 근데 이거 물맛이 왜 이래?

‘강물을 그대로 퍼 온 건가. 뭔가 짭조름한데.’

환경 오염이 진행되지 않은 무림이라 해도 찝찝한 건 어쩔 수 없다.

내가 미간을 좁힌 채 입맛을 다시고 있던 바로 그 순간이었다.

삐빅.



- [강력한 마비산]에 중독되었습니다.

- [강력한 마비산]은 정신을 흐리게 만들고 몸을 굳게 만드는 마취약의 일종입니다.

- 당신은 정신이 혼미해지는 것을 느낍니다!

- 당신의 [열양지기]가 독에 저항합니다!

- 빨리 조치를 취하지 않는다면 상태 이상, [전신 마비]가 발동됩니다!



……?

아니, 시발. 이거 뭔데.

서서히 마비되어 가는 몸뚱어리도 잊은 채 멍하니 시스템 창을 바라보던 내 머릿속에, 얼마 되지 않은 짤막한 기억이 벼락처럼 스쳐 지나갔다.



‘내일이면 자연스럽게 알게 될 것이다.’

‘어차피 곧 있으면 자정인데, 그냥 속 시원하게 알려 주면 안 됩니까?’

‘밤이 깊었군. 잊지 마라, 내일부터 시작이다.’



“……!”

문경, 이 개새끼가!

피가 거꾸로 솟구치는 듯한 빡침.

동시에 마비산을 머금은 혈류가 빠르게 돌며 눈앞이 아득해진다.

헉, 하고 헛숨을 들이킨 나는 황급히 공력을 끌어올림과 동시에 마음속으로 명령어를 외쳤다.

‘인벤토리 오픈, 소환!’

생각과 동시에 손에 끼워지는 반지.

다른 사람들의 시선 때문에 평소에는 인벤토리에 넣어둔 만독지환(萬毒指環)이 묘한 광택을 흩뿌린다.

띠링.



- [만독지환]의 사용조건을 충족했습니다

- 특수 스킬, [독성 흡수]가 발동되었습니다!

- [강력한 마비산]이 저항합니다!



스스슥!

느껴진다. 몸속 깊은 곳에서 각기 다른 목적을 가진 두 기운이 충돌하는 것이.

그러나 만독지환은 적천강의 무형지독마저 흡수한 사천당문의 신물.

거기에 더해 독성과 상극인 열양지기까지 더해지니, 이내 맥없이 스러질 수밖에 없었다.

띠링.



- [해독]을 완료했습니다!

- [강력한 마비산]의 독성이 체내에서 모두 사라집니다!

- 모든 상태 이상이 회복되었습니다!



“……후우. 이 미친 노인네.”

나는 참았던 숨과 함께 욕설을 중얼거렸다.

자정이 넘었다고 바로 이런 함정을 파 놓다니. 내일부터 시작이라는 게 그런 의미가 있을 줄은 몰랐다.

‘젠장. 누가 살수 아니랄까 봐.’

처음에는 암천의 암습인 줄 알았다.

설마 진짜 무림인으로 만들어 주겠다는 게 이런 뜻이었나? 가뜩이나 진이 빠진 상태였는데, 갑자기 벌어진 일에 심장이 벌렁거리고 다리에 힘이 풀렸다. 나는 깊은 한숨과 함께 침상에 주저앉았다.

푸푹!

“……?”

삐빅.



- [강력한 미혼산]에 중독되었습니다!



살성, 이 시벌놈아.
```

## Final English reading copy

```markdown
# Chapter 490

“So, did you finish your conversation?”

The Wudang Daoists returned exactly half an hour later, just as they had said they would.

I still had plenty of questions, and I wanted to move somewhere else and keep talking. Mungyeong, however, had other ideas.

“We’re done. Go back.”

“…What? We’re done? You haven’t even told me what kind of training this is!”

“You’ll naturally find out tomorrow.”

“It’s already the hour of the Pig.[^1] It’ll be midnight soon. Can’t you just tell me and get it over with?”

“It’s late. Don’t forget. We begin tomorrow.”

“No, wait.”

“Wait?”

*Shhk.*

I alternated my gaze between the short sword rising slightly from his sleeve and Mungyeong, then pointed beyond him into the darkness with a stiff expression.

“I mean over there. You can go that way.”

“…”

“Just keep going straight, then turn right.”

“It seems that wasn’t what you were trying to say.”

“I thought you might not know, so I figured I’d better make sure. Hehe.”

“I know. Shut up and get lost.”

“Yes, sir. Have a peaceful night.”

A little while later, after confirming that Mungyeong’s back had completely disappeared from sight, I muttered under my breath.

“Goddammit…”

One mountain after another.

Just when I thought I had finally gotten used to Jeok Cheongang’s methods, now I had to start worrying about the Slaughter Saint’s mood too.

My eyes were already going dark just thinking about the hardships waiting ahead.

*Actually, the Old Master is much better.*

Leaving aside the intensity of his training, Jeok Cheongang at least told me what kind of training I would be doing.

His temper might have been as hot as fire, but he had still prepared something resembling a curriculum.

*But what kind of training is so secret that he won’t even tell me?*

There was a simple reason I was so curious. The Quest I had accepted by accident didn’t contain any information either.

*Quest window, open.*

*Ding.*



> **System**
>
> **Quest**
>
> **Fake Murim Martial Artist**
>
> Mungyeong sensed the war clouds that will soon hang over the world and, after careful consideration, decided to teach you personally.
>
> However, everything requires a period of preparation.
>
> Before passing down his secret martial arts, Mungyeong will test you through various methods.
>
> When this first test ends is up to you.
>
> **Grade:** None
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Earn Mungyeong’s recognition *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

I looked at the Quest window two or three more times, but it remained unchanged.

Compared to the training Quest at Mount Jiuhua, where the objective had been clearly stated, this was nothing but vague nonsense.

*Earn Mungyeong’s recognition.*

At this point, I would rather run around with iron balls hanging from me. At least then I would have a clear objective and be able to check my progress.

But this was basically the crime of getting on someone’s bad side.

Didn’t it mean I had to keep getting put through the wringer until he decided he liked me?

*This feels like it’ll take a while.*

I didn’t know what Mungyeong’s training methods would be like, but one thing was certain: earning his recognition wouldn’t be easy.

Objectively speaking, it would be strange if it were easy.

*It’s probably going to be brutal, but I’ll have to endure it.*

The man I was dealing with wasn’t some ordinary martial artist. He was the Slaughter Saint, a Supreme Peak master counted among the greatest in the world. Being taught secret martial arts by someone of that caliber was a fortuitous encounter in itself.

And when I thought about it, I had already experienced two such fortuitous encounters.

The first was, without a doubt, the System.

And the second…

*The Old Master.*

There was no way I could leave Jeok Cheongang out of it.

If I hadn’t met him, if I hadn’t learned the Fire Gate Clan’s martial arts—passed down to only one person in each generation—then even with the System, I probably wouldn’t have reached my current strength or position.

Following that train of thought, Jeok Cheongang’s face suddenly flashed through my mind.

*Still, I should go see him.*

Of course, Jeok Cheongang and I were not formally Master and Disciple.

But just because we didn’t call each other Master and Disciple didn’t mean ours was merely a relationship of convenience.

We were the kind of people who understood each other without speaking. Jeok Cheongang and I were the sort who toyed with the words *Master* and *Disciple* in our hearts.

“…”

Or maybe not. I’m suddenly not so sure.

Jeok Cheongang might think differently, but that was how I saw it.

And it was obvious that Jeok Cheongang must be troubled after swallowing his pride and personally asking Mungyeong to teach someone who was practically his Disciple.

*He’s probably off somewhere moping by himself again.*

Other people whispered that Jeok Cheongang was nothing more than a hot-tempered, impossibly eccentric old man. But the Jeok Cheongang I knew was a tenderhearted person.

He might scold and grumble, but deep inside, his feelings for the people he cared about were soaked through with affection.

I glanced up at the bright moon and began to walk.

*I’ll find him soon enough. There are plenty of people around.*

That comfortable thought vanished without a trace less than half an hour later.

“You haven’t seen him?”

“No, sir. I haven’t seen him for a while.”

“If you’re lying to me…”

“Why would I lie to the Captain? If I didn’t want to get beaten to death, I’d make up things that never happened and tell you.”

“What about Young Hero Cheong? You haven’t seen Young Hero Cheong either?”

“No, Benefactor. Why? Is something wrong?”

“It’s… Never mind. It’s nothing. Get back to what you were doing.”

“Oh! If nothing’s wrong, would you like to see Mimi? She ate ten Blood Fish, so her belly is incredibly round!”

“Yeah. Great.”

This place wasn’t even that large. Where on earth had he disappeared to?

I searched here and there for the missing Jeok Cheongang, but no matter whom I stopped and asked, the answers were never helpful.

“Hey, you beggar passing by. Come here.”

“No.”

“You haven’t been beaten enough lately.”

“Damn it. I have a reputation to maintain too. No matter how much of a Supreme Peak master you are, if you treat me, the Successor Beggar, like some stray dog you’re calling over from the street, what will the Sect’s disciples think?”

“Two silver nyang.”

“Are you seriously treating me like a beggar…”

“Ten nyang.”

*Fwoosh!*

“Hm. One cannot ignore a friend’s summons. What is it?”

“Our Old Master—no, our Master. Do you know where he is?”

“Sir Jeok? No idea. I haven’t seen him once since he arrived here.”

“Can you ask the other Beggars’ Sect disciples?”

“Well, we’re all busy with our assigned tasks. Still, you never know. I’ll make a round and let you know if I hear anything.”

“Yeah, thanks.”

“What are friends for?”

“Then get to it.”

“…What about the silver?”

“I’ll pay you later. But if you find my Master’s location, I’ll give you double.”

“T-Twenty nyang! Beggerrr!”

But even Gung Gibang, who had become a slave to capitalism and run off enthusiastically, ultimately failed to find Jeok Cheongang.

I tossed him five silver nyang, then continued visiting various places. The answers I received were always more or less the same.

“Sir Zhuge, have you perhaps seen my Master?”

“Oh, you came at the perfect time. I’m testing our clan’s formation, and I think that with a little more refinement, I can suppress the energy leaking from this gap—”

“That’s great. Good luck.”

“Great Hero Jin! I saw him!”

“Really? Where?”

“About two shichen ago, he was over by the water, beating someone senseless.”

“The person getting beaten was me.”

“…Ah.”

“Great Hero Jin! Great Hero Jin!”

“Yes. You there, with your hand raised. Where did you see him?”

“If you mean Sir Jeok, I haven’t seen him.”

“No, but why are you—”

“Would you sign this martial artist’s uniform for me? My son dreams of becoming a fine martial artist like Great Hero Jin. He says he’ll have no regrets if he can get your autograph…”

“…What’s your son’s name?”

“Zhuge Sopyeong. Please write something telling him to practice his martial arts diligently and not be a picky eater. Especially green onions.”

“Wait. Then may I ask for your autograph too?”

“I got here first. Get in line!”

“What? Why are you suddenly lining up? Move to the back! Don’t line up! Ah, this is driving me crazy.”

About half an hour later, after completing my grand tour, I returned to the temporary private tent that had been set up for me. By then, it was already past midnight.

After signing autographs with inspirational messages for Zhuge Sopyeong, Changwoo, Myoryeong, Jinsu, and the other budding talents, I was completely drained.

“…So where the hell is the Old Master?”

This wasn’t even the Liaodong Plain. How could he simply vanish into thin air?

At this point, he had clearly made up his mind to stay hidden. He had probably predicted that I would come looking for him and deliberately disappeared.

*I’ll be seeing him soon enough anyway. For him to avoid me this much…*

He must have been even more troubled than I had imagined.

I let out a small sigh, picked up the water pitcher from the wooden table in the corner of the tent, and gulped down the water.

I had been walking and talking all day, so my throat was parched. But why did the water taste like this?

*Did they scoop it straight from the river? It’s a little salty.*

Even in the unpolluted Murim, I couldn’t help feeling uneasy.

That was when it happened.

*Beep.*



> **System**
>
> - You have been poisoned by **Potent Paralysis Powder**.
>
> - **Potent Paralysis Powder** is a type of anesthetic that clouds the mind and stiffens the body.
>
> - You feel your consciousness becoming hazy!
>
> - Your **Scorching Yang Qi** resists the poison!
>
> - If you do not take action quickly, the Status condition **Full-Body Paralysis** will activate!



…?

No, fuck. What the hell was this?

I stared blankly at the System window, forgetting even the body that was slowly becoming paralyzed. Then a short memory flashed through my mind like lightning.

*You’ll naturally find out tomorrow.*

*It’s already the hour of the Pig. It’ll be midnight soon. Can’t you just tell me and get it over with?*

*It’s late. Don’t forget. We begin tomorrow.*



“……!”

Mungyeong, you son of a bitch!

A surge of rage made it feel as though my blood were boiling backward.

At the same time, the bloodstream carrying the paralysis powder raced through my body, and my vision began to fade.

I sucked in a startled breath, hurriedly raised my internal energy, and shouted a command in my mind.

*Inventory Open, Summon!*

A ring appeared on my finger at the same moment.

I normally kept the Myriad-Poison Ring in my inventory to avoid other people’s eyes, but now it scattered a strange sheen.

*Ding.*



> **System**
>
> - The usage conditions for the **Myriad-Poison Ring** have been met.
>
> - Special Skill **Poison Absorption** has activated!
>
> - **Potent Paralysis Powder** resists!



*Hissss!*

I could feel it. Deep inside my body, two energies with entirely different purposes collided.

But the Myriad-Poison Ring was a treasured artifact of the Sichuan Tang Clan, one that had even absorbed Jeok Cheongang’s Formless Ultimate Poison.

And with the addition of Scorching Yang Qi, the natural opposite of poison, the paralysis powder had no choice but to collapse helplessly.

*Ding.*



> **System**
>
> - **Detoxification** complete!
>
> - All traces of **Potent Paralysis Powder** have disappeared from your body!
>
> - All Status conditions have been cleared!



“…Phew. You crazy old man.”

I muttered the curse along with the breath I had been holding.

He had set up a trap like this the moment midnight passed. I never imagined that “we begin tomorrow” would mean this.

*Damn it. He really is an assassin.*

At first, I thought it was an ambush by Dark Heaven.

Was this what he meant by turning me into a true Murim martial artist? I was already exhausted, and the sudden attack had sent my heart pounding and made my legs go weak. With a deep sigh, I collapsed onto the bed.

*Phut-phut!*

“…?”

*Beep.*



> **System**
>
> - You have been poisoned by **Potent Soul-Bewitching Powder**!



Slaughter Saint, you fucking bastard.

[^1]: The hour of the Pig corresponds roughly to 9–11 p.m. in traditional East Asian timekeeping.
```
