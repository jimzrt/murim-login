<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0557.txt",
      "sha256": "9c94005a90614fe88e6fb929d58c8eaf859ee33a66c0dcc40d8e460bb744c162",
      "bytes": 12635
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5530a18677ae5cdfdb187f4793a3b144b362d05a3e655fc316b0b3016ff44ffe",
      "bytes": 4637
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "01989605809221e04f50ac9feef592018674d4aee683dd0a5a42c7e56522a635",
      "bytes": 175916
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1f40ce79ef5b7258bae1ee07c0d82ea079696136a6c7d6d8ed949a22663e31b1",
      "bytes": 553
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "df75541eb5c1d1eeeec7e794d11704df548af7cc9fb5536734dac70891876ae1",
      "bytes": 1252
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61693795214a59a9409884bd5cc353de2fc1d37ea4cc5382d289182b76afcd28",
      "bytes": 168779
    }
  ],
  "estimated_tokens": 9580
}
-->

# Durable State Update — Chapter 557

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 557. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 557. Profile updates may replace only one
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
  "chapter": 557,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 557,
    "continuity_sources": [557],
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
    "The Fire Dragon Pavilion’s six-member first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can’t Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, and leadership of the Fire Dragon Pavilion’s first mission to Nanman.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven’s second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho’s dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun is now Ares Guild’s Vice Guild Master and chief mourner for Lee Jungryong, with dozens of A-rank Hunters serving as his new subordinates; he intends to preserve Lee’s legacy and regards Jin Taekyung and Choi Minwoo as its enemies.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero’s only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee’s corruption.",
    "Go Jun possesses a battered necklace recovered from the ruins of the Arch Lich’s former stronghold; it is not Lee Jungryong’s keepsake, but Go Jun bribed an investigation leader to obtain it because he considers it meaningful.",
    "Taekyung and the Skeleton King have been forcibly moved into the Mutated Gate’s Forest of Giants, while twenty low-level Hunters remain unconscious inside the Skeleton King’s reinforced bone barrier and hostile giants advance."
  ],
  "continuity_sources": [
    556,
    555
  ],
  "open_questions": [
    "What is the Lord of Heaven’s identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo’s political engagement end?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What did Lee Jungryong leave Go Jun beyond his dying wish, what is the necklace recovered from the Arch Lich’s ruins, and what will happen to Taekyung, the Skeleton King, and the twenty Hunters in Forest of Giants?"
  ],
  "safe_through": 556,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can’t Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 소격변 as Small Cataclysm, 낭중지추 as needle in a bag, 국장 and 국가장 as national funeral, 상주 as chief mourner, 변이 게이트 as Mutated Gate, 아크 리치 as Arch Lich, 스켈레톤 킹 as Skeleton King, 거인의 숲 as Forest of Giants, 돌발 퀘스트 as Unexpected Quest, 사이클롭스 as Cyclops, and 엔트 as Ent."
  ],
  "version": 1
}
```

## Exact glossary matches

| 열화문    | **Fire Gate Clan**               |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 장로     | **Elder**                                    |
| 일격     | **One Strike**                         |
| 극양                        | **Extreme Yang**      |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 지능               | **Intelligence**               |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 열화신창 | **Blazing Flame Divine Spear** | Jin's spear technique; its first form appears in this chapter. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 소격변 | **Small Cataclysm** | Name given to the Sichuan Province monster wave. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 555
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 552
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung is accompanying him while learning his martial arts through observation, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

## Korean source

```text
＃557화



후우우.

후텁지근한 숲의 공기 사이로 내뱉은 숨이 섞여 들어간다. 나는 사방에서 몰려드는 적들을 바라보며 조용히 뇌까렸다.

‘중심은 낮게. 하체는 굳건하게. 공격을 시도할 때는…….’

강맹하며, 망설임 없이.

번쩍.

눈을 반개(半開)함과 동시에 그대로 땅을 박찼다.

파앙-!

발끝에서 압축된 공기가 터져 나감과 동시에 무지막지한 풍압(風壓)이 전신을 덮쳤다.

그러나 인간의 한계를 뛰어넘은 육체는 압력을 밀어 냈고, 비스듬히 기운 신형은 바람을 거스르며 포탄처럼 쏘아졌다.

