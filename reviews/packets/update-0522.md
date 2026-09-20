<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0522.txt",
      "sha256": "42f73e63d36313e8d9b6061115b688e09676fff2020ebdea96efa00841a87e61",
      "bytes": 13403
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9516060be111d49f62c981442b10ab0b627b841b67ec7703bfd4c2574e449158",
      "bytes": 4461
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "64cd8fb4c8747cb48df6679f201570de17fee035b6ae67fc3809e0150ce53748",
      "bytes": 166781
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "27ab64f14cb0d105dc0c89621d41c5738298b817f0c1acfe1c9fa993a0eb39e6",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2ba76fa9465880a1bba5aa77ecc47d54988ce1736dde941080e710cfeda73ffc",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2c6b947b48b0a2802e1adf952f7c78cac6c161ef4abdeb10f776d1f697f7097f",
      "bytes": 1630
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "815716140f79b0a3b1fe5bcc3e05a965a3bb243c7d8106d876c92120fb7ebdf1",
      "bytes": 699
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "dbfcdfa613c6f3558dbc8a8fdb1fda85bde958987e8c340ea1acd0a15ed1645f",
      "bytes": 1062
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "87ea52d418b6a6604622677c9d1b3b46f4a5fe1c5da942b8f357c48b8d4ea227",
      "bytes": 680
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "795a31a19f07402740f09f028708913625a39fb2dfc930a188b35f04b5e58398",
      "bytes": 157699
    }
  ],
  "estimated_tokens": 11815
}
-->

# Durable State Update — Chapter 522

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 522. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 522. Profile updates may replace only one
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
  "chapter": 522,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 522,
    "continuity_sources": [522],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he entered a new realm, achieved Returned to Youth, and began his long-promised duel with Nangong Cheon, the Azure Sky Sword King.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; he is training Taekyung to control the violent internal energy produced by the Fire Gate Divine Technique.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but its permanence and repeatability remain unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "Mae Jonghak remains the New Murim Alliance's administrator after Jeok Cheongang refused the Alliance Leader position because it was troublesome; Mae accepts the burden because someone must do it.",
    "Song Ho is the reinstated Chief of the Hidden Shadow Pavilion and commands a vetted intelligence network, including five concealed agents whom Taekyung detected inside the Alliance.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "A Heaven Grade emergency report from Wudang depicts a monster connected to but distinct from the Water God Dragon."
  ],
  "continuity_sources": [
    521,
    520
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "How will the New Murim Alliance proceed with Mae Jonghak still administering it after Jeok Cheongang refused the Alliance Leader position?",
    "What monster is depicted in Wudang's emergency report, and how is it related to the Water God Dragon?"
  ],
  "safe_through": 521,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, 시주 as Benefactor, 계율원주 as Discipline Hall Master, 십이지파 as Twelve Sects of the Demonic Cult, 모용세가 as Murong Family, 요녕 as Liaoning, 진돗개 하나 as Jindotgae One, 소하문 as Xiao He Gate, 장충도 as Long Serpent Saber, 방가 as Fang Family, 월미도 as Moon Beauty Saber, 검기상인 as the level of injuring others with Sword Energy, 내성 as Inner City, 맹주부 as Alliance Leader's Office, 은잠술 as concealment technique, 식경 as half an hour, 지(地)급 as Earth Grade, and 천(天)급 as Heaven Grade."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 무당파    | **Wudang**                       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 가주     | **Family Head**                              |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 지능               | **Intelligence**               |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 하남     | **Henan**              |
| 무당산    | **Mount Wudang**       |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 오크 | **Orc** | Monster species. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 혈어 | **Blood Fish** | Local name for the aggressive mutated fish in the Gate's waterways. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 적천강 | 창천검왕 | long-standing martial rival and duel partner | Azure Sky Sword King | blunt and familiar | Explicitly names him while coming to fulfill their long-delayed duel promise. |
| 창천검왕 | 적천강 | long-standing martial rival and duel partner | Fire King | formal and familiar | Addresses Jeok Cheongang by title while welcoming the promised duel. |
| 창천검왕 | 벽력도왕 | Ten Kings peers | Sir Peng | formal but familiar | Tells Peng to calm himself after Peng's argument with Taekyung. |
| 벽력도왕 | 창천검왕 | Ten Kings peers | Great Hero Nangong | respectful and familiar | Addresses Nangong Cheon while crediting him with preventing a catastrophe. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 521
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 520
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 521
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 517
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 521
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; he is the New Murim Alliance's sole identified suitable candidate for Alliance Leader and currently handles its administrative affairs.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 521
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

