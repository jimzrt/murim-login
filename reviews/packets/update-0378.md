<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0378.txt",
      "sha256": "962bd52f1b903b50cf75748c160b649bef3de97e2e63ac797847b344fc841bc6",
      "bytes": 13072
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1ed938e32675caf3e638f8c00404a8c17170b1cb650deaec82bfdfe6ca08b656",
      "bytes": 2750
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1853b5e96124f7d86a1921953bf2f03c5d6d91526a0f20b684fc6893835cffb1",
      "bytes": 130730
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6e9436e62872f2ba5c0905cf5b749b597c678c7896be0e9036a5e9c7aa1ff345",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5252815e902bad0a15c6b38b4648d1895f08810df2dd373dc00b1d8cafe323a1",
      "bytes": 622
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "29f80cc67a6ec20a06d24939b5730372758221eb5b19d459f6b3665aed2ceab5",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "83568e215496f1e1430b4ff7cfe8798a6a757be14c0019077b3a9e3996974d59",
      "bytes": 100928
    }
  ],
  "estimated_tokens": 9181
}
-->

# Durable State Update — Chapter 378

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 378. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 378. Profile updates may replace only one
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
  "chapter": 378,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 378,
    "continuity_sources": [378],
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; Mungyeong captured the Third Fiend in the hidden cavern, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake, has reached Level 120 and the Supreme Peak realm, manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang.",
    "Mungyeong is the Divine Physician and former Slaughter Saint; he has sworn never to kill again and intends to live as a physician.",
    "Dong Feng is Mungyeong's Disciple and has served him for decades after Mungyeong saved him from an epidemic.",
    "Hyuk Mujin and Gung Gibang remain badly wounded after fighting the Third Fiend.",
    "Cheongpung remains a Supreme Peak master at the Sichuan Tang Clan with Mimi and is now Mimi's temporary guardian.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring is now bound to Jin Taekyung, alongside White Flame and the Fire Dragon Armor.",
    "Aehyang is manipulating the Sichuan City Lord under the direction of an unidentified person, while Jin Taekyung's party travels down the Yangtze aboard three Water Dragon Stronghold ships."
  ],
  "continuity_sources": [
    377
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Will Mungyeong remain outside the coming war, or will the crisis force him to intervene?"
  ],
  "safe_through": 377,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address.",
    "Render 환영진 as illusion formation and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, and 화룡갑 as Fire Dragon Armor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 시스템              | **System**                     |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 드레이크 | **Drake** | High-tier dragonkin monster. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 377
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 377
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 377
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃378화



띠링.



- [로그아웃]을 성공적으로 완료했습니다.



경쾌한 시스템 알림과 함께, 잠시 떨어져 나갔던 감각들이 돌아오기 시작했다.

등을 타고 전해지는 침대의 푹신함, 전용기 내부의 따뜻한 공기.

그리고 내 양어깨를 잡고 흔드는 누군가의 손길과 외침까지.

“진태경 씨! 일어나십시오! 진태경 씨!”

- 일어나라! 간악한 인간아!

귓가를 파고드는 다급한 두 사람, 아니 한 몬스터와 인간의 목소리에 눈동자를 깜빡였다.

선명해지는 시야 속, 익숙한 얼굴이 눈에 들어왔다.

“어, 최 팀…….”

쫘악!

“일어나라고!”

- 잘했다! 조금 덜 간악한 인간이여!

“…….”

뭐야, 이거.

생각지도 못한 따귀 한 방을 얻어맞은 나는 얼떨떨한 목소리로 대답했다.

“저 일어났는데…….”

“도대체 어떻게 된 사람입니까! 그렇게 깨웠는데 왜 이제야 일어나요!

- 죽어, 그냥 죽어!

“죄, 죄송…….”

박력 보소. 이 정도로 극대노한 최 팀장을 보는 건 처음이다.

무슨 일이 벌어져도 침착을 유지하며 명품이나 자랑하던 최 팀장의 눈에서 번갯불이 튀고 있었다.

‘그런데 왜 저래. 아직 비행기 안인 것 같은데.’

