<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0070.txt",
      "sha256": "b3314bbe341f4cedf44858bbe1ba9db300bcff851e384272080b1480dc3b5234",
      "bytes": 12876
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f5c811a1a0d3b32ff0ed3cb7ea07856769fa90c312d712c4695854d5e0125a4d",
      "bytes": 3943
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "dbdabc0fc718e52389fec5ab9cb9fd0d0524aa68aebb808026241861a21eca82",
      "bytes": 2796
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "7de179f94b3250ee7c448974532d453e9b0cf128a19ac90b66561c5c1f56756b",
      "bytes": 1183
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "58c143988769dd17763be08cd1e02f1bd8ab6674b01ee6e59ab1045ff4461cfb",
      "bytes": 23754
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "4fd1b147643a35837e8e82b74c9f8066d3d4c455d94472a714e763e4fac6806b",
      "bytes": 8155
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "de1882d1e10be0d41517f43c37f7f443710c1f1f904928e57a151a8a04c34a70",
      "bytes": 2803
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "2246852c06b381ac8154362624df9ea129260f684d2a7a8f364994475915cacd",
      "bytes": 3040
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "31a89af7902482171ae3ccd53b70fcaba1e22b7ade3fd0202258dc3f8faaaa4b",
      "bytes": 2200
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "22624ef10ad0c482cf683229bcd86c0f90bf27a9b14775bc153115392bebb0db",
      "bytes": 2818
    }
  ],
  "estimated_tokens": 11358
}
-->

# Durable State Update — Chapter 70

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 70. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 70. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 70,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 70,
    "continuity_sources": [70],
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
    "Jin Wikyung stops Taekyung and Mukyung from fighting and requires both brothers to apologize and cooperate.",
    "Mukyung imposes rules of polite speech, silence, and obedience over the training hall during the cohabitation.",
    "The Returnee title grants Taekyung All Stats +10 and activates the Login and Logout functions.",
    "Mukyung has spent three years attempting to open the Ren and Du meridians.",
    "Wipeng visits Song Sword Sect with thirty retainers, delivers Wikyung's New Year's Day summons, and implies that the summons is also a warning.",
    "Mukyung now trains Taekyung harshly, and the System has created a Peak-Grade Quest requiring Taekyung to earn Mukyung's recognition while Logout is restricted."
  ],
  "continuity_sources": [
    69,
    68
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons.",
    "It remains unresolved whether Jin Wikyung will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack."
  ],
  "safe_through": 69,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협.",
    "Use Alliance Leader for 맹주 and summon for 소집 to preserve the distinction from an invitation.",
    "Retain Great Hero for 대협 and Ghost Sword for 귀검.",
    "Use Sleep Mode for 수면 모드 and Medicine King Hall Master for 약왕당주.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, and Heart Demon for 심마.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정 in the Quest mission.",
    "Render 두 시진 as two hours and 아스모데우스 as Asmodeus."
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
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |

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
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 선배     | **Senior**                                   |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |

## Listed compact profiles

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 69
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother; returns to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 69
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 69
- **Aliases:** None revealed
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 68
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 62
- **Aliases:** Blood Wolf Sword
- **Role:** Sect Leader of the Mount Heng Sword Sect; Lee Seogeun’s father
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Father of Lee Seogeun; leader of the Mount Heng Sword Sect

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 37
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, and quietly amused; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃70화



밖은 어스름한 새벽이었다. 겨울철 공기는 얼음장처럼 차가웠고 걸을 때마다 연무장 바닥에 낀 서리가 바스러졌다.

미리 몸을 풀고 있던 진무경이 나를 보며 씩 웃었다.

“그래, 마음의 준비는 끝났고?”

당연히 아니지. 하지만 쓰린 속을 감추고 고개를 끄덕였다.

누가 그랬다. 피할 수 없다면 즐기라고. 강해지는 과정 중 하나라고 생각하니 마음이 한결 편안…….

스르릉.

“그럼 그 대단한 실력 좀 보자.”

이 새끼 한국인인가. 성격이 왜 이렇게 급해?

피할 시간도 없다. 순식간에 코앞까지 짓쳐 든 진무경을 향해 황급히 창대를 휘둘렀다.

캉! 카가가각!

서로 맞댄 무기 너머로 진무경의 입김이 흘러나온다.