쐐애애액!

머리카락이 세차게 흩날렸다. 맹렬한 바람과 함께 주위의 풍경이 빠르게 스쳐 지나간다.

같이 가자며 고래고래 외치는 스켈레톤 킹의 목소리가 파공성에 파묻히고.

깊고 끈끈한 늪과, 울창한 풀숲을 짓밟으며 진군하는 수백의 몬스터가 어느덧 코앞에 있었다.

- 그워어어어어!

수백여 그루, 혹은 마리.

엔트(Ent)라는 이름을 가진 저 괴물들을 무슨 단어로 헤아려야 할지는 모르겠지만, 적어도 한 가지는 확실했다.

‘내가 이겨.’

이건 짐작이 아니라 확신이다. 마치 자신이 왕이라도 되는 양, 엔트들의 뒤에서 이쪽을 지켜보는 사이클롭스도 예외일 수 없다.

지금 내 전신을 타고 흐르는 삼 갑자의 강대한 열양지기가 확신의 증거고, 숱한 강적들을 쓰러트리며 이 자리에 있는 나 자신이 증인이며, 백염의 창날을 휘감으며 솟구친 청백색의 강기(罡氣)가 바로 판사다.

그리고 그 판결은 신속하고, 파괴적이었다.

‘지금.’

사아악.

푸른 불꽃이 주변의 습기를 증발시켰다. 찰나라고 부를 수조차 없는 짧은 순간, 백염의 투명한 창날은 이미 선두에 선 놈들을 비스듬히 스친 후였다.

슈왁!

요란한 폭발음도, 비명도 없었다.

단지 한 줄기 바람이 불었고, 창날에 서린 극양의 기운이 허공을 따라 미세한 선을 만들었을 뿐이다.

그 선은 마치 전설 속에서나 등장할 법한 어떤 것의 일부를 닮아 있었다.

‘화룡신창. 일 초식.’

화룡일미(火龍一尾).

뒤에 마땅히 이어져야 할 네 글자를 마음속으로 뇌까리기도 전에, 허공에 그어진 희미한 선이 일렁였다.

잠들어 있던 청백색의 불꽃이 짧은 잠에서 깨어났다.

화륵.

작았던 불씨가 타오른다.

엔트의 몸통과, 가지와, 무성한 잎사귀를 장작 삼아 겁화(劫火)로 화한 불꽃이 선에 닿은 모든 것을 집어삼킨 순간.

콰아아아아-!

청백색의 빛이 터져 나와 사방을 밝게 물들였다.

불꽃이 지나간 자리에는 온통 그을리고 녹아버린 땅과 우뚝 굳어 버린 수백의 엔트. 그리고 어디선가 울려 퍼진 맑은 종소리뿐이었다.

띠링. 띠링. 띠링.



- 치명적인 일격!

- [Lv.95 타락한 엔트 대전사]를 처치했습니다!

- [Lv.90 타락한 엔트 선봉대]를 처치했습니다!

- [Lv.89 타락한 엔트 선봉대]를 처치했습니다!

.

.

.

- 처치한 대상과의 레벨 차이가 20 이상이므로, 획득하는 경험치가 감소합니다.

- 일격에 20개체 이상의 [타락한 엔트]를 처치했으므로, 보너스 경험치가 주어집니다!

- 대량의 경험치와 명성을 획득했습니다!



하지만 시스템 알림은 그것으로 끝이 아니었다.

띠링.



- 당신은 수많은 적에 의해 포위되었습니다. 그러나 두려워하지 마십시오. 물러서야 할 것은 당신이 아니라, 바로 적들입니다.

- 칭호, [일기당천]의 칭호 효과가 발동됩니다!

- 확인된 적들의 숫자 : 281

- 다수의 적을 상대하게 되었으므로, 적의 숫자에 따라 당신의 모든 능력치가 일시적으로 상승합니다!

- 다수의 적과 전투를 치를 시, 전투 시 체력의 소모가 크게 줄어들며, 피로를 쉽게 느끼지 못합니다!



일기당천(一騎當千).

두 달 전, 아크 리치의 명령을 따르던 언데드 군단을 단신으로 쓸어 버리며 얻은 칭호가 드디어 빛을 발하는 순간이다.

