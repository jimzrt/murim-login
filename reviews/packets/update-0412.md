<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0412.txt",
      "sha256": "e0e98c0d73e5effeb573e0adb808e129795332c7fda1a9dde8e2a74ff531d477",
      "bytes": 12763
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "797be551a409aa764938eff1ca32181dc3a965316cd02de5c23a7e979a578bb7",
      "bytes": 1363
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "850bda0db577c6b68d9d4d5d96b2a0cd5b6de0645d410997ab21de7590735d5f",
      "bytes": 137994
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "719f20122b7923f66ad4ea8c963a139f692d0a8f855d057908e252915e837687",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cbe4d20d27ede32059018939a801db6b8b8c2221029149904da05bd4b402543e",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1211e558e6dc94ddf4459f32a0f85b79d0b5bdfc6cb200ad52b0226dbef78a03",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "7ac9cd8f11c544fdb0365fdd8bee38cfd00843fbafa66b239b780ace7fdcc958",
      "bytes": 893
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "26af96b514481c6a54bbfaadc20ac5c2f626ac12bc34fcabc06afcdeaa754c65",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "01a3072b450642fac379ba84ffd0549df92ca1b52eff11abbe6ce01e349868a6",
      "bytes": 124558
    }
  ],
  "estimated_tokens": 9672
}
-->