“자세는 제법이구나.”

그럴 수밖에. 목숨이 왔다 갔다 하는 게이트에서 7년을 창 하나로 버틴 나다. 권각술과는 쌓인 깜냥부터 다르다.

나는 녀석의 눈을 노려보며 대답했다.

“이번에는 쉽지 않을 겁니다.”

한 글자씩. 또박또박.

“너…….”

범상치 않은 내 기세를 느낀 걸까? 진무경의 눈동자가 파르르 떨렸다.

“눈깔 똑바로 안 떠?”

“아.”



* * *



스르륵. 쿵!

진태경이 쓰러졌다. 그리 놀라운 일은 아니다. 벌써 다섯 번째 기절이니까. 정말 놀랄 만한 일은 따로 있다.

‘날 상대로 이백 합을 버틸 줄이야.’

두 시진 동안 이어진 다섯 번의 비무.

사람이라면 응당 지치기 마련이다. 하지만 진태경은 달랐다. 오뚝이처럼 일어났고 점점 강해졌다. 결국 마지막에는 진무경도 진심으로 상대해야 했다.

‘이 녀석, 정체가 뭐야?’

적수공권일 때는 여든 먹은 노인네처럼 엉거주춤하던 동생. 그러나 창을 잡자 모든 것이 달라졌다.

맞기 싫어 살살 비위를 맞추던 겁쟁이는 어디 가고 노련한 창수(槍手)가 그곳에 있었다.

‘낭인 같았다. 수도 없이 죽음의 위기를 넘긴.’

투박해 보일 정도로 간결한 움직임, 스스로의 직감에 의존하는 변칙적인 공격과 회피. 낭인의 싸움에는 정해진 것이 없다. 진무경의 눈에 비친 진태경이 바로 그랬다.

그렇기에 더욱 큰 의문이 남는 거고.

‘도대체 어떻게?’

걸음마와 동시에 검을 잡는 명문가의 자제들도 일류 언저리만 기웃거리는 놈들이 부지기수다. 한데 저놈은 삼 년 만에 절정의 벽 앞에 섰다.

그것도 기녀들의 분 냄새가 아닌, 노련한 낭인의 냄새를 풀풀 풍기면서. 생각할수록 기가 찼다.

‘이게 가능한 일인가?’

가능하긴 하다. 초절정 고수의 벌모세수, 영약을 이용한 체질 개선. 그다음 피똥 쌀 만큼 창을 휘두르며 실전 경험을 쌓으면 된다. 삼 년간 하루도 빠짐없이!

“……말도 안 되는 소리지.”

허탈한 목소리로 중얼거린 진무경이 머리를 벅벅 긁었다.

그렇다면 이제 남은 답은 하나밖에 없다.

‘천재.’

이 단어 하나면 모든 의문이 명쾌하게 해결된다.

왜? 천재니까. 말 그대로 하늘이 내린 놈. 재능을 타고난 놈이니까. 모든 면에서 천재는 앞서간다. 출발점부터가 다르다.

“드르렁. 푸우.”

“…….”

그런데 하필 이런 놈이 천재라고?

그럴 리가 없다. 그래서는 안 되는 거다! 문득 분노가 치밀어 오른 진무경은 동생의 엉덩이를 걷어찼다.

“푸루루루룹.”

데굴데굴 굴러간 진태경이 몸을 부르르 떨었다.

“워, 월화 누나. 거긴 안 돼요.”

“……!”

“갑자기 이러시면. 앗. 아아!”

뚜둑.

실오라기 같던 마지막 인내심이 끊어졌다.



* * *



삐빅!



- 수면 모드가 강제 종료 됩니다!



이거 강제 종료도 되는 거였구나.

새로운 기능을 알았다는 기쁨도 잠시였다. 수면 모드가 왜 강제 종료 됐겠는가. 누가 깨우니까 종료된 거지.

“신성한, 연무장에서, 뭐? 거긴 안 돼요? 안 돼요?”

뻑! 뻑! 뻑!

새우처럼 웅크린 나는 죽어 가는 목소리로 말했다.

“살려 주세요…….”

“안 돼요!”

퍼버버벅!

정확히 몇 대를 맞았는지 모르겠다. 중간에 두 번 정도 의식이 끊겼기 때문이다.

