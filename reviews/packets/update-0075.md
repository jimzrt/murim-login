<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0075.txt",
      "sha256": "11119c77c18d6cfdb817452c443d4d1f6b69114cfc385ff2c113ec835d6fdfae",
      "bytes": 12543
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "600a96365de6435c2e71f96b077dbbd814688e38a2122c9d6568f77c531b98ca",
      "bytes": 5363
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "de36ca558b7f84d2a543a7703bc703a14537c028a639dfe71d1722750c174d39",
      "bytes": 4009
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "d9bd379324ec29a9577d603a99f46d5d7e7fb8544820823fa7f830c93c5579e5",
      "bytes": 2803
    },
    {
      "path": "characters/Seong Jinho.md",
      "sha256": "727f3ca55f4e645502f87e73837145539435b5fa668bca2c2532db36a756ecfa",
      "bytes": 2027
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2c4e645b01ee0ac4881512abdf96178d983a82513c008ac83294bbb982f5b143",
      "bytes": 3859
    }
  ],
  "estimated_tokens": 10978
}
-->

# Durable State Update — Chapter 75

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 75. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 75. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 75,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 75,
    "continuity_sources": [75],
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
    "After ten days of Mukyung's training, Taekyung has mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique; Mukyung is astonished by his growth and feels jealousy and fighting spirit.",
    "Mukyung's final spar with Taekyung ended when Mukyung used Sword Energy to cut Taekyung's uniform without injuring him, then declared training complete.",
    "The Training? Trial! Quest succeeded according to Mukyung's evaluation; Taekyung received a Level Up, a Quest completion Reward in his Inventory, and notice of an additional Reward.",
    "Taekyung has the First Stage Skill Martial Arts Manual Creation, which can create manuals for mastered martial arts; the available manuals are the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique.",
    "Hyuk Mujin remains badly injured and under treatment after the attack.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training.",
    "Jin Wikyung plans to summon every sect in Shanxi Province on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, visits Song Sword Sect, and delivers Wikyung's summons as both summons and warning.",
    "Jin Wikyung searched the family records for Dark Heaven but found no information.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months.",
    "Soyul is five years old and does not know that her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates the Login and Logout functions.",
    "Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who recently became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraces and praises him after acknowledging a minor misunderstanding.",
    "Jin Wikyung is exhausted by the Jin Family's administrative workload but has restored his office to an orderly state.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect and personally requested Taekyung and Mukyung's visit.",
    "Taekyung received the forcibly created Quest [Yesterday's Enemy, Today's Ally] to deliver an invitation to the Mount Heng Sword Sect for New Year's Day; the Quest is incomplete, has an unknown Reward, and has no Failure penalty.",
    "Taekyung, Mukyung, and Hyuk Mujin have departed for Eung-hyeon in a four-horse carriage; Mukyung accepted the trip because Peak martial arts may be revealed to him."
  ],
  "continuity_sources": [
    74
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "It remains unresolved whether Taekyung will complete the forced Quest and successfully log out from the current prompt."
  ],
  "safe_through": 74,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, and four-horse carriage for 사두마차.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 비급 제작 as Martial Arts Manual Creation, 맷집 as Toughness, 천무지체 as Heavenly Martial Physique, 장칠득 as Jang Childeuk, 장 무인 as Martial Artist Jang, 인의예지 as benevolence, righteousness, propriety, and wisdom, 호환 as killed by a tiger, and 일각 as fifteen minutes.",
    "Use Squad Leader for 조장님, Third Young Master for 삼공자님, Mujin for 무진아, and seventh-tier student for 내신 칠 등급."
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
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |

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
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |

## Exact glossary matches

| 무림     | **Murim**          |
| 조필     | **Jopil**          |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 팀장      | **Team Leader**       |
| 성진호 | **Seong Jinho** |

## Listed compact profiles

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 72
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Seong Jinho.md

# Seong Jinho (성진호)

- **Safe through:** Chapter 53
- **Aliases:** Jinho; Mr. Seong Jinho
- **Role:** Manager of Hope Goshiwon; thirty-year-old exam candidate; civilian and Taekyung’s older friend
- **Personality:** Knowledgeable about IT, shamelessly blunt, melodramatic when threatened, and a heavy drinker
- **Voice:** Casual and teasing; invokes laws and hierarchy for comic effect; speaks informally to Taekyung while demanding respect as his older brother
- **Relationships:** Three years older than Jin Taekyung; treats him as a younger brother and drinking companion

