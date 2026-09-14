<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0068.txt",
      "sha256": "35c33412c8c8e4cd61c4bea1f8d86d6ce09c6d7174933d9943baadbc257102d4",
      "bytes": 14640
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f77476abcb36cf1c68656821526b6e65c8c663c537e0e3fde0e00334906b4a70",
      "bytes": 2954
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "999fac98cba01ae9e8fe2c7ef48c06d20b6e9f9a3ad7fc6d0c551e9c1ae7cd3a",
      "bytes": 2374
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "df433e5bafedb30b21460ab9f8c03f121395b612c0f32d7cd777bf1b55b9fe66",
      "bytes": 1183
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8134ebf3c1d9709edcd8365f7852b6f4f123fef4e2775620216d32b8467d4af3",
      "bytes": 23754
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "d5ddbddcf5d2bdbb0b0271b630c2a3548cb4ca9af5f7a13a6ff40e43defa54cf",
      "bytes": 8155
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "1bb89ec7df91b89dee7e08a882d67787d5832927851bab32785b260463454022",
      "bytes": 2803
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "b2470cc26f299f65fe1be9b7b917601330f2d5dbf8d4a8c6828e5cc7569143b9",
      "bytes": 4605
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fb2e79375dca5d984dcadd9f140ab392984cadec22907470ed6359da84444a4b",
      "bytes": 2467
    }
  ],
  "estimated_tokens": 11539
}
-->

# Durable State Update — Chapter 68

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 68. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 68. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 68,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 68,
    "continuity_sources": [68],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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
    "Jin Mukyung recognizes Taekyung as a First Rate martial artist standing before the Peak realm and is astonished by his transformation over three years.",
    "Taekyung's spar with Mukyung ends with Mukyung's victory and the destruction of Taekyung's pavilion; Taekyung survives and recovers in the Medicine King Hall.",
    "Hyuk Mujin is badly injured in the incident and remains under treatment after Taekyung is discharged.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder's hidden disciple.",
    "Jin Mukyung reunites with Jin Wikyung after three years but remains detached and prioritizes sword training.",
    "Jin Wikyung plans to summon every sect in Shanxi Province on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin.",
    "Jin Wikyung searched the family's records for Dark Heaven but found no information.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months.",
    "Soyul is five years old and does not know that her parents are dead.",
    "Taekyung is Level 50 with fifty remaining points and fifteen years of internal energy after investing fifty points in Agility during the duel.",
    "Taekyung's bruises largely disappear overnight after circulating his qi and sleeping, which he attributes to Sleep Mode.",
    "Jin Wikyung arranges fifteen days of temporary cohabitation between Taekyung and Jin Mukyung while Taekyung's residence is rebuilt.",
    "Jin Wikyung publicly maintains a formal image but is openly recognized within the family as excessively devoted to Taekyung.",
    "Jin Wikyung stops Taekyung and Mukyung from fighting and requires both brothers to apologize and cooperate."
  ],
  "continuity_sources": [
    67,
    66
  ],
  "open_questions": [
    "The identity of the assassin who attacked Taekyung and Hyuk Mujin remains unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons.",
    "It remains unresolved whether Jin Wikyung will become Alliance Leader."
  ],
  "safe_through": 67,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun.",
    "Use junzi for 군자 with a cultural footnote.",
    "Retain Hyung-nim for 형님 in Taekyung's deferential speech.",
    "Use Three Questions Gorge for 삼문협.",
    "Use Alliance Leader for 맹주 and summon for 소집 to preserve the distinction from an invitation.",
    "Retain Great Hero for 대협 when Taekyung addresses Gong Yacheong.",
    "Use Sleep Mode for 수면 모드.",
    "Use Medicine King Hall Master for 약왕당주."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 아이템              | **Item**                       |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |

## Listed compact profiles

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 67
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother; returns to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 66
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 67
- **Aliases:** None revealed
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 35
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 66
- **Aliases:** None revealed
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃68화



결국 승자는 진위경이었다. 촉촉한 눈망울로 ‘보름만. 아니 열흘만 같이 살면 안 될까?’ 하며 줄기차게 애원하는 통에 나와 진무경은 두 손 두 발 다 들었다.

그래서 결국 이 상황까지 오게 된 거다.