# Durable State Update — Chapter 412

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 412. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 412. Profile updates may replace only one
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
  "chapter": 412,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 412,
    "continuity_sources": [412],
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
    "Jin Taekyung is leading more than two hundred suicide-squad members through the Arch Lich's battlefield toward Lee Jungryong and Wu Heixing.",
    "The Arch Lich's Magic Traps are indiscriminate and lethal, but Johnson's Barrier saved the suicide squad from the latest blast.",
    "The Arch Lich monitors the battlefield through Familiars and commands elite undead from its throne.",
    "The Arch Lich remembers an ancient human Adversary who defeated it in a final battle after it served a king.",
    "The Arch Lich has dispatched twenty elite undead guards and redirected half of them against Jin.",
    "Jin is facing ten Darkened Liches and Death Knights around Level 120 after breaking through the monster army's front lines."
  ],
  "continuity_sources": [
    411
  ],
  "open_questions": [
    "Did the historical Adversary actually die, as the Arch Lich suspects?",
    "What was the Arch Lich's former identity and what became of the king it served?",
    "Can Jin and the suicide squad defeat the ten elite undead blocking their advance?"
  ],
  "safe_through": 411,
  "temporary_decisions": [
    "Render 어둠에 물든 as Darkened.",
    "Render 강기 as Force.",
    "Render 결사대 as suicide squad.",
    "Render 매직 트랩 as Magic Trap.",
    "Render 대적자 as the Adversary."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 드레이크 | **Drake** | High-tier dragonkin monster. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 411
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 411
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 411
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 411
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 399
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃412화



푸드드득.

전장 한가운데 위치한 고목에 내려앉은 까마귀가 눈을 번뜩였다.

자신의 패밀리어를 전망 좋은 자리에 앉힌 아크 리치는 썩 즐거운 기분으로 상황을 지켜보았다.

‘어찌할 텐가. 인간이여.’

쉴 새 없이 번들거리는 까마귀의 검은 눈동자에 한 사람이 비친다.

벌어진 입. 잘게 떨리는 손. 그런 진태경의 모습에 아크 리치는 문득 의문이 들었다.

‘데스나이트 로드가 저렇게 겁 많은 인간에게 쓰러졌단 말인가?’

비록 약간의 결함이 있었다고는 하나, 데스나이트 로드는 분명 불후의 역작이었다.

아크 리치는 고결한 심성과 강한 무력을 지닌 레이페이라는 훌륭한 재료에 욕심을 숨길 수 없었다.

그렇기에 친히 자신의 원천이라 할 수 있는 마력 중 일부를 부여해 주었고, 덕분에 레이페이는 일반적인 데스나이트의 한계를 벗어난 존재로 거듭나게 되었다.

그런 데스나이트 로드가 한낱 겁쟁이 따위에게 쓰러질 리가.

‘정확히 무슨 일이 있었던 거지?’

그날, 아크 리치는 진태경과 레이페이의 전투를 끝까지 지켜보지 않았다. 아니, 지켜볼 필요가 없다고 생각했다.

저 어린 인간이 도착했을 때는 이미 인간의 군대가 전멸한 후였고, 아크 리치에게는 뻔한 결말을 지켜보는 것보다 다른 전선의 상황이 더 중요했으니까.

귀중한 권속의 소멸을 뒤늦게 알아차리고 패밀리어를 보냈을 때는 모든 것이 끝난 뒤였다.

아크 리치가 볼 수 있었던 것은 어느새 나타난 수천의 인간들과 함께 있는 진태경. 그리고 하나도 빠짐없이 전멸한 몬스터 군단뿐이었다.

‘분명 저 인간 홀로 행한 일은 아니었을 터, 단순히 운이 좋았던 것뿐인가.’

하지만 그 운도 여기까지다. 자그마치 열 기에 달하는 데스나이트와 리치는 한 개 군단, 그 이상의 전력을 지녔으니까.

‘더군다나 지난번과 달리 도와줄 놈들도 마땅치 않지.’

이제 저 인간에게 남은 길은 단 한 가지밖에 없다.

동료의 죽음을 무력하게 지켜보며 쓰러지는 것. 그것만이 유일한 결말이자 아크 리치가 내리는 벌이다.

까아아악!

주인의 마음에 동화된 까마귀가 기분 나쁜 울음소리를 터트린 바로 그 순간이었다.

저벅, 저벅.

겁 없이 자신의 권속들에게 다가오던 인간이 걸음을 멈췄다.

그리고 강대한 마력을 뿜어내는 데스나이트와 리치를 향해 덜덜 떨리는 손을 들어 올렸다.

‘항복할 셈인가.’

겁만 많은 인간인 줄 알았는데, 이 정도로 멍청하기까지 할 줄이야. 항복한다고 해서 살려줄 수 있을 거라 생각했다면 크나큰 오산…….

“하나, 둘, 셋, 넷…….”

- ……?

아크 리치는 실로 오랜만에 당황했다.

진태경의 입에서 유창한 마계어가 흘러나왔다는 사실에 한 번, 그리고 그가 하는 행동이 이해가 가지 않아서 두 번.

‘도대체 저게 무슨 짓이지?’

의문이 풀리기까지는 그리 오랜 시간이 걸리지 않았다.

“……아홉, 열.”

말이 끝남과 동시에 진태경의 턱을 타고 침 한 방울이 똑, 하고 떨어져 내렸다.

소매로 문지른 입가에는 흐뭇한 미소가 떠올라 있었다.

“플레이팅 예술이다, 진짜. 진슐랭 별 세 개를 부여하노라.”

- ……?

- ……?

아크 리치와 그의 충실한 권속들은 플레이팅과 진슐랭이 무엇을 뜻하는 단어인지 알아들을 수 없었다.

하지만 그 뒤에 이어진 진태경의 행동이 무엇을 의미하는지는 알았다.

고오오오오옹.

눈에 보이지도 않을 빠르기. 어느새 한껏 뒤로 젖혀진 창날에 모여드는 무시무시한 기운.

그 광경에 아크 리치는 차갑게 굳어 있던 심장이 쿵, 하고 내려앉는 듯한 충격을 느꼈다.

뼈를 타고 흐르는 오싹한 한기와 함께 그의 사념(思念)이 터져 나왔다.

- 피하……!

그러나 그의 사념이 전달되는 속도보다, 창이 뻗어 나오는 속도가 더 빨랐다.

우우웅!

바람이 찢어지고.

콰아아아아!

공간이 갈라졌다.

찰나를 쪼개고 쪼갠 시간 속, 푸른 화염을 머금은 거대한 와류(渦流)가 모든 것을 집어삼켰다. 수많은 몬스터, 데스나이트와 리치. 그리고 얼마 떨어지지 않은 고목나무에 앉아 모든 것을 지켜보던 까마귀 무리까지.

화아아악!

눈부신 섬광이, 모두의 눈 앞을 가렸다.



* * *



스아아아-

어디선가 불어온 바람이 전신에 스며든다. 그것은 오직 나만이 느낄 수 있는 바람이었고, 새롭게 찾아온 힘이었다.

‘그래, 이거지.’

나는 천천히 사그라드는 빛 너머로 보이는 공백을 보며 웃었다. 데스나이트와 리치, 그 외의 수많은 몬스터가 있던 바로 그 자리다.

모든 것이 깨끗이 말소(抹消)된 그곳은 시스템 알림으로 가득했다.

띠링. 띠링. 띠링…….



- [Lv.115 어둠에 물든 데스나이트]를 처치하셨습니다!

- [Lv.120 어둠에 물든 리치]를 처치하셨습니다!

- [Lv.122 어둠에 물든 데스나이트]를 처치하셨습니다!

.

.

.

- 처치한 몬스터의 숫자가 너무 많습니다!

- 대량의 경험치와 명성을 획득하셨습니다!

- 레벨 업!

- 레벨 업!

- 레벨 업!

- 당신은 극히 뛰어난 업적을 달성하셨습니다!

- 업적 달성의 보상으로 칭호, [일기당천一騎當千]을 획득하셨습니다!

- 칭호, [일기당천]의 효과로 다수의 적을 상대할 때 모든 스탯이 일정 수치 상승하며, 피로의 소모가 크게 줄어듭니다! 전투 시 적군은 위축되며, 아군은 사기가 크게 상승합니다!

- 극히 뛰어난 업적을 달성했으므로, 대량의 경험치와 추가 보상이 지급됩니다!

- 레벨 업!

- 새로운 스탯, [위압]이 생성되었습니다!

- 칭호, [일기당천]의 효과로 [위압]이 크게 상승합니다!

- 당신을 마주한 적들은 두려움과 공포를 느낄 것입니다!



나는 눈을 감고 시스템이 주는 여운을 즐겼다.

쉴 새 없이 울려 퍼지는 시스템 알림의 향연. 천국의 종소리가 이런 것인가 싶다.

일섬의 피로를 말끔히 씻어 내리는 레벨 업 네 번에, 지금 같은 대규모 전장에서 탁월한 효과를 발휘할 수 있는 칭호. 거기에 더해 위압이라는 새로운 스탯까지.

‘짜릿해. 늘 새로워. 시스템이 최고야.’

늘 오늘 같다면 죽어도 여한이 없을 것 같다.

- 그것이 사실인가? 오오, 오오오……!

저 시벌 놈이.

스켈레톤 워로드의 산통 깨는 말과 함께 눈을 뜬 내가 가장 먼저 마주한 것은, 석상처럼 굳어 있는 수많은 인간과 몬스터였다.

“……진태경 씨.”

「혀, 형님.」

최 팀장과 샤오 쉔이 넋 나간 표정으로 나를 바라본다.

아니, 비단 두 사람뿐만이 아니라 이백여 명의 결사대 모두가 마찬가지였다.

날 향한 그들의 눈빛과 목소리에는 숨길 수 없는 경외심이 깃들어 있었다.

「맙소사.」

「바, 방금 도대체 무슨 일이 벌어진 거야?」

「데스나이트와 리치가 열 마리나 있었어. 바로 저 자리에! 내가 똑똑히 봤다고!」

그래. 있었지.

근데 지금은 없어.

“Goddamn! holy shit! what the fuck is this! 퍽킹! 퍽킹 김치! 지저스 김치!”

“에에, 에에에에? 나니? 나이이?!”

“…….”

용병업체나 UN에서 파견된 헌터도 있다 보니 국적에 따라 반응도 각양각색이다.

나는 여전히 말을 잇지 못하는 최 팀장을 향해 입을 열었다.

“왜 그렇게 놀라세요. 처음 보는 것도 아니시면서.”

“혹시 방금 그게, 지난번 블랙 드레이크를 처치하실 때 쓰셨던……?”

“맞아요.”

한두 번 일섬을 본 전력이 있던 최 팀장이 침을 꿀꺽 삼켰다.

“……이런 위력은 아니었던 것으로 기억합니다만.”

“그때는 힘 조절했죠.”

당연히 구라다. 사실 내가 써 놓고도 얼떨떨해서 뭐라 말을 해야 할지 모를 정도다.

초절정의 경지에 오른 후 처음이자 마지막으로 사용했던 일섬은 서천마군과의 일전 때였고, 피로가 극에 달한 탓에 곧바로 의식을 잃어버렸으니까.

‘나도 이 정도일 줄은 몰랐는데.’

하나하나가 네임드급에 가깝다는 데스나이트와 리치가 자그마치 열 마리. 그중 예닐곱 마리 정도만 처치해도 성공이라고 생각했다.

어차피 100레벨 이상부터는 상당한 경험치가 들어오고 다른 잡몹까지 더해진다면 레벨 업에는 충분할 테니, 볼썽사납게 탈진해서 쓰러질 일 따위는 없을 거라고 생각했지, 뭐.

‘……근데 생각했던 것 이상이네.’

양날의 검. 아니, 양날의 창이지만 확실히 엄청난 한 방이다.

다닥다닥 붙어 있던 수백 마리의 정예 몬스터는 물론이고 데스나이트와 리치까지 날려 버렸으니.

덕분에 나와 결사대를 포위하던 몬스터 군단엔 커다란 공백이 생겼고, 놈들 역시 혼란에 빠진 모습이었다.

‘지금 같은 좋은 기회를 놓치면 병신이지.’

나는 망설임 없이 창을 치켜세웠다.

예상치 못한 상황이 벌어짐으로써 양측의 전투가 일시적으로 멈춘 상태지만, 몬스터 군단이 정신을 차리고 극심한 수적 열세에 시달리는 결사대가 재차 포위당한다면 그때는 정말 장담할 수 없다.

“뭐 해, 이 자식들아!”

“예?”

“What?”

“에에에에?”

공력이 실린 외침에 퍼뜩 정신이 든 사람들을 향해 고함쳤다.

존댓말이고 뭐고 다 필요 없다. 지금은 한 가지만 생각해야 할 때다.

“닥치는 대로 쓸어 버려!”

“……!”

띠링.



- 칭호, [일기당천]의 효과로 인해 아군의 사기가 크게 상승합니다! 당신의 통솔을 따르는 이들은 끈끈한 결속력을 지니며, 더욱 뛰어난 활약을 펼칠 것입니다!

- 칭호, [일기당천]의 효과로 인해 적들이 크게 위축됩니다!

- 칭호, [일기당천]으로 인해 [위압]의 효과가 증가합니다!

- [위압]의 영향으로 적들이 두려움을 느끼고 뒷걸음질 칩니다!



시스템 메시지가 알려 준 그대로였다.

내가 보여 준 신위에 아직 살아 있던 몬스터들은 슬금슬금 물러났고, 이미 이지를 상실한 언데드 몬스터 역시 위축되어 흠칫거린다.

반면 우리는?

“돌격-!”

쐐액! 콰드드득!

우렁찬 외침과 함께 내가 일섬으로 생겨난 공백으로 뛰어들어 종횡무진 창을 휘두르자, 한 몸이 되어 쏘아진 이백여 명의 결사대가 귀가 먹먹해지는 함성을 내질렀다.

「와아아아아!」

「진 선생을 따르자! 놈들을 모조리 쓸어버려라!」

“퍽킹! 퍽킹 진기스칸! 지저스 킴치맨!”

“에에에에에?!”

퍼걱! 촤아아악!

녹색 핏물이 튀고, 언데드의 뼈가 산산조각나며 부서진다.

서걱!

등을 돌려 도망치려는 트롤의 상반신을 깔끔하게 갈라 버린 내게, 스켈레톤 워로드가 분노한 목소리로 외쳤다.

- 간악한 인간이여! 저기! 저놈을 처치해라!

“뭐? 누구?”

- 자꾸 에에에에 거리는 저 이상한 인간 놈을 처치해라!

“…….”

- 아니면 내가 죽이겠다! 한 번만 더 하면 반드시 죽일 거다!

어, 그래.

나도 아까부터 듣는데 좀 빡치긴 하더라.



* * *



- 큭!

아크 리치는 외마디 신음을 흘렸다.

패밀리어와의 링크(Link)가 강제적으로 끊어진 것으로도 모자라, 열 기나 되는 호위대가 일거에 소멸했다.

일반적인 몬스터와 달리 그들은 자신의 힘이 부여된 권속. 아크 리치 역시 타격을 피할 수 없었다.

- 이런 미친. 어찌 인간 따위가…….

순간 흐트러진 마력을 수습한 아크 리치는 말을 잇지 못하고 멈칫했다.

인간 따위? 그 말은 틀렸다. 분명 인간은 하찮은 존재지만, 결코 방심해서는 안 된다.

이미 뼈아픈 과거가 있으니.

‘혹시, 혹시 저놈이?’

문득 뇌리를 스치는 어떤 불길한 상상에, 아크 리치의 안광이 거세게 타올랐다.
```

## Final English reading copy

```markdown
# Chapter 412

*Fwoooosh.*

A crow landed on an ancient tree in the middle of the battlefield, its eyes flashing brightly.

The Arch Lich had perched its Familiar in a spot with an excellent view, and it watched the situation with considerable pleasure.

*What will you do, human?*

One person was reflected in the crow’s endlessly gleaming black eyes.

An open mouth. Hands trembling slightly.

Looking at Jin Taekyung like that, the Arch Lich suddenly found itself wondering.

*Was the Death Knight Lord really defeated by a human this cowardly?*

The Death Knight Lord may have had a few flaws, but it was undoubtedly an undying masterpiece.

The Arch Lich had been unable to resist coveting Lei Fei, an excellent material with a noble spirit and formidable martial power.

That was why it had personally granted him a portion of the mana that could be called its own source. Thanks to that, Lei Fei had become an existence that surpassed the limits of an ordinary Death Knight.

There was no way such a Death Knight Lord could have been defeated by some mere coward.

*What exactly happened?*

That day, the Arch Lich had not watched the battle between Jin Taekyung and Lei Fei to the end. No—it had not thought there was any need to watch.

By the time that young human arrived, the human army had already been wiped out. To the Arch Lich, the situation on another front was more important than watching an obvious conclusion unfold.

By the time it belatedly noticed the destruction of its precious retainer and sent a Familiar, everything was already over.

All the Arch Lich had been able to see was Jin Taekyung, now accompanied by several thousand humans who had appeared out of nowhere—and the monster army, annihilated without a single survivor.

*That human clearly couldn’t have done it alone. Was it simply a matter of luck?*

But that luck ended here.

As many as ten Death Knights and Liches possessed the strength of an entire legion, if not more.

*And unlike last time, there aren’t any suitable people around to help him.*

There was only one path left for that human now.

He would helplessly watch his companions die before falling himself.

That was the only possible ending—and the punishment the Arch Lich had chosen for him.

*Cawww!*

The crow, taking on its master’s mood, let out an unpleasant cry.

Step. Step.

That was the exact moment when the human who had been fearlessly approaching its retainers stopped walking.

Then he raised a trembling hand toward the Death Knights and Liches radiating immense mana.

*Is he planning to surrender?*

The Arch Lich had thought he was merely a cowardly human. It had not expected him to be this stupid as well.

If he thought surrendering would convince the Arch Lich to spare him, he was making a terrible mistake—

“One, two, three, four…”

—…?

The Arch Lich was flustered for the first time in a very long while.

First, because fluent Demon Realm language had flowed from Jin Taekyung’s mouth.

Second, because it could not understand what he was doing.

*What in the world is he up to?*

It did not have to wonder for long.

“…Nine, ten.”

As soon as he finished speaking, a droplet of saliva fell from Jin Taekyung’s chin with a soft *plop*.

He wiped his mouth with his sleeve, a satisfied smile spreading across his face.

“Plating is an art, seriously. I hereby award it three Jin-shelin stars.”

—?

—?

The Arch Lich and its loyal retainers had no idea what the words *plating* or *Jin-shelin* meant.

But they understood the meaning of Jin Taekyung’s next action.

*Gooooooong.*

At a speed too fast for the eye to follow, a terrifying force gathered along the spearhead, which had already been drawn far back.

At that sight, the Arch Lich felt a shock as though its cold, hardened heart had dropped into its stomach.

A bone-deep chill ran through it, and a thought burst forth.

“Dodge—!”

But the spear shot forward faster than the thought could be conveyed.

*Woooooong!*

The wind tore apart.

*Kraaaaaaaaaash!*

Space split open.

Within time that had been divided and divided again into a single instant, a massive vortex filled with blue flames swallowed everything.

Countless monsters. Death Knights and Liches.

Even the flock of crows perched on an ancient tree not far away, watching everything unfold.

*Fwoooooosh!*

A blinding flash covered everyone’s vision.

* * *

*Whoooooosh.*

A wind that had come from somewhere seeped through my entire body.

It was a wind only I could feel—and a new power that had come to me.

*Yes. This is it.*

I smiled as I looked at the empty space visible beyond the slowly fading light.

It was the exact place where the Death Knights, Liches, and countless other monsters had been standing.

Everything there had been cleanly erased, and the area was filled with System notifications.

*Ding. Ding. Ding…*

> **System**
> - You defeated **Lv. 115 Darkened Death Knight**!
> - You defeated **Lv. 120 Darkened Lich**!
> - You defeated **Lv. 122 Darkened Death Knight**!
> - …
> - You have defeated too many monsters!
> - You have gained a massive amount of EXP and Fame!
> - Level Up!
> - Level Up!
> - Level Up!
> - You have accomplished an exceptional feat!
> - As a Reward for your achievement, you have obtained the Title **One Against a Thousand**!
> - Due to the effect of the Title **One Against a Thousand**, all Stats rise by a set amount when facing multiple enemies, and fatigue consumption is greatly reduced! During battle, enemies will be intimidated, while allies’ morale rises dramatically!
> - Because you have accomplished an exceptional feat, a massive amount of EXP and additional Rewards will be granted!
> - Level Up!
> - A new stat, **Intimidation**, has been created!
> - Due to the effect of the Title **One Against a Thousand**, **Intimidation** has increased significantly!
> - Enemies who face you will feel fear and terror!

I closed my eyes and savored the afterglow given to me by the System.

A feast of System notifications ringing without pause.

So this was what the bells of heaven sounded like.

Four Level Ups that completely washed away the fatigue of One Annihilation. A Title capable of displaying exceptional effects on a large-scale battlefield like this one. And on top of that, a new stat called Intimidation.

*It’s thrilling. It’s always fresh. The System is the best.*

If every day could be like this, I felt I could die without regrets.

“Is that true? Oh, ohhh…!”

That fucking bastard.

The Skeleton Warlord’s mood-killing words made me open my eyes. The first thing I saw was a large number of humans and monsters frozen like statues.

“…Mr. Jin Taekyung.”

「H-Hyung.」

Team Leader Choi and Shao Shen stared at me with dazed expressions.

No, it was not only those two.

All two hundred or so members of the suicide squad were the same.

There was unmistakable awe in their eyes and voices as they looked at me.

「Good heavens.」

「W-What in the world just happened?」

「There were ten Death Knights and Liches. Right there! I saw them with my own eyes!」

Yeah. They had been there.

But now they were gone.

“Goddamn! Holy shit! What the fuck is this? Fucking! Fucking kimchi! Jesus kimchi!”

“Eeeh, eeeeeh? Nani? Naiii?!”

“…”

Some of the Hunters had been dispatched by mercenary companies or the UN, so their reactions varied greatly depending on their nationality.

I turned toward Team Leader Choi, who still could not seem to form a sentence.

“Why are you so surprised? It’s not like this is your first time seeing it.”

“Was that what you used last time, when you defeated the Black Drake…?”

“That’s right.”

Team Leader Choi had seen One Annihilation once or twice before, and he swallowed hard.

“…I remember it not having this kind of power.”

“I was holding back then.”

That was an obvious lie.

In truth, even I was so stunned by what I had done that I had no idea what to say.

The first and last time I had used One Annihilation after reaching the Supreme Peak realm was during my battle with the Western Heaven Demon Lord. Since my fatigue had been at its limit, I had lost consciousness immediately afterward.

*I didn’t know it would be this powerful either.*

There had been ten Death Knights and Liches, each one close to Named level.

I had considered it a success if I managed to kill six or seven of them.

After all, monsters at Level 100 or above gave a considerable amount of EXP. With all the other small fry thrown in, there would be enough to level up, so I’d figured there was no way I’d collapse from exhaustion and make a spectacle of myself.

*…But this is more than I expected.*

A double-edged sword.

No—a double-edged spear.

But it was undeniably one hell of a powerful strike.

It had blown away not only the hundreds of elite monsters packed tightly together, but also the Death Knights and Liches.

Thanks to that, a massive gap had opened in the monster army surrounding me and the suicide squad. The monsters themselves also appeared to be in confusion.

*I’d be an idiot to let this opportunity pass.*

Without hesitation, I raised my spear.

The unexpected situation had temporarily halted the battle on both sides. But if the monster army recovered and the suicide squad, already suffering from an overwhelming numerical disadvantage, was surrounded again, I could make no guarantees.

“What are you waiting for, you bastards?”

“Huh?”

“What?”

“Eeeeeh?”

I shouted at the people who had been jolted back to their senses by my cry charged with internal energy.

There was no time for honorifics or anything else.

Right now, there was only one thing to think about.

“Wipe out everything in your path!”

“……!”

*Ding.*

> **System**
> - Due to the effect of the Title **One Against a Thousand**, the morale of your allies has risen dramatically! Those who follow your command will possess strong cohesion and display even greater performance!
> - Due to the effect of the Title **One Against a Thousand**, the enemy has become greatly intimidated!
> - Due to the Title **One Against a Thousand**, the effect of **Intimidation** has increased!
> - Under the influence of **Intimidation**, the enemy feels fear and takes a step backward!

The System messages described exactly what was happening.

The monsters still alive after witnessing the divine might I had displayed slowly retreated. Even the undead monsters, which had already lost their minds, were intimidated and flinched.

But what about us?

“Charge!”

*Whoosh! Kra-d-d-d-d-k!*

With a thunderous shout, I leaped into the gap created by One Annihilation and swung my spear in every direction.

The roughly two hundred members of the suicide squad surged forward as one, letting out a roar loud enough to make my ears ring.

「Waaaaaaaaah!」

「Follow Mr. Jin! Wipe them all out!」

“Fucking! Fucking Jin Genghis Khan! Jesus Kimchiman!”

“Eeeeeeeh?!”

*Splat! Shraaaaaak!*

Green blood sprayed through the air, and undead bones shattered into countless pieces.

*Slash!*

I cleanly split the upper body of a Troll trying to turn its back and flee.

The Skeleton Warlord shouted at me in an enraged voice.

“Wicked human! Over there! Kill that one!”

“What? Who?”

“Kill that strange human who keeps going ‘eeeeeeh’!”

“…”

“Or I’ll kill him myself! If he does it one more time, I swear I’ll kill him!”

“Yeah, okay.”

I had been hearing it too, and it was starting to piss me off.

* * *

“Ghk!”

The Arch Lich let out a strangled groan.

As if the Link with its Familiar being forcibly severed were not enough, all ten of its guards had vanished in an instant.

Unlike ordinary monsters, they were retainers empowered by the Arch Lich itself.

The Arch Lich could not avoid taking damage.

“This is insane. How can a mere human…”

After gathering its disrupted mana, the Arch Lich stopped short, unable to continue.

*A mere human?*

That was wrong.

Humans were certainly insignificant beings, but they could never be underestimated.

The Arch Lich already had a painful history to prove it.

*Could that guy…?*

At the ominous possibility that suddenly flashed through its mind, the light in the Arch Lich’s eyes burned fiercely.
```