띠링. 띠링. 띠링.

연달아 울리는 종소리와 함께 [근력], [체력]을 포함한 모든 능력치가 소량 상승했다.

하지만 이것으로 끝이 아니다. [일기당천]의 가장 큰 효과 중 하나는, 한 가지 스탯을 극대화시키는 것에 있었다.



- [위압]이 대폭 상승합니다!

- 들불처럼 일어난 위엄과 기세가 적들을 압도하고 있습니다!

- 당신의 [위압]에 적들이 크게 위축됩니다!

- 당신의 [위압]에 아군의 사기가 크게 상승합니다!



‘위압.’

적을 억누르고, 아군을 북돋는 힘. 나 한 사람을 넘어 전장의 흐름을 바꿀 수 있는 능력. 시스템이 알려 준 정보는 조금도 틀리지 않았다.

어느덧 사방에서 좁혀 오던 포위망이 주춤거리고, 두껍고 난폭하게 움직이던 나뭇가지는 우뚝 멈춰 있었다.

- 그우우우…….

엔트. 거대한 나무에 깃든 악한 정령들이 위축된 울음소리를 흘렸다.

단단한 나무껍질 사이로 보이는 수백 쌍의 까만 눈동자가 잘게 흔들리고 있었다.

‘두려움.’

익숙한 감정이다. 한때는 내 것이었으나 이제는 마주하는 적들의 것이 되어 버린.

가슴 깊숙한 곳에서 차오르는 고양감을 느끼며, 나는 한 걸음을 내디뎠다.

저벅.

- 그워어어어.

- 그륵. 구우우.

구구구궁.

내가 나아가는 만큼 엔트가 물러선다. 아니, 밀림 전체가 움직였다.

놈들이 한데 뭉쳐 흘리는 마력은 내 전신으로부터 뿜어지는 기파과 위압에 짓눌렸다.

‘힘. 기세.’

전투를 결정지는 두 가지 요인 중 어느 것 하나 나에게 미치지 못한다. 그러니 싸우지 않을 이유가 없고, 이기지 못할 이유가 없다.

물론 그럼에도 단 하나의 변수는 있었다.

- 크아아아아아!

사이클롭스(Cyclops).

바위보다 거대한 외눈을 지닌, 신화 속 거인의 포효에 온 밀림이 들썩인다.

주춤거리며 뿌리로 뒷걸음질하던 엔트들이 흠칫 몸을 떨었다.

띠링.



- [거인의 포효]가 발동되었습니다!

- [위압]의 효과가 미약하게 해소됩니다!

- 일부의 적들이 [위압]의 압박에서 벗어납니다!



이 게이트의 보스 몬스터다운 능력이다.

하지만 그런 사이클롭스도 내 압박을 완전히 걷어낼 수는 없었고, 나 역시 놈에게 충분한 시간을 줄 생각이 없었다.

아니다. 정정한다. 내가 아니라, 우리다.

“하아압!”

콰드드드득! 퍼버벅!

힘찬 외침과 함께 허공에서 쏘아진 뼈의 창이 엔트들을 꿰뚫는다.

어느새 내 뒤를 따라 도착한 스켈레톤 킹이 길길이 날뛰며 소리를 내질렀다.

“다 덤벼라! 이 하찮은 몬스터들아!”

“…….”

이 새끼, 정체성을 완전히 잃어버렸는데.

그 와중에 [일기당천]의 효과를 톡톡히 봤는지, 잔뜩 고양된 스켈레톤 킹은 앞뒤 보지 않고 달려나가기 시작했다.

“감히 존귀한 이 몸에게 대적하려 드느냐! 죽어! 죽어! 다 죽어어어!”

파파파팟!

스켈레톤 킹이 약간 맛이 간 놈이긴 해도, 한 단계의 진화까지 거친 네임드 몬스터다.

녀석이 지닌 힘은 누구도 부정할 수 없었고, 땅과 허공에서 솟구친 뼈들은 쉼 없이 나뭇가지를 부수며 엔트의 몸통을 꿰뚫었다.

퍼버벅!

“어딜 감히 이 몸 앞에서 앙증맞은 잎사귀를 흔드느냐!”

와지끈!