엉겁결에 사과하긴 했는데, 이게 따귀까지 맞을 일인가 싶어 어리둥절하던 그 순간.

“지금 이럴 때가 아닙니다! 어서……!”

“꺄아아악!”

이어지려던 최 팀장의 목소리가 스튜어디스들의 비명에 파묻혔다. 조종사로 짐작되는 남자들의 외침이 뒤를 이었다.

“메이데이! 메이데이! 메이데이!”

“관제탑! 관제타아압!”

“……뭐여, 시벌.”

도대체 지금 무슨 일이 벌어지고 있는 거지?

정신없이 주위를 둘러보는 내게, 최 팀장의 믿을 수 없는 한마디가 날아들었다.

“몬스터의 습격입니다!”

“몬스터? 습격?”

뭔 개소리야. 우리는 중국 중앙위원회에서 보내 준 전용기를 타고 2만 5천 피트 상공을 날아가는 중이었는데.

지금쯤이면 목적지인 쓰촨성 청두 국제공항이 보여도 이상하지 않을…….

“어?”

무심코 고개를 돌려 창밖을 확인한 나는 멍하니 입을 벌렸다.

까마득한 높이로 내려다보이는 거대한 규모의 공항에서, 불길이 솟구치고 크고 작은 점들이 움직였다.

전투다. 인간과 몬스터 간의 죽고 죽이는 전투가 벌어지고 있었다.

심지어 그것으로 끝이 아니었다.

- 캬우우우우!

내가 타고 있는 전용기를 향해 빠르게 가까워지는 몬스터의 거대한 동체.

“저건…….”

틀림없다. 두 눈을 비비고 다시 봐도 와이번(Wyvern)이다.

드레이크와 함께 용족(龍族)으로 분류되는 A급 몬스터.

물론 땅에서 만나도 지랄 같지만, 2만 5천 피트 상공에서는 더더욱 만나기 싫은 놈들이 나타났다.

그것도 무려 십여 마리나!

‘……이게 무슨 개 같은 상황이야.’

지상에서는 청두 국제공항을 둘러싼 치열한 전투가 벌어지고, 2만 5천 피트 상공에서는 와이번 무리가 내가 탄 전용기를 쫓아 오고 있다.

잠깐 정지했던 두뇌가 결론을 도출해 내기까지는 그리 오랜 시간이 필요하지 않았다.

“리치(Rich)!”

나도 모르게 벼락처럼 튀어나온 외침.

현대 시간으로 일주일 전, 유례없는 몬스터 웨이브와 함께 나타난 최상위 언데드 몬스터가 어느새 여기까지 마수를 뻗친 것이 틀림없었다.

“관제탑이 응답하지 않습니다!”

“와이번이, 와이번이……!”

“끼아아아악!”

- 내 이럴 줄 알았다! 우린 이제 다 죽은 목숨이야!

나는 당황한 와중에도 스켈레톤 워로드의 말을 정정해 주었다.

“맞는 말이긴 한데, 넌 이미 죽은 목숨 아니었냐?”

- 닥쳐라, 이 간악한 인간! 모든 게 너 때문이다! 아아, 군단이여! 본 사령관을 용서하라!

몬스터고 인간이고 할 것 없이 패닉에 빠진 비명과 고함이 사방에서 빗발쳤다.

이들 중 그나마 이성을 유지하고 있는 건 한 사람뿐이었다.

“모두 진정하세요! 걱정하시는 일은 일어나지 않을 겁니다!”

역시 최 팀장, 믿음직하다. 분명 이 위기를 타개할 만한 수를 생각해냈음이 틀림없다.

침착한 어조로 혼란을 가라앉힌 최 팀장이 나를 가리켰다.

“여기 계신 진태경 씨가 해결해 줄 겁니다!”

“……?”

“진태경 씨. 어떻게 해야 합니까?”

“아니, 왜 그걸 저한테…….”

“저는 진태경 씨를 믿습니다!”

“…….”

그러니까 왜 날 믿냐고. 지금 같은 상황이면 하느님이나 부처, 알라를 믿는 게 더 도움이 될 것 같은데.