진위경이 자리를 뜨고, 둘만 남은 지하 연무장은 고요하기만 했다.

먼저 침묵을 깨트린 건 진무경이었다.

“규칙을 알려 주마.”

“규칙? 남자들끼리 사는데 뭔 규칙?”

“첫 번째. 지금부터 나를 대할 때는 예의를 지켜서, 존댓말을 쓸 것.”

“싫다면?”

진무경이 옆에 서 있던 수련용 강철 인형을 후려쳤다.

펑! 콰직!

강철 인형이 훨훨 날아 연무장 벽에 처박혔다. 움푹 꺼진 가슴에 수인(手印)이 뚜렷하게 찍혀 있었다.

“첫 번째 규칙이 뭐라고?”

나는 진무경을 노려봤다. 산전수전 다 겪은 나다. 고작 이 정도로 내 기를 꺾을 생각이었다면 단단히 착각한 거지.

“존댓말을 쓰라고 하셨습니다.”

……하지만 성숙한 사회인은 불필요한 싸움을 피하는 법.

이게 바로 어른의 싸움이다. 후후.

‘그런데 왜 눈물이 나려고 하냐.’

아, 엄마 보고 싶다.

“좋아. 그럼 두 번째. 쥐 죽은 듯이 지낼 것. 만약 큰 소리를 내서 내 잠을 깨우거나 수련을 훼방 놓는다면…….”

펑! 콰직!

두 번째 강철 인형이 날아가는 모습에 나는 정신없이 고개를 끄덕였다.

“마지막 세 번째. 연무장을 사용하는 것은 자유지만 내가 비키라면 군말 없이 비켜라. 알겠나?”

“네, 네.”

“이제야 정신을 차렸군.”

만족스럽게 고개를 끄덕인 진무경이 출구를 가리켰다.

“이제 나가. 네 방은 3층이다.”

지하 연무장을 재빨리 빠져나가는 내 등 뒤로 기합 소리가 울려 퍼졌다. 거의 짐짝 취급 하는 모습에 오기가 솟구친다. 잠시 뒤를 돌아보며 다짐했다.

‘기다려라. 곧 따라잡을 테니까.’

쉬이익! 서걱!

검기가 세 번째 강철 인형을 갈랐다. 힘없이 떨어지는 인형의 목을 보며 나는 생각을 살짝 수정했다.

‘기다려라. 언젠가는 따라잡는다.’



* * *



방 안은 삭막했다. 화려하다 못해 호화스럽게 꾸며져 있던 예전 방과는 달리 꼭 필요한 가구 몇 개가 전부였다.

“아무리 그래도 이건 심한데.”

진무경답다고 해야 하나?

만난 지 하루밖에 되지 않았지만 진무경의 성향을 파악하는 데에는 충분했다. 거추장스러운 건 질색이고, 효율을 중시하는 타입. 수련을 게을리하지 않는 노력파이기도 하다.

“…….”

뭐야, 생각하면 할수록 대단한 놈이잖아?

존댓말 안 썼다고 친동생을 개처럼 두들겨 패는 과격한 면모도 있지만, 곰곰이 생각해 보면 정당방위다.

역지사지(易地思之). 인간관계의 기본 아닌가.

‘나 같아도 이런 놈이 동생이면 두들겨 패고도 남았지.’

형들은 가문 일으켜 세워 보겠다고 으쌰으쌰 노력하는데 막냇동생이란 놈은 무공은 뒷전이요, 술과 여자에 미쳐 있다.

진위경이 보살이라 그렇지, 진무경처럼 주먹이 나가는 게 정상이다.

‘무공도 강하고.’

혹시 모르지. 개과천선한 동생의 모습을 보고 친히 무공을 가르쳐 줄지도.

‘이건…… 기회다.’

눈이 번쩍 뜨인다.

워낙 바쁜 탓에 가끔 얼굴만 구경하는 진위경, 위팽과는 달리 진무경은 연무장에만 틀어박혀 있다.

함께 사는 열흘 동안 절정 고수에게 일대일 과외를 받는다면 내 무공도 크게 진일보할 수 있지 않을까?

‘지금보다 더. 훨씬 더.’

마음 깊숙한 곳에서 욕심이 불쑥 고개를 쳐든다. 아니, 이건 허기다. 지금껏 가지지 못했던 모든 것에 대한 허기.