“네깟 놈들이 아무리 덤벼 봤자 뼈에 계란 치기다!”

- 구워어어!

구슬픈 비명이 울려 퍼지는 산림 파괴의 현장.

스켈레톤 킹의 난입과 동시에 텅 비어 버린 길을 따라, 나는 화살처럼 쏘아졌다.

쉬이이익! 서걱!

바람처럼 스쳐 지나감과 동시에 창날로 사방을 내리긋자, 허공을 가로지르는 불꽃과 함께 엔트들이 비명도 지르지 못하고 소멸한다.

띠링. 띠링. 띠링.

귓가를 시끄럽게 울리는 종소리를 들으며 몸을 틀었다. 맹렬한 기세로 쏘아진 나무줄기가 옆구리를 스치며 지면을 꿰뚫는다.

콰앙!

폭발하듯 터져 나오는 진흙. 나는 재차 휘둘려지는 나무줄기를 밟으며 가볍게 몸을 튕겼다.

타닥. 스윽.

문경의 가르침을 받은 이후 더욱 부드럽고 정교해진 움직임.

깃털처럼 나아간 신형은 어느새 유난히도 큰 거목(巨木)의 앞에 도달해 있었다.



[Lv.102 타락한 엔트 장로]



- 인. 간! 죽. 어. 라!

높은 것은 레벨뿐만이 아닌 모양이다. 상당한 지능까지 갖추었는지 언어를 구사하는 엔트 장로를 향해, 나는 망설임 없이 창날을 비스듬히 내리그었다.

“치코리타 어서 오고.”

- ……!

쉭, 서걱!

방어를 위해 황급히 끌어모은 수백 개의 나뭇가지도. 나를 향해 쏘아 보낸 가시도 전부 소용없다.

창날이 스친 궤적을 따라, 둘레만 수 미터에 이르는 거목이 스르륵 분리된다.

쿠웅! 화륵!

굉음과 함께 쓰러진 거목이 활활 타오른다.

빽빽한 나이테가 새겨진 나무 밑동을 밟고 솟구친 나는, 마침내 허공을 가린 거대한 존재와 마주할 수 있었다.



[Lv.130 ‘붉은 눈’ 사이클롭스]



놈이다. 이 밀림의 주인. 수백의 엔트를 종으로 삼은 흉포한 외눈의 거인.

비로소 확인된 놈의 정체는 소격변 당시 아크 리치의 휘하에 있던 어느 몬스터보다도 레벨이 높으며, 이명(異名)마저 붙어 있는 네임드 몬스터였다.

‘이런 하급 게이트에 네임드 몬스터라…….’

문득 마음이 무거워졌지만, 생각은 다음으로 미뤄야 한다. 까마득한 허공으로부터 내리꽂히는 거대한 그림자 때문이었다.

후웅!

지름만 십여 미터에 달하는 바위. 아니, 운석에 가까운 그것이 바람을 뭉개며 떨어져 내린다.

그리고 내가 선택한 것은 회피가 아닌 정면 돌파였다.

‘속전속결.’

나는 아래에서 위로 쏘아지고. 바위는 위에서 아래로 내리꽂힌다.

피할 수 없는 격돌의 순간, 나는 백염에 깃든 열양지기를 창날의 끝으로 쏟아부으며 바위의 정중앙을 향해 내질렀다.

그리고…….

서걱.

마치 뜨거운 칼로 치즈를 가르듯, 부드럽게 바위를 파고 들어간 창날이 회전했다.

콰드득.

정확히 일점(一點)을 돌파한 뒤 내부를 찢어발기는 막강한 강기에, 거대한 바위의 표면에 선명한 균열이 아로새겨진 다음 순간.

콰아아아아앙!

우레와 같은 굉음과 함께 수백, 수천 개의 파편으로 나뉜 바위가 사방으로 흩어졌다.

- ……!

하나뿐인 붉은 눈동자를 부릅뜬 사이클롭스가 그 힘을 이기지 못해 몸을 휘청였다.

쿠궁. 콰직!

- 그워어어어!

거인의 움직임에 지면이 부서지고 작은 체구의 엔트들이 짓밟혀 비명을 내지른다.

그러나 사이클롭스도, 나도 지상의 일에는 아무런 관심도 없었다.