## Korean source

```text
＃522화



씨벌. 산 넘어 산이네.

뒤통수를 거하게 얻어맞은 기분이다.

세상 어디에도 절대라는 것은 없지만, 그래도 호북에서의 일은 잘 마무리되었다고 생각했는데…….

‘마력의 영향을 받은 건, 수신룡뿐만이 아니었어.’

다른 곳에서 게이트가 열렸나? 아니면 수신룡이 완전히 흡수하지 못했던 마력이 새어 나가 또 다른 무언가에게 영향을 준 걸까?

그림을 보고 있자니 모래를 씹은 것처럼 입 안이 까끌거린다.

사태의 심각성을 인지한 것은 나 혼자만이 아니었다.

“저게, 도대체 뭐지?”

“한 가지는 확실한 것 같구려. 사람이라 부를 수 없는 무언가라는 것.”

벽력도왕과 창천검왕. 두 노고수의 뇌까림에 매종학이 입을 열었다.

“무당파에서 알려온 바에 의하면, 저 괴이한 존재가 근래에 호북에서 흉성을 떨치던 살귀(殺鬼)의 정체라고 했소.”

“살귀?”

미간을 좁힌 적천강의 시선이 이쪽을 향한다. 눈빛의 의미를 알아차린 내가 고개를 끄덕였다.

“알고 계신 그놈이 맞을 겁니다.”

“염병할. 등잔 밑이 어둡다더니.”

맞다. 저 말 그대로 등하불명(燈下不明)이다.

하지만 이 경우에는 못 알아볼 수밖에 없었다. 등잔의 불빛이 너무 밝아 눈도 제대로 뜨지 못했기 때문이다.

당장 호북성 곳곳에서 수백여 명이 죽어 나가고 있는데, 이미 무당파가 쫓고 있는 살귀에게 관심을 기울이는 것이 오히려 이상한 일이다.

마침내 드러난 흉수의 정체가 마력에 미쳐 버린 이무기일 경우에는 더더욱 그럴 수밖에 없다.

‘거기까지 신경 쓸 틈이 없었어.’

또 다른 괴물, 그래. 몬스터(Monster)가 나타났을 거라고는 미처 생각하지 못했다.

내가 짐작하고 있던 살귀의 정체는 무림에서 흔히 보이는 미친놈, 그 이상도 이하도 아니었으니까.

‘그나저나 이놈. 도대체 무슨 몬스터지?’

이 시대의 그림이라고 해 봤자 역사 교과서에서나 보던 딱 그 정도다. 죽간에 그려진 그림도 마찬가지였다.

그나마 최대한 사실에 가깝게 그리려고 노력한 흔적이 보이긴 했지만, 입체감을 포함한 여러 가지 부분에서 확연히 부족했다.

그림을 통해 알아볼 수 있는 것이라고는 딱 한 가지.

창천검왕의 말처럼 인간이 아닌 또 다른 존재라는 것뿐이다.

이마 한가운데에 삐죽 솟은 뿔이나 비상식적으로 길고 두꺼운 팔과 다리.

유일하게 색이 들어간 붉은 눈은 사마외도(邪魔外道)라는 네 글자로 설명할 수 있는 종류가 아니었다.

‘몬스터는 확실한데. 수신룡처럼 마력에 의해 변이된 건가?’

타닥. 탁.

초조하게 손가락으로 벽면을 두드리던 내가 물었다.

“다른 그림은 없습니까?”

나를 유심히 주시하고 있던 천면호리가 고개를 끄덕였다.

“유감스럽게도, 그렇다네. 무당파로서도 그것이 최선이었어.”

“그건 좀 아쉽네요. 하지만 이게 전부는 아닐 것 같은데.”

“눈치가 빠르군. 이틀 전, 무당파로부터 두 번째 서신이 도착했네.”

천면호리의 눈짓에 중년의 문사가 또다시 고리를 잡아당겼다.

쉬잉, 텅!

둥그런 관을 타고 내려온 타원형의 목갑. 그 안에서 나온 것은 빽빽한 글자가 적힌 한 통의 서신이었다.

“직접 읽어 보게. 자네는 호북에서 벌어진 사건의 중심에 있었으니, 나와 은영각이 파악하지 못한 무언가를 발견할 수도 있을 것 같으니.”

“안 그래도 그럴 생각이었습니다.”

“노부도 어디 한 번 같이 읽어 보도록 하지.”

나와 적천강은 머리를 맞대고 서신을 읽어 내려갔다.

한 번으로도 부족할 것 같아 두 번, 세 번을 읽었고 일각이 흐른 뒤에야 서신에서 눈을 뗐다.

“어떻습니까?”

천면호리의 질문에 적천강이 눈살을 찌푸렸다.

“글쎄.”

“그렇군요.”

“……왜 더 안 물어보나?”

그거야 처음부터 별 기대도 안 했으니까 그렇지.

하지만 딱히 할 말이 없는 것은 나도 마찬가지였다. 서신에 적힌 내용대로라면, 이미 천면호리와 은영각은 저 괴물이 나타나게 된 정황을 어느 정도 포착해 냈을 테니까.

“서신을 보았으니 알겠지만, 이 괴물은 본래 장강 하구에 살고 있던 어부였네.”

나는 서신의 첫 줄에 적힌 내용을 가리키며 말을 받았다.

“이름은 장삼. 나이는 오십 대에 가정도 있다고 적혀 있네요.”

무당파에서도 이런 괴물이 하늘에서 뚝 떨어졌다고는 생각하지 않았다.

그들은 죽은 몬스터의 사체의 면밀하게 살핀 끝에 여러 가지 특징을 발견했다.

그리고 곧장 이를 바탕으로 조사에 착수했고 괴물의 정체가 무당산에서 불과 백 리도 떨어져 있지 않은 마을에 살던 어부임을 밝혀 냈다.

“한 달도 전에 홀로 뱃일을 하러 나갔다가 자취를 감추었다더군. 여러 시일이 지나도록 모습을 드러내지 않자 그의 자식들이 관아에 청을 넣었지.”

관아로서도 그를 찾지 못했을 것이다.

어부들의 죽음은 흔하진 않아도 종종 있는 일이었고, 그때의 호북성은 잇따른 여러 사건으로 공포와 혼란에 잠겨 있었으니까.

당장 이곳저곳에서 지체 높으신 분들도 어느 협곡의 미니언마냥 픽픽 죽어 나가는 마당에 어부 따위 신경이나 썼겠는가.

‘어차피 적극적으로 찾으려고 했어도 불가능했겠지만.’

무당파의 고수들도 장삼을 잡기 위해 적지 않은 시일을 소모해야 했다. 이런 상황에서 관아가 나섰다 한들 성과는 없었을 것이다.

그리고 사실 그런 사정보다 더욱 주목해야 하는 것은, 흔하디흔한 장삼이사(張三李四) 중 하나였던 초로의 어부가 어쩌다 흉측한 괴물이 되어 살귀라 불렸냐는 거다.

“이렇게 된 원인에 대해 짐작 가는 바가 있나?”

천면호리의 물음에 내가 입을 열었다.

“아무래도 혈어(血魚)가 가장 유력하지 않을까 싶습니다.”

“혈어에 관해서는 이미 보고를 들었지. 안 그래도 이미 은영각의 요원 몇을 호북으로 파견하여 살아 있는 혈어를 포획하라고 지시해두었네.”

“잘하셨네요. 몬, 아니 괴물이 된 장삼은 본래 어부였고 동정호와 장강의 지류는 이어져 있으니까…….”

가만히 듣고 있던 매종학이 고개를 중얼거렸다.

“그 지류를 타고 흘러나간 혈어를, 장삼이 먹었을 가능성도 있겠군.”

“혹은, 먹혔거나요.”

“……!”

“……!”

“어쨌건 지금으로서는 그랬을 가능성이 가장 크다고 봅니다. 흉측해진 외관이나, 무당파의 추적을 며칠이나 피할 수 있었던 이유는 그로 인해 강해졌기 때문이겠죠.”

그때, 천면호리가 굳은 얼굴로 덧붙였다.

“자네가 쓰러트린 그 이무기처럼, 다른 곳에서 같은 일이 일어났을 가능성은 어찌 보나? ‘균열’이라 부르는 그것 말일세.”

“…….”

“말해 보게. 자네에게 직접 듣고 싶었네.”

이쪽의 표현으로는 균열. 다른 말로는 게이트.

이에 관해서는 나로서도 생각해보지 않은 것이 아니다.

하지만 그런 상황이 벌어지는 건 생각하는 것도, 입에 담기도 싫다.

미신 같은 걸 믿는 건 아니지만 말이 씨가 된다고, 일말의 가능성조차 배제하고 싶은 게 솔직한 마음이니까.

그렇다고 대답을 회피할 수는 없는 법. 나는 껄끄러운 표정으로 입을 열었다.

“확신할 수는 없지만, 생각하신 부분에 대해서는 아무래도 가능성이 희박하다고 생각합니다.”

“그 이유는?”

“같은 일이 일어났다면, 고작 이 정도로는 안 끝났을 테니까요.”

두 번째 게이트는 아직 터지지 않았다. 그게 내 결론이다.

그건 분명 안도해야 하는 일이었지만, 나를 포함하여 이미 사정을 아는 몇몇 사람들의 표정은 밝지 않았다.

내 말에 담긴 진정한 의미를 깨달았기 때문일 것이다.

쉽게 말하자면 이거다.

안 터져서 그렇지, 게이트 또 터지면 진짜 좆 된다.

“화약고. 실로 화약고가 따로 없군.”

천면호리의 입술 사이로 흘러나온 중얼거림.

화약고는 불이 닿지 않는 이상 안전하다. 하지만 그건 누군가 불을 붙이기만 한다면 어느 것보다 위험하다는 뜻도 된다.

세상에 어떤 미친놈이 그런 짓을 벌일까 싶지만, 유감스럽게도 암천이라는 미친놈들은 이미 한 번 호북성의 화약고에 불을 붙였다.

현재의 무림은 터지기 직전의 거대한 화약고나 마찬가지다.

그리고 두 번째, 세 번째 게이트가 바로 화약고를 터트릴 거대한 불씨가 될 것이다.

‘그나마 다행인 점이 한 가지는 있지.’

천주라는 놈의 진짜 정체가 무엇인지. 남천마후가 어떤 방법으로 게이트를 열었는지는 나도 모르겠다.

하지만 한 가지는 짐작할 수 있었다.

‘게이트를 여는 일이, 놈들에게도 그리 쉬운 일이 아니라는 것.’

게이트가 무슨 객잔 대문도 아니고. 놈들이 원하는 대로 휙휙 열어젖혔다면 이미 천하 무림이 개판 오 분 전이 되고도 남았을 것이다.

오크가 문파를 세우고, 라이칸스로프와 오우거가 어깨동무하고 하남 대로변을 돌아다니고 있었겠지.

무림맹이 결성되기도 전에 어어, 씨발 저것들 뭐여. 하다가 사분오열되는 거다.

하지만 암천은 그러지 않았다.

왜? 어려우니까.

그래서 더욱 서둘러야 한다. 또 다른 화약고가 터지기 전에 놈들을 저지해야 했다.

그리고 두 번째 다행인 점은, 무림맹이라는 깃발 아래에 하나로 뭉친 이 거대한 집단에는 그럴 만한 역량이 충분하다는 것이다.

“……무림에 환란이 닥쳤군. 생각했던 것 이상으로 훨씬 거대한.”

탄식처럼 중얼거리는 매종학을 향해 천면호리가 딱딱하게 굳은 얼굴로 입을 열었다.

“당장 알아봐야 할 것이 있습니다. 맹주, 송구스럽지만 다른 분들과 함께 다른 곳으로 자리를 옮기시겠습니까?”

“그리하겠소.”

“존명. 추후 보고 올리겠습니다. 그럼 모두 다음 기회에 뵙지요.”

천면호리의 말은 그것이 마지막이었다.

전각을 빠져나가기도 전에 다급한 외침이 곳곳에서 울려 퍼졌고, 피로에 찌들어 있던 사람들은 언제 그랬냐는 듯 눈을 부릅뜨며 지시에 따라 움직이기 시작했다.

무림맹 해체 후에도 그 명맥을 이어가고 있던 은영각(隱映閣)이 다시금 움직이기 시작한 것이다.

그리고 바빠지는 것은 저들뿐만이 아니었다.

“나도 가 보아야겠소. 곧 밀려들 일이 산더미라.”

매종학의 말에 창천검왕이 고개를 끄덕였다.

“본인 역시 마찬가지요. 혹 내 못난 자식놈에게 오늘 이곳에서 들은 이야기를 들려주어도 괜찮겠소?”

“그대들을 이곳으로 데려온 사람이 누구인지 잊었나 보구려.”

아무에게도 알려 주어서는 안 될 기밀이었다면, 무림맹주와 은영각주가 앞장서서 데려오는 일 역시 없었을 것이다.

매종학이 한 말에 담긴 뜻을 알아들은 창천검왕이 포권을 취했다.

“고맙소.”

“며칠 후면 알게 될 이야기요. 단, 그때까지는 새어 나가지 않게 조심해 주시오.”

“물론이오. 명심하리다.”

벽력도왕 역시 사태의 심각성을 파악했는지, 딱딱하게 굳은 얼굴로 입을 열었다.

“이보게, 검성. 나도 물어보고 싶은 것이 있네만.”

“하북팽가 역시 마찬가지요. 알려 주어도 상관 없…….”

“아니, 그거 말고. 저 안에서 도대체 무슨 이야기들을 한 건가?”

“…….”

“…….”

하북팽가 태상가주 지능 수준 실화냐. 대흉근이 웅장해진다…….

나를 포함한 모두가 짜게 식은 눈빛을 보내자, 벽력도왕이 변명처럼 웅얼거렸다.

“도대체가 알아들을 수 있는 이야기들을 해야지. 무림에 큰 환락이 닥친 건 나도 알겠는데…….”

“팽가야.”

“응.”

“그럼 좀 닥치고 있어라. 노부가 보기에는 그게 돕는거다.”

“무어라!”

벽력도왕을 향해 한숨을 푹 내쉰 적천강이 매종학을 응시했다.

“이 멍청한 노인네는 노부가 맡을 테니, 어서 가시오. 바쁠 텐데.”

“고맙소. 그나저나 적 대협.”

“말씀하시오.”

매종학이 적천강의 손을 꼭 붙들고 말을 이었다.

“정말 맹주 하실 생각 없소?”

“…….”

“…….”

솔직히 말해 봐. 당신 청풍이랑 한 핏줄이지.
```