부와 명예? 탐난다. 하지만 그건 내가 얻고자 하는 것의 일부에 지나지 않는다.

‘강해지고 싶다.’

충분히 강해졌다고 생각했지만, 아니었다.

내 사람을 지키기에는 아직 턱없이 모자라다. 일전에 조필을 상대하면서, 이번에 대장로를 보며 느꼈다.

압도적인 힘의 차이.

지금 수준으로는 내 사람이 아니라 내 목숨 하나 지키기에도 빠듯하다. 나는 이제 막 우물 밖으로 고개를 내민 개구리에 불과했다.

‘얼마나 걸릴지는 모르지만 금방 따라잡아 주지.’

삼류에서 초일류. F급에서 C급까지 오르는 데 걸린 시간은 고작 두 달. 지금의 각오는 결코 허언이 아니다.

전쟁도 끝났겠다, 이제 시간은 많다. 로그아웃 전까지 최대한 기량을 끌어 올릴 생각이었다.

‘돌아가자마자 재측정부터 해야 하나?’

공력만 받쳐 줘도 B급까지는 무난하게 나올 것 같은데.

꼬리를 무는 행복한 상상에 흐뭇하게 웃던 그 순간이었다.

“어?”

뭐지?

매우 중요한 걸 잊고 있는 느낌. 놓쳐서는 안 될 것을 놓친 기분. 어제 진무경과 만나기 전에도 느꼈던 위화감이다.

그리고 위화감의 정체를 깨닫기까지는 그리 오랜 시간이 걸리지 않았다.

“퀘, 퀘스트창 오픈.”

띠링.



- 현재 진행 중인 퀘스트가 없습니다.



진행 중인 퀘스트가 없다고?

시스템 메시지를 본 순간 눈앞이 아찔했다. 그것이 어떤 의미인지 잘 알고 있으니까.

‘……로그아웃 퀘스트는?’

무림과 현실을 오고 갈 수 있는 유일한 방법. 로그아웃 퀘스트가 어디에도 보이지 않는다.

생각지도 못한 상황에 멍하니 시스템 메시지를 바라보던 그때였다.

띠링.

맑은 종소리와 함께 새로운 창이 허공에 펼쳐졌다.



- 업적, [귀환]을 달성했습니다!

- 칭호, [귀환자]를 획득했습니다!

- 새로운 기능이 활성화되었습니다!



“귀환자? 새로운 기능?”

뭐야, 이거. 황급히 상태창을 열어 보니 아니나 다를까, 귀환자라는 세 글자가 반짝반짝 빛나고 있다.

“칭호 확인.”

띠링.



아이템창



[귀환자]

설명 : 떠나는 것은 쉬워도 돌아오는 것은 어렵습니다. 당신이 보여 준 희생과 용기에 찬사를 보냅니다.

효과 : 모든 능력치 +10, [로그아웃], [로그인] 기능 활성화





그 순간.

퍼버펑.

머릿속에서 폭죽이 터졌다.



* * *



진무경은 호흡했다. 코와 입, 활짝 열린 전신을 이용한 호흡이었다. 단전의 공력과 천지의 기운이 섞여 들어간다.

솨아아.

단전의 다른 이름은 기해(氣海)다. 기의 바다, 기운이 모이고 흐르는 곳. 진무경은 전신 세맥을 타고 흐르는 기의 물결을 느꼈다. 그리고 환희했다.

‘이거야.’

다섯 살 때 처음 검을 잡았다. 진위경이 서투른 솜씨로 깎은 목검이었다. 까슬한 그 감촉이 좋았고, 휘두를 때마다 흩어지는 바람 소리도 좋았다. 그날 이후 단 하루도 수련을 쉬어 본 적이 없다.



‘천재야, 천재.’

‘저놈은 그냥 타고난 거라니까. 그게 아니고서야…….’



누군가는 감탄했고, 누군가는 시기했다. 의도는 달랐을지언정 하는 말은 같았다. 무공의 천재. 타고난 재능.

그들이 입을 모아 떠들 때도 진무경은 연무장에 틀어박혀 수련을 이어 갔다. 그에게 있어 수련은 고통이 아니라 강해지는 과정이었고, 기쁨이었다.