## Korean source

```text
＃75화



현대와 무림을 구분하는 방법은 우습게도 냄새와 온도다.

VR 헬멧 안의 땀 냄새. 창문 너머에서 비춰 오는 햇살 때문에 적당히 달궈진 캡슐 안의 열기.

“후아.”

헬멧을 벗고 캡슐을 빠져나오자 좀 살 것 같다. 그래 봤자 열탕에서 온탕으로 바뀐 정도지만.

‘얼마나 지난 거지?’

손목에 찬 시계를 확인했다. 약 7년 전, 헌터 훈련소 앞 가판대에서 샀던 만이천 원짜리 싸구려 디지털시계는 알람과 스톱워치 기능이 있다는 장점이 있었다.

삑.



[02:05:35]



두 시간 하고도 5분 35초.

무림에서 20일 정도를 머물렀으니 지난번과 비교해 얼추 시간이 맞아떨어진다.

‘현대로 왔으니 시간 배율이 역전되었을 거고.’

로그아웃을 한 지금은 현대에서의 열흘이 무림의 한 시간이다. 나는 고시원 공용 샤워장에서 몸을 씻은 다음 방으로 돌아왔다.

방문을 닫으려던 찰나, 검은 그림자가 휙 솟구쳤다.

“왁!”

그래, 성진호 이 인간일 줄 알았다.

“어.이.구. 깜.짝. 놀.랐.네.”

“……뭐냐 그 반응은. 알고 있었어?”

“들숨 날숨이 아주 격렬하시던데. 진호 씨, 흥분하셨나 봐.”

날이 지날수록 예리해진 오감은 굳이 [기감]이 아니어도 주위의 소리와 움직임을 잡아낼 수 있다.

나름 숨죽인 채 기다리고 있었던 모양이지만 내 귀에는 그의 작은 움직임과 숨소리 하나하나가 천둥처럼 들렸다.

“숨 좀 작게 쉬어. 명색이 고시원 총무인데 숨소리가 커서 민원 들어오면 곤란하지.”

“젠장. 어떻게 알았지? F급 헌터 주제에…… 아, 너 얼마 전에 C급 됐지. 참.”

“인성 봐라. F급이라고 놀리는 게 아주 입에 붙었구만.”

“야, 네가 내 나이 돼 봐라. 어제 먹은 반찬도 기억 안 나는데 겨우 일주일 전에 있었던 일이 팍팍 떠오르겠냐?”

“일주일?”

겨우 그것밖에 안 됐나?

내게는 한 달도 훨씬 지난 일이 진호 형에게는 고작 지난주에 있었던 일이다. 미묘한 괴리감이 느껴졌다.

“어. 표정이 왜 그래? 문제라도 있냐?”

“문제는 무슨. 그런데 무슨 일로 찾아왔어?”

“이 자식 이거 말 뽄새 보게. 우리가 볼일 있어야 볼 수 있는 비즈니스 관계야? 어?”

“본론만. 짧게.”

진호 형의 얼굴이 굳어졌다. 장난이 너무 심했나?

생각해 보니 요즘 내가 너무 무심했던 것 같기도 하다. 무림으로 돌아가기 전에도 여러 가지 문제로 얼굴도 자주 못 봤는…….

“저녁. 사 줘.”

“…….”

“삼겹살. 철판구이. 치맥.”

시바. 그럼 그렇지.

그 와중에 메뉴도 자기가 고르고 자빠졌네.

“나한테 돈 맡겨 뒀어?”

“네 돈이 내 돈. 내 돈이 내 돈 아니냐.”

“발음 똑바로 해라. C급 헌터 주먹맛 보고 싶지 않으면.”

움찔한 진호 형이 손바닥을 싹싹 비볐다.

“부탁드립니다. 선생님의 돈으로 제 메마른 위장에 기름칠 좀 해 주십시오.”

“…….”

태세 전환 봐라. 우디르도 울고 가겠다.

어이가 없었지만 한편으로는 피식 웃음이 나왔다. 한 달 가까이 제대로 된 진짜 음식을 못 먹은 위장도 비명을 질러 대던 차였다.

‘간만에 제대로 먹어 보자.’

나는 엄숙한 목소리로 말했다.

“태도가 마음에 드는군. 앞장서라.”

“어디로 모실까요?”

“삼겹살이나 철판구이는 질렸다. 오늘은 좀 더 비싸게 먹어 보자꾸나.”

“서, 선생님. 그렇다면!”

진호 형이 눈을 부릅떴다.

“한우! 방목으로 키워져 환상적인 마블링을 자랑하는 그것?”

“뭔 개소리야. 곱창 먹으러 갈 건데.”

“…….”

“싫으면 굶든가.”

턱.

내 어깨를 붙잡은 진호 형이 비장한 얼굴로 말했다.

“예전부터 꼭 그렇게 먹어 보고 싶었습니다.”

그날 오후 다섯 시부터 시작된 이른 식사는 3차 막걸리 집에서 끝났고, 진호 형은 술에 떡이 됐다.

“크워어어.”

“…….”

이거 어디서 많이 본 장면인데.

묘한 기시감을 느끼며 진호 형을 들쳐 업었을 때, 휴대폰이 울렸다.



〈 명품충



명품충

내일 같은 시간, 같은 장소에서 뵙죠.



짤막한 문자 한 통. 발신인은 최 팀장이었다.



* * *



수면 모드의 단점이자 장점은 수면 시간이 줄어든다는 점이다. 조필과의 싸움에서 큰 부상을 입었을 때를 제외하면 세 시간을 넘긴 적이 없다.

‘수련하기에는 좋지.’

새벽 세 시.

최적의 컨디션으로 눈을 뜬 나는 가부좌를 틀었다. 언제부턴가 하루의 시작과 끝은 늘 운기조식이다.

솨아아.

공력의 물결이 흐르기 시작했다.

단전에서 솟구친 15년의 공력이 신체 내부에 쌓인 노폐물을 정화시키며 잠들어 있던 혈도에 생기를 불어넣었다.

띠링.



- [운기조식]을 마쳤습니다.

- [공력]이 아주 약간 증가했습니다.



시스템 알림과 함께 눈을 떴을 때는 두 시간이 훌쩍 지난 후였다. 무림이었다면 곧장 연무장으로 나가 몸을 풀었겠지만 현실은 여러 가지 제약이 많다.

양계장처럼 다닥다닥 붙어 있는 고시원에서는 더더욱.

‘망할 놈의 고시원. 빨리 탈출하든가 해야지.’

수련도 돈으로 하는 시대다. 잘 버는 놈들이야 널찍한 개인 트레이닝 룸을 몇 개씩 가지고 있지만 나처럼 없는 놈들은 열악한 환경에 맞추는 수밖에.

“후읍. 흡.”

오전 내내 동네를 뛰고, 돌아와서는 기본적인 맨몸 운동을 쉬지 않고 이어 갔다. 능력치가 높아진 덕분인지 지치기는커녕 오히려 활력이 샘솟는다.

그런 나를 보며 진호 형이 질린 얼굴로 물었다.

“지치지도 않냐?”

“별로.”

“한 손 팔 굽혀 펴기를 너처럼 쉽게 하는 놈은 처음 본다. 몇 개째야?”

“몰라. 삼백까지 세고 귀찮아서 안 셌어.”

“괴물이네. 원래 C급 헌터쯤 되면 그 정도는 하는 거냐?”

“그런데, 성진호 씨.”

“어?”

“왜 왔어?”

십여 분 전 퀭한 몰골로 나타나더니 아직도 내 방에서 안 나가는 진호 형이었다.

“보면 모르냐. 라면 먹으려고 왔지.”

톡톡. 촤아악.

다 익어 가는 면발 위로 날계란을 투하하는 모습이 자연스럽다.

반숙을 만들기 위한 버너 화력 컨트롤은 절정 고수라고 해도 좋을 정도다.

“그걸 굳이 여기서 처먹어야 하는 이유 세 가지만 대 봐.”

“첫째. 내 방에 TV가 없으니까. 둘째. 네 방에 TV가 있으니까. 셋째. 라면은 TV를 보면서 먹어야 제맛이니까.”

청산유수로 흘러나오는 말을 들으니 피가 거꾸로 솟는다.

“차라리 하나 사! 돈 없으면 그냥 가져가!”

“아, 그건 좀. 어차피 나갈 건데 짐 늘려 봤자 뭐하냐.”

“그럼 귀찮게 자꾸 들락거리지 말고…… 응? 방금 뭐라고?”

“뭐가?”

“아니, 나간다고?”

“아, 그거.”

진호 형이 떡이 진 머리를 긁적였다.

“그냥 그렇게 됐다. 뭐, 날짜까지 확정된 건 아닌데 조만간 방 빼려고. 언제까지 여기 처박혀 있을 수도 없는 노릇이고.”

“…….”

“뭘 그런 눈으로 쳐다봐?”

“아니, 뭐. 그냥.”

나는 머쓱한 얼굴로 시선을 피했다.

고시원에 사는 사람들 중 사연 없는 사람이 어디 있겠나. 나도 그렇고 진호 형도 마찬가지다. 구태여 이유를 묻는 건 실례다.

‘그래도 아쉽긴 하네.’

몇 년간 친구처럼, 형제처럼 지냈던 사람이다. 이렇게 갑자기 나간다니.

복잡 미묘한 기분에 사로잡혀 있던 나는 조심스레 입을 열었다.

“형, 혹시…….”

“네 마음은 알겠는데. 정중하게 거절한다.”

무슨 말을 하려는지 알아챈 걸까? 내 말을 단칼에 잘라 낸 진호 형이 말을 이었다.

“인마, 형 나이가 서른이야. 내 밥그릇은 내가 챙겨.”

“그렇다면 어쩔 수 없고.”

진호 형이라면 같이 살아도 될 것 같았는데, 섣부른 오지랖이 그의 자존심을 건드린 모양이었다.

형이 구겨진 얼굴로 냄비 뚜껑을 열었다.

“차라리 처음부터 말을 하든가.”

“애초에 생각도 없었으면서 무슨.”

“무슨 헛소리야. 네가 안 먹는다고 해서 하나만 끓였는데.”

“……?”

아니, 잠깐만. 이거 이야기 흐름이 어떻게 되는 거냐.

몇 초간의 침묵 끝에 내가 입을 뗐다.

“무슨 얘기야 그게. 갑자기 뭘 끓여.”

“당연히 라면이지.”

진호 형이 흉흉한 눈빛으로 나를 노려봤다.

“꼭 안 먹는다고 해 놓고 맛있게 끓이면 한 젓가락 달라는 놈이 있어요. 내가 너한테 한두 번 당해?”

“…….”

“C급 헌터라는 놈이 가난한 형님 밥그릇에 손을 뻗쳐? 네가 그러고도 사람이냐?”

“…….”

앞에서 밥그릇 운운한 게, 진짜 밥그릇이었구나.

방금 들은 말 그대로 돌려주고 싶다.

‘저게 사람이냐.’

저런 인간하고 같이 살 생각을 한 내가 병신이지.

나는 자괴감을 느끼며 옷을 걸쳐 입었다. 슬슬 최 팀장을 만나러 갈 시간이다.

쾅!

부서져라 방문을 닫고 빠져나오는 내 등 뒤로 마지막 외침이 울려 퍼졌다.

- 마트 가는 거면 김치 좀!

아, 죽이고 싶다.



* * *



‘장소가 어디였지?’

약 20일 전의 기억을 더듬어 약속 장소에 도착했다.

빌딩 숲 중심부에 위치한 대형 카페. 창가에 앉아 있던 잘생긴 남자가 나를 발견하고 손을 흔들었다.

“여깁니다.”

굳이 말하지 않아도 알 수 있었다. 매장 안에 수십 개의 테이블이 있는데도 앉아 있는 손님은 오직 최 팀장 혼자였으니까.

‘여전히 잘생겼네.’

얇은 캐주얼 정장을 걸친 최 팀장은 방금 화보에서 튀어나온 것 같았다. 20대에 모든 걸 가진 성공한 인생. 외모, 재력, 성격…… 아니다. 성격은 빼자.

가벼운 악수를 나눈 우리는 자리에 앉았다.

“식사는 하셨습니까?”

“아뇨.”

최 팀장이 고개를 갸웃했다.

“그래요? 라면 드신 것 같은데.”

“…….”

젠장, 이 자식 완전 개코네.

고시원에서 있었던 이야기를 구구절절하게 설명하기에는 너무 부끄럽다. 나는 황급히 화제를 돌렷다.

“점심시간인데 사람이 없네요.”

“영업을 안 하니까요.”

“예?”

“유리창도 커튼으로 가리고 문에 클로즈(Closed) 팻말도 걸어 놨는데 당연히 안 들어오죠.”

주위를 둘러보니 정말 최 팀장의 말대로였다.

약속 장소가 여기니, 당연히 열려 있을 거라고 생각하고 들어와서 눈치를 못 챈 모양이다. 이 상황 자체가 너무 이상해서 눈을 깜빡였다.

“그런데 지금 영업하는 중이잖아요.”

매장 안의 불빛은 환하고, 에어컨 바람으로 시원하다. 언뜻 보이는 직원들만 열 명인데 왜 문을 닫아 놓은 거지?

최 팀장은 태연하게 대꾸했다.

“해야죠. 손님이 있으니까.”

“영업 안 한다면서요?”

“그거야 사장 마음 아니겠습니까.”

“어…… 팀장님. 혹시나 해서 물어보는 건데요.”

“굳이 안 물어보셔도 됩니다. 이 카페 제 거니까요.”

그래, 그럴 것 같더라.

곰곰이 생각해 보니 지난번에 만났을 때도 카페 안에는 우리 둘뿐이었다.

‘파도 파도 끝이 없네.’

나는 혀를 내두르며 말했다.

“팀장님, 돈 많으시네요.”

“부족하지 않을 만큼 있습니다. 그러니까 이런 계약서도 내밀 수 있는 거고요.”

최 팀장이 부드럽게 웃으며 서류철을 내밀었다.

“자, 이제 일 얘기를 해 볼까요?”

더 이상 망설일 이유는 없다. 나는 힘차게 고개를 끄덕였다.

“그러시죠.”

한 시간 후, 내가 마지막 서명을 끝마침과 동시에 시스템 알림이 울렸다.

띠링.
```