눈앞의 적을 쓰러트리는 것. 그것만이 중요했다.

- 이이이인. 가아아안…….

사이클롭스의 포효가 0.1배속을 한 것처럼 느리다.

느려진 세상 속, 나는 한 치의 망설임도 없이 허공을 밟으며 다시 한번 솟구쳤다.

파앙!

허공답보(虛空踏步). 발끝에서 압축된 공기는 폭발과 함께 나를 멀리, 그리고 높게 밀어냈고.

후우웅.

위기를 느낀 사이클롭스가 뒤늦게 휘두른 주먹은 하품이 나올 정도로 느렸다.

퍼엉!

무시무시한 파공성. 그러나 거인의 일권이 텅 빈 허공을 후려쳤을 때. 나는 이미 그곳을 지나 놈의 정수리 위로 솟구친 후였다.

고오옹.

강대한 열양지기를 머금은 창날 위로 푸른 불꽃이 번진다.

예리하면서도 파괴적인 힘.

유서 깊은 노빠꾸 문파. 열화문의 삼백 년 마초 정신이 집약된 열화신창(火龍神槍)의 두 번째이자 마지막 초식.

‘천격(天格).’

푸른 불꽃이, 거인의 머리 위로 떨어져 내렸다.

슈화아아악, 서걱!
```

## Final English reading copy

```markdown
# Chapter 557

*Whew.*

My breath mingled with the muggy air of the forest. Watching the enemies closing in from every direction, I quietly muttered to myself.

*Keep my center low. Keep my lower body firm. When launching an attack…*

*Be fierce. Without hesitation.*

*Flash.*

The instant I half-opened my eyes, I kicked off the ground.

*Bam—!*

Compressed air burst from my toes, and tremendous wind pressure swept over my entire body.

But my superhuman physique pushed through the pressure. My body tilted at an angle and shot forward like a cannonball, flying against the wind.

*Whoooosh!*

My hair whipped wildly around my face. The scenery rushed past in a blur amid the fierce wind.

The Skeleton King’s voice, shouting that he wanted to come with me, was swallowed by the sound of the air splitting apart.

The hundreds of monsters advancing through the deep, viscous swamp and trampling the dense undergrowth were suddenly right in front of me.

—Gwoooooar!

Hundreds of them.

Or perhaps hundreds of trees.

I didn’t know which word I was supposed to use to count those monsters called Ents, but at least one thing was certain.

*I’ll win.*

This wasn’t a guess. It was absolute certainty.

Even the Cyclops watching us from behind the Ents as though it were their king was no exception.

The three jiazi of mighty Scorching Yang Qi flowing through my entire body were proof of that certainty. I myself—standing here after defeating countless powerful enemies—was its witness. And the blue-white Force surging around the blade of White Flame was its judge.

The verdict was swift.

And destructive.

*Now.*

*Hiss.*

Blue flames evaporated the moisture around me. In a moment too brief to even call an instant, the transparent spearhead of White Flame had already swept diagonally across the Ents at the front.

*Shwaak!*

There was no explosive sound.

No scream.

There was only a single gust of wind, and the Extreme Yang energy clinging to the spearhead had drawn a faint line through the air.

The line resembled part of something that ought to exist only in legend.

*Fire Dragon Divine Spear. First form.*

*Fire Dragon’s Single Tail.*

Before I could finish muttering the four words that should have followed in my mind, the faint line suspended in the air began to ripple.

Blue-white flames that had been lying dormant awoke from their brief slumber.

*Fwoosh.*

The tiny embers flared to life.

The trunks, branches, and lush leaves of the Ents became kindling. The flames transformed into hellfire and devoured everything the line had touched.

*Kraaaaaash—!*

Blue-white light burst outward, illuminating every direction.

Where the flames had passed, the ground was blackened and melted. Hundreds of Ents stood rigid and motionless.

And somewhere in the distance, a clear bell rang.

*Ding. Ding. Ding.*