후우.

날숨과 함께 빠져나가는 것은 탁기(濁氣)만이 아니다. 진무경은 머릿속의 잡념을 탁기와 함께 내뱉었다.

지금부터는 오로지 운기조식에만 집중해야 했다.

‘오늘은 할 수 있을까?’

지난 삼 년간 하루도 빠짐없이 싸워 왔던 적을 만나러 갈 때다. 임독양맥이라는 이름의 적을.

지금까지는 번번이 물러서야 했지만…… 진무경은 아직 포기하지 않았다. 단 한 번만 이긴다면 임독양맥을 타통하고 새로운 영역에 발을 디딜 수 있다.

‘어디 해보자고.’

결의에 찬 진무경이 공력을 힘껏 끌어 올린 그 순간이었다.

“호오오오우우우우!”

뭐지? 심마(心魔)인가?

듣는 것만으로도 오싹한 괴성. 마귀가 기쁨에 차 내지르는 웃음 같기도 했다. 진무경이 황급히 공력을 가라앉히려던 그때, 다시 한번 마귀가 외쳤다.

“소리 벗고 속옷 질러! 호오오오우우우!”

마귀가 아니다. 출입을 금지한 전각에서 저런 개소리를 지껄일 수 있는 놈은 한 명밖에 없다.

“진태경 이 쳐 죽일…… 커헉!”

솟구친 울화에 공력이 산산이 흩어졌다.



* * *



“뭐? 태원진가?”

이제 막 자리에 누우려던 참이었다. 야심한 밤, 난데없는 총관의 보고에 송검문주는 잠이 확 달아나는 것을 느꼈다.

“화, 확실해?”

“저야 모르죠. 무림인도 아닌데.”

낙향 문사 출신인 총관의 말에 송검문주가 뒷목을 잡았다.

머리에 든 거라고는 먹물과 똥밖에 없는 놈한테 물어본 게 잘못이다.

“그럼 태원진가인 건 어떻게 알았어?”

“문 지키는 놈들이 헐레벌떡 달려와서 말하던데요. 지금 밖에 태원진가 사람들이 와 있다고. 그리고 그 누구냐. 위, 위 뭐시긴가 하는 작자가 문주를 만날 수 있겠냐고 물어봤답니다.”

위 뭐시기?

송검문주는 침을 꿀꺽 삼켰다.

“그자의 이름이 설마 위팽은 아니겠지?”

“아, 맞습니다. 위팽.”

송검문주는 목침으로 총관의 대가리를 깨 버릴 뻔했다.

‘귀검(鬼劍) 위팽이 직접 왔다고?’

소가주 진위경의 오른팔이자 태원진가의 핵심 고수.

이번 전쟁에도 혁혁한 공을 세웠다는 절정 고수의 방문에 혼백이 빠져나가는 것 같았다.

“자고 있는 놈들 당장 다 깨워!”

비상사태다. 송검문주는 허겁지겁 뛰쳐나가는 와중에도 오만 가지 생각이 다 들었다.

‘보복인가?’

송검문은 산서성 중부에 있는 중소 문파다. 문도라고 해 봐야 오십 명이 채 되지 않고 대부분이 이, 삼류에 머무르는 수준.

그간 태원진가와 가깝다는 이유로 이런저런 도움을 받았지만 막상 전쟁이 일어났을 땐 슬그머니 발을 뺐다.

어쩌면 오늘의 방문은 당연한 수순일지도 모른다.

‘그래도 그렇지. 귀검이 직접 오다니. 그것도 이 시간에.’

공명정대하기로 소문난 태원진가가 그럴 리는 없겠지만, 멸문지화가 목적이라면 막을 힘이 없다.

송검문의 최고수인 그조차 위팽의 삼초지적이나 될지 의문이니까.

“문주님!”

상관의 등장에 똥 마려운 강아지처럼 끙끙대던 수문위사들의 얼굴이 밝아졌다.

하지만 송검문주는 그들처럼 기뻐할 수 없었다.

그는 딱딱하게 굳은 얼굴로 불청객들을 향해 공손히 포권을 취해 보였다.

“송검문을 이끌고 있는 황 모입니다.”

동시에 죽립을 눌러쓴 서른 명의 불청객들이 좌우로 갈라섰다. 흐릿한 달빛 아래, 한 사람이 모습을 드러냈다.

