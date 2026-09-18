<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0414.txt",
      "sha256": "63c9565430921a5bd96656d4a51c3ed9f9967c4f6457401bc87f581f10f35a9d",
      "bytes": 13426
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5662f1a3596c521c59828855814920fe4153fb023c33eab70e1da0ae622dea77",
      "bytes": 1366
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "44096aaa557a04ff6b60deb415c7f5b343c62f49e1f28341ba489f47d26a35a7",
      "bytes": 138476
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "fd405a25fed6393a9615f98e6777994f7c2ef75ecf6e504be7fd3f12bf2eff7c",
      "bytes": 811
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "61ef58c5ca16de856e764ab535246dc2c1f40b3b04a7fa993e434374d9b9bbf0",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "010e8e879eb6329422c65077d24445d9ee3ec402949bd4011b417f3826377e3d",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "27a2868d652ea32a27b575605aeae870fe6b7468191a467dc5ffffff06ad14fb",
      "bytes": 1163
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "ca687eb92f021cf0cfb88268cda9727180c9684974fcf6b290e727bd17ca37e1",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ca6b72c80c8c285ab10d6bdc073c6f502541b604057f8a9b21f56facd71d63be",
      "bytes": 125818
    }
  ],
  "estimated_tokens": 10171
}
-->

# Durable State Update — Chapter 414

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 414. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 414. Profile updates may replace only one
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
  "chapter": 414,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 414,
    "continuity_sources": [414],
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
    "Wu Heixing and the Red Guard Gang are engaged in a losing battle against the monster army despite Wu's S-rank strength.",
    "Lee Jungryong killed a Lich with a single spear throw, and Wu Heixing defeated one of two attacking Death Knights.",
    "Go Jun has entered the battlefield with Ares Guild forces after Lee Jungryong delayed intervention.",
    "Lee Jungryong wants the Red Guard Gang eliminated so Ares can replace its influence and support.",
    "Lee Jungryong heard Jin Taekyung approaching from the west and is waiting for his arrival."
  ],
  "continuity_sources": [
    413,
    412
  ],
  "open_questions": [
    "Why did Lee Jungryong include Wu Heixing in the operation, and how is that choice connected to Jin Taekyung?",
    "What does Lee Jungryong intend to do when Jin Taekyung arrives?",
    "Will the Red Guard Gang be destroyed, allowing Ares Guild to assume its political position?",
    "Can the remaining Red Guard Gang and Ares forces survive the surrounding monster army and Death Knights?"
  ],
  "safe_through": 413,
  "temporary_decisions": [
    "Render 일기당천 as One Against a Thousand.",
    "Render 위압 as Intimidation.",
    "Render 홍위방 as Red Guard Gang.",
    "Render 십이혈라검 as Twelve Blood Net Sword.",
    "Render 결사대 as suicide squad."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 살기     | **killing intent**                               |                                                       |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 대사      | **Master** for a senior Buddhist monk                           |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 장유 | **Jangyu** | Martial artist eliminated during the fist-and-foot assessment. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |

## Listed compact profiles

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 413
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and angered by operational failures that endanger his Master.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong; leader of Lee's security detail; regarded by Lee as stronger than Park Tae Seop; after Go Jun's defeat by Jin Taekyung, Lee reaffirmed his faith in Go Jun and promised to give him the strength to defeat Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 413
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 413
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 413
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 413
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃414화



몇 번을 봐도 반갑지 않은 얼굴들이 있다. 내게는 이정룡과 우헤이싱이 딱 그런 부류에 속했다.

그래도 먼저 말을 건 이유는, 오늘의 우헤이싱이 제법 봐줄 만한 얼굴을 하고 있었기 때문이었다.

“여기서 보네. 다시는 못 볼 줄 알았는데.”

내 활기찬 인사에 너덜너덜한 몰골을 한 우헤이싱이 독기 어린 눈빛을 쏘아 보냈다.

「닥쳐.」

“오…….”

「한마디만 더 했다간, 조부님의 명예를 걸고 네놈을 갈기갈기 찢어 버리겠다.」

중국산 김전일인가. 이런 애들은 왜 돌아가신 할아버지 명예를 신용 카드처럼 내미는지 이해할 수가 없다.

나는 진지한 얼굴로 입을 열었다.

“혹시 할아버지랑 사이 안 좋았어?”

「뭐?」

“아니, 그렇잖아. 왜 실현 불가능한 일에 할아버지 명예를 걸어. 차라리 네가 갈기갈기 찢기는 쪽에 거는 게 훨씬…….”

「이 개새끼가!」

분노 가득한 외침과 함께 벌떡 일어난 우헤이싱을, 이정룡이 손을 들어 가로막았다.

“그만하지.”

「이 선생님! 하지만 저 자식이…….」

“결전을 앞두고 아군끼리 싸우는 건 백해무익한 일이야. 흥분을 가라앉히게.”

으득.

부서져라 이를 간 우헤이싱이 나를 노려보며 대답했다.

「알겠습니다. 이 선생님께서 그렇게까지 말씀하시니 이쯤 하겠습니다.」

“잘 생각했네.”

저놈이 저렇게 순순히 물러나는 성격이었나, 입가에 부드러운 미소를 띤 이정룡을 바라본 나는 살짝 고개를 돌렸다.

짧은 순간 마주친 최 팀장의 눈빛에서 많은 생각이 읽힌다.

“진태경, 자네는?”

나는 최 팀장에게서 시선을 떼며 자연스럽게 어깨를 으쓱해 보였다.

“웃어른 말씀인데 들어야죠.”

“자네가 그런 걸 따지는 사람인 줄은 몰랐는데.”

“장유유서(長幼有序) 아닙니까.”

내 태연자약한 대답에 이정룡은 뜻 모를 너털웃음을 지었고, 우헤이싱은 다시 한번 나를 죽일 듯이 노려보았다.

「장유유서? 어울리지도 않는 개소리는 집어치워라. 그럼 너보다 일곱 살이나 많은 나는?」

“너는 유서 쓰기 싫으면 눈깔부터 착하게 떠.”

「이런 자라 좆 같은……!」

“지랄하지 말고.”

다시 한번 울컥한 우헤이싱의 말은 이어지지 못했다.

나는 차가운 눈빛으로 녀석을 응시하며 말을 이었다.

“겨우 이 정도에 발끈할 정신이 남아 있으면, 네가 데려온 친구들 상태나 살펴보고 와.”

「……!」

“목숨 걸고 여기까지 따라온 사람들이다. 한 번 쓰고 버리는 소모품이 아니라고.”

나는 경멸을 숨기지 않고 드러냈다.

현재 우헤이싱의 주위에 남아 있는 헌터들은 불과 오십여 명 남짓.

본부에서 전달받은 바로는 결사대 오백으로 출발했다고 들었는데, 대부분이 죽거나 낙오한 것이 틀림없었다.

“병력 손실? 충분히 그럴 수 있지. 전투 중이니까. 그런데…….”

그 와중에 놈의 방어구는 피를 뒤집어썼을지언정 외관은 멀쩡했다. 전우들이 죽어 가는 와중에도 몸을 아끼면서 싸웠다는 뜻이다.

“할 말 있냐, 병신아?”

어릴 적 봤던 고전 히어로 무비에서 그런 대사가 나왔다.

큰 힘에는 큰 책임이 따른다고. 그리고 그건 방사능 거미에 물린 사람에게만 해당되는 말이 아니다.

거미줄이 아니라 오러 블레이드를 뽑아내는 놈이라면, 그걸 이용해서 막대한 부와 명예를 쌓고 자신이 저지른 범죄를 무마한 놈이라면 최소한의 책임을 져야 한다는 게 내 생각이다.

“넌 S급은 될 수 있어도 헌터는 못 돼. 그러니까 앞으로 자기소개할 때 헌터라고 하지 말고 그냥 운 좋은 S급 우헤이싱입니다. 라고 해라. 알겠냐?”

「…….」

말없이 주먹을 부르르 떠는 우헤이싱을 대신해 이정룡이 입을 열었다.

“그는 최선을 다했네.”

“방어구 보니까 아닌 것 같아서요. 저 정도면 당장 슥 닦아서 중고나라에 내놔도 될 것 같던데.”

“튼튼하고 좋은 방어구를 차고 있다는 것이 비난할 이유는 아니지.”

“지난번부터 느낀 건데…… 유난히 편을 드시네요. 혹시 저 새끼한테 무슨 약점이라도 잡혔습니까?”

“사람은 누구나 약점이 있지. 그리고 난 약점을 숨기는 데에 능한 편이고.”

“컴퓨터 한 번 검사해 보세요. 누가 압니까, 부길드장님 야동 보는 모습을 중국 해커들이 단톡방에 공유하고 있을지.”

“유의하도록 하지.”

역시 강적이다.

이정룡은 한 치의 동요 없이 빙긋 웃었지만, 그의 뒤에 서 있는 한 남자는 달랐다.

나는 미약한 살기를 피워 올리는 녀석을 향해 손을 흔들어 알은체를 했다.

“이게 누구야, 석 팀장. 우리 고준이 아냐?”

이정룡의 경호팀장이자 제자.

분명 중국으로 출발하기 전 흠씬 두들겨 패 주었던 기억이 있는데, 지금 보이는 모습은 멀쩡하다 못해 오히려 더욱 단단해졌다.

한층 깊고 심유해진 눈빛만 봐도 놈의 실력이 한층 진일보했다는 걸 알 수 있었다.

‘인내심도 길렀고.’

석고준은 이정룡이 길러 낸 충견 중의 충견.

예전 같았다면 진작 달려들고도 남았을 텐데, 살기를 씻은 듯이 갈무리한 녀석은 무기를 뽑는 대신 침묵을 선택했다.

그런 제자의 모습을 흡족하게 바라본 이정룡이 입을 열었다.

“지금 우리는 아크 리치의 코앞까지 도달했네. 좌표상으로는 불과 20km밖에 남지 않았지.”

나는 피로 찐득거리는 머리칼을 쓸어올렸다.

“지구상에서 가장 길고 치열한 20km겠죠.”

“맞네. 아크 리치는 충분한 전력을 남겨 두었어.”

“몇이나 됩니까?”

“추정치 5만.”

그 한마디가 흘러나온 순간, 우리의 대화에 모든 촉각을 기울이고 있던 결사대 사이에서 외마디 탄식이 터져 나왔다.

나와 이정룡, 우헤이싱이 이끄는 결사대를 모두 합치면 오백 남짓이다.

단순 추정치만으로도 백 배에 달하는 대군을 뚫고 아크 리치에 도달해야 한다는 건 저들에게 끔찍한 절망감을 선사하기 충분했다.

그래서였을까, 누군가가 두려움 섞인 목소리로 외쳤다.

「지, 지금이라도 후퇴해야 합니다!」

둑이 허물어지듯, 또 다른 헌터들의 외침이 잇따랐다.

「Fuck!」

「몬스터의 숫자가 너무 많소!」

「이대로면 전멸뿐입니다.」

「나는 아크 리치를 쓰러트리기 위해 왔지, 개죽음을 당하러 온 것이 아니란 말이오!」

거의 없다시피 한 미약한 피해로 여기까지 온 서부 전선의 결사대 이백여 명도 예외는 아니었다.

하지만 들불처럼 번져 가는 두려움 속에서도 흔들림 없는 두 사람이 있었다.

굳은 신뢰의 눈빛으로 나를 바라보는 샤오 쉔, 그리고…….

“가능성이 있군요.”

나에 대한 신뢰를 넘어, 스스로 한 가지 상황을 추론해 낸 최 팀장. 그가 차분한 목소리로 말을 이었다.

“추정치 5만은 총사령부의 예측을 훨씬 뛰어넘는 숫자입니다.”

「그러니 당연히 후퇴해야 하는 것 아닙니까?」

결사대 중 누군가의 외침에 최 팀장이 즉각 고개를 저었다.

“그리고 저희가 상대한 몬스터의 숫자 역시 생각보다 적었고요.”

「어?」

“분명 많은 숫자였지만, 전선에서 맞닥트린 몬스터의 병력은 생각만큼 압도적이지 않았습니다.”

「그렇다면…….」

“어쩌면 아크 리치는 이런 상황을 경계했을지도 모르겠습니다. 전선에 모든 전력을 쏟아붓는 것보다, 어떤 상황에서도 대비할 수 있는 마지막 한 수로 5만의 군단을 남겨 둔 겁니다.”

최 팀장을 바라보던 헌터들의 얼굴이 딱딱하게 굳었다. 그가 한 말을 제대로 이해해서가 아니라, 지면으로부터 점점 거세어지는 진동 때문이었다.

드득. 드드드드득.

수십 킬로 밖에서도 느껴지는 울림에 모두의 몸이 잘게 떨렸다.

파괴된 도로와 양옆에 늘어선 광활한 평야. 사방을 가득 메운 자욱한 안개 너머로, 수만의 몬스터 군단이 하나가 되어 내지르는 괴성과 발걸음이 희미하게 울려 퍼진다.

- 크워어어어어!

「이런 미친…….」

「도망, 도망쳐야 해. 이건 이길 수 없는 싸움이야.」

사람들의 발걸음이 주춤주춤 밀려났다.

그중 예외가 있다면 흔들림 없는 자세로 서 있는 아레스 길드원들이었고, 그들 앞에 선 이정룡은 흥미로운 눈빛으로 최 팀장을 바라보고 있었다.

“그래서?”

허공에서 두 사람의 시선이 마주쳤다. [영웅의 혼]을 움켜쥔 최 팀장의 손에 힘이 들어가는 것이 보였다.

“비록 총사령부의 예측은 빗나갔지만, 아크 리치가 총공세를 가하지 않음으로서 전선에는 여력이 생겼을 겁니다.”

“그럼에도 아군의 병력은 적들에 비해 부족함이 있었다.”

“바로 그 부족한 부분을 채우기 위해 남겨 둔 이들이 있지 않습니까.”

드득. 드드드득.

더욱더 거세지는 진동과 괴성. 불안과 동요로 가득 찬 사람들의 웅성거림 속, 마나를 실은 최 팀장의 한 마디가 모두의 귓가를 파고들었다.

“단숨에 전황을 뒤엎을 수 있는 존재. 한 사람, 한 사람이 일인군단(一人群團)이라 불리는 S급 헌터들 말입니다.”

바로 그 순간.

쏴아아아악-!

모두의 머리 위에서 눈부신 빛무리가 터져 나왔다.

휘황한 빛과 함께, 예리한 검에 베인 것처럼 갈라지는 허공이 보였다. 보이지 않는 공기를 계단처럼 밟으며 내려오는 세 사람도.

「증조모께서는 어린 나를 무릎에 앉혀 두고 종종 말씀하셨지. 왕족은 신분에 걸맞은 의무를 다해야 한다고. 평민인 자네들은 모르겠지만 말이야.」

나는 실소를 흘리며 허리를 굽혔다. 평소에는 재수 없기 짝이 없는 놈이지만, 이번만큼은 장단을 안 맞춰 줄 수가 없다.

“필릭스 왕자 전하.”

「그대의 입으로 들으니 듣기 좋구나, 진. 동양의 헌터여.」

한껏 고고한 필릭스 왕자의 태도에, 옆에 있던 미녀가 혀를 찼다.

「얘 좀 어떻게 해 줄 수 없니? 아예 입을 틀어막든가.」

“오늘은 봐줘야 할 것 같은데요. 누나.”

「어머.」

내 대답에 눈을 동그랗게 뜬 파이 첸이 이내 배시시 웃어 보였다.

「듣기 좋네. 온 보람이 있어. 안 그래요?」

파이 첸의 물음에, 마지막 한 사람이 껄껄 웃었다.

「이렇게 되면 나도 뭔가를 기대해 봐도 되는 건가? 어떻게 생각해, 진?」

“왜, 키스라도 해 드려요?”

「오, 나쁘진 않군. 하지만 정중하게 거절하지. 나는 이미 사랑하는 프레드와 결혼했고, 입양한 자식도 다섯이나 있으니까.」

쉬이이익. 탁.

허공을 미끄러져 내려온 그, 매직 존슨이 솥뚜껑만 한 손바닥으로 내 어깨를 두드렸다.

「진. 이 용감한 꼬마 녀석. 도대체 어떻게 이런 위험한 텔레포트를 할 생각을 한 거야? 몇 번이나 포기할 뻔했어.」

“하지만 결국 존슨도 하셨잖아요.”

「확률이 달랐어. 이번에는 실패할 확률이 10%뿐이었다고. 넌 나보다 최소한 80%는 용감한 녀석이야.」

용기에는 크기가 없다. 죽음을 무릅쓰고 이 자리에 왔다는 것 자체만으로도, 그들은 세계 최고의 헌터라고 불릴 자격을 입증했다.

그리고 예상치 못한 지원군을 맞이한 사람들은, 믿을 수 없다는 듯 눈을 부릅떴다.

「파, 파이 첸?」

「필릭스 왕자와 매직 존슨도 있다!」

「S급 헌터들이다! S급 헌터들이 우리를 도우러 왔어!」

「I love you, Johnson! fucking nice gay!」

하지만 그것으로 끝이 아니었다.

쿵, 쿵, 쿵.

앞서 느꼈던 것과는 다른, 또 다른 종류의 진동.

그것은 걸음을 맞춰 이동하는 수많은 군세(軍勢)의 등장을 알리는 신호였고, 그들은 저 멀리 까마득한 지평선을 메우며 한 줄기의 점으로 모습을 드러냈다.

「우리가 무턱대고 온 줄 알았어?」

파이 첸이 씩 웃으며 말을 이었다.

「서부, 동부를 합쳐 1만이야. 이 정도라면 너희가 빠져나갈 시간 정도는 벌어 줄 수 있겠지.」

누군가의 입에서 넋 나간 음성이 흘러나왔다.

「이제는 살 수 있어…….」

그리고 그에 대답하는 목소리가 있었다.

“아닙니다.”

최 팀장. 그가 [영웅의 혼]을 치켜세웠다.

짙은 안개에서도 투명한 검신은 아름답게 빛났다.

“우린 승리할 겁니다.”

나 역시 그렇게 믿는다.
```

## Final English reading copy

```markdown
# Chapter 414

Some faces are never a welcome sight, no matter how many times you see them. For me, Lee Jungryong and Wu Heixing fell squarely into that category.

Even so, I was the one who spoke first because Wu Heixing looked almost presentable today.

“Fancy seeing you here. I thought I’d never see you again.”

At my cheerful greeting, Wu Heixing—looking like he had been dragged through a war—shot me a venomous glare.

“Shut up.”

“Oh…”

“Say one more word, and on my grandfather’s honor, I’ll tear you limb from limb.”

*A Chinese knockoff of Kindaichi, is he?* I could never understand why people like him treated their late grandfathers’ honor like a credit card.

I opened my mouth with a serious expression.

“Were you and your grandfather not on good terms?”

“What?”

“No, I mean, think about it. Why swear on your grandfather’s honor over something impossible? You’d be much better off swearing on getting torn limb from limb yourself…”

“You fucking bastard!”

As Wu Heixing sprang to his feet with an enraged shout, Lee Jungryong raised a hand to stop him.

“That’s enough.”

“Mr. Lee! But this bastard…”

“Fighting among allies when we’re about to face the final battle is entirely counterproductive. Calm yourself.”

*Crack.*

Wu Heixing ground his teeth hard enough to splinter them, then glared at me.

“Yes, sir. Since Mr. Lee has gone so far as to say that, I’ll stop here.”

“Good thinking.”

*Was he really the type to back down so obediently?*

As I watched Lee Jungryong, who wore a gentle smile around his lips, I turned my head slightly.

I could read countless thoughts in the brief glance I exchanged with Team Leader Choi.

“What about you, Jin Taekyung?”

I broke eye contact with Team Leader Choi and casually shrugged.

“When an elder speaks, you have to listen.”

“I didn’t know you were the sort to care about things like that.”

“Respect your elders, right?”

At my calm, unruffled answer, Lee Jungryong gave a hearty laugh whose meaning I could not decipher. Wu Heixing glared at me as if he wanted to kill me all over again.

“Respect your elders? Spare me that bullshit. What about me? I’m seven years older than you.”

“If you don’t want to write your will, start by making your eyes look nicer.”

“You turtle-dick-looking bastard…!”

“Don’t bullshit me.”

Wu Heixing’s second outburst was cut short.

I fixed him with a cold stare and continued.

“If you still have enough energy left to lose your temper over something this trivial, go check on the condition of the friends you brought here.”

“…”

“They followed you this far with their lives on the line. They’re not disposable supplies you use once and throw away.”

I made no attempt to hide my contempt.

There were barely fifty Hunters left around Wu Heixing.

According to the report from headquarters, the suicide squad had set out with five hundred people. Most of them had either died or fallen behind.

“Losses? Sure, that can happen. We’re in the middle of a battle. But…”

Even though Wu Heixing’s armor was drenched in blood, its exterior was still intact. That meant he had fought while taking care to protect himself even as his comrades died around him.

“Got anything to say, you fucking idiot?”

A line from an old superhero movie I had seen as a kid came to mind.

*With great power comes great responsibility.*

And that did not apply only to someone bitten by a radioactive spider.

If you were someone who could draw an aura blade instead of spiderwebs, someone who had used it to amass immense wealth and fame while covering up the crimes you had committed, then you had a responsibility to bear. At the very least, that was what I believed.

“You might be S-rank, but you’re no Hunter. So from now on, when you introduce yourself, don’t say you’re a Hunter. Just say, ‘I’m Wu Heixing, the lucky S-rank.’ Got it?”

“…”

As Wu Heixing silently trembled with his fists clenched, Lee Jungryong spoke in his place.

“He did his best.”

“Looking at that armor, I’m not so sure. It looks like I could wipe it down and put it on Junggonara as used equipment right now.”

[^1]: Junggonara is a popular Korean online marketplace for secondhand goods.

“Wearing sturdy, high-quality armor is not a reason to criticize him.”

“I’ve felt this since last time, but you take his side an awful lot. Did that bastard happen to get some kind of leverage over you?”

“Everyone has weaknesses. And I happen to be quite good at hiding mine.”

“Have your computer checked. Who knows? Maybe Chinese hackers have shared videos of the Vice Guild Master watching porn in a group chat.”

“I’ll keep that in mind.”

*He really is a formidable opponent.*

Lee Jungryong smiled without the slightest sign of disturbance, but the man standing behind him was different.

I waved at the man radiating a faint killing intent.

“Look who it is. Team Leader Seok. Isn’t that our Go Jun?”

Lee Jungryong’s Head of Security and Disciple.

I distinctly remembered beating him half to death before we left for China, but the man standing before me looked not merely fine, but even more solid than before.

Even from his deeper, more penetrating gaze, I could tell that his skills had advanced another step.

*And he’s developed patience, too.*

Go Jun was the most loyal of all the loyal hounds Lee Jungryong had raised.

In the past, he would have rushed at me without hesitation. But this time, he had gathered up his killing intent until not a trace remained and chosen silence instead of drawing his weapon.

Lee Jungryong looked pleased by his Disciple’s behavior and opened his mouth.

“We’ve made it right to the Arch Lich’s doorstep. According to the coordinates, only twenty kilometers remain.”

I swept back my hair, which was sticky with blood.

“Probably the longest and fiercest twenty kilometers on Earth.”

“That’s right. The Arch Lich has kept sufficient forces in reserve.”

“How many?”

“An estimated fifty thousand.”

The moment those words left his mouth, a single groan escaped from among the suicide squad, who had all been listening to our conversation with every nerve.

The suicide squads led by me, Lee Jungryong, and Wu Heixing numbered roughly five hundred in total.

Even by a simple estimate, the thought of breaking through an army a hundred times larger to reach the Arch Lich was enough to fill them with horrifying despair.

Perhaps that was why someone shouted in a trembling voice.

“We should retreat while we still can!”

Like a collapsing dam, the cries of other Hunters followed.

“Fuck!”

“There are too many monsters!”

“We’ll all be wiped out if we keep this up!”

“I came here to defeat the Arch Lich, not to die a meaningless death!”

The roughly two hundred members of the Western Front’s suicide squad, who had made it this far with barely any losses, were no exception.

And yet, even amid fear spreading like wildfire, two people remained unshaken.

Shao Shen, looking at me with unwavering trust, and…

“There’s a possibility.”

Team Leader Choi had gone beyond simply trusting me. He had independently deduced one possible explanation for the situation. He continued in a calm voice.

“An estimated fifty thousand is far beyond the number predicted by the High Command.”

“Then shouldn’t we obviously retreat?”

At the shout from one of the suicide squad members, Team Leader Choi immediately shook his head.

“And the number of monsters we faced was also lower than expected.”

“Huh?”

“There were certainly many of them, but the monster forces we encountered on the front lines were not as overwhelming as we anticipated.”

“Then…”

“The Arch Lich may have been wary of exactly this situation. Rather than commit all its forces to the front lines, it kept an army of fifty thousand in reserve as a final move that could respond to any situation.”

The Hunters staring at Team Leader Choi grew rigid. Not because they had properly understood what he was saying, but because of the vibrations growing steadily stronger beneath their feet.

*Grk. Gr-r-r-r-rk.*

The rumbling could be felt from dozens of kilometers away, and everyone’s body trembled.

A ruined road stretched before us, with vast plains on either side. Beyond the thick fog filling every direction, the roars and footsteps of tens of thousands of monsters merged into one faint, distant thunder.

“Grooooooar!”

“This is insane…”

“Run. We have to run. This is a battle we can’t win.”

People began to shuffle backward.

The only exception was the Ares Guild members, who stood firm without wavering. In front of them, Lee Jungryong watched Team Leader Choi with interest.

“So?”

Their eyes met across the open air. I saw Team Leader Choi’s grip tighten around **Hero’s Soul**.

“Although the High Command’s prediction was wrong, the front lines must have had forces to spare because the Arch Lich did not launch an all-out attack.”

“Even so, our forces were still insufficient compared to the enemy.”

“That is exactly why those people were left behind.”

*Grk. Gr-r-r-rk.*

The vibrations and roars grew even stronger. Amid the murmuring of people filled with anxiety and agitation, a single sentence from Team Leader Choi, carried by mana, pierced everyone’s ears.

“People who can overturn the entire course of a battle in an instant. S-rank Hunters—individuals who can each be called a one-person army.”

At that exact moment—

*Fwoooooosh!*

A dazzling mass of light burst above everyone’s heads.

Amid the brilliant radiance, the air split apart as if sliced by a sharp sword. Three people descended, stepping on invisible air as though it were a staircase.

“When I was a child, my great-grandmother would sit me on her lap and often tell me that royalty must fulfill the duties befitting their station. Of course, commoners like you would not understand.”

I let out a snort and bowed at the waist. He was usually annoying beyond belief, but this time I had no choice but to play along.

“His Highness, Prince Felix.”

“It is pleasing to hear it from your lips, Jin. Hunter of the Orient.”

At Prince Felix’s lofty, self-important attitude, the beautiful woman beside him clicked her tongue.

“Can’t you do something about him? At least tape his mouth shut.”

“I think we should indulge him today, big sis.”

“Oh my.”

Faye Chen opened her eyes wide at my answer, then broke into a bright smile.

“That sounds nice. Coming here was worth it after all. Don’t you agree?”

At Faye Chen’s question, the last person laughed heartily.

“Does this mean I can hope for something as well? What do you think, Jin?”

“What, should I kiss you?”

“Oh, that wouldn’t be bad. But I’ll politely decline. I’m already married to my beloved Fred, and I have five adopted children.”

*Fwoosh. Thump.*

Sliding down through the air, Magic Johnson patted my shoulder with a palm as large as a pot lid.

“Jin. You brave little rascal. How did you even think of attempting such a dangerous teleport? I almost gave up several times.”

“But you did it too, Johnson.”

“The odds were different. This time, there was only a ten percent chance of failure. You’re at least eighty percent braver than I am.”

Courage didn’t come in sizes.

Simply by risking death to come here, they had proved themselves worthy of being called the greatest Hunters in the world.

And the people who had received this unexpected reinforcement stared wide-eyed as if they could not believe what they were seeing.

“F-Faye Chen?”

“Prince Felix and Magic Johnson are here too!”

“They’re S-rank Hunters! S-rank Hunters came to help us!”

“I love you, Johnson! Fucking nice gay!”

But that was not the end.

*Boom. Boom. Boom.*

Another vibration, different from the one we had felt moments earlier.

It was the signal announcing the arrival of countless forces advancing in step. Far away, they appeared as a thin line of dots stretching across the distant horizon.

“Did you think we came all this way without a plan?”

Faye Chen continued with a grin.

“Ten thousand from the Western and Eastern Fronts combined. That should be enough to buy you time to get out.”

A dazed voice escaped someone’s lips.

“Now we can survive…”

“No.”

It was Team Leader Choi.

He raised **Hero’s Soul**.

Even through the dense fog, the transparent blade shone beautifully.

“We’re going to win.”

*I believed it too.*
```