> **System**
>
> - Critical Strike!
>
> - You defeated **Level 95 Corrupted Ent Great Warrior**!
>
> - You defeated **Level 90 Corrupted Ent Vanguard**!
>
> - You defeated **Level 89 Corrupted Ent Vanguard**!
>
> - …
>
> - …
>
> - …
>
> - Since the level difference between you and the defeated targets is 20 or more, the EXP gained is reduced.
>
> - Since you defeated 20 or more **Corrupted Ents** with a single strike, bonus EXP has been awarded!
>
> - You obtained a large amount of EXP and Fame!

But the System notifications did not end there.

*Ding.*

> **System**
>
> - You have been surrounded by a great many enemies. But do not be afraid. It is not you who must retreat, but the enemy.
>
> - The effect of the Title **One Against a Thousand** has activated!
>
> - Number of identified enemies: 281
>
> - Since you are facing a large number of enemies, all your attributes will temporarily increase according to the number of enemies.
>
> - When fighting a large number of enemies, your Stamina consumption during battle is greatly reduced, and you will not easily feel fatigue!

**One Against a Thousand.**

Two months ago, I had single-handedly swept away the undead army serving the Arch Lich. The Title I had earned then was finally showing its worth.

*Ding. Ding. Ding.*

Along with the bells ringing one after another, all my attributes—including **Strength** and **Stamina**—rose slightly.

But that wasn’t the end.

One of the greatest effects of **One Against a Thousand** was its ability to maximize a single attribute.

> **System**
>
> - **Intimidation** has increased dramatically!
>
> - Your majesty and aura, rising like a wildfire, are overwhelming your enemies!
>
> - Your enemies are greatly intimidated by your **Intimidation**!
>
> - Your allies’ morale is greatly increased by your **Intimidation**!

*Intimidation.*

The power to suppress enemies and encourage allies. An ability that could change the flow of an entire battlefield instead of affecting only me.

The information the System had given me was not wrong in the slightest.

The encirclement that had been closing in from every direction began to falter. The thick branches that had been moving violently and relentlessly came to a sudden stop.

—Gwooooo…

The Ents—evil spirits dwelling within gigantic trees—let out timid cries.

Hundreds of pairs of black eyes trembled faintly between their hard bark.

*Fear.*

It was a familiar emotion.

Once, it had belonged to me.

Now it belonged to the enemies standing before me.

Feeling exhilaration welling up from deep within my chest, I took a step forward.

*Step.*

—Gwoooooar…

—Grrk. Gwooooo…

*Rumble-rumble-rumble.*

The Ents retreated as I advanced.

No—the entire jungle moved.

The mana released by the Ents as they gathered together was crushed beneath the aura and Intimidation radiating from my entire body.

*Strength. Momentum.*

Neither of the two factors that decided a battle could match me.

So there was no reason not to fight.

And no reason I couldn’t win.

Of course, there was still one variable.

—Kraaaaaaaar!

The Cyclops.

The roar of the mythical giant with a single eye larger than a boulder shook the entire jungle.

The Ents, which had been edging backward on their roots, flinched.

*Ding.*

> **System**
>
> - **Giant’s Roar** has activated!
>
> - The effect of **Intimidation** has been slightly neutralized!
>
> - Some enemies have escaped the pressure of **Intimidation**!

It was a fitting ability for the boss monster of this Gate.

But even the Cyclops couldn’t completely dispel my pressure, and I had no intention of giving it enough time to do so.

No.

Correction.

Not me.

Us.

“Haaap!”

*Krkrkrkrk! Pow-pow-pow!*

With a powerful shout, a spear of bone shot through the air and pierced the Ents.

The Skeleton King had arrived behind me at some point. He went completely berserk as he screamed,

“Come at me, you worthless monsters!”

“……”

This bastard had completely lost his identity.

And perhaps he was benefiting fully from the effect of **One Against a Thousand**, because the Skeleton King was so exhilarated that he charged forward without a thought.

“How dare you oppose this exalted body! Die! Die! Dieee!”

*Papapapat!*

The Skeleton King might have been a little off his rocker, but he was still a Named Monster who had undergone an entire evolution.

No one could deny the power he possessed. Bones erupted from the ground and the air, breaking branches without pause and piercing the Ents’ trunks.

*Pow-pow-pow!*

“How dare you wave those adorable little leaves before this body!”

*Craack!*

“No matter how many of you attack, it is nothing but an egg striking a boulder of bone!”

—Gwoooooar!