마지막 힘을 쥐어짜 연무장에 다잉 메시지를 남기다가 쓰러진 것이 마지막 기억이었고, 눈을 떠 보니 이미 밤이었다.

‘뭐 했다고 벌써 밤이냐.’

시간 여행자가 된 기분이다. 진무경을 만난 후로는 아주 그냥 하루가 휙휙 지나간다. 나는 전신을 엄습하는 통증을 느끼며 중얼거렸다.

“진무경, 세긴 세다.”

진무경을 제외한다면 지금까지 내가 상대한 절정 고수는 두 명이다. 대장로, 그리고 조필.

‘그중에서 대장로는 제외.’

대장로의 경우는 천운이 따랐다고 봐야 한다. 그는 태원진가 무인들의 희생과 이천백의 기습이 아니었다면 죽었다 깨어나도 이길 수 없는 고수였다.

‘그럼 조필과 진무경을 비교한다면?’

고민은 그리 길지 않았다.

두 명 모두 겪어 봤기에 선택은 쉬웠다.

‘진무경이 더 강해.’

조필은 분명 괴물 같은 놈이다. 화염신장에서 뿜어져 나오는 무지막지한 열기를 떠올리면 지금도 소름이 돋는다.

하지만 뭐랄까, 절정 고수답게 강하고 화염신장이라는 치명적인 무공을 사용했지만 그게 전부였다.

‘정확히는 무공의 활용 차이라고 해야겠지.’

진무경은 조필과 다르다. 그는 비무 중에도 최소 십여 개의 무공을 사용하며 내 공격을 철저히 차단했다.

무림인에게 무공이란 또 다른 무기다. 진무경은 적재적소에 알맞은 무기를 꺼내 쓸 줄 아는 녀석이다.

‘그에 비하면 나는?’

처음부터 있었던 진가심법은 제외. 무림에서 익힌 무공이라고는 진가창법과 진가보법 두 개가 전부다.

물론 둘 다 의심할 여지가 없는 일류 무공이지만…… 바꿔 말하면 딱 일류 수준에서나 쓸 만한 무공이라는 말도 된다.

무공의 한계. 내가 느낀 것을 진위경이 모를 리 없다.

‘그게 나를 진무경한테 붙여 준 이유고. 윽.’

고통에 절로 눈살이 찌푸려진다. 상반신을 조금 일으켰을 뿐인데, 전신의 뼈마디가 욱신거리고 살갗이 아려 왔다.

수면 모드를 통한 휴식에도 한계가 있었던 모양이다.

‘하긴, 그렇게 얻어맞았으니.’

진무경의 인정을 받아 퀘스트를 완료하려면 오늘 같은, 아니 오늘보다 더한 날들을 보내야 한다.

어쩌면 흠씬 두들겨 맞기만 하고 퀘스트까지 실패할지 모른다.

‘산 넘어 산이군.’

그래서 기쁘다.

F급 헌터였던 내게는 산을 오를 수 있는 자격조차 주어지지 않았으니까. 하지만 모든 것이 달라졌다.

넘어야 할 산이 있고, 그 산에 오를 자격이 주어졌다. 그것도 누구보다 빠르게!

‘이럴 때가 아니지.’

나는 통증도 잊은 채 자리에서 일어났다. 덧없이 흘려보내는 1분 1초가 아쉬웠다.



* * *



진무경은 지하 연무장에 있었다. 최대한 발소리를 죽이며 지하로 통하는 계단을 내려가자 그의 모습이 보였다.

“합!”

짧은 기합성과 함께 검이 움직였다.

쉭! 쉬쉬쉭!

검신을 따라 바람이 갈라진다. 빛살 같은 속도로 허공을 찌르고 베어 내는 진무경의 움직임은 거침없었다.

그렇게 일각 정도가 흘렀을까? 검을 내린 진무경이 긴 날숨을 토해 냈다.

“후우.”

소매로 땀을 훔친 그가 나를 향해 고개를 돌렸다.

이미 아까 전부터 내 존재를 눈치채고 있었던 모양이다.

“말해 봐.”

뜬금없는 한마디.

당황한 나는 엉겁결에 반문했다.

“뭐, 뭘요?

“내가 방금 펼친 무공에 대해서.”

“어, 그게 일단 굉장히 빠…….”

“참고로 빠르다, 강하다. 이딴 헛소리 지껄이면 죽는다.”

