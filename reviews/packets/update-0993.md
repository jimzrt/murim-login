<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0993.txt",
      "sha256": "62aa691fa3e2cff1c47c4f86f9339cd87290b85fbb593f572f6f3b9a07d112db",
      "bytes": 12656
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a661ff9b583a25fab78eb101805e334996b3d31c9b66ff002a311c1b7ce7a04b",
      "bytes": 1356
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "60c0f9e2555db00145e7bf3cbc2cd62bdeb21aaa35bdb6fe1fe86992c552acab",
      "bytes": 759
    },
    {
      "path": "characters/Heavenly Power Demon.md",
      "sha256": "75320a8671b98a2667342944fb67d7929f65fd404b22c4077c95c3920533bbe8",
      "bytes": 993
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "66d64522ac587be26316c29f43159ef0fe0dfeb98874ce4b69c65c49dd7d1dd7",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8fbcc1dd25b8f4f0b738dc3f7dba066fa4ce96570f669f029ab2c861c98180b0",
      "bytes": 1391
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "117bb56ae28b8dcb67d1e68a184a22679d8b03aa4cae450bf7bf2c09233bdd4a",
      "bytes": 1001
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bd5753e5df794eedf5b2ea27975a392475eb9bba5427ebd9beecb42050b7771b",
      "bytes": 273611
    }
  ],
  "estimated_tokens": 9934
}
-->

# Durable State Update — Chapter 993

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
1 and safe_through 993. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 993. Profile updates may replace only one
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
  "chapter": 993,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 993,
    "continuity_sources": [993],
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
    "Memories of the original Jin Taekyung appeared in Taekyung’s dream; whether some part of the original’s consciousness remains inside him is unresolved.",
    "Taekyung and Jeok Cheongang will discuss the consciousness mystery privately.",
    "The Bow Saint may know part of the truth about the chosen one; she is still in Hebei.",
    "Peng Cheolhu died after passing everything he had to Jin Taekyung through Transmitting Internal Energy Across the Body.",
    "Dark Heaven threatens the world, and the Eight Heavens Blood Calamity and Peng Cheolhu’s death have intensified mobilization against it.",
    "Unprecedented snowfall and rapidly changing heavenly patterns are occurring around the world.",
    "Cheongpung is in Qinghai with the Slaughter Saint."
  ],
  "continuity_sources": [
    991,
    992
  ],
  "open_questions": [
    "Does any part of the original Jin Taekyung’s consciousness remain inside Taekyung?",
    "What is behind the worldwide weather and heavenly-pattern changes?",
    "Is the upheaval a scheme laid by some unknown power, as Mae Jonghak suspects?",
    "What are Dark Heaven and the Lord of Heaven planning?",
    "What does the Bow Saint know about the chosen one, and will she discuss it with Taekyung?"
  ],
  "safe_through": 992,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 팽철후    | **Peng Cheolhu**   |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 삼성     | **Three Saints**    |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 팔천협    | **Eight Spring Gorge** |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 평화 | **Peace Guild** | Guild name. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 상단전 | **upper dantian** | Advanced dantian whose opening signifies entry into the Martial Extremity realm. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 격체전공 | **Transmitting Internal Energy Across the Body** | Technique for transferring internal energy between bodies. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 당주 | **Hall Master** | Murim Alliance office held by the envoy. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 팽철후 | longtime friends and rivals adopting brotherly terms | Jeok hyung | informal and familiar | Peng accepts Jeok as his older brother; Jeok offers to call him younger brother, though they reserve that address for a future reunion. |
| 팽철후 | 적천강 | longtime friends and rivals adopting brotherly terms | Jeok hyung | informal and familiar | Peng addresses Jeok as hyung in their final conversation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 992
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Heavenly Power Demon.md

# Heavenly Power Demon (천력마)