## Final English reading copy

```markdown
# Chapter 522

“Fuck. It’s one problem after another.”

It felt like I had been struck hard in the back of the head.

Nothing in this world was absolute, but I had still thought the events in Hubei had been wrapped up properly…

*The Water God Dragon wasn’t the only thing affected by mana.*

Had another Gate opened somewhere else? Or had some of the mana the Water God Dragon failed to absorb leaked out and affected something else?

Looking at the picture made my mouth feel gritty, as if I were chewing sand.

I was not the only one who understood how serious the situation was.

“What in the world is that?”

“One thing seems certain. It is something that cannot be called human.”

The Thunderbolt Saber King and the Azure Sky Sword King muttered to themselves. Mae Jonghak then opened his mouth.

“According to what Wudang told us, that bizarre existence is the true identity of the Killing Ghost that had been spreading terror across Hubei recently.”

“The Killing Ghost?”

Jeok Cheongang narrowed his brow and looked in my direction. I understood the meaning in his eyes and nodded.

“It’s probably the one you know.”

“Damn it. They say it’s darkest beneath the lamp.”

He was right. This was exactly what they meant by darkness beneath the lamp.

But in this case, we could not have recognized it. The lamp had been so bright that we could barely open our eyes.

With hundreds of people dying all over Hubei Province, it would actually have been strange to focus on the Killing Ghost already being pursued by Wudang.

That was even more true when the culprit finally revealed was an imugi driven mad by mana.

*We didn’t have time to worry about anything else.*

I had never imagined that another monster would appear. I had assumed the Killing Ghost was nothing more or less than the sort of lunatic commonly found in the Murim.

*Come to think of it, what kind of monster is this bastard?*

The pictures from this era were exactly the sort of crude drawings one saw in history textbooks. The same was true of the picture drawn on the bamboo slip.

There were signs that someone had tried to depict it as accurately as possible, but it was obviously lacking in many ways, including any sense of depth.

There was only one thing we could determine from the picture.

Just as the Azure Sky Sword King had said, it was another existence that was not human.

The horn jutting from the center of its forehead. Its arms and legs, absurdly long and thick.

Its red eyes were the only part drawn in color, and they were beyond anything the four words *demonic, heterodox arts* could explain.

*It’s definitely a monster. But was it mutated by mana, like the Water God Dragon?*

Tap. Tap.

I had been anxiously drumming my fingers against the wall when I asked,

“Are there any other pictures?”

The Thousand-Faced Fox, who had been watching me closely, nodded.

“Unfortunately, there are not. That was the best Wudang could do.”

“That’s a shame. But I don’t think this is everything.”

“You’re quick. A second letter arrived from Wudang two days ago.”

At the Thousand-Faced Fox’s signal, the middle-aged scholar pulled on the ring again.

Whoosh—thunk!

An oval wooden case came sliding down through the round tube. Inside was a letter covered in densely packed writing.

“Read it yourself. You were at the center of the incident in Hubei, so you may notice something that I and the Hidden Shadow Pavilion failed to discover.”

“I was planning to do that anyway.”

“This old man will read it with you.”

Jeok Cheongang and I put our heads together and read through the letter.

Once did not seem sufficient, so we read it a second time, then a third. Only after fifteen minutes had passed did we finally take our eyes off the letter.

“What do you think?”

At the Thousand-Faced Fox’s question, Jeok Cheongang furrowed his brow.

“Who knows?”

“I see.”

“…Why aren’t you asking anything else?”

Because you never expected much in the first place.

But I had nothing particularly useful to say either. If the letter contained everything it claimed to, then the Thousand-Faced Fox and the Hidden Shadow Pavilion had already managed to uncover most of the circumstances that led to the monster’s appearance.

“As you can tell from the letter, this monster was originally a fisherman who lived at the mouth of the Yangtze.”

I pointed to the first line of the letter and continued.

“It says his name was Jang Sam, that he was in his fifties, and that he had a family.”

Wudang had not thought that a monster like this had simply fallen from the sky.

After carefully examining the corpse of the dead monster, they had discovered several distinguishing features.

They immediately began an investigation based on those findings and determined that the monster had been a fisherman who lived in a village less than a hundred li from Mount Wudang.

“They say he went out alone to fish more than a month ago and vanished without a trace. When he failed to return after several days, his children petitioned the local authorities.”

The local authorities probably had not been able to find him either.

Fishermen dying was not common, but it did happen from time to time. Besides, Hubei Province had been drowning in fear and chaos because of the succession of disasters.

With high-ranking people dropping dead here and there like minions in some canyon, who would have spared any thought for a mere fisherman?

*Even if they had actively searched for him, they probably couldn’t have found him.*

Even Wudang’s masters had needed quite some time to capture Jang Sam. Under those circumstances, the local authorities would have accomplished nothing even if they had joined the search.

And in truth, there was something far more important than those circumstances.

How had an aging fisherman, once as ordinary as they came, become a hideous monster known as the Killing Ghost?

“Do you have any idea what caused this?”

At the Thousand-Faced Fox’s question, I opened my mouth.

“I think the Blood Fish is the most likely culprit.”

“I have already received a report regarding the Blood Fish. In fact, I have dispatched several Hidden Shadow Pavilion agents to Hubei and ordered them to capture a live specimen.”

“Good call. Jang Sam, who became a mon—who became a monster, was originally a fisherman, and Dongting Lake is connected to the tributaries of the Yangtze…”

Mae Jonghak, who had been listening quietly, nodded and muttered,

“There is a chance Jang Sam ate one of the Blood Fish that flowed out through those tributaries.”

“Or was eaten by one.”

“……!”

“……!”

“In any case, that seems the most likely explanation for now. His hideous appearance, as well as his ability to evade Wudang’s pursuit for several days, was probably because the change made him stronger.”

The Thousand-Faced Fox added in a stiff voice,

“Just as the imugi you defeated appeared, what do you think of the possibility that the same thing occurred somewhere else? The phenomenon known as a ‘rift.’”

“…”

“Tell me. I wanted to hear it directly from you.”

In our terminology, it was a rift. In other words, a Gate.

I had thought about the possibility before.

But I did not want to think about such a situation, much less say it aloud.

I did not believe in superstitions, but people said that speaking of something could make it happen. If I was being honest, I wanted to rule out even the smallest possibility.

Still, I could not avoid answering. I opened my mouth with an uncomfortable expression.

“I can’t say for certain, but I think the possibility is fairly low.”

“Why?”

“If the same thing had happened, it wouldn’t have ended with something this minor.”

The second Gate had not erupted yet. That was my conclusion.

It was certainly something we should have been relieved about, but the expressions of several people who already knew the circumstances—including me—remained grim.

They must have realized the true meaning behind my words.

Put simply:

*It hasn’t happened yet. But if another Gate blows, we’re truly fucked.*

“A powder keg. There is no better way to describe it than a powder keg.”

The Thousand-Faced Fox muttered the words under his breath.

A powder keg was safe as long as no fire touched it. But that also meant it became more dangerous than anything else the moment someone set it alight.

You might wonder what kind of lunatic would do such a thing, but unfortunately, the lunatics known as Dark Heaven had already lit the powder keg that was Hubei Province once before.

The Murim of today was no different from a gigantic powder keg on the verge of exploding.

And the second and third Gates would be the enormous sparks that set it off.

*There is at least one thing we can be thankful for.*

I did not know the true identity of that bastard, the Lord of Heaven. I also did not know how the Southern Heaven Demon Empress had opened the Gate.

But there was one thing I could guess.

*Opening a Gate isn’t easy for them either.*

A Gate was not the front door of an inn. If they could fling them open whenever they wanted, the entire Murim would already have descended into complete chaos.

Orcs would have founded sects, while Lycanthropes and ogres would be walking arm in arm down the main roads of Henan.

Before the Murim Alliance could even be formed, everyone would be shouting, *Uh, fuck, what are those things?* Then we would have fallen apart completely.

But Dark Heaven had not done that.

Why?

Because it was difficult.

That was why we needed to hurry even more. We had to stop them before another powder keg exploded.

The second thing we could be thankful for was that this enormous group, united beneath the banner of the Murim Alliance, had more than enough ability to do so.

“A calamity has befallen the Murim. Something far more enormous than I imagined.”

Mae Jonghak muttered the words like a sigh. The Thousand-Faced Fox opened his mouth with a rigid expression.

“There is something we need to investigate immediately. Alliance Leader, I apologize, but would you move elsewhere with the others?”

“Of course.”

“Understood. I will report to you later. Then I will see you all next time.”

Those were the Thousand-Faced Fox’s final words.

Before we had even left the pavilion, urgent shouts rang out from every direction. The people who had been worn down by exhaustion opened their eyes wide as though they had never been tired and began moving according to their orders.

The Hidden Shadow Pavilion, which had maintained its existence even after the dissolution of the Murim Alliance, had begun moving once again.

And they were not the only ones who suddenly became busy.

“I should go as well. I’ll soon be buried under a mountain of work.”

At Mae Jonghak’s words, the Azure Sky Sword King nodded.

“I am in the same position. Would it be all right if I told my good-for-nothing son what I heard here today?”

“You seem to have forgotten who brought you here.”

If this had been classified information that could not be told to anyone, the Alliance Leader and the Chief of the Hidden Shadow Pavilion would never have brought them here themselves.

Understanding the meaning in Mae Jonghak’s words, the Azure Sky Sword King clasped his hands in a formal salute.

“Thank you.”

“It will be public knowledge in a few days. Until then, be careful not to let anything slip.”

“Of course. I will bear it in mind.”

The Thunderbolt Saber King seemed to have grasped the seriousness of the situation as well. He opened his mouth with a stiff expression.

“Hey, Sword Saint. There is something I would like to ask you, too.”

“The same goes for the Hebei Peng Family. It doesn’t matter if you tell them—”

“No, not that. What in the world did you talk about in there?”

“…”

“…”

*Is this really the Intelligence level of the Grand Family Head of the Hebei Peng Family? My pecs are getting majestic…*

When everyone, myself included, gave him a thoroughly cold look, the Thunderbolt Saber King mumbled as if making an excuse.

“You have to talk about things people can actually understand. I know a great pleasure has befallen the Murim, but…”

“Peng.”

“Yeah?”

“Then keep your mouth shut for a while. This old man thinks that would be helping.”

“What did you say?!”

Jeok Cheongang let out a deep sigh and looked at Mae Jonghak.

“I’ll take care of this stupid old man, so go on. You must be busy.”

“Thank you. By the way, Great Hero Jeok.”

“Speak.”

Mae Jonghak clasped Jeok Cheongang’s hand tightly and continued.

“Do you really have no intention of becoming the Alliance Leader?”

“…”

“…”

*Be honest. You and Cheongpung are related by blood, aren’t you?*
```