귀신이네. 나는 살기 위해 머리를 쥐어짰다.

진무경의 무공이 어땠더라? 곰곰이 생각해 보니 희미하게 떠오르는 느낌이 있었다.

“거칠다?”

진무경의 눈썹이 꿈틀거렸다. 정답인가?

“너 지금 나한테 말 놓은 거냐?”

“……거칠었던 것 같아요.”

“그따위 말은 삼척동자도 할 수 있어. 더 자세히.”

머릿속의 이미지가 점점 또렷해진다. 허상의 적을 향해 쏟아지던 검날과 움직임이 떠올랐다. 빠르고, 거침없는 동작들. 그리고 사방을 짓누르던 기세.

그건 마치…….

“폭포?”

“…….”

“엥?”

뭐야, 정답이야?

한동안 말이 없던 진무경이 돌연 검집을 휘둘렀다.

딱!

“악! 왜 때려요!”

“그냥.”

그가 묘한 눈빛으로 나를 응시했다.

“어쩌다 너 같은 놈이 나왔을까?”

저게 욕일까, 칭찬일까.

속뜻이 뭔지는 모르겠지만 질문에 대한 답은 억울해서라도 들어야겠다. 나는 욱신거리는 이마를 문지르며 물었다.

“그래서, 정답입니까?”

“천무학관에는 수천 권의 무공 비급이 존재한다. 정파 무림의 후학 양성을 생각한 선배 고인들의 안배지.”

“그런데요?”

“방금 네가 본 낙류검(落流劍)도 그중 하나다. 서고 깊숙이 파묻혀 있었던 것을 내가 찾아냈지.”

낙류. 풀이하자면 떨어지는 물의 흐름. 즉, 폭포다.

그냥 생각나는 대로 말한 건데 설마 정답일 줄이야.

“오, 오오.”

설마 나, 진짜 천재인 건가? 무공 입문 두 달 만에 이 정도면 앞으로 얼마나 강해질지 내가 생각해도 나 스스로가 무서워진다.

“설마 겨우 이 정도로 난 천재니, 뭐니 하는 낯부끄러운 생각을 하는 건 아니겠지?”

“…….”

진짜 귀신이네. 그래도 조금은 재능이 있는 것 같은데.

나는 미련을 버리지 못하고 조심스럽게 물었다.

“원래 다들 이 정도는 하는 건가요?”

내 질문에 진무경이 순간 움찔했다.

“그, 그럼. 눈 달린 놈이면 이 정도는 맞춰야지.”

“에이.”

“에이? 눈깔 하나 뽑아 줘?”

“……그건 좀.”

이 자식은 오늘따라 유난히 정색하네. 무슨 기분 나쁜 일이라도 있나. 한발 물러났는데도 진무경은 화를 삭이지 못하고 씨근덕거렸다.

“기본이야, 기본. 누구나 다 하는 거라고.”

“알았다니까요. 왜 자꾸 화를 내고 그러세요? 무섭게.”

“너 지금 반항하냐? 질풍노도의 시기라서 질풍십이권으로 맞고 싶어?”

질풍십이권이 뭔지는 모르겠지만 맞으면 아플 것 같다.

맹렬히 고개를 흔들었지만 진무경의 화는 좀처럼 가라앉지 않았다.

“네가 무공을 알아? 어?”

“모, 모릅니다.”

“너 무공 익힌 지 얼마나 됐어.”

반사적으로 대답이 튀어 나갔다.

“두 달, 두 달이요.”

“그래, 두 달밖에 안 된 놈이…… 뭐? 두 달?”

진무경이 핏줄 선 눈동자로 나를 노려본다.

“삼 년이 아니라 두 달?”

다급한 상황. 7년의 사회생활을 통해 얻은 눈치가 빛을 발하는 순간이다. 나는 재빨리 입을 열었다. 특히 일정 부분을 강조하는 것도 잊지 않고.

“삼 년 하고도! 두 달이요.”

풍 맞은 것처럼 부들거리던 진무경의 주먹이 안정을 되찾았다. 왠지는 몰라도 목소리까지 살짝 온화해진 느낌이다.

“자식이, 깜짝 놀랐네.”

내가 더 놀랐다. 이 새끼야…….

‘분노 조절 장애인가.’