순간 할 말을 잃은 나를 향해 사람들의 시선이 우수수 날아와 꽂힌다.

“그, 그러고 보니 저 헌터님에 관해서 들은 적이 있어. 샤오 양 주석 동지께서도 특별히 요청할 만큼 대단한 실력자라던데.”

“저도 소문은 들었습니다. 어쩌면 새로운 S급 헌터일지도 모른다고. 네임드 몬스터를 둘씩이나 혼자서 잡았대요.”

“오오, 오오오!”

“살았다! 우린 살았어!”

- 너, 간악한 인간! 강한 줄은 알았지만 상상 이상이로군! 기뻐하라, 군단이여. 본 사령관은 살았다!

“……넌 이미 죽었다니까.”

미치겠네. 이미 전부 다 제정신이 아니다. 나는 어처구니없는 눈빛으로 최 팀장을 바라보았다.

“도대체 뭘 믿고 이러는 겁니까?”

최 팀장이 망설임 없이 대답했다.

“말했잖습니까. 진태경 씨를 믿는다고요.”

“그러니까 그 근거 없는 믿음이 어디서…….”

“근거 있는 믿음입니다.”

“예?”

“지금 같은 상황에서 진태경 씨가 보여 주는 태도, 말투, 표정. 그 모든 것들이 제 믿음에 대한 근거입니다.”

“……!”

그제야 비로소 깨달을 수 있었다. 지금의 나는 예기치 못한 상황에 당황했을 뿐, 그 어떤 두려움이나 공포도 느끼지 못하고 있다는 사실을.

정답은 생각보다 가까이에 있다.

‘강하니까.’

나는 강하다. 더욱더 강해졌다. 그 어떤 위험도 피해 갈 수 있을 만큼.

그것이 지상을 파도처럼 휩쓸고 있는 몬스터들도, 바짝 뒤를 쫓아오는 와이번 무리도 두렵지 않은 이유였다.

“그렇다는 거지…….”

내심 작게 중얼거린 나는 입을 열었다.

“기장이 누굽니까?”

내 물음에 저 앞 조종석에서 손 하나가 불쑥 솟아올랐다.

바들바들 떨리는 손. 나머지 한 손으로는 필사적으로 조종간을 붙잡고 달려드는 와이번을 피하려 안간힘을 쓰고 있을 것이다.

“저, 접니다만.”

“잠깐만 문 열어도 돼요?”

“예?”

“비행기 문 좀 열어도 되냐고요.”

얼마나 충격적이었는지, 기장이 미친놈 보는 듯한 시선으로 고개를 내밀었다.

“당연히 안 됩니다! 기압 차단 장치 때문에 열지도 못할뿐더러, 기체가 기압을 감당하지 못하고 파손될 겁니다! 그러면 호흡도 제대로 할 수 없어요!”

최 팀장이 손가락에 끼고 있던 반지를 만지작거리며 끼어들었다.

“기압은 제가 막을 수 있을 것 같습니다. 무슨 생각이신지는 모르지만 한 번 해보시죠.”

“오케이.”

“하지 말라고! 이 빵즈(棒子) 놈들아! 우릴 다 죽일 셈이냐!”

“……뭐, 빵즈?”

감히 자랑스러운 대한의 김치맨 앞에서 한국인을 비하하는 말을 하다니.

무심코 튀어나온 말실수를 알아차린 기장의 얼굴이 하얗게 질렸다.

“아니, 그게 아니고.”

“짱깨 새끼가. 팍 씨.”

“……!”

“야, 기장!”

“예, 예?”

“연다?”

“앗. 아앗!”

기장이 말릴 틈도 없이 나는 문을 열었다. 아니, 잘랐다.

스걱!

강기(劍罡). 현대에서는 오라 블레이드(Aura Blade)라 불리는 그것이 단단한 합금을 가르며 작은 문을 만든다.

무림의 초절정 고수가 그렇듯, 이곳에서는 S급 헌터만이 보여 줄 수 있는 강대한 힘.

최 팀장의 눈동자가 경악으로 부릅떠졌다.

