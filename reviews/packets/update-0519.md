<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0519.txt",
      "sha256": "78c8c6e65db600428f1d9602b08d78c1e3c4a1c5613bfeb8dbed4085a7ee0b44",
      "bytes": 14607
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e26be95f6171d45ac23ae4deabab79c4813751d9bce33eb590d8c972a21843c3",
      "bytes": 4551
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "171b2dc6dd2a978de79e0b2cde609b691d8064d0f6bf42fae295efe0be6dec17",
      "bytes": 165721
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ac468d476e4cadb8576345f6bd629b3570f4c29b83d95e8571ac5ca9bda1f979",
      "bytes": 553
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "3c5fd00d56b8562a469aaec0813de3d2d8b64e9ebb2ccc7a301adb1ad4f01703",
      "bytes": 1001
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "d01c4ea87473b06d95b2c8f49000a927b4ad0bf1f85dc30e6ce6b6d7838fc56f",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "31afed669d0c0e106cb6a57bfceae26680f29c42cd92af736692b714806df929",
      "bytes": 1630
    },
    {
      "path": "characters/Moon Beauty Saber.md",
      "sha256": "dbe4f95ea61cdc06bf96a71fc5e920c7ea59d02e662e8c5ce5617d233d5003c5",
      "bytes": 637
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "951a90b4b4b10dbb3e0b55aa482c6195ee4aea4e6948b4dc81b241d12544ff26",
      "bytes": 750
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0f312e86dd4193318bfcb76c6c5131cfebcbc971b6509c8f0bb1cc9603299fb9",
      "bytes": 156842
    }
  ],
  "estimated_tokens": 12321
}
-->

# Durable State Update — Chapter 519

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 519. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 519. Profile updates may replace only one
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
  "chapter": 519,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 519,
    "continuity_sources": [519],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm, achieved Returned to Youth, and begun his long-promised duel with Nangong Cheon, the Azure Sky Sword King.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song and will be founded in three days; major orthodox and unorthodox factions, eccentric experts, distant great families, and uncertain allied factions are gathering in Henan.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle; Shaolin's new Abbot wants to meet Taekyung.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "A Dark Heaven assault has erupted near Mount Song; Taekyung and Unnamed are leading a large Murim response, and a person emerging from a burning building has caused Taekyung to realize that the apparent fiend is on their side."
  ],
  "continuity_sources": [
    518,
    517
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Who is the person emerging from the burning building, and why does Taekyung recognize the apparent fiend as belonging to his side?"
  ],
  "safe_through": 518,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, 시주 as Benefactor, 계율원주 as Discipline Hall Master, 십이지파 as Twelve Branches of the Demonic Cult, 모용세가 as Murong Family, 요녕 as Liaoning, 진돗개 하나 as Jindotgae One, 소하문 as Xiao He Gate, 장충도 as Long Serpent Saber, 방가 as Fang Family, 월미도 as Moon Beauty Saber, and 검기상인 as the level of injuring others with Sword Energy."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 남궁세가   | **Nangong Family**               |
| 삼류     | **Third Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 주화입마   | **qi deviation**                                 |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 보상               | **Reward**                     |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 월미도 | **Moon Beauty Saber** | Sobriquet of the Fang Family's top-tier wandering martial artist. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 평화 | **Peace Guild** | Guild name. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 석가 | **Shakyamuni** | Buddhist figure invoked by Hong Dao in his earlier conversation with Jeok Cheongang. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 무명 | 굉도 | disciple_to_master | Master | deferential | Refers to Hong Dao as 스승님 while explaining his Dharma name and training. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 무명 | master_to_disciple | Disciple | affectionate and familiar | Hong Dao addresses Unnamed as 제자야 while discussing his residence. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 창천검왕 | long-standing martial rival and duel partner | Azure Sky Sword King | blunt and familiar | Explicitly names him while coming to fulfill their long-delayed duel promise. |
| 창천검왕 | 적천강 | long-standing martial rival and duel partner | Fire King | formal and familiar | Addresses Jeok Cheongang by title while welcoming the promised duel. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 517
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 517
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 508
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 518
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Moon Beauty Saber.md

# Moon Beauty Saber (월미도)