진위경에게 물어보면 금방 들통나겠지만, 적어도 지금 당장 질풍십이권을 체험하는 불상사는 일어나지 않을 것이다.

어쨌건 그사이에 진무경의 분노는 수그러들었다.

“딱 한 번 말한다. 잘 들어.”

“가슴에 새기겠습니다.”

내가 넙죽 고개를 숙이자 그가 고압적인 자세로 선언했다.

“난 가르치고, 넌 복종한다.”

“…….”

애견 훈련소야 뭐야.

“반론은 없다. 왜? 내가 너보다 강하니까.”

맞는 말이라 반박할 생각도 들지 않는다.

돈, 권력, 무력. 형태는 달라도 세상은 강자를 중심으로 돌아가는 법이니까. 나는 그 중심에 서고 싶다.

“어찌하겠느냐?”

아주 오래전부터, 내 대답은 정해져 있었다.
```

## Final English reading copy

```markdown
# Chapter 70

Outside, dawn was dim. The winter air was cold as ice, and frost crumbled underfoot with every step across the training ground.

Jin Mukyung, who had already been warming up, grinned at me.

“Well, have you finished preparing yourself mentally?”

Of course not. But I hid my churning stomach and nodded.

Someone once said that if you couldn’t avoid something, you should enjoy it. When I thought of this as just another part of becoming stronger, I felt a little more at ease…

Shing.

“Then let’s see that impressive skill of yours.”

*Is this bastard Korean? Why is he so impatient?*

I had no time to avoid him. Jin Mukyung rushed toward me in an instant, and I hurriedly swung my spear shaft at him.

Clang! Kaga-gang!

Jin Mukyung’s breath drifted between us through the weapons we had crossed.

“Your stance isn’t bad.”

It had to be. I had survived seven years in a Gate where my life had been on the line, using nothing but a spear. The experience I’d built up with the spear was on a completely different level from my fists and kicks.

I glared into his eyes and answered.

“This time, it won’t be easy.”

One word at a time. Clearly and distinctly.

“You…”

Perhaps he sensed that something about my momentum was different. Jin Mukyung’s pupils trembled.

“Can’t you keep your damn eyes open?”

“Oh.”

* * *

Swoosh. Thud!

Jin Taekyung collapsed. It was not particularly surprising. This was already his fifth knockout.

The truly surprising thing was something else.

*I can’t believe he lasted two hundred exchanges against me.*

Five spars over two hours.

Anyone would naturally become exhausted. But Jin Taekyung was different. He kept getting back up like a roly-poly toy, growing stronger each time. By the end, even Jin Mukyung had been forced to face him seriously.

*What the hell is this guy?*

When he fought unarmed, his movements had been awkward enough to resemble those of an eighty-year-old man. But the moment he picked up a spear, everything changed.

The coward who had fawned over Jin Mukyung to avoid getting hit had vanished. In his place stood a seasoned spearman.

*He was like a wandering martial artist. Someone who had survived countless brushes with death.*

His movements were simple to the point of seeming crude. His attacks and evasions were irregular, relying on his own instincts. There was nothing fixed about the way a wandering martial artist fought.

That was exactly what Jin Taekyung looked like to Jin Mukyung.

And that was why the question only grew larger.

*How?*

Even among the heirs of prestigious families who picked up a sword as soon as they learned to walk, countless people only hovered around the threshold of First Rate. Yet this man had stood before the wall of the Peak realm in just three years.

And he did it while giving off not the scent of a courtesan’s powder, but the strong scent of a seasoned wandering martial artist. The more Jin Mukyung thought about it, the more absurd it seemed.

*Was something like this even possible?*

It was possible.

Having a Supreme Peak master cleanse his tendons and marrow. Improving his constitution with elixirs. Then swinging a spear until he shit blood while building real combat experience.

For three years without missing a single day!

“…That’s ridiculous.”

Jin Mukyung muttered hollowly and scratched his head.

If that was the case, only one answer remained.

*A genius.*

That one word resolved every question with perfect clarity.

Why?

Because he was a genius. Someone blessed by heaven, just as the word implied. Someone born with talent.

Geniuses were ahead in every way. They started from a completely different place.

“Zzz… Hoo…”

“…”

But of all people, this guy was a genius?

That was impossible. It couldn’t be true!