“진태경 씨, 이건……!”

“팀장님!”

콰아아아아!

지금 놀라고 있을 때가 아니다. 엄청난 바람과 기압으로 기체가 휘청이고 기내는 엉망이 되고 있었으니까.

사람들의 비명과 내 외침에 정신을 차린 최 팀장이 반지를 문질렀다.

“빈틈없는 장벽이 주위를 감싼다. 배리어(Barrier)!”

“오.”

주문 영창과 함께 투명한 기의 막이 새로운 입구를 물 샐 틈 없이 가로막았다.

이런 방법이 있었구나. 나는 짧은 감탄과 함께 기내 밖으로 상반신을 내밀었다.

나를 아군으로 인식한 최 팀장의 배리어 마법은 아무런 제지 없이 통과시켜 주었다.

쿠구구구구!

압사라도 시킬 것처럼 상반신을 후려치는 풍압에 나는 씩 웃었다.

‘이거, 장난 아닌데?’

하지만 못 견딜 정도는 아니다.

아니, 내가 못 견디는 것이 오히려 이상했다. 서천마군이 내뿜던 기파에 비교하면, 이 정도는 살랑거리는 봄바람이나 다름없었으니까.

- 캬우우우우!

바로 그 봄바람에, 몬스터의 날카로운 괴성이 섞여 들어온다.

나는 어느새 지척까지 다가온 와이번 무리를 보며 거리를 가늠했다.

‘약 백여 미터. 한 번도 해 본 적은 없지만…… 이 정도 거리라면 충분하겠지.’

인벤토리 오픈. 장착.

스윽.

헌터 마켓에서 할인 구매한 창 한 자루가 손아귀에 잡힌다.

나는 창 던지기 선수처럼 어깨를 한껏 뒤로 젖혔다. 허리부터 손목까지. 필요한 근육과 힘줄이 활시위처럼 팽팽하게 당겨졌다.

- 캬우우!

뭔가 이상함을 눈치챈 선두의 우두머리 와이번이 괴성과 함께 고개를 젖혔다.

새하얀 기류가 놈의 주둥이를 향해 빨려 들어가는 것이 보였다.

‘저건…….’

- 브레스! 브레스다! 피해라, 간악한 인간이여!

스켈레톤 워로드의 외침은 정답이었다.

무수히 많은 몬스터 중에서도 오직 용족에게만 허락된 권능. 바로 브레스(Breath)가 쩍 벌어진 주둥이 안에서 형체를 갖추는 광경이 똑똑히 보였다.

고오오옹.

거대한 바람의 구(球). 금속을 종잇장처럼 갈기갈기 찢어 버릴 수 있는 에어 브레스가 완전한 형체를 갖춘 그때.

“야, 와이번!”

- 캬우?

“넣는다!”

나는 벼락처럼 외치며 한껏 젖혔던 어깨를 전방으로 뿌렸다.

화륵, 쐐애애애액!

창날에 서린 화염의 강기가 공기를 태우고 바람을 가른다.

일직선으로 뻗어 나가는 청백색의 빛줄기에, 와이번의 샛노란 눈동자가 크게 뜨였다.

- 키이이익!

후우우웅!

창날의 끝에서 터져 나가는 압축된 공기. 새하얀 구름. 그리고…….

퍼걱! 퍼버벙!

마치 실이 끊어진 연처럼, 지상을 향해 추락하는 거대한 동체가 있었다.



* * *



- 캬우?

- 키잇?

십여 쌍의 샛노란 눈동자들이 서로를 바라본다.

날 때부터 흉포하기 짝이 없는 와이번이지만, 지금 이 순간만큼은 당혹감에 사로잡혀 어찌할 바를 몰랐다.

- 키키킷?

- 키익…….

뭐야, 대장 죽은 거야?

아마 그런 것 같은데…….

자신들만의 대화를 주고받은 와이번들은 황당했다.

그들의 우두머리는 동족 중에서도 ‘검은 별’이라 불릴 만큼 강한 존재였다.

그리고 지금, 검은 별은 검은 점이 되어 까마득한 지상으로 추락하는 중이었다.