- **Safe through:** Chapter 518
- **Aliases:** None
- **Role:** Moon Beauty Saber is a top-tier wandering martial artist of the Fang Family who has long since reached the level of injuring others with Sword Energy.
- **Personality:** Dignified, condescending, status-conscious, and quick to assert his superiority.
- **Voice:** Formal, self-assured, and patronizing toward people he considers beneath him.
- **Relationships:** He identifies himself as a member of the Fang Family and treats lower-status martial artists condescendingly.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 518
- **Aliases:** None
- **Role:** Unnamed is a young Shaolin monk and practical Disciple of the late Hong Dao who achieved enlightenment after three months of treatment and training in Repentance Cave, becoming a Supreme Peak master and Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** His current voice is rough, formal, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

## Korean source

```text
＃519화



쿠웅!

불길에 휩싸인 커다란 객잔. 검게 그을린 목제 기둥이 쓰러지고 잿가루가 피어오른다. 그 사이로 모습을 드러낸 마귀의 얼굴은 너무 익숙하다 못해 충격적이었다.

“이게 다 뭐 하는 짓거리냐?”

“…….”

그건 제가 할 말인데요.

순간 침묵이 흘렀다. 나를 바라보는 무명의 시선이 지진이라도 난 것처럼 흔들렸다. 작게 달싹이는 입술 사이로 흘러나온 전음(傳音)이 귓가를 파고들었다.

- 왜, 왜 적 시주께서 저기에서 나오십니까?

그걸 내가 어떻게 알아.

- 암천 아니었습니까?

내가 물어보고 싶은 건데, 그건.

- 아미타불. 혹시 암천이십니까?

아니, 이건 또 무슨 미친 소리야.

우리가 암천이면 넌 바티칸 교황청 소속이냐.

무명의 말에 어이가 없어진 건 나뿐만이 아니었다. 전음 도청에 일가견이 있는 적천강의 얼굴은 이미 악귀처럼 일그러져 있었다.

“뭐? 노부가, 암천?”

“아, 아니, 그게 아니고요. 지금 사소한 오해가…….”

결론부터 말하자면 오해를 풀고자 한 내 시도는 수포로 돌아갔다. 정확히는, 무림맹 창설을 앞두고 한껏 전의를 불태우던 우리의 자랑스러운 무림 십자군이 용납하지 않았다.

“암천!”

“마두가 스스로 암천이라고 밝혔다!”

키워드 입력.

“잠깐 기다려 보시오. 열화신룡과 아는 사이 같은데.”

“당연히 아는 사이겠지! 열화신룡이 암천과 싸운 것이 한두 번인가!”

“그렇군. 암천의 마두다!”

기적의 논리.

“마귀 같은 놈! 생긴 것도 흉신악살이 따로 없구나!”

“머리카락도 죄다 시뻘건 것이, 세상을 피로 물들일 상이로다!”

외모 비하.

“일단 죽여라!”

“놈을 잡으면 영웅이 된다!”

중세 십자군식 결론 도출.

이 모든 전개가 찰나라고 부를 수 있을 만큼 짧은 시간 만에 이루어졌다. 어느덧 천여 명에 달하는 무림 십자군의 집단 광기에, 넋이 나가 있던 나와 무명이 황급히 손을 내저었다.

“아닙니다. 아니에요!”

“아미타불! 모두 멈추십시오! 저분은 소승의 스승님이신 굉도 선사의…….”

무명의 외침에, 비교적 가까이에 있던 무림인들이 눈을 부릅떴다.

“헛.”

“그게 사실이오?”

이제야 좀 말이 통하겠는데요.

딱 그런 눈빛으로 나를 바라본 무명이 고개를 끄덕였다.

“그렇습니다.”

“허어. 그냥 마두도 아니고 굉도 선사를 해한 흉수라니!”

“예?”

“천인공노할 마두 같으니! 저놈의 사지를 찢어 죽여라!”

“…….”

시벌 못 해 먹겠네, 진짜.

이 무림인이라는 새끼들은 사람 말을 끝까지 들으면 주화입마에 걸리기라도 하는지, 도무지 알아 처먹으려고 하질 않는다.

그리고 이 집단 광기의 대미를 화려하게 장식한 것은 무너진 건물의 잔해에서 모습을 드러낸 낯선 인물이었다.

“멈추어라, 악적! 감히 하남에서 이런 참혹한 짓을 벌이다니!”

이 미쳐 돌아가는 상황을 입을 벌린 채 바라보던 적천강이 참혹한 표정으로 중얼거렸다.

“이것들이 죄다 제정신이 아니군. 우선 노부의 말부터 듣고…….”

“문답무용! 이 월미도(月美刀)가 네놈을 용서치 않으리라!”

“……일단 맞자.”

그래, 적천강 성격에 저 정도면 오래 참았다.

쉬익. 파팡!

월미도 디스코팡팡 잘 가고.

빛살처럼 쇄도하던 월미도의 신형이 포탄처럼 도로 튕겨 나가 잔해 깊숙이 처박혔다. 이 자리에 모인 무림인들의 입장에서는 본 적도 없고, 볼 수도 없었던 일권(一拳). 그 엄청난 무위에 주위의 공기가 삽시간에 얼어붙었다.

“워, 월미도가 단 일 격에……!”

“아아, 마두의 무공이 하늘에 닿았구나!”

무공은 둘째 치고 분노가 하늘에 닿은 것 같은데. 그리고 굳이 내가 아니어도 지금의 적천강을 건드려선 안 된다는 것 정도는 모두가 알고 있는 듯했다. 마두를 쓰러트려 이름을 알리고는 싶지만, 쓰러지기는 싫은 것이 사람 심리 아닌가.

‘이제야 좀 조용해졌네.’

모두가 잠잠해진 지금이 오해를 풀 수 있는 유일한 기회다. 한차례 목을 가다듬은 나는 입을 열었다. 아니, 열려고 하던 그때였다.

“심각한 오해가 있으신 것 같은데, 저기 계신 분은 마두가 아니라…….”

“갈(喝)! 모두 길을 터라!”

“아이, 씻팔!”

돌아 버리겠네. 어떤 새끼야, 또.

하지만 홍해처럼 갈라지는 인의 장막 사이로 모습을 드러낸 방해꾼은 내가 새끼라고 부를 수 있을 만한 사람이 아니었다.

“벽력도왕(霹靂刀王)께서 오셨다!”

“팽 대협께서 친히 마두를 단죄하고자 오셨다!”

저벅. 저벅.

용기백배한 분위기 속에서 걸음을 옮기는 거대한 덩치의 노인. 딱 벌어진 어깨와 부리부리한 눈. 어깨에 엄청난 크기의 도를 걸친 벽력도왕의 모습에 적천강이 한숨을 내쉬었다.

“이제야 말이 통하는 상대가 왔군.”

동감이다.

벽력도왕이라면 적천강과 티격태격하기는 해도 상당한 친분이 있는 사이다. 오랜 앙숙이라고 쓰고 친우라고 읽을 수 있는 상대이기도 하다. 그라면 어렵지 않게 적천강의 정체를 알아차릴 것이다.

아니나 다를까, 적천강을 위아래로 훑어보던 벽력도왕이 눈을 크게 떴다.

“여기서 뭘 하고 있나?”

“이야기하자면 길어. 우선 사람들부터 물려라.”

“묻는 말에 대답부터 해라.”

“응?”

“찢어 죽여도 시원찮을 마두 새끼가 여기서 뭐 하냐고.”

“……!”

“……!”

적천강의 눈꺼풀이 파르르 떨렸다.



* * *



다그닥. 다그닥.

고요한 침묵 속에서 말발굽 소리만 울려 퍼진다. 말없이 마차 밖의 풍경을 바라보던 거구의 노인이 불쑥 입을 열었다.

“사실 보자마자 눈치챘지. 모를 수가 없었어.”

사람들의 시선 속에서, 벽력도왕이 진중한 목소리로 말을 이었다.

“적발에 적염이라면 누가 봐도 화왕이지. 다른 사람들은 적가가 반로환동했다는 사실을 꿈에도 몰랐겠지만, 나는 알아차릴 수 있었어.”

“그렇군요.”

고개를 끄덕인 내가 물었다.

“그런데 왜 다짜고짜 도를 휘두르신 겁니까?”

“그건…….”

“아, 한 수 교환하고 후달리시니까 전원 총공격 명령하신 이유에 대해서도 추가 설명 요구합니다.”

“후달려? 허허허.”

또다시 내려앉은 무거운 침묵. 나를 포함한 사람들의 불신 가득한 눈빛을 마주한 벽력도왕은 굳은 얼굴로 입을 열었다.

“그건, 실전을 경험시켜 주기 위해서였다.”

“아. 실전이요.”

“곧 벌어질 암천과의 싸움을 위한 초석이랄까. 상대가 화왕 적천강이라면 모두에게 좋은 경험이 되지 않겠느냐.”

나는 진지하게 물었다.

“혹시 그 경험이라는 게, 사후 세계 경험 말씀하시는 겁니까?”

“…….”

벽력도왕은 꿀 먹은 벙어리가 되어 입을 다물었다. 양심이 있다면 그럴 수밖에 없는 게, 의방으로 실려 간 사람들의 숫자만 해도 스무 명에 달한다. 그중 대부분이 화왕과 벽력도왕, 두 십왕(十王)이 주고받은 공격의 여파에 휘말린 삼류 무인이었다.

‘그 정도로 끝난 거면 다행이긴 한데.’

일제강점기의 윤동주 시인이 잎새에 이는 바람에도 괴로워했다면, 그들은 휘몰아치는 칼바람에 존나 아파했다.

“그……래도 다들 무사하다고 들었는데.”

“무사하죠. 최소한 앞으로 보름 동안은 무사할 겁니다. 의방에만 누워 있을 테니까.”

사후 체험의 결과는 확실했다.

아무리 칼끝에서 살아가는 무림인이라고 해도 PTSD는 무시 못 한다. 의방에 들러 피해자들을 만나 봤더니 얼굴이 파랗게 질린 채 말도 못 하더라.

특히 월미도인지 하는 낭인은 심각했다. 얼마나 몸을 떨어 대는지, 하남이 아니라 남극 세종기지로 착각했을 정도였다.

“팽 대협께서 총공격 명령만 안 내리셨어도 이런 일까지는 안 일어났습니다.”

계속되는 내 맹비난에 벽력도왕이 고리눈을 치켜떴다.

“그러는 네놈은?”

“저요?”

“그래. 네놈 말이다! 인근에 있는 무림인들을 싹 다 긁어모아 온 것이 네놈 아니냐!”

“그 부분은 인정합니다. 하지만 그 상황에서는 불가항력이었어요. 안 그래요?”

내 물음에 구석 자리에 앉아 있던 공범, 무명이 염주를 어루만졌다.

“진 시주의 말씀이 옳습니다. 설령 석가모니께서 빈승과 같은 처지셨다고 해도 멸마(滅魔)를 부르짖으며 달려가셨을 겁니다.”

“보리수나무 뽑아서 마두 대갈통 으깨기 가능?”

“아미타불. 가능.”

“…….”

적천강 못지않게 한 성깔 하는 벽력도왕이지만 무명만큼은 대놓고 핍박하지 못했다. 절친한 벗이었던 법왕 굉도가 남긴 유일한 제자는 그에게 있어 아픈 손가락이었다.

“끄응.”

앓는 소리를 흘린 벽력도왕이 나를 노려보며 윽박질렀다.

“그런데 이놈이 아까부터!”

“뭐요. 왜요.”

“너, 나랑 친하냐?”

“안 친한데요.”

“그럼 하북팽가가 우스워?”

“그게 왜 또 그렇게 됩니까? 괜히 할 말 없으시니까 논지를 흐리시네.”

“대가리에 피도 안 마른 어린놈이 자꾸 아까부터 따박따박 말대꾸를…….”

“어우. 틀니 딱딱.”

틀니가 정확히 뭘 뜻하는지는 몰라도, 말에 담긴 감정은 제대로 전해진 것이 분명했다.

“이놈이 감히!”

얼굴이 벌겋게 달아오른 벽력도왕이 자리를 박차고 일어나려던 그때, 시종일관 입을 다물고 있던 두 사람이 거의 동시에 입을 열었다.

“고정하시오, 팽 대협.”

“시끄럽다. 전부 주둥이 닫아라.”

전혀 다른 목소리와 분위기. 어쩌면 십왕(十王)이라는 두 글자만이 두 사람을 이어 주는 유일한 공통점일지도 모르겠다.

“본인이 경솔했던 것 같소. 오랜만에 피가 끓어올라서 그만.”

담백하게 자신의 잘못을 인정하는 창천검왕(蒼天劍王)을 뒤따라 적천강이 말을 이었다.

“노부는 하나도 잘못한 것 없다. 네놈들이 경솔했던 거지.”

“…….”

그래, 이래야 우리 노야지.

늘 푸른 상록수가 따로 없다. 벽력도왕이 이게 사람인가, 하는 표정으로 적천강을 바라보며 물었다.

“적가야. 네놈은 죄책감이 조금도 안 느껴지나?”

“노부가 죄책감을 왜 느껴? 무인들끼리 만나면 푸닥거리 한번 할 수도 있지. 객잔 들어갔을 때도 이미 치고받고 싸우는 놈들 있더만.”

“남궁 대협이 때마침 나서지 않았으면 어쩔 뻔했느냐!”

벽력도왕의 말대로, 사태를 수습한 평화의 비둘기는 바로 창천검왕이었다. 적천강과의 짧은 공방 끝에 약간의 내상을 입은 그는 공력을 가라앉힌 뒤에야 모습을 드러냈는데, 군웅 사이에 포함되어 있던 남궁세가의 식솔 하나가 그를 알아본 것이다.



‘어어, 어어어! 태상 가주니임!’



흡사 귀신이라도 본 듯한 비명이었지.

암천이라는 두 글자에 눈깔이 뒤집혀 있던 다른 무림인들도 그제야 제정신이 돌아왔다. 남궁세가도 암천이었냐고 묻는 미친놈도 있긴 했지만, 우리의 자랑스러운 무림 십자군 구성원들은 다행히 이성을 되찾을 수 있었다. 사실 적천강이 반로환동만 안 했어도 알아볼 사람들이 몇 명 정도는 있었을 거다.

“하마터면 대참사가 일어날 뻔했어!”

“충분히 설명할 수 있었다. 그리고 그건 팽가 네놈 눈깔이 개눈깔이라 그런 일이 벌어진 거지.”

“객잔이 무너지고! 사람이 다치고!”

“크흠.”

본인도 찔리는 구석이 있는지, 헛기침을 내뱉은 적천강이 이내 뻔뻔한 표정으로 입을 열었다.

“장소가 장소인지라 적당히 힘 조절 했어. 기껏해야 무너지는 잔해에 조금 부딪힌 정도인데 그 정도면 침 바르면 낫지. 객잔 주인에게는 충분히 보상할 거고. 노부가 봐도 좀 많이 타긴 했더군.”

“……구화산 태워 버렸다고 마교도 천 명을 죽인 그 인간이 하는 말이 맞나? 듣다 보니 가슴이 웅장해지는군.”

“그건 당연히 죽여야지. 그 썅노무 새끼들은 처음부터 보상할 생각도 없었으니까.”

“…….”

뭘까. 말도 안 되는 억지인데 나름대로 논리정연한 이 느낌은.

순간 말문이 막힌 벽력도왕이 중얼거렸다.

“……반로환동으로 뒤집어쓴 가죽만 바뀌었지, 알맹이는 여전하군. 여전히 성격이 지랄맞아.”

“팽가 네놈은 얼굴 가죽이라도 좀 바꿔 봐라. 반로환동도 못 하고 나이만 처먹은 놈이 무슨.”

“뭣이!”

“어허. 반로환동 못 한 놈이 성낸다더니. 딱 그 모양이군.”

“적가 네놈이 감히!”

“응? 뭐라고? 반로환동도 못 한 무명소졸이 하는 말이라 잘 안 들리는데?”

광역 딜 야무지게 넣는 것 보소.

다른 사람은 몰라도, 나는 봤다. 마차 창가 자리에서 어깨를 움찔거리는 창천검왕의 모습을. 그때, 내 시선을 슬그머니 피하며 창밖을 바라보던 그의 입술이 불쑥 열렸다.

“두 분, 이제 그만하는 것이 좋겠소.”

처음에는 단순히 화제를 돌리려나 싶었던 나는, 이내 창천검왕을 따라 창밖의 풍경을 확인하고 중얼거렸다.

“어. 확실히 그러시는 게 좋겠네요.”

내 시선 끝에는 길게 늘어선 성벽과 수많은 인파가 있었다. 그리고 철문 위의 거대한 현판에 용사비등한 필체로 적혀 있는 세 글자도 함께.

무림맹(武林盟).
```