“반갑소, 위팽이오.”

듣던 대로 젊었고, 생각보다 무례했다. 송검문이 제아무리 한미한 문파라지만 일문의 문주에게 저런 태도라니?

그러나 감히 불만을 표시할 수는 없었다. 저 무례한 젊은 놈은 귀검이고 뒤에는 태원진가라는 이름이 있다.

우방의 위기를 외면한 대가가 이 정도라면 싸게 먹힌 거다.

송검문주는 바짝 마른 입술을 핥았다.

“귀검의 위명은 익히 들었습니다. 미리 기별이라도 주셨다면 마중이라도 나갔을 터인데…….”

“문주께서는 괘념치 마시오. 어차피 소가주님의 서신만 전달하고 갈 생각이었으니.”

“서신, 말입니까?”

고개를 끄덕인 위팽이 밀봉된 서신을 건넸다. 수문위사가 들고 있는 횃불 아래로 뚜렷하게 찍힌 태원진가의 인장이 보인다.

“이건…….”

“초대장이오. 돌아오는 원단에 본가를 방문해 주십사 청하는.”

무림에서 살아온 세월이 짧지 않은 송검문주는 금방 속뜻을 알아차렸다.

‘초대는 무슨.’

이건 소집인 동시에 경고다. 이 초대에 응하지 않는다면 향후 산서 무림의 흐름에서 밀려날 거라는 경고.

원단은 전쟁에서 승리한 군주가 새로운 가신을 받아들이는 날이 될 것이다.

‘태원진가가 칼을 뽑았구나.’

잠깐의 침묵 끝에 송검문주가 입을 뗐다.

“전부터 소가주를 뵙고 싶었는데…… 이번이 좋은 기회가 되겠군요.”

“문주님께서 방문해 주신다니 영광입니다.”

위팽이 정중하게 포권을 취했다. 지금까지와는 다른 태도 변화에 송검문주는 입술을 깨물었다.

“오는 길이 고단하셨을 터인데. 이럴 게 아니라 들어가서 여독을 푸시는 게 어떻겠습니까?”

“호의는 감사하지만 이만 떠나야 할 것 같습니다. 잡아야 할 놈이 있어서 말입니다.”

“위 대협이 쫓고 있는 놈이라. 거 아주 악질인 모양입니다.”

“흉악한 살수지요. 감히 삼공자를 해치려 했으니 말입니다.”

“사, 삼공자를 말이오? 어떤 놈이 감히 산서잠룡을?”

“글쎄요. 본가를 적대시하는 누군가가 보낸 살수로 짐작하고 있습니다.”

“허어.”

“한데…….”

위팽의 눈빛이 순간 번쩍였다. 예리한 시선이 송검문 내부를 샅샅이 훑었다.

“쫓다 보니 송검문까지 왔지 뭡니까.”

“그, 그럴 리가. 무슨 오해가 있는 것 아니오?”

심장이 덜컥 내려앉은 송검문주가 황급히 변명을 시작하려던 그때였다. 위팽이 웃으며 손을 내저었다.

“하하, 물론 착각이겠지요. 태원진가와 송검문의 우애가 두텁다는 것은 천하가 다 아는 사실인데 그럴 리 있겠습니까?”

“……!”

“환대해 주셔서 감사합니다. 원단에 다시 뵙지요. 이럇!”

위팽과 그 수하들이 어둠 속으로 사라진 후에도 송검문주는 오랫동안 그 자리에 서 있었다.
```

## Final English reading copy

```markdown
# Chapter 68

In the end, Jin Wikyung was the winner. He kept pleading with moist, puppy-dog eyes, saying, “Just half a month. No, just ten days. Can’t you two live together?” until Jin Mukyung and I threw up our hands and surrendered.

And that was how we ended up in this situation.

After Jin Wikyung left, the underground training hall was quiet with just the two of us remaining.

Jin Mukyung was the first to break the silence.

“I’ll tell you the rules.”

“Rules? What rules do two men need to live together?”

“First. From now on, you will treat me with respect and use polite speech.”

“What if I refuse?”

Jin Mukyung struck the steel training dummy standing beside him.

Boom! Crack!