- 키리릭?

- 크르르륵.

심지어 어떻게 죽었는지 제대로 본 놈도 없었다.

다만 저 콩알만 한 인간 하나가 창을 던져서 맞추지 않았나 짐작할 뿐이다.

하지만 말도 안 되는 소리다.

어떻게 인간 따위가 감히 위대한 드래곤의 후예를…….

“야, 거기 그린 와이번!”

- 키릭?

“넣을게!”

퍼걱!

이번에는 똑똑히 볼 수 있었다. 빛줄기에 터져 나가는 동료의 머리통을.

- 키릭!

- 캬우우우!

대장에 이어 또 다른 혈족이 죽다니!

극도로 분노한 와이번들은 저 빌어먹을 인간에 대한 복수를 다짐했다.

- 키잇!

물론 오늘은 아니고. 나중에, 조금 더 나중에 복수하기로.

“야, 거기 블루 와이번!”

퍼걱!

……복수, 할 수 있을까?

십여 쌍의 날개가 필사적으로 퍼덕이기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 378

Ding.

> **System**
>
> **Logout** completed successfully.

Along with the cheerful System notification, the sensations that had briefly fallen away began to return.

The softness of the bed against my back. The warm air inside the private jet.

And the hands gripping and shaking both my shoulders, along with someone's shouting.

“Mr. Jin Taekyung! Wake up! Mr. Jin Taekyung!”

—Wake up, you wicked human!

At the urgent voices drilling into my ears—two voices, no, one monster and one human—I blinked.

As my vision cleared, a familiar face came into view.

“Uh, Team Leader Choi…”

Smack!

“Wake up!”

—Well done, you slightly less wicked human!

“…”

What the hell?

After taking a completely unexpected slap, I answered in a dazed voice.

“I’m awake…”

“What is wrong with you?! We’ve been trying to wake you up! Why are you only getting up now?!”

—Just die! Go ahead and die!

“S-Sorry…”

Talk about forceful. This was the first time I had ever seen Team Leader Choi this furious.

Lightning was practically shooting from the eyes of the man who usually remained calm no matter what happened and spent his time showing off designer goods.

*But what’s wrong with him? We’re still on the plane, aren’t we?*

I had apologized reflexively, but I was still bewildered. Was this really enough to earn a slap?

Then—

“This is no time for this! Hurry—”

“Aaaah!”

The rest of Team Leader Choi’s words were drowned out by the flight attendants’ screams. Shouts from men I presumed were the pilots followed.

“Mayday! Mayday! Mayday!”

“Control tower! Control toweeer!”

“…What the hell?”

What on earth was happening?

As I frantically looked around, Team Leader Choi threw out an unbelievable statement.

“We’re under attack by monsters!”

“Monsters? An attack?”

What kind of bullshit was this? We were flying at an altitude of twenty-five thousand feet in a private jet sent by China’s Central Committee.

By now, it shouldn’t have been strange to see our destination, Chengdu International Airport in Sichuan Province—

“Huh?”

I absentmindedly turned my head to look out the window, then stared with my mouth hanging open.

Far below, a vast airport spread out beneath us. Flames surged upward, and countless large and small dots moved across the grounds.

It was a battle. A savage fight to the death between humans and monsters was taking place.

And that was not all.

—Kyaoo-o-o-o!

A gigantic monster’s body rapidly approached the private jet I was riding in.

“That’s…”

There was no mistaking it. Even after rubbing my eyes and looking again, it was a Wyvern.

An A-rank monster classified as dragonkin alongside the Drake.

They were bastards I would hate to encounter even on the ground, but I especially did not want to meet them at twenty-five thousand feet.

And there were more than ten of them!

*…What the hell kind of situation is this?*

A fierce battle was raging around Chengdu International Airport below, while a group of Wyverns pursued the private jet I was riding in at twenty-five thousand feet.

It did not take my temporarily frozen brain long to reach a conclusion.

“Lich!”

The name burst from my mouth like lightning.

A week ago, by modern-world time, the highest-tier undead monster had appeared alongside an unprecedented monster wave. It had undoubtedly extended its sinister reach all the way here.