A sudden surge of anger rose within Jin Mukyung, and he kicked his younger brother in the rear.

“Prrrblblbl.”

Jin Taekyung rolled away several times before shuddering all over.

“W-Wolhwa noona. Not there.”

“…”

“If you suddenly do this… Ah. Aah!”

Crack.

The last thread of Jin Mukyung’s patience snapped.

* * *

Beep!



> **System**
>
> - Sleep Mode has been forcibly terminated!

*So it can be forcibly terminated?*

My joy at discovering a new function lasted only a moment. Why had Sleep Mode been forcibly terminated?

Because someone had woken me up, obviously.

“In the sacred training hall, you say what? ‘Not there’? ‘Not there’?”

Whack! Whack! Whack!

I curled up like a shrimp and spoke in a dying voice.

“Please, spare me…”

“No!”

Thwack-thwack-thwack!

I had no idea how many times I was hit. My consciousness had cut out twice in the middle of it.

My last memory was of squeezing out my remaining strength to leave a dying message on the training hall floor before collapsing.

When I opened my eyes, it was already night.

*What did I do for it to be night already?*

I felt like a time traveler. Ever since I had met Jin Mukyung, entire days had been flying by.

I muttered as pain swept through my entire body.

“Jin Mukyung is really strong.”

Excluding Jin Mukyung, I had faced two Peak masters so far.

The Head Elder and Jopil.

*The Head Elder doesn’t count.*

In his case, I had to admit that heaven itself had helped me. If not for the sacrifices of the Jin Family of Taiyuan’s martial artists and Lee Cheonbaek’s surprise attack, he was a master I could never have defeated, even if I had died and come back to life.

*Then what if I compare Jopil and Jin Mukyung?*

I did not have to think for long.

I had experienced fighting both of them, so the choice was easy.

*Jin Mukyung is stronger.*

Jopil was unquestionably a monster. Even now, I got goose bumps whenever I remembered the savage heat pouring from his Flame Divine Palm.

But how should I put it? He was strong like a Peak master, and he used the deadly Flame Divine Palm, but that was all.

*More precisely, it was a difference in how they used their martial arts.*

Jin Mukyung was different from Jopil. Even during our spar, he had used at least ten different martial arts to completely shut down my attacks.

To a martial artist, martial arts were another weapon. Jin Mukyung knew how to draw out the right weapon at exactly the right moment.

*Compared to him, what did I have?*

I could exclude the Jin Family’s Cultivation Technique, which I had possessed from the beginning. As for martial arts I had learned in Murim, I had only the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique.

Of course, both were unquestionably First Rate martial arts.

But put another way, they were only useful up to the First Rate level.

The limits of martial arts. Jin Wikyung could not possibly have failed to notice what I had felt.

*That was why he had sent me to Jin Mukyung. Ugh.*

My brow furrowed automatically from the pain. I had only raised my upper body a little, but every joint in my body throbbed, and my skin ached.

It seemed even Sleep Mode had its limits when it came to rest.

*Well, I did get beaten half to death.*

To complete the Quest by earning Jin Mukyung’s recognition, I would have to endure days like today—or even worse ones.

Maybe I would simply get beaten senseless and fail the Quest anyway.

*It really is one mountain after another.*

And that made me happy.

As an F-rank Hunter, I had not even been given the right to climb a mountain. But everything had changed.

There was a mountain I had to climb, and I had been given the right to climb it.

And I could do it faster than anyone else!

*This isn’t the time for this.*

I rose from my place, forgetting the pain. Every minute and second I wasted felt unbearable.

* * *

Jin Mukyung was in the underground training hall.

I descended the stairs leading underground, keeping my footsteps as quiet as possible, and saw him.

“Hah!”

With a short shout, his sword moved.

Whoosh! Shh-shh-shhk!

The wind split along the blade.

Jin Mukyung’s movements were as unrestrained as he thrust and slashed through the empty air at the speed of a ray of light.

About fifteen minutes passed.

Jin Mukyung lowered his sword and let out a long breath.

“Hoo.”

He wiped the sweat from his brow with his sleeve, then turned his head toward me.

It seemed he had noticed my presence some time ago.

“Tell me.”

The words came out of nowhere.

Confused, I reflexively asked:

“Tell you what?”

“About the martial art I just performed.”

“Uh, well, first of all, it was really fast…”