The steel dummy went flying and slammed into the wall of the training hall. A distinct handprint was stamped into its caved-in chest.

“What did I say the first rule was?”

I glared at Jin Mukyung. I had been through all kinds of hardship. If he thought he could crush my spirit with something like this, he was seriously mistaken.

“You said I was to use polite speech, sir.”

…

But a mature member of society knew how to avoid unnecessary fights.

This was the adult way to fight. Heh.

*Then why do I feel like crying?*

Ah, I miss Mom.

“Good. Second. You will live as quietly as a dead mouse. If you make enough noise to wake me up or interfere with my training…”

Boom! Crack!

As the second steel dummy went flying, I nodded frantically.

“Last, the third rule. You may use the training hall freely, but if I tell you to move, you will do so without complaint. Understood?”

“Yes, yes.”

“You’re finally coming to your senses.”

Jin Mukyung nodded with satisfaction and pointed toward the exit.

“Now leave. Your room is on the third floor.”

As I hurried out of the underground training hall, the sound of someone shouting through a training exercise echoed behind me. The way he treated me like a piece of luggage made my competitive spirit flare up. I turned around for a moment and made a vow.

*Wait for me. I’ll catch up soon.*

Whoosh! Slash!

Sword Energy cleaved through the third steel dummy. As I watched its head fall limply to the floor, I slightly revised my vow.

*Wait for me. I’ll catch up someday.*

* * *

The room was bleak. Unlike my previous room, which had been decorated so lavishly that it bordered on gaudy, this one contained only a few pieces of absolutely necessary furniture.

“This is a bit much, even for him.”

Or should I say this was just like Jin Mukyung?

We had only met the day before, but that had been enough to figure out his personality. He hated anything superfluous and valued efficiency. He was also the sort of diligent person who never neglected his training.

“…”

What the hell? The more I thought about it, the more impressive the bastard seemed.

He had a violent side, beating his own little brother like a dog for failing to use polite speech, but when I thought about it carefully, that had been self-defense.

Put yourself in the other person’s shoes. Wasn’t that the basis of human relationships?

*If I had a little brother like this, I would’ve beaten him too—and then some.*

His older brothers were working their asses off to rebuild the family, while the youngest was neglecting martial arts and going crazy over alcohol and women.

Jin Wikyung only let it slide because he was a saint. Reacting with his fists like Jin Mukyung did was perfectly normal.

*And he’s strong, too.*

Who knew? Maybe seeing his younger brother reform would move him to personally teach me martial arts.

*This is an opportunity.*

My eyes lit up.

Unlike Jin Wikyung and Wipeng, whom I only occasionally saw because they were so busy, Jin Mukyung was holed up in the training hall all day.

If I received one-on-one lessons from a Peak master during the ten days we lived together, wouldn’t my martial arts improve by leaps and bounds?

*More than now. Much more.*

Greed suddenly raised its head from deep inside me.

No, this wasn’t greed. It was hunger—the hunger for everything I had never been able to possess.

Wealth and fame? I wanted them. But they were only a part of what I truly sought.

*I want to become stronger.*

I had thought I had become strong enough, but I hadn’t.

I was still woefully inadequate when it came to protecting the people who mattered to me. I had felt it when I faced Jopil, and again when I watched the Head Elder.

The overwhelming difference in power.

At my current level, protecting even my own life would be difficult, let alone the lives of the people around me. I was nothing more than a frog that had just poked its head out of a well.

*I don’t know how long it’ll take, but I’ll catch up soon enough.*

It had taken only two months to rise from Third Rate to First Rate, from F-rank to C-rank. The resolve I felt now was not empty talk.

The war was over, and I had plenty of time now. I intended to raise my abilities as much as possible before logging out.

*Should I get myself measured again as soon as I return?*

If my internal energy could support it, I thought reaching B-rank would be easy.

That was when I was smiling contentedly at the happy thoughts chasing one another through my mind.

“Huh?”

What was this?

I felt as though I had forgotten something important. As if I had overlooked something I absolutely could not afford to miss. It was the same sense of wrongness I had felt before meeting Jin Mukyung yesterday.

It did not take long to realize what that wrongness was.

“Q-Quest Window, open.”

Ding.



> **System**
>
> - There are no quests currently in progress.

There were no quests in progress?