“The control tower isn’t responding!”

“The Wyverns, the Wyverns…”

“Kyaaaah!”

—I knew this would happen! We’re all dead!

Even in my panic, I corrected the Skeleton Warlord.

“That’s true, but weren’t you already dead?”

—Shut up, you wicked human! This is all your fault! Ahhh, my legion! Forgive your commander!

Human or monster, screams and shouts erupted from every direction as everyone fell into a panic.

Only one person among them had retained any semblance of sanity.

“Everyone, calm down! Nothing you’re worried about is going to happen!”

As expected of Team Leader Choi. Reliable as ever. He must have thought of a way to overcome this crisis.

After calming everyone down in a steady voice, Team Leader Choi pointed at me.

“Mr. Jin Taekyung will solve this!”

“…”

“Mr. Jin Taekyung, what should we do?”

“Wait, why are you asking me…?”

“I believe in you, Mr. Jin Taekyung!”

“…”

That was exactly the problem. Why did he believe in me? In a situation like this, believing in God, Buddha, or Allah would probably be more useful.

For a moment, I lost my ability to speak. Then the gazes of everyone around me flew toward me and pierced into my body.

“N-Now that you mention it, I’ve heard about that Hunter. They say he’s so capable that even Comrade Chairman Xiao Yang made a special request for him.”

“I’ve heard the rumors too. They say he might be a new S-rank Hunter. Apparently, he defeated two Named Monsters all by himself.”

“Ooh! Ooooooh!”

“We’re saved! We’re going to live!”

—You, wicked human! I knew you were strong, but this is beyond my imagination! Rejoice, my legion. Your commander lives!

“…I already told you, you’re dead.”

This was driving me insane. None of them were in their right minds anymore.

I stared at Team Leader Choi with utter disbelief.

“What exactly are you basing this on?”

Team Leader Choi answered without hesitation.

“I already told you. I believe in you.”

“Which means, where does that baseless faith—”

“It is not baseless.”

“Excuse me?”

“The way you are acting in a situation like this. Your tone of voice. Your expression. All of it is the basis for my belief.”

“…”

Only then did I finally realize it.

I had been caught off guard by the unexpected situation, but I was not afraid. I did not feel even the slightest bit of fear or dread.

The answer was closer than I had thought.

*Because I’m strong.*

I was strong. Stronger than before. Strong enough to avoid any danger.

That was why I was not afraid of the monsters sweeping across the ground like a wave, or the pack of Wyverns closing in right behind us.

“So that’s how it is…”

I muttered quietly to myself, then opened my mouth.

“Who’s the captain?”

A hand suddenly rose from the cockpit ahead.

It was trembling violently. With his other hand, the captain was probably gripping the controls for dear life and desperately trying to evade the Wyverns charging at us.

“I-I am.”

“Can I open the door for a moment?”

“What?”

“I’m asking if it’s okay for me to open the plane door.”

The captain must have been so shocked that he poked his head out and stared at me as if I were insane.

“Of course not! Not only is it impossible to open because of the pressure-sealing system, but the aircraft will be damaged because it can’t withstand the pressure difference! You won’t even be able to breathe properly!”

Team Leader Choi fiddled with the ring on his finger and cut in.

“I think I can block the pressure. I don’t know what you have in mind, but go ahead and try.”

“Okay.”

“Don’t! You *bangzi* bastards! Are you trying to kill us all?!”

“…What, *bangzi*?”[^1]

[^1]: *Bangzi* is a derogatory Chinese term for Koreans.

I could not believe he had insulted Koreans in front of a proud Korean Kimchi Man.

The captain’s face went pale when he realized his verbal slip.

“No, that’s not what I meant.”

“You chink bastard. Damn it.”

“…”

“Hey, Captain!”

“Yes, yes?”

“Should I open it?”

“Ah! Aah!”

Before the captain had time to stop me, I opened the door.

No—I cut it open.

Slice!

Force—the phenomenon called an Aura Blade in modern times—cut through the sturdy alloy and created a small opening.