- **Safe through:** Chapter 987
- **Aliases:** None
- **Role:** The Heavenly Power Demon was a former Elder of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war before dying after passing his remaining internal energy to Jin Taekyung.
- **Personality:** Quiet and self-possessed despite his severe imprisonment, he is reflective about the moral ambiguity of the Great Faction War and disillusioned with the Divine Cult's corruption.
- **Voice:** Gruff and dry, with formal self-reference as 노부.
- **Relationships:** He was once an Elder and commander under the Great Heavenly Demon Divine Cult's Cult Leader, has spent more than forty years imprisoned by the Sichuan Tang Clan, and identifies the Western Heaven Demon Lord as one of the Divine Cult's four Protectors who served closest to and led astray the Cult Leader.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 992
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 992
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 992
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu was the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family who died as his accumulated internal energy and remaining life force melted into the flames of Taekyung’s advancement.
- **Personality:** Boisterous and teasing with old friends, yet calm and accepting in the face of death; willing to give everything he has left to protect the world.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** He was Jeok Cheongang’s long-standing rival and friend, Hong Dao’s close friend, protective toward Hong Dao’s Disciple Unnamed, father of Peng Cheolyeong, and longtime friend and former youthful rival of Murong Baek; Jeok and Peng parted reconciled as brothers in all but blood.

## Korean source