## Final English reading copy

```markdown
# Chapter 75

The way to tell the modern world apart from Murim is, oddly enough, by smell and temperature.

The smell of sweat inside a VR helmet. The heat inside a capsule warmed just right by sunlight streaming through the window.

“Phew.”

Once I took off the helmet and climbed out of the capsule, I finally felt like I could breathe. It was still only the difference between a scalding bath and a hot bath, though.

*How much time has passed?*

I checked the watch on my wrist. The cheap twelve-thousand-won digital watch I had bought from a street stall in front of the Hunter training center about seven years ago had the advantage of coming with an alarm and stopwatch function.

Beep.



[02:05:35]



Two hours, five minutes, and thirty-five seconds.

I had spent around twenty days in Murim, so the timing roughly matched what had happened last time.

*Since I came to the modern world, the time ratio must have been reversed.*

Now that I had logged out, ten days in the modern world amounted to one hour in Murim. I washed myself in the communal shower of the goshiwon[^1] and returned to my room.

Just as I was about to close the door, a black shadow shot upward.

“Wah!”

Of course. It was Seong Jinho.

“Oh. My. God. What a surprise.”

“……What’s with that reaction? You knew I was here?”

“Your inhaling and exhaling were extremely intense. Mr. Jinho, were you excited?”

My five senses had grown sharper with each passing day. I could pick up every sound and movement around me without even using Qi Sense.

He seemed to have been waiting in silence, but to my ears, every tiny movement and breath he made sounded like thunder.

“Breathe a little more quietly. You’re supposedly the goshiwon manager, so it would be a problem if people filed complaints because your breathing was too loud.”

“Damn it. How did you know? You’re just an F-rank Hunter…… Oh, right. You became C-rank a while ago.”

“Look at the way you talk. Making fun of me for being F-rank has really become a habit.”

“Hey, if you were my age, would you remember something that happened barely a week ago? I can’t even remember what side dishes I ate yesterday.”

“A week?”

Was that really all the time that had passed?

To me, it had been well over a month. To Jinho-hyung, it had been barely a week. I felt a subtle sense of disconnect.

“Hey. Why do you look like that? Is something wrong?”

“What do you mean, something’s wrong? Anyway, what brings you here?”

“Listen to the way you talk. Are we some kind of business relationship that we can only see each other when there’s business involved?”

“Just get to the point. Keep it short.”

Jinho-hyung’s face hardened. Had I gone too far with the teasing?

Come to think of it, I had been too indifferent lately. Even before returning to Murim, I hadn’t been able to see him often because of all sorts of problems……

“Buy me dinner.”

“…….”

“Grilled pork belly. Teppanyaki. Fried chicken and beer.”

Shit. Of course.

And he even had the nerve to choose the menu himself.

“Did I leave money with you?”

“Your money is my money. And my money is my money, isn’t it?”

“Pronounce that properly. Unless you want to feel the fist of a C-rank Hunter.”

Jinho-hyung flinched and rubbed his palms together.

“Please, sir. Use your money to put some grease on my parched stomach.”

“…….”

Talk about changing his tune. Even Udyr would weep.

It was absurd, but I let out a quiet laugh. My stomach had also been screaming after going nearly a month without a proper meal.

*Let’s eat something decent for once.*

I spoke in a solemn voice.

“I approve of your attitude. Lead the way.”

“Where would you like to go, sir?”

“I’m tired of grilled pork belly and teppanyaki. Let’s go for something pricier today.”

“Th-then, sir!”

Jinho-hyung’s eyes widened.

“Hanwoo![^2] The pasture-raised beef famous for its incredible marbling?”

“What the hell are you talking about? We’re going out for gopchang.[^3]”

“…….”

“If you don’t like it, starve.”

Thump.

Jinho-hyung grabbed my shoulder and spoke with a solemn expression.

“I’ve always wanted to eat that.”

The early dinner that began at five that afternoon ended at a third-round makgeolli bar, and Jinho-hyung was completely plastered.

“Krroooorr.”

“…….”

I had seen this scene somewhere before.

As I felt a strange sense of déjà vu and hoisted Jinho-hyung onto my back, my phone rang.



〈Designer-Brand Junkie

**Designer-Brand Junkie**

See you tomorrow at the same time, same place.



It was a short text message. The sender was Team Leader Choi.



* * *



The downside—and upside—of Sleep Mode was that it reduced the amount of time I needed to sleep. Other than when I had suffered serious injuries fighting Jopil, I had never slept for more than three hours.

*It’s useful for training.*

Three in the morning.

I woke up in peak condition and sat cross-legged. At some point, circulating my qi had become how I began and ended every day.

Fwoosh.

A wave of internal energy began to flow.

The fifteen years of internal energy surging from my dantian cleansed the waste products accumulated inside my body and breathed vitality into dormant acupoints.

Ding.

> **System**
>
> - You have finished circulating your qi.
>
> - Your internal energy has increased very slightly.

By the time I opened my eyes at the System notification, more than two hours had passed. If I were in Murim, I would have gone straight to the training yard to warm up, but the real world came with all sorts of restrictions.

Especially in a goshiwon, where the rooms were packed together like a chicken farm.

*Damn goshiwon. I need to get out of here soon.*

This was an age when training was done with money, too. People who made good money had several spacious private training rooms, while people like me had no choice but to adapt to poor conditions.

“Huff. Inhale.”

I spent the entire morning running around the neighborhood, then continued with basic bodyweight exercises without taking a break after I returned. Maybe it was because my Stats had increased, but instead of getting tired, I felt more and more energized.

Watching me, Jinho-hyung asked with a horrified look:

“Don’t you get tired?”

“Not really.”

“I’ve never seen anyone do one-arm push-ups as easily as you. How many have you done?”

“I don’t know. I counted to three hundred, then got too lazy to keep counting.”

“You’re a monster. Is that normal for a C-rank Hunter?”

“By the way, Seong Jinho.”

“Huh?”

“Why are you here?”

Jinho-hyung had appeared ten minutes earlier with a haggard face, and he still hadn’t left my room.

“Can’t you tell? I came to eat ramen.”

Tap tap. Ssshhk.

He naturally dropped a raw egg onto the noodles, which were almost cooked.

His control of the burner flame to leave the egg perfectly runny was worthy of a Peak master.

“Give me three reasons you have to stuff your face with that here.”

“First, there’s no TV in my room. Second, there’s a TV in your room. Third, ramen tastes best when you eat it while watching TV.”

The words poured out of him like a flowing stream, and my blood started boiling.

“Just buy one! If you don’t have money, take mine!”

“Ah, maybe not. I’m leaving soon anyway. Why bother adding to my luggage?”

“Then stop coming in and out of here and bothering me…… Huh? What did you just say?”

“What?”

“No, wait. You’re leaving?”

“Ah, that.”

Jinho-hyung scratched his matted hair.

“It just worked out that way. The date isn’t set yet, but I’m planning to move out soon. I can’t stay holed up here forever.”

“…….”

“Why are you looking at me like that?”

“No, it’s nothing.”

I awkwardly looked away.

Who living in a goshiwon didn’t have a story of their own? I had mine, and Jinho-hyung had his. It would be rude to ask for the reason.

*Still, it’s a shame.*

He was someone I’d spent years with, like a friend and a brother. And now he was leaving so suddenly.

Caught up in complicated feelings, I cautiously opened my mouth.

“Hyung, by any chance……”

“I know what you’re about to say, but I respectfully decline.”

Had he realized what I was going to say? Jinho-hyung cut me off decisively and continued.

“Kid, I’m thirty years old. I’ll fill my own bowl.”

“Then there’s nothing I can do.”

I had thought I could probably live with Jinho-hyung, but my premature meddling seemed to have pricked his pride.

With a crumpled expression, he opened the lid of the pot.

“You should’ve just said so from the start.”

“What are you talking about? You weren’t even planning to.”

“What nonsense. I only cooked one because you said you weren’t eating.”

“……?”

Wait a second. How had the conversation suddenly ended up here?

After several seconds of silence, I finally spoke.

“What are you talking about? What’s this about cooking something all of a sudden?”

“Obviously, ramen.”

Jinho-hyung glared at me with a threatening look.

“There’s always someone who says he isn’t eating, then asks for a bite when you cook it well. How many times have I fallen for that one with you?”

“…….”

“So a C-rank Hunter reaches into his poor hyung’s bowl? Are you even human?”

“…….”

So when he had been talking about his bowl earlier, he had meant an actual bowl.

I wanted to throw his own words right back at him.

*Is that thing even human?*

I was a fucking idiot for thinking I could live with someone like him.

Feeling deeply ashamed of myself, I threw on some clothes. It was almost time to meet Team Leader Choi.

Bang!

I slammed the door hard enough to break it and left. One last shout rang out behind me.

“If you’re going to the market, get some kimchi!”

Ah, I wanted to kill him.



* * *



*Where was the place again?*

I dredged up my memories from about twenty days ago and arrived at the meeting place.

It was a large café in the heart of a forest of skyscrapers. A handsome man sitting by the window spotted me and waved.

“Over here.”

I didn’t need him to say anything. There were dozens of tables in the café, yet Team Leader Choi was the only customer sitting inside.

*He’s still handsome.*

Wearing a thin casual suit, Team Leader Choi looked as though he had just stepped out of a fashion shoot. A successful man in his twenties who had everything: looks, money, personality……

No. Leave personality out of it.

After exchanging a brief handshake, we sat down.

“Have you eaten?”

“No.”

Team Leader Choi tilted his head.

“Really? You look like you’ve eaten ramen.”

“…….”

Damn it. This guy’s nose was incredible.

It was too embarrassing to explain the whole story about what had happened at the goshiwon, so I hurriedly changed the subject.

“It’s lunchtime, but there’s no one here.”

“We’re closed.”

“What?”

“The windows are covered with curtains, and there’s a ‘Closed’ sign on the door. Of course no one’s coming in.”

I looked around. Just as Team Leader Choi had said, everything was covered up.

I had assumed the café would naturally be open since it was the meeting place, so I hadn’t noticed. The whole situation was so strange that I blinked.

“But you’re open right now.”

The lights inside were bright, and the air-conditioning kept the place cool. I could glimpse at least ten employees, so why had they closed the door?

Team Leader Choi answered calmly.

“We have to. There’s a customer.”

“You said you weren’t open.”

“That’s up to the owner, isn’t it?”

“Uh…… Team Leader, I’m asking just to be sure.”

“You don’t need to ask. This café is mine.”

Right. I had figured as much.

Thinking back, the café had also been empty except for the two of us the last time we met.

*I keep digging, and the hole never ends.*

I clicked my tongue and said:

“Team Leader, you have a lot of money.”

“I have enough that I don’t need to worry about running short. That’s why I can put a contract like this in front of you.”

Team Leader Choi smiled gently and handed me a folder.

“Now, shall we talk business?”

There was no reason to hesitate any longer. I nodded firmly.

“Let’s.”

An hour later, the System alert rang out just as I finished signing the last page.

Ding.

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities.

[^2]: Hanwoo is a Korean breed of native cattle whose beef is prized for its marbling.

[^3]: Gopchang is a Korean dish made from grilled intestines, usually beef intestines.
```