It was the kind of overwhelming power that only an S-rank Hunter could display here, just as a Supreme Peak master could in the Murim.

Team Leader Choi’s eyes widened in shock.

“Mr. Jin Taekyung, this is…”

“Team Leader!”

Whoooosh!

This was no time to be surprised. The tremendous wind and pressure had sent the aircraft swaying, turning the cabin into a complete mess.

Team Leader Choi came to his senses at the people’s screams and my shout, then rubbed his ring.

“A flawless barrier surrounds us. Barrier!”

“Oh.”

Along with the incantation, a transparent mana barrier blocked the new opening without leaving so much as a gap.

So there was a way to do that.

With a brief exclamation of admiration, I stuck my upper body outside the cabin.

Team Leader Choi’s barrier spell recognized me as an ally and let me pass through without resistance.

Rumble, rumble, rumble!

The wind pressure slammed into my upper body as if it wanted to crush me. I grinned.

*This is no joke.*

But it was not unbearable.

No, it would have been strange if I could not withstand it. Compared to the energy waves emitted by the Western Heaven Demon Lord, this was no more than a gentle spring breeze.

—Kyaoo-o-o-o!

The monster’s sharp cry blended into that spring breeze.

The pack of Wyverns had already approached within a short distance, and I estimated the gap between us.

*About a hundred meters. I’ve never tried this before…but at this distance, it should be enough.*

*Inventory, open. Equip.*

Sssshk.

A spear purchased at a discount from the Hunter Market slid into my hand.

Like a javelin thrower, I pulled my shoulder as far back as I could. From my waist to my wrist, every muscle and tendon I needed drew taut like bowstrings.

—Kyaoo!

The leader Wyvern at the front noticed that something was wrong and threw its head back with a shriek.

I could see a mass of pure-white air being sucked toward its snout.

*That’s…*

—Breath! It’s using Breath! Dodge it, wicked human!

The Skeleton Warlord’s shout was correct.

Among countless monsters, Breath was a power granted only to the dragonkin. I could clearly see it taking shape inside the Wyvern’s wide-open maw.

Gooooom.

A gigantic sphere of wind. An Air Breath capable of shredding metal like paper had taken complete shape.

“Hey, Wyvern!”

—Kyaoo?

“I’m putting it in!”

I shouted like a thunderbolt and whipped my pulled-back shoulder forward.

Fwoosh! Sssshaaa!

The Force of flame wrapped around the spearhead, scorching the air and slicing through the wind.

The Wyvern’s bright-yellow eyes widened at the blue-white streak of light shooting straight toward it.

—Kiiiiik!

Whoooosh!

Compressed air burst from the tip of the spear. A cloud of pure white formed, and then—

Crunch! Boom-boom!

A gigantic body fell toward the ground like a kite whose string had been cut.

* * *

—Kyaoo?

—Kiiit?

More than ten pairs of bright-yellow eyes looked at one another.

Wyverns were ferocious creatures from the moment they were born, but even they were utterly bewildered at that moment, unable to figure out what to do.

—Kikik?

—Kiiik…

*What? Is the boss dead?*

*I think so…*

After exchanging words among themselves, the Wyverns were dumbfounded.

Their leader was an exceptionally powerful creature, strong enough to be called the “Black Star” among its kind.

And now, the Black Star had become a black dot as it fell toward the distant ground below.

—Kiririk?

—Grrrrk.

What was more, none of them had properly seen how it died.

They could only guess that the tiny human had thrown a spear and hit it.

But that was ridiculous.

How could a mere human dare to attack a descendant of the great dragon—

“Hey, Green Wyvern!”

—Kik?

“I’m putting it in!”

Crunch!

This time, they saw it clearly.

Their comrade’s head burst apart in the streak of light.

—Kik!

—Kyaoo-o-o!

After their leader, another of their bloodline had died!

The enraged Wyverns swore revenge on that accursed human.

—Kiiit!

Of course, not today.

They would take revenge later. A little later.

“Hey, Blue Wyvern!”

Crunch!

…Could they actually get their revenge?

More than ten pairs of wings began beating for dear life.
```