```text
＃993화



시스템 창 오픈.

마음속으로 그 짧은 명령어를 뇌까린 그 순간.

띠링. 띠링. 띠리링!

특유의 맑은 종소리와 함께, 마치 둑이 허물어지듯 무수한 홀로그램 창이 허공에서 쏟아져 내렸다.



- 돌발 퀘스트, [격체전공]을 성공적으로 완료했습니다!

- 퀘스트 보상이 지급됩니다!

- 당신의 [공력]이 비약적으로 상승합니다!

- 대량의 경험치를 획득했습니다!

- 20의 보너스 스탯 포인트를 획득했습니다!

- 레벨 업!

- [격체전공]은 성공확률이 매우 희박한, 그렇기에 이제는 그 어떤 무림인도 도전하지 않는 대법입니다. 이러한 과정을 두 번이나 성공시킨 당신의 인내와 대담함에 경의를 표합니다.

- 희귀한 업적, [이걸 두 번이나 하네. 이걸 두 번이나 하네.]를 달성하셨습니다.

- 업적 달성 보상이 지급됩니다!

- 대량의 경험치를 획득했습니다!

- 당신의 [인내]가 비약적으로 상승합니다!



가장 먼저 눈에 띈 것은 퀘스트 완료와 업적 달성을 알리는 시스템 메시지였다.

비록 실질적인 레벨 업은 한 번에 불과했지만, 격체전공의 성공으로 얻은 스탯 상승은 어마어마한 수준.

하지만 나는 빠르게 내용을 훑은 다음 손짓 한 번으로 십여 개의 메시지를 지웠다.

내가 확인해야 할 홀로그램 창은 이것으로 끝이 아니었으니까.



- [천력마(天力魔)]의 공력을 성공적으로 흡수했습니다!

- [벽력도왕(霹靂刀王)]의 공력을 성공적으로 흡수했습니다!

- [열양지기]의 성질이 변화합니다. 당신의 몸속 깊은 곳에서 새롭게 태어난 불길은 더욱 거세고 뜨겁게 타오를 것입니다!

- 대해(大海)을 정복한 자는 천하를 오시할 것이나, 하늘과 가장 가까운 산봉우리에 오른 이는 대해마저 굽어보리라.

- 축하합니다! [중단전]이 완전히 개방되었습니다!

- [등봉조극(登峰造極)]의 경지에 도달했습니다!

- 돌발 퀘스트, [환골탈태(換骨奪胎)]가 시작됩니다. 당신은 해당 퀘스트를 거부할 수 없습니다!

- 돌발 퀘스트, [환골탈태]를 성공적으로 완료했습니다!

- 기의 수발이 매우 자유로워집니다. 그 자체로 완벽해진 근골은 탁기(濁氣)마저 거부합니다!

- 위대한 업적, [전신성형]을 달성했습니다!

- 퀘스트 완료 및 업적 달성 보상이 지급됩니다!

- 모든 능력치가 크게 향상됩니다! 자세한 세부 사항은 [상태창]을 열어 확인할 수 있습니다.

- 30의 보너스 스탯 포인트를 획득했습니다!

- 대량의 경험치와 명성을 획득했습니다!

- 레벨 업!



줄줄이 쏟아지는 홀로그램 창들을 확인하며, 머릿속에 떠오른 생각은 단 하나뿐이었다.

‘이런 미친.’

물론 막대한 보상이 기다리고 있을 거라는 사실은 나로서도 충분히 짐작하고 있었다.

벽력도왕 팽철후.

한 시대를 풍미했던 거인이 얼마 남지 않은 생명을 대가로 내게 건네준 힘은, 그만큼 순수하면서도 거대한 것이었으니까.

하지만 그럼에도 시스템이 전한 보상 목록은 예상했던 범위를 훌쩍 뛰어넘는 것이었다.

두 번의 레벨 업과 추가로 주어진 막대한 보너스 포인트. 거기에 더해 전체적인 능력치 향상까지.

‘능력치 향상 정도는 세부 내용을 확인해 봐야겠지만, 그렇다고 해도 이걸 다 합친다면…….’

단번에 10레벨 이상을 올렸다고 해도 과언이 아니다.

아니, 실제로는 그보다도 훨씬 낫다.

강해지는 만큼 레벨 업 역시 요원해지던 상황.

레벨은 높아질수록 필요 경험치가 기하급수적으로 올라가지만, 이번에 보상으로 얻은 엄청난 양의 스탯 포인트는 말 그대로 보너스였으니까.

‘빚을 졌군. 그것도 엄청나게 많은 빚을.’

엄청난 보상을 얻었음에도 마음이 복잡하다.

나는 기쁨과 씁쓸함에 휩싸인 채, 당신의 모든 것을 전해 주겠노라 말하며 환하게 웃던 벽력도왕의 모습을 떠올렸다.

온 산의 국화밭이 붉게 물들고 말과 사람의 시체가 산처럼 쌓였던 그 날, 팔천협(八天峽)에서 쓰러져가던 무수한 희생자들도 함께.

그와 동시에 가슴 깊이 새겼다.

지금 내게 주어진 이 막대한 보상들은, 죽은 이들의 목숨값이라는 사실을.

‘이 빚은…… 반드시 갚는다.’

그리 유복한 삶을 살아오지 못했던 내게 있어 빚은 늘 지긋지긋한 의미였지만, 이번만큼은 아니다.

나 역시 그들과 같은 곳을 바라보고 있었으니까.

이 빚을 전부 청산하는 그 날, 모두가 바라는 평화가 찾아올 테니까.

그리고 그러기 위해서는, 어떠한 고난과 역경이 찾아오더라도 인내하고 극복해야만 했다.

슬픔에 주저앉거나 현재에 만족하지 않고 계속해서, 포기 따위는 잊은 채로 높은 곳을 향해 나아가야 했다.

격체전공을 이루는 과정 속에서 똑똑히 보았던, 짙은 뭉게구름에 가려진 그곳으로.

봉우리 위의 하늘로.

‘그래, 상단전(上丹田).’

물론 결코 쉽게 이룰 수 없는 일이라는 것쯤은 나도 안다.

중원 최고의 고수들인 삼성(三星)도, 그런 그들과 어깨를 나란히 하는 적천강도 상단전이 열린 상태인지는 확신할 수 없는 상황이었으니까.

‘아니, 설령 이미 그 단계에 도달했다 하더라도 저마다의 격차는 엄연히 존재하겠지.’

모든 것에는 순서가 있는 법.

나는 비좁은 개울을 넓혀 드넓은 대해로 만들었고, 구름을 찌를 듯이 높게 솟아오른 산봉우리를 올라야 했다.

지금까지는 뜻하지 않게 얻은 시스템과 수많은 기연(奇緣) 덕분에 가공할 만한 속도로 성장했지만, 그런 나조차도 구름에 가로막혀 나아가지 못했다.

저 구름 위에서, 하계(下界)를 굽어보던 절대자들에게는 미치지 못했다.

‘만약, 그때 기세를 몰아 계속해서 몰아붙였더라면 어땠을까.’

문득 머릿속을 스친 아쉬움.

그러나 그에 대한 답은 이미 알고 있는 것이나 다름없었다.

‘실패했겠지. 그것도 아주 높은 확률로.’

그 당시의 상황에서 상단전을 뚫으려 했다면 그건 도전이 아니라 도박이다.

중단전을 완전히 개방하고 극도의 고양감을 느끼고 있던 나조차도, 본능적으로 용기와 만용(蠻勇)의 차이를 깨닫고 물러나지 않았었나.

돌이켜볼수록 뭐라 형용할 수 없을 정도로 아쉽지만, 냉정하게 생각하면 아주 좋은 판단…….

‘잠깐.’

도대체 무엇일까. 이 기분은.

나는 불현듯 미간을 좁힌 채 떠올렸다.

엄청난 격통을 수반했던 격체전공의 과정과 내 것이 아닌 기억으로 비롯된 이상한 꿈을.

하지만 그것이 전부가 아니었다.

이 순간 전신을 엄습해 오는 알 수 없는 기시감은, 그 사이 어딘가에 맞물려 깎여 나간 기억의 흔적을 알려 주고 있었다.

“판단. 좋은 판단…… 분명 어디에서 들었는데.”

나도 모르게 저절로 달싹이는 입술. 그 사이로 흘러나오는 목소리가 남의 것처럼 낯설다.

그렇게 어느 정도의 시간이 흘렀을까.

무언가에 홀린 사람처럼 텅 빈 허공을 바라보며 같은 말을 뇌까리던 나는, 이내 머릿속에서 잊혀졌던 기억의 일부를 되찾을 수 있었다.

‘분명 누군가가 비슷한 말을 했었어. 현실이 아니라, 내 의식 속에서.’

깜빡이는 것조차 잊은 눈동자가 따끔거린다.

제법 긴 시간이 흐른 탓인지, 고심에 고심을 거듭한 머리가 뜨겁게 달아올랐다.

아니, 어느새 보이지 않은 작은 송곳이 머릿속을 천천히 파고들고 있었다.

서서히 번져 오는 두통.

하지만 나는 고통으로 인해 눈살을 찌푸리면서도, 계속해서 뇌리를 헤집었다. 다른 커다란 기억들에 가려진 자그마한 조각을 찾아 어둠 속을 헤맸다.

그리고 마침내.

기억해 냈다.

아직은 때가 아님을 깨닫고, 구름 너머의 상단전을 뒤로 한 채 돌아서던 그때의 나를.

이내 무아(無我)의 세계로 빠져들던 내 귓가로 아스라이 울려 퍼지던 누군가의 한 마디를.



‘좋은 판단이다. 그때처럼.’



“……!”

그 순간, 나도 모르는 사이에 눈이 부릅떠졌다.

목소리의 주인이 누구인지 깨달아서?

틀렸다.

불현듯 엄습해 온, 어마어마한 격통 때문이었다.

흡.

생각지도 못한 통증을 느낀 나는 본능적으로 숨을 삼켰다. 이를 악무는 것으로도 모자라 두 눈을 질끈 감았다.

보이지 않는 송곳처럼 조금씩 머리를 파고들던 두통은, 어느덧 약왕당주가 애병처럼 들고 다니는 대침만큼이나 거대해진 채로 머릿속을 들쑤시고 있었다.

‘이게 무슨……!’

새하얗게 물든 시야 속, 나는 익사 직전의 위기에 처한 사람처럼 사지를 허우적거렸다.

그러나 이러한 상황 속에서도 단 한 가지, 아직 해결되지 않은 뇌리의 의문만큼은 내려놓지 않았다.

마지막 순간, 환청처럼 울려 퍼진 그 목소리의 주인은 누구인가.

도대체 누구이길래, 현실이 아닌 심상의 공간에서 내게 말을 걸 수 있었는가.

‘어떻게, 도대체 어떻게 그럴 수 있었지?’

한 가지만큼은 확신할 수 있다.

그 순간 들었던 목소리는, 적천강의 것도 아니었고 벽력도왕은 더더욱 아니었다.

그리고 그 두 명의 노강호를 제외한다면, 그때의 내게 의사를 전달할 수 있는 이는 아무도 없었다.

‘그렇다면 누가.’

진심으로 궁금했다. 머릿속이 찢어지는 듯한 고통을 느끼고 있는 와중에도 알고 싶었다.

그 목소리의 주인이 누구이며, 어찌 우리 모두의 이목을 속이며 다가와 내게 속삭일 수 있었는지.

동시에 묻고 싶었다.

당신은 어찌 나를 알고 있었느냐고.

‘그때처럼……이라고 했다. 분명히.’

틀림없다.

나는 그를 모르지만, 그는 나를 알고 있다.

대관절 언제, 어디에서 마주쳤는지는 몰라도 우리의 만남은 오늘이 처음이 아니었다.

하지만…….

‘왜 아무런 기억도 나지 않는 거지? 왜?’

말에 담긴 내용만 기억날 뿐. 목소리의 높낮이와 굵기는 물론 성별조차 구분할 수 없었다.

나는 그가 여인인지, 사내인지. 만약 사내라면 청년과 노인 어디 즈음에 머무르고 있는지조차 짐작하지 못했다.

그저 어렴풋이 기억나는 것이라고는, 끔찍한 두통을 인내하며 대가로 얻어낸 그 순간의 감각뿐이었다.

‘왠지 모를 익숙함.’

난생처음 듣는 것처럼 생소한 동시에, 묘한 낯익음이 어렴풋이 떠오른다.

그리고 그것이, 내가 얻어낼 수 있는 전부였다.

화악!

섬광이 폭발한다. 새하얗게 물들어 있던 시야가 서서히 걷히더니, 흐릿하던 눈동자에 초점이 돌아오기 시작했다.

“……아.”

참았던 숨을 토해 낸 나는, 영원히 이어질 것만 같던 고통의 시간이 마침내 끝났다는 것을 깨달았다.

그 고통과 함께, 내게 허락된 기억 또한 한계를 맞이했다는 사실도.

‘빌어먹을.’

나는 고통의 잔재로 파르르 떨리는 손끝을 말없이 바라보다, 이내 힘주어 그러쥐었다.

으득.

환골탈태까지 거치며 이제는 철피(鐵皮)나 다름없어진 손바닥의 피부와 날카로운 손톱이 팽팽하게 맞물린다.

이상하리만치 요동치는 감정에 힘입은 탓일까.

몸 안에 잠들어 있던 거대한 기운이 들끓어 오르던 바로 그 순간이었다.

띠링.



- 새로운 퀘스트, [알 수 없는 목소리]가 생성되었습니다.

- 당신은 해당 퀘스트의 승낙 여부를 결정할 수 없습니다.

- 퀘스트가 강제 진행됩니다.

- 새롭게 갱신된 퀘스트 정보를 확인하시겠습니까?



알 수 없는 목소리.

홀로그램 창에 적힌 퀘스트의 제목을 바라보던 나는, 굳게 닫혀 있던 입술을 열었다.

“예.”
```