## Final English reading copy

```markdown
# Chapter 519

KABOOM!

A large inn was engulfed in flames. Blackened wooden pillars collapsed, sending clouds of ash into the air. The face of the fiend who emerged through the wreckage was so familiar that it was shocking.

“What the hell are you all doing?”

“…”

*That’s what I wanted to ask.*

A moment of silence followed. Unnamed’s gaze trembled as he stared at me, as though an earthquake had struck. Sound Transmission slipped through his faintly moving lips and pierced my ears.

*Why, why is Benefactor Jeok coming out of there?*

*How should I know?*

*Wasn’t he Dark Heaven?*

*That’s what I want to ask.*

*Amitabha. Could you be Dark Heaven?*

*What kind of crazy question is that?*

*If we’re Dark Heaven, does that make you a member of the Vatican?*

I wasn’t the only one dumbfounded by Unnamed’s words. Jeok Cheongang, who was exceptionally skilled at eavesdropping on Sound Transmission, already had a face twisted like an evil spirit.

“What? This old man is Dark Heaven?”

“N-no, that’s not what I meant. There’s been a small misunderstanding…”

To get straight to the point, my attempt to clear up the misunderstanding ended in failure.

More precisely, our proud Murim Crusade, already burning with fighting spirit ahead of the founding of the Murim Alliance, refused to let it happen.

“Dark Heaven!”

“The fiend just declared himself Dark Heaven!”

*Keyword entered.*

“Wait a moment. He seems to know the Blazing Flame Divine Dragon.”

“Of course he knows him! How many times has the Blazing Flame Divine Dragon fought Dark Heaven?”

“I see. He’s a Dark Heaven fiend!”

*The miracle of logic.*

“You fiend! You look like a demon straight out of hell!”

“His hair is red as blood. He looks like the type to dye the world red!”

*Personal attacks based on appearance.*

“Kill him first!”

“Capture him and you’ll become a hero!”

*Medieval Crusader-style conclusion reached.*

The entire chain of events took place in less time than could reasonably be called an instant.

Faced with the collective madness of more than a thousand Murim Crusaders, Unnamed and I—both of us standing there in a daze—hurriedly waved our hands.

“No! That’s not it!”

“Amitabha! Everyone, stop! That man is not a fiend! He is the late Master Hong Dao’s…”

At Unnamed’s shout, the Murim practitioners who were relatively close widened their eyes.

“Gasp.”

“Is that true?”

*Now we’re finally getting somewhere.*

Unnamed looked at me with exactly that expression and nodded.

“It is.”

“Good heavens. Not just an ordinary fiend, but the culprit who did that to Master Hong Dao!”

“What?”

“What an unforgivable fiend! Tear that bastard limb from limb!”

“…”

*Fuck. I can’t work with this.*

Did these martial artists suffer qi deviation whenever they listened to someone all the way to the end? They simply refused to understand a single word anyone said.

And the grand finale of this collective madness was provided by an unfamiliar figure emerging from the wreckage of the collapsed building.

“Stop, you wicked fiend! How dare you commit such a heinous crime in Henan!”

Jeok Cheongang, who had been staring at the situation with his mouth hanging open, muttered with a grim expression.

“Not one of these people is in his right mind. First, listen to what this old man has to say…”

“Enough talk! This Moon Beauty Saber will not forgive you!”

“…Let’s start with you taking a beating.”

Fair enough. Considering Jeok Cheongang’s personality, he had shown remarkable restraint up to that point.

Whoosh. Fwoom!

*Moon Beauty Saber, enjoy your ride on the Disco Pang Pang.*

Moon Beauty Saber’s figure, rushing forward like a streak of light, flew backward like a cannonball and slammed deep into the wreckage.

The punch was something none of the martial artists gathered there had seen—or had even been capable of seeing.

The overwhelming force of that punch instantly froze the air around them.

“Moon Beauty Saber was sent flying in a single blow…!”

“Aaah! The fiend’s martial arts have reached the heavens!”

*Forget his martial arts. His anger looks like it has reached the heavens.*

And regardless of whether I was here or not, it seemed everyone understood that they absolutely should not provoke Jeok Cheongang in his current mood.

Everyone wanted to defeat a fiend and make a name for themselves. But no one wanted to be defeated in the process. That was human nature, wasn’t it?

*It’s finally quiet.*

Now that everyone had fallen silent, this was my only chance to clear up the misunderstanding.

I cleared my throat and opened my mouth.

Or rather, I was about to.

“There seems to be a serious misunderstanding. The person over there isn’t a fiend, but—”

“Yaaah! Make way!”

“Oh, for fuck’s sake!”

*I’m going to lose my mind. Who is it this time?*

But the intruder who appeared through the wall of people splitting apart like the Red Sea was not someone I could simply call a bastard.

“The Thunderbolt Saber King has arrived!”

“Great Hero Peng has come to personally punish the fiend!”

Thud. Thud.

An enormous old man walked forward through the atmosphere of renewed courage.

Broad shoulders. Bulging eyes. A massive saber slung over one shoulder.

At the sight of the Thunderbolt Saber King, Jeok Cheongang sighed.

“Someone who can finally understand what people are saying has arrived.”

*I agree.*

The Thunderbolt Saber King might bicker with Jeok Cheongang constantly, but the two were actually quite close.

He was the sort of person who could be described as a longtime archrival, but read as a friend.

Surely he would recognize Jeok Cheongang’s identity without any trouble.

As expected, the Thunderbolt Saber King looked Jeok up and down, then opened his eyes wide.

“What are you doing here?”

“It’s a long story. First, make these people withdraw.”

“Answer my question first.”

“Hm?”

“I asked what a bastard fiend who deserves to be torn limb from limb is doing here.”

“…”

“…”

Jeok Cheongang’s eyelids began to tremble.

* * *

Clip-clop. Clip-clop.

In the quiet silence, the only sound was the steady rhythm of horse hooves.

The enormous old man, who had been silently watching the scenery outside the carriage, suddenly spoke.

“To tell you the truth, I recognized you the moment I saw you. There was no way I wouldn’t.”

With people watching him, the Thunderbolt Saber King continued in a serious voice.

“Red hair and a red beard. Anyone would know you were the Fire King. The others couldn’t have dreamed that you had Returned to Youth, but I was able to figure it out.”

“I see.”

I nodded, then asked,

“Then why did you suddenly start swinging your saber?”

“That was…”

“Oh, and I’d also like an explanation for why you ordered an all-out attack after getting cold feet from exchanging a single move.”

“Getting cold feet? Hahahaha.”

A heavy silence descended once more.

Faced with the distrustful eyes of everyone—including me—the Thunderbolt Saber King spoke with a stiff expression.

“It was to give them experience in actual combat.”

“Ah. Actual combat.”

“A foundation for the battle against Dark Heaven that will soon take place. If their opponent was the Fire King, Jeok Cheongang, then wouldn’t it be valuable experience for all of them?”

I asked seriously,

“By ‘experience,’ do you mean experience of the afterlife?”

“…”

The Thunderbolt Saber King fell silent, as though he had swallowed honey.

If he had any conscience at all, he had no choice but to do so. The number of people carried to the medical clinic alone was close to twenty.

Most of them were Third Rate martial artists who had been caught in the aftermath of the attacks exchanged between the Fire King and the Thunderbolt Saber King—the two Ten Kings.

*It was fortunate that it ended there.*

If the poet Yun Dong-ju suffered at even the wind stirring a leaf, they suffered like hell in the howling blade wind.[^1]

“Still… I heard everyone is safe.”

“They’re safe. At least for the next two weeks. They’ll be lying in the medical clinic the whole time.”

The results of their afterlife experience were undeniable.

No matter how accustomed martial artists were to living on the edge of a blade, PTSD was not something to dismiss.

I had visited the victims in the medical clinic. Their faces had gone pale, and they couldn’t even speak.

The worst of all was the wandering martial artist called Moon Beauty Saber. He was trembling so violently that I almost mistook Henan for Antarctica’s King Sejong Station.

“None of this would have happened if Great Hero Peng hadn’t ordered that all-out attack.”

At my continued barrage of criticism, the Thunderbolt Saber King raised his round eyes.

“And what about you?”

“Me?”

“Yes, you! Wasn’t it you who rounded up every martial artist in the area and brought them here?”

“I admit that part. But given the circumstances, it was unavoidable. Isn’t that right?”

At my question, Unnamed—the accomplice sitting in a corner—ran his fingers over his prayer beads.

“Benefactor Jin is correct. Even if Shakyamuni had been in my position, he would have rushed forward crying out for the destruction of demons.”

“Could you uproot a bodhi tree and crush the fiend’s skull with it?”

“Amitabha. It is possible.”

“…”

The Thunderbolt Saber King had just as much of a temper as Jeok Cheongang, but he couldn’t openly bully Unnamed.

Unnamed, the only Disciple left behind by his close friend the Dharma King Hong Dao, was someone the Thunderbolt Saber King couldn’t help but feel protective of.

“Grrr.”

After making a pained sound, the Thunderbolt Saber King glared at me and shouted,

“But you’ve been mouthing off since earlier!”

“What? Why?”

“Are you close with me?”

“No.”

“Then do you think the Hebei Peng Family is a joke?”

“How does that follow? You have nothing left to say, so you’re just muddying the issue.”

“You’re a kid whose blood hasn’t even dried on his head, yet you keep talking back to me…”

“Oof. Clack, clack. Dentures.”

I had no idea exactly what the dentures were supposed to imply, but the emotion contained in my words clearly got through.

“How dare you!”

The Thunderbolt Saber King’s face flushed red, and he was just about to leap to his feet when the two people who had remained silent throughout the journey spoke almost simultaneously.

“Calm yourself, Sir Peng.”

“Quiet. All of you, shut your mouths.”

The two voices and atmospheres were completely different.

Perhaps the only thing connecting the two men was the two characters in their title: Ten Kings.

“I was rash. My blood was running hot after so long, and I lost control.”

The Azure Sky Sword King calmly admitted his mistake.

Jeok Cheongang followed after him.

“This old man did nothing wrong. You were the ones being rash.”

“…”

*That’s our Old Master.*

He was an evergreen tree, if ever there was one.

The Thunderbolt Saber King stared at Jeok with an expression that seemed to ask whether he was even human, then spoke.

“Jeok, do you feel even a little guilty?”

“Why should this old man feel guilty? When martial artists meet, they can have a little brawl. There were already people fighting when I entered the inn.”

“What would have happened if Great Hero Nangong hadn’t stepped in at the right moment?”

As the Thunderbolt Saber King said, the dove of peace who had brought the situation under control was the Azure Sky Sword King.

After a brief exchange with Jeok Cheongang, he had suffered a minor Internal Injury. He only appeared after settling his internal energy, and one of the Nangong Family members among the gathered heroes recognized him.

*Whoa, whoa, whoaaaa! Grand Family Head!*

It was a scream as though he had seen a ghost.

The other Murim practitioners, whose eyes had been blinded by the words *Dark Heaven*, finally returned to their senses as well.

There was even one lunatic who asked whether the Nangong Family was Dark Heaven, but fortunately, the members of our proud Murim Crusade managed to regain their sanity.

In truth, if Jeok Cheongang hadn’t Returned to Youth, at least a few people would have recognized him.

“That was almost a catastrophe!”

“I could have explained everything. And it happened because your eyes are as bad as a dog’s, you Peng bastard.”

“The inn collapsed! People were injured!”

“Ahem.”

Perhaps he felt a bit guilty himself. Jeok Cheongang cleared his throat, then opened his mouth with a shameless expression.

“It was the location, so this old man controlled his strength appropriately. At most, they were struck by a few pieces of falling debris. At that level, some spit would fix them right up. This old man will compensate the innkeeper sufficiently. Even I admit that the place burned rather badly.”

“Is that really coming from the man who killed a thousand members of the Demonic Cult because they burned down Mount Jiuhua? The more I listen, the more my chest swells.”

“Those bastards obviously had to die. They never intended to pay compensation in the first place.”

“…”

*What is this?*

It was completely unreasonable, yet it somehow felt strangely logical.

The Thunderbolt Saber King, momentarily left speechless, muttered,

“Returned to Youth only changed the skin you’re wearing. The contents are still the same. Your personality is still completely fucked.”

“You should try changing the skin on your face, Peng bastard. What kind of person grows old without even Returning to Youth?”

“What did you say?”

“Ho. They say a man who failed to Return to Youth gets angry when reminded of it. You’re a perfect example.”

“How dare you, Jeok!”

“Hm? What did you say? I can’t hear you. The words of an insignificant nobody who couldn’t even Return to Youth are hard to make out.”

*Would you look at him dealing some clean area-of-effect damage.*

Everyone else might have missed it, but I saw the Azure Sky Sword King’s shoulders twitch from his seat by the carriage window.

Then, as he stealthily avoided my gaze and looked out the window, his lips suddenly parted.

“You two should stop now.”

At first, I thought he was simply trying to change the subject.

Then I followed his gaze out the window and muttered,

“Yeah. You definitely should.”

At the end of my line of sight stood a long stretch of city walls and a massive crowd.

And above the iron gates was a huge sign bearing three characters written in a bold, soaring hand.

**Murim Alliance.**

[^1]: Yun Dong-ju was a Korean poet of the Japanese colonial period, known for poetry marked by intense sensitivity and introspection.
```