“For the record, if you say some pointless bullshit like ‘It was fast’ or ‘It was strong,’ I’ll kill you.”

*What a ghost.*

I racked my brain for an answer that would keep me alive.

What had Jin Mukyung’s martial art been like?

As I thought about it carefully, a vague impression began to surface.

“Rough?”

Jin Mukyung’s eyebrow twitched.

*Was that the right answer?*

“Did you just speak informally to me?”

“…It seemed rough.”

“Even a little kid could say that. Be more specific.”

The image in my head gradually became clearer.

I remembered the sword blades pouring toward an imaginary enemy and the movements that accompanied them. Fast, unrestrained motions. And an aura that seemed to press down from every direction.

It was like…

“A waterfall?”

“…”

“Huh?”

*What? Was that the right answer?*

After remaining silent for a while, Jin Mukyung suddenly swung his scabbard.

Smack!

“Ow! Why did you hit me?”

“Just because.”

He stared at me with a strange look in his eyes.

“How did someone like you ever come out?”

Was that an insult or a compliment?

I had no idea what he truly meant, but I had to hear the answer to his question if only to soothe my wounded pride. Rubbing my throbbing forehead, I asked:

“So, was that the correct answer?”

“There are thousands of martial arts manuals in Heaven’s Gate Temple. They were arrangements left behind by the departed Seniors who hoped to cultivate the younger generation of the orthodox Murim.”

“And?”

“The Falling Flow Sword you just saw is one of them. I found it buried deep in the archives.”

Falling flow. In other words, water falling down.

A waterfall.

I had only said the first thing that came to mind, but it had actually been the right answer.

“Oh, ooh.”

*Am I really a genius?*

If I could recognize martial arts like this after only two months of learning them, I was afraid of how strong I might become in the future. Even I found myself frightening.

“Surely you’re not having the embarrassing thought that you’re a genius or something after managing only that much?”

“…”

*He really is a ghost.*

Still, I seemed to have at least a little talent.

Unable to let go of the thought, I cautiously asked:

“Can everyone normally do this much?”

Jin Mukyung flinched.

“O-Of course. Anyone with eyes should be able to guess this much.”

“Come on.”

“‘Come on’? Do you want me to pluck out one of your eyes?”

“…That might be a bit much.”

*Why is this bastard being especially stone-faced today? Did something unpleasant happen?*

Even after I backed down, Jin Mukyung could not contain his anger. He snorted irritably.

“It’s basic. Basic. Everyone can do it.”

“I get it. Why do you keep getting angry? You’re scaring me.”

“Are you rebelling against me? Is it because you’re going through the storm-and-stress stage of adolescence? Do you want to get beaten with the Twelve Gale Fists?”

I did not know what the Twelve Gale Fists were, but getting hit by them sounded painful.

I shook my head fiercely, but Jin Mukyung’s anger showed no sign of fading.

“Do you know martial arts? Huh?”

“N-No, sir.”

“How long have you been learning martial arts?”

The answer slipped out reflexively.

“Two months. Two months.”

“Right, a bastard who’s only been at it for two months… What? Two months?”

Jin Mukyung glared at me with bloodshot eyes.

“Not three years, but two months?”

This was an emergency.

The social instincts I had gained through seven years of working life shone at that moment. I hurriedly opened my mouth, making sure to emphasize one particular part.

“Three years! Plus two months!”

Jin Mukyung’s fist had been trembling as though he had suffered a stroke, but it steadied again. For some reason, even his voice seemed slightly gentler.

“You little bastard. You startled me.”

*You startled me even more, you son of a bitch.*

*Does he have anger-management issues?*

If Jin Mukyung asked Jin Wikyung, my lie would be exposed immediately. But at least I would not have the misfortune of experiencing the Twelve Gale Fists right now.

In any case, Jin Mukyung’s anger subsided in the meantime.

“I’ll say this only once. Listen carefully.”

“I’ll engrave it on my heart.”

I bowed deeply, and he declared in a domineering tone:

“I teach, and you obey.”

“…”

*Is this a dog-training school or what?*

“There will be no objections. Why? Because I’m stronger than you.”

It was true, so I had no desire to argue.

Money, power, and force. Their forms might differ, but the world always revolved around the strong.

I wanted to stand at its center.

“What will you do?”

My answer had been decided a long time ago.
```