The instant I saw the System message, my vision swayed. I knew exactly what that meant.

*…What about the Logout Quest?*

The Logout Quest—the only way to travel between Murim and reality—was nowhere to be seen.

I was staring blankly at the System message, unable to process this unexpected situation, when—

Ding.

A new window unfolded in midair to the sound of a clear chime.



> **System**
>
> - Achievement **Return** achieved!
> - Title **Returnee** acquired!
> - A new feature has been activated!

“Returnee? A new feature?”

What was this?

I hurriedly opened my Status Window, and sure enough, the word *Returnee* was sparkling brightly.

“Check Title.”

Ding.



> **System**
>
> **Item Window**
>
> **Returnee**
>
> **Description:** Leaving is easy, but returning is difficult. Your sacrifice and courage deserve praise.
>
> **Effect:** All Stats +10; **Logout** and **Login** functions activated.

At that moment—

Boom, boom, boom!

Fireworks exploded inside my head.

* * *

Jin Mukyung breathed.

He breathed through his nose and mouth—and with his entire body opened wide. The internal energy in his dantian mingled with the qi of heaven and earth flowing into him.

Whoosh.

Another name for the dantian was the qi sea—the sea of qi, the place where energy gathered and flowed. Jin Mukyung felt the waves of qi running along the tiny meridians throughout his body.

And he rejoiced.

*This is it.*

He had first picked up a sword at the age of five. It had been a wooden sword Jin Wikyung carved with clumsy hands. He had liked the rough texture, and he had liked the sound of wind scattering every time he swung it. From that day onward, he had never taken even a single day off from training.



*He’s a genius. A true genius.*

*That boy was simply born with it. Otherwise…*



Some people had admired him. Others had envied him. Their intentions had been different, but they all said the same thing.

A genius of martial arts. A born talent.

Even while people chattered about him, Jin Mukyung remained shut away in the training hall, continuing his practice. To him, training was not painful. It was the process of becoming stronger, and it was a source of joy.

Whoosh.

What escaped with his breath was not only turbid qi. Jin Mukyung exhaled the distracting thoughts in his mind along with it.

From this point on, he had to focus solely on circulating his qi.

*Can I do it today?*

It was time to face the enemy he had fought every day for the past three years.

The enemy known as the Ren and Du meridians.

Until now, he had been forced to retreat every time, but Jin Mukyung had not given up. If he won just once, he could open the Ren and Du meridians and set foot in a new realm.

*Let’s give it a try.*

Just as Jin Mukyung resolutely drew up his internal energy with all his might—

“Hoooooowuuuuuuuu!”

What was that? A Heart Demon?

The howl was chilling enough to raise goose bumps just by hearing it. It sounded like a demon laughing in delight. Jin Mukyung hurriedly tried to suppress his internal energy when the demon shouted again.

“Take off your voice and shout your underwear! Hoooooowuuuuuuuu!”

It wasn’t a demon.

There was only one person who could spout such bullshit from an off-limits pavilion.

“Jin Taekyung, you fucking—urk!”

His rising fury caused his internal energy to scatter in all directions.

* * *

“What? The Jin Family of Taiyuan?”

The Sect Leader of Song Sword Sect had just been about to lie down. It was the middle of the night, and the unexpected report from the general steward jolted the Sect Leader of Song Sword Sect wide awake.

“Are you sure?”

“How would I know? I’m not even a martial artist.”

The general steward was a former scholar who had retired to the provinces, and his response made the Sect Leader of Song Sword Sect clutch the back of his neck.

He had made the mistake of asking someone whose head contained nothing but ink and shit.

“Then how do you know they’re from the Jin Family of Taiyuan?”

“The gate guards came running and said there were people from the Jin Family of Taiyuan outside. And, uh, what was his name? They said some fellow called Wi… Wi-something asked if he could meet you.”

Wi-whatever?

The Sect Leader of Song Sword Sect swallowed.

“His name wasn’t Wipeng, was it?”

“Ah, yes. Wipeng.”

The Sect Leader nearly smashed the steward’s head with his wooden pillow.

*Ghost Sword Wipeng came here in person?*

He was the right hand of the Lesser Family Head, Jin Wikyung, and one of the core masters of the Jin Family of Taiyuan.