The plaintive cries of the Ents rang across the scene of forest destruction.

The Skeleton King’s intrusion had left the path completely empty, and I shot forward along it like an arrow.

*Whoooosh! Slash!*

As I passed through like the wind, I swept my spearhead in every direction. Flames crossed through the air, and the Ents vanished without even having the chance to scream.

*Ding. Ding. Ding.*

I twisted my body at the sound of the bells ringing loudly in my ears.

A tree trunk shot toward me with tremendous force, grazed my side, and pierced the ground.

*Boom!*

Mud burst out like an explosion.

I stepped on another trunk whipping toward me and lightly propelled myself into the air.

*Tap. Swish.*

My movements had become smoother and more precise after receiving Mungyeong’s teachings.

My body glided forward like a feather, and before I knew it, I had arrived before an unusually massive tree.

**Level 102 Corrupted Ent Elder**

—H-u-man! D-i-e!

Apparently, its level wasn’t the only thing that was high. It possessed considerable intelligence as well, since the Ent Elder could speak.

Without hesitation, I brought my spearhead down diagonally.

“Welcome, Chikorita.”

—……!

*Whoosh. Slash!*

The hundreds of branches it hastily gathered for defense were useless.

The thorns it shot at me were useless, too.

Along the path traced by my spearhead, the massive tree—with a circumference of several meters—slowly split apart.

*Crash! Fwoosh!*

The fallen tree burst into flames amid a thunderous roar.

I kicked off the stump, its dense growth rings exposed, and shot upward.

At last, I came face-to-face with the gigantic being blocking the sky.

**Level 130 ‘Red Eye’ Cyclops**

It was the one.

The master of this jungle.

A savage one-eyed giant that had made hundreds of Ents its slaves.

Its identity was finally confirmed. It was a Named Monster with a level higher than any monster that had served under the Arch Lich during the Small Cataclysm—and it even possessed an epithet.

*There’s a Named Monster in a low-grade Gate like this…*

My mood suddenly grew heavy, but I had to put that thought aside.

A gigantic shadow was plunging down from the distant sky.

*Whoom!*

A rock more than ten meters in diameter.

No—a boulder closer to a meteorite smashed through the wind as it fell.

And I chose to break through head-on rather than evade.

*Finish it quickly.*

I shot upward from below.

The rock plunged downward from above.

At the unavoidable moment of impact, I poured the Scorching Yang Qi within White Flame into the tip of my spear and thrust toward the exact center of the rock.

And then…

*Slash.*

The spearhead smoothly burrowed into the rock as though it were a hot knife cutting through cheese.

It rotated.

*Krkrkrk.*

The spear broke through a precise single point, and mighty Force tore through the rock’s interior.

A clear crack appeared across the surface of the massive boulder.

Then—

*Kraaaaaaang!*

With a thunderous roar, the rock shattered into hundreds and thousands of fragments that scattered in every direction.

—……!

The Cyclops opened wide its single red eye and staggered, unable to withstand the force.

*Rumble. Crack!*

—Gwoooooar!

The ground broke beneath the giant’s movements. Small-bodied Ents were trampled underfoot and screamed.

But neither the Cyclops nor I paid any attention to what was happening below.

Defeating the enemy in front of us.

That was all that mattered.

—Huuuuuu… maaaaan…

The Cyclops’s roar felt as though someone had slowed it to 0.1 speed.

In the slowed world, I stepped on empty air without hesitation and shot upward once more.

*Bam!*

**Stepping on Empty Air.**

Compressed air exploded beneath my toes, propelling me farther and higher.

*Whoooom.*

The Cyclops, sensing danger, swung its fist too late.

It was slow enough to make me yawn.

*Boom!*

The punch produced a terrifying sound as it split the air.

But when the giant’s fist slammed into empty space, I had already passed through and shot upward above its crown.

*Gooooong.*

Blue flames spread across the spearhead, which held immense Scorching Yang Qi.

A sharp yet destructive force.

The second and final form of the Blazing Flame Divine Spear, which concentrated three hundred years of the Fire Gate Clan’s macho spirit—the time-honored clan with absolutely no concept of retreat.

*Heavenly Strike.*

Blue flames descended upon the giant’s head.

*Shwoooooosh. Slash!*
```