## Final English reading copy

```markdown
# Chapter 993

*Open System window.*

The moment I muttered that short command in my mind—

Ding. Ding. Diiiing!

A familiar, clear chime rang out, and countless holographic windows poured from the air as if a dam had burst.



> **System**
> Sudden Quest, **Transmitting Internal Energy Across the Body**, completed successfully!
>
> Quest rewards have been issued!
>
> Your **internal energy** has increased dramatically!
>
> You have gained a large amount of **EXP**!
>
> You have received 20 bonus stat points!
>
> Level up!
>
> **Transmitting Internal Energy Across the Body** is a technique with such a low chance of success that no martial artist dares attempt it anymore. We commend your patience and audacity in succeeding at the process twice.
>
> You have earned the rare achievement **You Did That Twice. You Did That Twice.**
>
> Achievement rewards have been issued!
>
> You have gained a large amount of **EXP**!
>
> Your **Endurance** has increased dramatically!



The first things that caught my eye were the System messages announcing the completed Quest and earned achievement.

I’d only leveled up once, but the stat increase from successfully completing Transmitting Internal Energy Across the Body was enormous.

I quickly skimmed the messages, then erased a dozen or so with a single wave of my hand.

There were still more holographic windows I needed to check.



> **System**
> Successfully absorbed the internal energy of the **Heavenly Power Demon**!
>
> Successfully absorbed the internal energy of the **Thunderbolt Saber King**!
>
> The nature of **Scorching Yang Qi** is changing. The new flame born deep within your body will burn fiercer and hotter than ever!
>
> He who conquers the great sea will look down upon the world, but he who climbs the peak closest to heaven will look down even upon the great sea.
>
> Congratulations! Your **Middle Dantian** has been fully opened!
>
> You have reached the **Supreme Peak** realm!
>
> Sudden Quest, **Bone Transformation**, has begun. You cannot refuse this Quest!
>
> Sudden Quest, **Bone Transformation**, completed successfully!
>
> You can now draw in and release qi with great freedom. Your Muscles and Bones, now perfect in themselves, even reject impure qi!
>
> You have earned the great achievement **Full-Body Plastic Surgery**!
>
> Quest and achievement rewards have been issued!
>
> All attributes have increased significantly! Open the **Status Window** to check the details.
>
> You have received 30 bonus stat points!
>
> You have gained a large amount of **EXP** and **Fame**!
>
> Level up!



As I read through the holographic windows pouring out one after another, only one thought came to mind.

*This is insane.*

Of course, I’d expected massive rewards.

The Thunderbolt Saber King, Peng Cheolhu.

The power that giant, who’d defined an entire era, had passed on to me at the cost of what little life he had left was just as pure as it was immense.

Even so, the rewards listed by the System went far beyond what I’d expected.

Two level-ups, a huge number of bonus points on top of that, and a boost to all my attributes.

*I’ll have to check the details to see just how much my attributes increased, but even so, if I add all this together…*

It wouldn’t be an exaggeration to say I’d gained more than ten levels in one go.

No, in practice, it was even better than that.

The stronger I got, the farther away my next level-up seemed. The EXP required rose exponentially with each level, but the huge number of stat points I’d just received as a reward was pure bonus.

*I’m in debt. Deep in debt.*

Even with all those incredible rewards, I felt conflicted.

Overwhelmed by both joy and bitterness, I remembered the Thunderbolt Saber King smiling brightly as he said he would pass everything he had on to me.

And with him, I remembered all the victims who’d fallen at Eight Spring Gorge that day, when the chrysanthemums covering the mountain had turned red and the bodies of people and horses had piled up like mountains.

At the same time, I engraved one thing deep in my heart.

This enormous reward I’d been given was payment for the lives of the dead.

*I’ll repay this debt… no matter what.*

I’d never had much of a comfortable life, and debt had always been a miserable thing to me. But not this time.

I was looking toward the same place they were.

The day I finally cleared this entire debt, the peace everyone wanted would arrive.

And to make that happen, I had to endure and overcome whatever hardships and adversity came my way.

I couldn’t let grief make me collapse, or settle for the present. I had to keep moving toward higher places, never giving up.

Toward the place I’d glimpsed while completing Transmitting Internal Energy Across the Body, hidden behind thick clouds.

Toward the sky above the summit.

*Right. The upper dantian.*

Of course, I knew it was no easy feat.

Even the Three Saints, the greatest masters in the Central Plains, and Jeok Cheongang, who stood shoulder to shoulder with them, might not have opened their upper dantian. I couldn’t be sure.

*No, even if they’ve already reached that stage, there must still be differences between them.*

Everything had its proper order.

I’d widened a narrow stream into a vast sea. Now I had to climb a mountain peak that rose as if it would pierce the clouds.

Until now, I’d grown at a terrifying pace thanks to the System I’d gained by chance and countless fortuitous encounters. But even I had been stopped by the clouds.

I still couldn’t reach the absolute beings who looked down on the lower world from above them.

*What if I’d ridden that momentum and kept pushing forward back then?*

A pang of regret suddenly crossed my mind.

But I already knew the answer.

*I would’ve failed. And the odds would’ve been very high.*

Trying to break through to the upper dantian in those circumstances wouldn’t have been a challenge. It would’ve been a gamble.

Even I, despite having fully opened my Middle Dantian and feeling an intense surge of elation, had instinctively understood the difference between courage and recklessness—and pulled back.

The more I thought about it, the more indescribably frustrating it felt. But looking at it objectively, it had been a very good decision…

*Wait.*

What was this feeling?

I suddenly furrowed my brow as I remembered the excruciating process of Transmitting Internal Energy Across the Body and the strange dream that had come from memories that weren’t mine.

But that wasn’t all.

The inexplicable déjà vu that had suddenly taken hold of my entire body was telling me there was a trace of a memory, somewhere in between, that had been ground away.

“Decision. A good decision… I’m sure I heard that somewhere.”

My lips moved on their own. The voice that came out sounded unfamiliar, as though it belonged to someone else.

How much time passed?

Staring blankly into empty air like a man in a trance, muttering the same words over and over, I eventually recovered part of a memory that had been forgotten.

*Someone definitely said something like that. Not in reality, but inside my consciousness.*

My eyes stung. I’d forgotten even to blink.

My head had grown hot from turning the thought over and over for so long.

No—invisible little awls were slowly burrowing into my mind.

A headache spread through me.

But even as the pain made me wince, I kept rummaging through my thoughts. I searched the darkness for a tiny fragment hidden beneath larger memories.

And finally—

I remembered.

I remembered myself, realizing it wasn’t time yet and turning away from the upper dantian beyond the clouds.

And then, as I slipped into a trance where I lost all sense of self, someone’s words echoed faintly in my ear.



*That was a good decision. Just like back then.*



“……!”

Before I knew it, my eyes had flown wide open.

Was it because I’d realized who the voice belonged to?

No.

It was because an immense pain had suddenly struck me.

Hngh.

The unexpected pain made me suck in a breath on instinct. I clenched my teeth and squeezed my eyes shut.

The headache that had been slowly burrowing into my mind like an invisible awl had grown as huge as the long acupuncture needle the Medicine King Hall Master carried around like a prized weapon, and it was now tearing through my head.

*What the hell is this…!*

With my vision gone white, I flailed my limbs like someone on the verge of drowning.

Even in the middle of all this, though, I couldn’t let go of the one question in my mind that remained unanswered.

Who was the owner of that voice that had rung out like a hallucination at the last moment?

Who could speak to me in a space inside my mind, rather than in the real world?

*How? How could they do that?*

There was one thing I could be sure of.

The voice I’d heard at that moment belonged neither to Jeok Cheongang nor, even less so, to the Thunderbolt Saber King.

And aside from those two old martial-world veterans, no one else could have communicated with me then.

*Then who was it?*

I genuinely wanted to know. Even as it felt like my head was splitting open, I wanted to know.

Who owned that voice, and how had they approached me and whispered without any of us noticing?

At the same time, I wanted to ask:

How did you know me?

*They said, “Just like back then”… They definitely did.*

There was no doubt.

I didn’t know them, but they knew me.

I couldn’t say when or where we’d met, but today wasn’t the first time we’d encountered each other.

But…

*Why can’t I remember anything? Why?*

I remembered only what they’d said. I couldn’t distinguish the pitch or depth of their voice, or even their gender.

I couldn’t guess whether they were a woman or a man. And if they were a man, I couldn’t even tell whether they were young or old.

All I could vaguely recall was the sensation of that moment—the feeling I’d dredged up while enduring that terrible headache.

*A strange familiarity.*

It felt as unfamiliar as something I’d never heard before, and yet there was a faint, peculiar sense that I knew it.

And that was all I managed to recover.

Whoosh!

A flash of light exploded. The whiteness in my vision slowly receded, and focus began to return to my blurry eyes.

“……Ah.”

I let out the breath I’d been holding and realized that the pain, which had seemed like it would go on forever, had finally ended.

Along with the pain, the memory I’d been allowed to recover had reached its limit, too.

*Damn it.*

I stared silently at my fingertips, trembling with the remnants of the pain, then clenched them tight.

Crack.

The skin of my palm, now almost like iron after undergoing Bone Transformation, pressed taut against my sharp fingernails.

Perhaps it was because my emotions were surging so strangely.

At that very moment, a vast energy sleeping inside my body began to boil—

Ding.



> **System**
> A new Quest, **Unknown Voice**, has been created.
>
> You cannot choose whether to accept this Quest.
>
> The Quest will proceed by force.
>
> Would you like to check the newly updated Quest information?



Unknown Voice.

As I stared at the Quest title on the holographic window, I opened my tightly shut lips.

“Yes.”
```