The visit from a Peak master who had made outstanding contributions in the recent war made the Sect Leader feel as though his soul were leaving his body.

“Wake up everyone who’s sleeping! Right now!”

This was an emergency.

Even as the Sect Leader rushed outside, all kinds of thoughts raced through his mind.

*Is this retaliation?*

Song Sword Sect was a small- to medium-sized sect in central Shanxi Province. It had fewer than fifty disciples in total, and most of them were only Second or Third Rate.

They had received various forms of assistance because of their close relationship with the Jin Family of Taiyuan, but when war had actually broken out, they had quietly withdrawn.

Perhaps this visit was only natural.

*Even so. Why did Ghost Sword come personally? At this hour?*

Though the Jin Family of Taiyuan was famous for its fairness and integrity and unlikely to do such a thing, if they had come to annihilate his sect, he had no power to stop them.

Even he, the strongest martial artist in Song Sword Sect, might not last three moves against Wipeng.

“Sect Leader!”

The moment their leader appeared, the gate guards—who had been whimpering like puppies desperate to pee—brightened.

But the Sect Leader could not share their joy.

With his face stiff, he politely clasped his hands toward the unexpected visitors.

“I am Huang, the man leading Song Sword Sect.”

At the same time, the thirty unexpected visitors wearing bamboo hats split to either side. Beneath the hazy moonlight, one man stepped forward.

“Good to meet you. I’m Wipeng.”

He was young, just as the Sect Leader had heard, and more impolite than expected.

Song Sword Sect might have been an insignificant sect, but how could he treat its Sect Leader like that?

Still, the Sect Leader did not dare show his displeasure. The rude young man was Ghost Sword, and behind him stood the name of the Jin Family of Taiyuan.

If this was the price for turning a blind eye to an ally’s crisis, then it was a bargain.

The Sect Leader licked his parched lips.

“I have heard plenty about Ghost Sword’s reputation. If you had sent word in advance, I would have come out to greet you…”

“Please do not trouble yourself, Sect Leader. I only intended to deliver a letter from the Lesser Family Head and leave.”

“A letter?”

Wipeng nodded and handed him a sealed letter. The seal of the Jin Family of Taiyuan was clearly visible in the torchlight held by one of the gate guards.

“This is…”

“An invitation. The Lesser Family Head requests that you visit our family on New Year’s Day.”

The Sect Leader of Song Sword Sect had lived in Murim for many years. He immediately understood the hidden meaning.

*What invitation?*

This was a summons, and a warning at the same time.

It was a warning that if they failed to answer the summons, they would be pushed out of the future course of Shanxi Murim.

New Year’s Day would be the day the victorious lord accepted new vassals.

*The Jin Family of Taiyuan has drawn its sword.*

After a brief silence, the Sect Leader finally spoke.

“I have wanted to meet the Lesser Family Head for some time… This will be an excellent opportunity.”

“It is an honor that you are willing to visit.”

Wipeng clasped his hands politely. The sudden change in his attitude made the Sect Leader bite his lip.

“You must be tired from your journey. Rather than standing here, why don’t you come inside and rest?”

“Thank you for the kind offer, but I think we should be leaving. There is someone we need to catch.”

“The man Great Hero Wipeng is pursuing? He must be quite the villain.”

“He is a vicious assassin. He dared to attempt to harm the Third Young Master.”

“T-The Third Young Master? Who would dare attack the Sleeping Dragon of Shanxi?”

“Well, we assume the assassin was sent by someone hostile to our family.”

“Oh dear.”

“But…”

Wipeng’s eyes flashed.

His sharp gaze swept through the interior of Song Sword Sect.

“Wouldn’t you know it, our pursuit led us all the way to Song Sword Sect.”

“T-That’s impossible. Surely there has been some misunderstanding?”

The Sect Leader’s heart dropped as he hurriedly began to make excuses, but Wipeng smiled and waved his hand.

“Haha. Of course it must be a mistake. The whole world knows that the Jin Family of Taiyuan and Song Sword Sect share a close friendship. How could that be the case?”

“…”

“Thank you for your hospitality. I’ll see you again on New Year’s Day. Hyah!”

Wipeng and his subordinates disappeared into the darkness.

The Sect Leader of Song Sword Sect remained standing in the same place for a long time.
```
