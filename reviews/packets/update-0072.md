<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0072.txt",
      "sha256": "8a4f933f054ca51d48424289adc11e585b690a0649ae396fda96aa07ebbd09d9",
      "bytes": 14065
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6dc07b37eefac8afb6f56f66de906e65049913c9575b597a6bcc74024bf3215a",
      "bytes": 4197
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "90ef6a27c463b5dae4eada1caa8c099d168f92e05c62f20b05273e04b860adf6",
      "bytes": 3458
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "41526dd8c4a866e2b116bd6ae164b2bfeb05dab7b292f5cdfbebbc6d51070438",
      "bytes": 1220
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "30b418e53cc658bfa18f83adfbaa63e73306195dc27725789d6295e8e82c04bf",
      "bytes": 23807
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "5f5b11064b44f95e445058879bfacec1b213aa4063da3da90056d3609355e81b",
      "bytes": 8155
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "2e4e8ba2984aa5ce51e1d164519edd1b43925c5df728de3f39f38454e966be34",
      "bytes": 2803
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "088125fa8b045f20487ca5730679ac2d0d3d207301c840012253ab301ae21b1f",
      "bytes": 2984
    }
  ],
  "estimated_tokens": 11980
}
-->

# Durable State Update — Chapter 72

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 72. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 72. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 72,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 72,
    "continuity_sources": [72],
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
    "Taekyung’s spar with Mukyung ends with Mukyung’s victory and the destruction of Taekyung’s pavilion; Taekyung survives and recovers in the Medicine King Hall.",
    "Hyuk Mujin is badly injured in the incident and remains under treatment after Taekyung is discharged.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder’s hidden disciple.",
    "Jin Mukyung reunites with Jin Wikyung after three years but remains detached and prioritizes sword training.",
    "Jin Wikyung plans to summon every sect in Shanxi Province on New Year’s Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin.",
    "Jin Wikyung searched the family’s records for Dark Heaven but found no information.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months.",
    "Soyul is five years old and does not know that her parents are dead.",
    "Taekyung is Level 50 with fifty remaining points and fifteen years of internal energy after investing fifty points in Agility during the duel.",
    "Jin Wikyung arranges fifteen days of temporary cohabitation between Taekyung and Jin Mukyung while Taekyung’s residence is rebuilt.",
    "Jin Wikyung publicly maintains a formal image but is openly recognized within the family as excessively devoted to Taekyung.",
    "Jin Wikyung stops Taekyung and Mukyung from fighting and requires both brothers to apologize and cooperate.",
    "Mukyung imposes rules of polite speech, silence, and obedience over the training hall during the cohabitation.",
    "The Returnee title grants Taekyung All Stats +10 and activates the Login and Logout functions.",
    "Mukyung has spent three years attempting to open the Ren and Du meridians.",
    "Wipeng visits Song Sword Sect with thirty retainers, delivers Wikyung’s New Year’s Day summons, and implies that the summons is also a warning.",
    "Mukyung is a naturally gifted martial-arts genius who can adapt the Jin Family’s forms between spear and sword.",
    "Mukyung’s training overwhelms Taekyung through practical combat, acupoint restraints, and a shallow neck cut presented as a lethal lesson; he tells Taekyung that he died once that day."
  ],
  "continuity_sources": [
    71,
    70
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung’s summons.",
    "It remains unresolved whether Jin Wikyung will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack."
  ],
  "safe_through": 71,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung’s deferential speech; use Three Questions Gorge for 삼문협.",
    "Use Alliance Leader for 맹주 and summon for 소집 to preserve the distinction from an invitation.",
    "Retain Great Hero for 대협 and Ghost Sword for 귀검.",
    "Use Sleep Mode for 수면 모드 and Medicine King Hall Master for 약왕당주.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, and Heart Demon for 심마; use Paralysis Acupoint for 마혈 and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
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
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |

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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |

## Listed compact profiles

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 71
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 71
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 70
- **Aliases:** None revealed
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 70
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

## Korean source

```text
＃72화



“넌 오늘 한 번 죽었다.”

서늘한 목소리가 이어졌다.

“사지가 잘려서, 분근착골을 당해서, 목이 베여서. 고통의 크기나 형태는 달라도 넌 죽었다. 확실하게.”

살았다는 안도감이 사라지자 그 빈자리를 채운 건 분노였다.

나는 후들거리는 다리로 일어섰다. 입 안 가득 고여 있는 핏물을 꿀꺽 삼키고 진무경을 노려봤다.

‘이런 미친 새끼.’

당장이라도 저 잘난 면상에 주먹을 꽂아 넣고 싶었지만 꾹 참았다. 내가 진무경보다 약해서가 아니다. 놈의 말이 틀리지 않다는 걸 알기 때문이다.

“……그래서? 하고 싶은 말이 뭐지?”

기다렸다는 듯이 대답이 튀어나왔다.

“네 명줄이 얼마 안 남았다는 얘기다.”

“뭐?”

“넌 반쪽짜리야. 무인도, 낭인도 아닌 반쪽짜리. 너처럼 어설픈 놈이 무림에 나가면 죽기 딱 좋지.”

반쪽짜리.

어쩌면 지금의 내 상태를 가장 정확히 표현한 말일지도 모르겠다. 나는 헌터인 동시에 무림인이니까.

“산서잠룡? 초일류 고수? 지나가던 개가 웃겠다. 넌 단순한 싸움꾼이야. 무인치고는 어설프고 낭인처럼 실리적으로 싸우는 것도 아니지. 운이 좋아 살아남은 걸 네 실력이라고 착각하지 마라.”

나는 간신히 입을 열었다.

“그럼 조필은? 네 말대로면 그것도 운인가?”

“일문일살 조필? 보나 마나 적을 앞에 두고 방심할 만큼 멍청한 놈이었겠지. 너는 그 상황을 뒤집을 만한 마지막 한 수가 있었던 거고.”

“……!”

“왜? 직접 보지도 않았으면서 너무 정확하게 맞췄다고 생각하나?”

진무경이 혀를 찼다.

“귀먹은 노인네도 태원진가의 삼공자가 망나니라는 사실을 아는데 조필이 몰랐을까. 방심한 순간 놈도 끝장난 거지.”

이 새끼 스토커야, 뭐야.

부처님 손바닥 위의 손오공이 된 기분이다. 그의 추측은 그만큼 정확했다.

“분명히 말해 두는데.”

진무경이 가라앉은 눈으로 나를 응시했다.

“그 운이 통하는 것도 여기까지야.”

“…….”

“무림에는 온갖 괴물들이 득실거린다. 그리고 그들은 조필처럼 방심하지 않아. 넌 더 이상 망나니 삼공자가 아니라 산서잠룡이니까.”

말 한마디, 한마디가 폐부를 찌른다. 진무경의 말은 모두 사실이었고, 이제는 현실을 받아들여야 할 때다.

“제기랄.”

맞다. 나는 반쪽짜리다.

시스템이라는 인생 최고의 행운 덕분에 어찌어찌 살아남았지만 그것도 딱 여기까지인 모양이다.

하지만…….

‘역시 난 운이 좋아.’

문제를 일찍 발견한 것도 모자라 풀이를 도와줄 훌륭한 해결사까지 내 눈앞에 있다.

“도와줘.”

진무경.

이미 완성된 절정의 무인이자 무공의 천재.

그리고.

“……형.”

내 형이다.

띠링.



제한 시간 : 9일 20시간 23분



* * *



무림인이라는 족속은 자존심이 강하다. 녹슨 칼 한 자루를 차고 싸구려 화주를 마시는 삼류 낭인도 그럴진대, 명문대파의 자제들은 그 오만함이 하늘을 찌를 정도다.

“도와줘, 형.”

그런 의미에서 이놈은 사람이 됐다. 삼 년 전이었다면 울먹거리며 큰형님께 달려갔을 텐데…… 성장했다. 기대 이상으로.

‘묘한 녀석이야.’

성격도, 무공도 종잡을 수가 없다. 그건 장점인 동시에 단점이다. 다만 한 가지 확실한 사실은, ‘진짜 고수’에게는 아무것도 통하지 않는다는 거다.

‘하지만 재능은 진짜다.’

진무경은 지난 삼 년간 천무학관에서 수많은 기재를 만났지만 진태경의 성장 속도는 타의 추종을 불허했다.

‘그놈들에게는 없는 장점도 있지.’

무공을 한눈에 파악하는 눈. 뛰어난 실전 감각과 다른 사람의 조언을 받아들이는 귀도 있다.

‘비록 아직은 뒤죽박죽 섞여 있는 반쪽짜리지만.’

시간이 흐른다면 부족한 부분은 채워지고 튀어나온 부분은 들어갈 것이다. 그때 진태경의 무공은 완성된다.

태극(太極)이 조화를 이룬 것처럼.

‘태극이라, 너무 거창한가?’

이거, 슬슬 부담이 되기 시작한다.

하지만 궁금해서 견딜 수가 없다. 저놈이 어떻게 성장할지. 어디까지 올라갈지.

‘갈 길이 바쁘겠군.’

늦어도 보름 안에는 출발해 천무학관으로 돌아가야 한다. 진무경은 마침내 입을 열었다.

“뭐 해? 창 들어.”

“형!”

환하게 밝아지는 진태경의 얼굴을 보니, 문득 드는 생각이 있었다.

‘그런데 이 자식이 언제부터 말 놨지?’

훈련 강도가 한 단계 올라가는 순간이었다.



* * *



쾅.

진위경은 잔뜩 충혈된 눈으로 마지막 서류에 인장을 찍었다.

근 열 시진에 달하는 중노동에서 해방됐지만 전혀 기쁘지 않았다. 어차피 내일 아침이면 새로운 일거리가 쌓여 있을 테니까.

‘이것들이 나 몰래 새끼를 치나.’

그나마 슬슬 끝이 보인다는 게 한 줄기 위안일까.

최종 검토까지 끝낸 진위경이 작은 종을 흔들었다. 맑은 종소리가 채 사라지기도 전에 건장한 체격의 하인 둘이 나타났다.

“부르셨습니까, 소가주님.”

“가져가게.”

“예.”

능숙한 솜씨로 수레에 서류를 차곡차곡 쌓은 하인들이 물러가려던 그때였다.

“아, 자네는 남고.”

지목당한 하인이 눈을 동그랗게 떴다.

“저 말씀이십니까?”

“맞네, 자네.”

하인과 단둘이 남게 된 진위경은 근엄한 목소리로 말문을 열었다.

“그래, 요즘 일은 할 만한가?”

“예에. 소가주님의 은덕 덕분입죠.”

“뭐 불편한 건 없고?”

“어이구, 그럴 리가요.”

하인, 칠득이는 연신 고개만 끄덕거렸다. 천자문도 못 뗀 까막눈이지만 그에게도 듣는 귀가 있고 보는 눈이 있다.

이번 전쟁에서 승리한 태원진가는 산서제일가로 우뚝 섰고 소가주인 진위경은 빠른 수습과 공정한 대처로 군자검(君子劍)이라 불리기 시작했다.

‘그런 대단하신 분께서 왜 나를?’

긴장 때문에 가슴이 두근거렸다. 내가 무슨 실수를 했나? 아니면 혹시라도 무공에 대한 재능을 본 건가?

전자라면 큰일이고, 후자라면 인생 역전의 기회다.

‘내가 근골 하나는 튼튼하지. 어릴 때부터 배앓이 한 번 안 했을 정도니까.’

검을 차고 영웅건을 휘날리는 자신의 모습이 벌써부터 눈앞에 어른거린다.

반면 몽롱하게 풀어지는 칠득이의 눈동자를 본 진위경은 흠칫했다.

‘뭐야, 이놈.’

뭔가를 간절히 원하는, 영혼을 바쳐 갈구하는 듯한 눈빛.

사내가 사내에게 보낼 만한 눈빛은 아니다.

‘설마?’

말로만 듣던 남색(男色)…… 아니, 아니다. 섣부른 오해는 금물이다. 믿어 주고 아껴 줘야 하는 태원진가의 식솔 아닌가.

진위경은 애써 의심을 지우며 입을 열었다.

“자네 이야기는 많이 들었네.”

“소, 소인에 관해서 말입니까?”

“물론일세. 오래전부터 눈여겨보고 있었지.”

정확히는 오래전부터가 아니라 사흘 전부터다.

진위경은 매우 중요한 임무를 맡길 믿을 만한 하인을 물색했고, 칠득이는 그가 직접 선발한 최적의 인재였다.

“인의예지(仁義禮智)를 두루 갖춘 인재. 그게 바로 자네였지.”

“이럴 수가……!”

인의예지를 두루 갖춘 특급 하인, 칠득이는 전율했다. 일자무식인 그는 인의예지가 무슨 뜻인지 몰랐지만 인재라는 말은 찰떡같이 알아들었다.

‘내가 인재라고?’

힘 좋고 성실하다는 칭찬은 들어 봤어도 인재라는 소리는 처음 듣는다. 게다가 다른 사람도 아니고 하늘 같은 소가주님께 이런 평가를 듣다니.

이게 꿈인가 생시인가. 칠득이는 극렬한 흥분 상태에 휩싸였다. 너무 흥분한 나머지 혀도 꼬였다.

“저도! 저도 소가주님을 항상 지켜보고 있었습니다!”

순간 진위경이 움찔 몸을 떨었다.

내가 방금 뭘 들은 거지?

“……그게 무슨 소린가?”

“오랫동안 이런 순간을 꿈꿔 왔습니다. 언젠가 소가주님의 뒤에 서는 그 날을!”

“잠깐만. 말이 좀 이상하잖은가. 왜 하필 자네가 내 뒤에 서?”

“헛.”

칠득이는 숨을 삼켰다. 뒤에 서지 말라. 즉, 앞장서서 공을 세우라는 뜻이다.

“그럼 제가 앞에 있겠습니다!”

“아냐! 그것도 이상해!”

하지만 칠득이의 야생마 같은 질주는 멈추지 않았다.

“소인, 이 한 몸 기꺼이 바치겠습니다!”

진위경은 눈앞이 캄캄해졌다!

“안 돼. 하지 마! 바치지 마!”

“소가주님!”

후욱, 후욱. 칠득이는 가쁜 숨을 내쉬었고, 진위경은 공력을 끌어 올렸다.

‘설마 이런 일이 생길 줄이야.’

아무리 그가 열린 사고방식의 소유자라고 해도 이건 아니다.

개인적인 성적 취향이야 그렇다 쳐도, 그 대상이 되는 건 사양이었다. 진위경은 침을 꿀꺽 삼켰다.

“자네, 그럼 정말 남색……?”

칠득이가 눈을 번쩍 떴다. 태원진가의 무인들이 입는 남색 무복을 입을 생각에 가슴이 쿵쾅거렸다.

“예! 시켜만 주십시오!”

“날 노리다니 어림도 없다. 이노옴-!”

철썩!

절정 고수의 따귀는 강력했다. 실 끊어진 인형처럼 풀썩 쓰러진 칠득이를 내려다보며 거친 숨을 내쉬던 진위경이 황급히 종을 울렸다.

띠링. 띵.

“소가주님, 부르셨…… 헉. 칠득아!”

기겁하는 하인에게 진위경이 말했다.

“당장 끌고 나가게!”

“이, 이게 무슨 일입니까?”

“저놈이 나를…… 아닐세, 됐네.”

도저히 식솔에게 할 수 있는 말이 아니다. 그는 난생처음 느껴 보는 분노와 서러움에 눈물이 날 것 같았다.

“조, 조치하겠습니다.”

눈치 빠른 하인이 칠득이를 업었을 때였다. 진위경은 가장 중요한 말을 잊지 않고 덧붙였다.

“그리고 저놈.”

“예?”

“보직 해임하게.”

“아.”

하인은 문득 칠득이가 맡은 임무를 떠올렸다.

‘식사 운반.’

인의예지를 두루 갖춘 특급 하인, 칠득이에게 주어진 가장 중요한 임무는 진무경과 진태경에게 매 끼니를 가져다주는 것이었다.

“내 아우들 근처에 얼씬거리지 못하게 해. 알았나!”

“옛!”



* * *



[훈련 1일 차]

오늘부터 일기를 쓰기로 했다.

이번 수련으로 배운 것을 잊지 않기 위해서다.

진무경의 지도 아래 온종일 창만 휘둘렀다. 하루의 시작과 끝은 늘 비무로 끝난다. 죽도록 맞았지만 버틸 만하다.

난생처음 먹을 갈아 보는데, 이거 은근히 재밌네.



[훈련 2일 차]

오늘도 죽어라 창만 휘둘렀다. 그 덕분인지 근력과 체력 능력치가 올랐고 진가창법이 구 성에 도달했다.

혼자 수련할 때보다 훨씬 빠른 속도긴 한데, 차라리 이 시간에 다른 절정 무공을 익히는 게 나을 것 같다는 생각이 든다.

하지만 진무경도 생각이 있겠지.

먹을 갈기 조금 귀찮아졌다. 피곤하다.



[훈련 3일 차]

또 진가창법이다. 다른 무공 가르쳐 달라고 했다가 뒤지게 맞았다. 정신이 썩어 빠졌단다.

필사적으로 공격을 피하는 와중에 진가보법이 팔 성으로 올랐다. 젠장, 이거 은근히 효과 있네.



[훈련 4일 차]

훈련을 시작한 이래 하루 두 시간 이상을 자 본 적이 없다.

대부분은 진무경과 수련, 비무, 수련, 비무의 반복이다. 어제부터는 밥 먹는 시간도 아깝다고 벽곡단으로 때우기 시작했다.

시스템이 있지만 슬슬 체력적으로 한계다.



[훈련 5일 차]

팔이 아파서 먹을 조금만 갈았다.

하늘이 노랗다. 잔다.



[훈련 6일 차]

시스템에 메모장 기능이 왜 없는지 이해가 안 되네.

먹 갈다가 열받아서 벼루를 깼다. 진무경한테 맞았다.



[훈련 7일 차]

진가보법이 구 성에 도달했다. 동시에 레벨도 하나 올랐다.

얼마나 지긋지긋하게 익혔는지, 요즘은 평소 걸어 다닐 때도 보법을 밟는다. 소름이 돋았다.



[훈련 8일 차]

오늘따라 손발이 꼬인다. 내가 알던 무공이 아닌 느낌.

천 번, 만 번도 넘게 펼친 무공이 낯설다. 진무경은 그게 자연스러운 현상이라고 했다.

뭔 개소리야?

표정이 불손하다고 맞았다.



[훈련 9일 차]

알 것 같다.



* * *



쾅!

목창 끝에서 응축된 공기가 터져 나갔다. 주르륵 밀려 나간 진무경이 부러진 검을 보며 혀를 찼다.

“아슬아슬하게 성공이군.”

나는 대답하지 않았다. 멍하니 창을 쥔 채 생각했다.

‘이런 거였구나.’

내가 익힌 무공들을 속속들이 안다고 생각했다. 하지만 아니었다. 그건 산 중턱에서 스스로 정상에 올랐다고 착각한 것에 불과했다. 무공이 오를 때마다, 새로운 풍경이 보인다.

‘바로 지금처럼.’

띠링. 띠링. 띠링.



- [진가창법]을 대성했습니다!

- [진가보법]을 대성했습니다!

- 업적, [일류 무공을 대성하다]를 달성했습니다!

- 보상으로 새로운 스킬, [비급 제작]이 생성됩니다!

- 모든 능력치가 크게 상승합니다!

- 레벨 업!

- 레벨 업!



시스템의 파도가 밀려왔다.
```

## Final English reading copy

```markdown
# Chapter 72

“You died once today.”

The cold voice continued.

“Your limbs were cut off, you were subjected to Tendon-Splitting and Bone-Twisting, and your throat was cut. The degree and form of the pain may have been different, but you died. Without a doubt.”

Once the relief of being alive faded, anger took its place.

I stood on trembling legs. After swallowing the blood pooled in my mouth, I glared at Jin Mukyung.

*What a fucking lunatic.*

I wanted to drive my fist into that smug face right away, but I held myself back. Not because I was weaker than Jin Mukyung. Because I knew he was right.

“…So? What are you trying to say?”

His answer came immediately, as if he had been waiting for me to ask.

“That you don’t have much life left.”

“What?”

“You’re only half-finished. You’re neither a martial artist nor a wandering martial artist. A half-baked mess. Someone as sloppy as you is just begging to die the moment he enters the Murim.”

Half-finished.

That might have been the most accurate description of my current state. I was a Hunter and a martial artist at the same time.

“Sleeping Dragon of Shanxi? First Rate master? Even a passing dog would laugh. You’re just a brawler. You’re sloppy for a martial artist, and you don’t even fight as pragmatically as a wandering martial artist. Don’t mistake surviving through good luck for skill.”

I barely managed to open my mouth.

“Then what about Jopil? Was that luck too, according to you?”

“Jopil, One Question, One Kill? He was obviously stupid enough to let his guard down in front of an enemy. You just happened to have one last move capable of turning the situation around.”

“……!”

“What? Do you think I guessed too accurately despite not seeing it myself?”

Jin Mukyung clicked his tongue.

“Even a deaf old man knows that the Third Young Master of the Jin Family of Taiyuan is a wastrel. Did Jopil not know? The moment he let his guard down, he was finished too.”

*What is this guy, a stalker?*

I felt like Sun Wukong trapped in the Buddha’s palm. His guess was that accurate.

“Let me make this clear.”

Jin Mukyung fixed me with a somber gaze.

“That luck of yours stops working here.”

“……”

“The Murim is crawling with all kinds of monsters. And they don’t let their guard down like Jopil did. You’re no longer the Jin Family’s wastrel of a Third Young Master. You’re the Sleeping Dragon of Shanxi.”

Every word stabbed straight into my vitals. Everything Jin Mukyung said was true, and it was time for me to face reality.

“Damn it.”

He was right. I was half-finished.

Thanks to the greatest stroke of luck in my life—the System—I had somehow survived this long. But it seemed that luck had taken me exactly this far.

*But… I really am lucky.*

Not only had I discovered the problem early, but an excellent problem-solver was standing right in front of me to help solve it.

“Help me.”

Jin Mukyung.

A fully realized Peak martial artist and a genius of martial arts.

And—

“…Hyung.”

My older brother.

Ding.

> **System**
>
> **Time Limit:** 9 days 20 hours 23 minutes

* * *

Murim people were a proud lot. Even a Third Rate wandering martial artist who wore a rusty sword at his waist and drank cheap baijiu was like that, so the arrogance of scions from prestigious sects reached the heavens.

“Help me, hyung.”

In that sense, this guy had become a decent human being. Three years ago, he would have run to his eldest brother with tears in his eyes… but he had grown. Far more than expected.

*He’s a strange one.*

Neither his personality nor his martial arts could be easily understood. That was both a strength and a weakness. But one thing was certain: nothing worked against a *true master*.

*But his talent is real.*

Over the past three years at Heaven’s Gate Temple, Jin Mukyung had encountered countless prodigies, but Jin Taekyung’s rate of growth was unmatched.

*He has advantages they don’t.*

He could understand martial arts at a glance. He had excellent combat instincts, and he also knew how to listen to other people’s advice.

*Though for now, he’s still a half-finished mess with everything jumbled together.*

As time passed, his weaknesses would be filled in and his excesses would be smoothed out. When that happened, Jin Taekyung’s martial arts would be complete.

Like taiji achieving harmony.

*Taiji? Is that a little too grandiose?*

This was starting to become burdensome.

But he could not stop wondering. How would that bastard grow? How far would he climb?

*I’m going to be busy.*

He had to leave and return to Heaven’s Gate Temple within fifteen days at the latest. Jin Mukyung finally opened his mouth.

“What are you doing? Pick up your spear.”

“Hyung!”

Seeing Jin Taekyung’s face brighten, Jin Mukyung suddenly had a thought.

*When did this bastard start speaking informally to me?*

That was the moment the intensity of his training rose another level.

* * *

Bang.

Jin Wikyung stamped his seal onto the final document with heavily bloodshot eyes.

He had been freed from nearly twenty hours of backbreaking labor, but he was not happy at all. New work would be piled up by tomorrow morning anyway.

*Are these things breeding when I’m not looking?*

The only comfort was that he could finally see the end.

After completing his final review, Jin Wikyung rang a small bell. Before its clear sound had even faded, two sturdily built servants appeared.

“Did you call, Lesser Family Head?”

“Take these away.”

“Yes, sir.”

The servants skillfully stacked the documents onto a cart. Just as they were about to leave, Jin Wikyung spoke.

“Ah. You stay.”

The servant he had pointed to blinked in surprise.

“Me, sir?”

“That’s right. You.”

Once he was alone with the servant, Jin Wikyung began speaking in a solemn voice.

“So, how have you been finding the work lately?”

“Very well, sir. It’s all thanks to your kindness, Lesser Family Head.”

“Nothing causing you any inconvenience?”

“Oh, goodness, of course not.”

The servant, Childeuk, did nothing but nod repeatedly. He was illiterate and could not even get through the Thousand Character Classic, but he still had ears to hear and eyes to see.

After its victory in the recent war, the Jin Family of Taiyuan had risen to become the foremost family in Shanxi. Its Lesser Family Head, Jin Wikyung, had begun to be called the Junzi Sword[^1] for his swift recovery efforts and fair handling of the aftermath.

*Why would such an esteemed person want me?*

His heart pounded with nerves. Had he made some mistake? Or had Jin Wikyung perhaps noticed his talent for martial arts?

The former would be disastrous. The latter would be a chance to turn his life around.

*My bones and muscles are sturdy, at least. I never even had a stomachache as a child.*

He could already see himself wearing a sword at his waist and letting his hero’s headband flutter in the wind.

But when Jin Wikyung saw Childeuk’s eyes growing hazy, he flinched.

*What the hell is wrong with this guy?*

Childeuk’s eyes were filled with desperate longing, as if he were willing to offer his soul to obtain whatever he wanted.

They were not the kind of eyes one man should direct at another man.

*Don’t tell me…?*

Male love, something he had only heard about…

No, that was not it. He could not jump to conclusions. Childeuk was a member of the Jin Family, someone he should trust and cherish.

Jin Wikyung forcibly erased his suspicions and spoke.

“I’ve heard a lot about you.”

“Y-You have, sir?”

“Of course. I’ve been keeping an eye on you for a long time.”

More precisely, not for a long time. Only for the past three days.

Jin Wikyung had been searching for a reliable servant to entrust with a very important task, and Childeuk was the ideal candidate he had personally selected.

“A talented man possessing all four virtues—benevolence, righteousness, propriety, and wisdom. That’s you.”

“How can this be…!”

Childeuk, an exceptional servant possessing all four virtues, shuddered with emotion. He had no idea what those four virtues meant, but he understood the word “talent” perfectly.

*I’m talented?*

He had been praised for his strength and diligence, but this was the first time anyone had called him talented. And to receive such an assessment from the Lesser Family Head himself, a man as lofty as the heavens…

Was this a dream or reality? Childeuk was swept up in overwhelming excitement. He was so excited that even his tongue became tangled.

“I’ve always been watching you too, Lesser Family Head!”

Jin Wikyung’s body flinched.

*What did I just hear?*

“…What do you mean?”

“I’ve dreamed of this moment for a long time. The day I would stand behind you, Lesser Family Head!”

“Wait. That sounds strange. Why would you stand behind me?”

“Ah.”

Childeuk swallowed. Jin Wikyung was telling him not to stand behind him. In other words, he wanted Childeuk to take the lead and win glory.

“Then I’ll stand in front!”

“No! That’s strange too!”

But Childeuk’s charge, like a wild stallion, did not stop.

“I will gladly offer this one body of mine!”

Jin Wikyung’s vision went dark.

“No. Don’t do it! Don’t offer it!”

“Lesser Family Head!”

Huff, huff.

Childeuk breathed heavily, and Jin Wikyung gathered his internal energy.

*I never thought something like this would happen.*

No matter how open-minded he was, this was too much.

Personal sexual preferences were one thing, but he had no desire to be the object of them. Jin Wikyung swallowed hard.

“Then… are you really into men?”[^2]

Childeuk’s eyes flashed. He was thinking about wearing the navy-blue uniform worn by the Jin Family’s martial artists.

“Yes! Just tell me to do it!”

“How dare you set your sights on me? Not a chance, you bastard!”

Smack!

A slap from a Peak master was powerful. Childeuk collapsed like a puppet with its strings cut, and Jin Wikyung stared down at him while breathing heavily before hurriedly ringing the bell.

Ding. Ding.

“Lesser Family Head, did you call—? Gasp. Childeuk!”

Jin Wikyung spoke to the horrified servant.

“Take him out immediately!”

“W-What happened?”

“That bastard tried to… No, never mind.”

It was not something he could say to one of his family’s servants. For the first time in his life, anger and wounded sorrow brought him close to tears.

“I-I’ll take care of it.”

Just as the quick-witted servant hoisted Childeuk onto his back, Jin Wikyung added the most important part.

“And that man.”

“Yes?”

“Remove him from his post.”

“Ah.”

The servant suddenly remembered Childeuk’s assignment.

*Delivering meals.*

The most important duty given to Childeuk, an exceptional servant possessing all four virtues, was to bring every meal to Jin Mukyung and Jin Taekyung.

“Don’t let him go anywhere near my younger brothers. Understood?”

“Yes, sir!”

* * *

### Training Day 1

I decided to start keeping a diary today.

So I would not forget what I learned during this training.

Under Jin Mukyung’s guidance, I did nothing but swing a spear all day. Every day begins and ends with a spar. I got beaten half to death, but it’s bearable.

This is my first time grinding ink, and it’s surprisingly fun.

### Training Day 2

I swung my spear to the point of death again today. Perhaps because of that, my Strength and Stamina stats increased, and the Jin Family’s Spear Technique reached the ninth stage.

It’s progressing much faster than when I trained alone, but I can’t help thinking that I would be better off learning another Peak martial art during this time.

Still, Jin Mukyung must have his reasons.

Grinding ink has become a little annoying. I’m tired.

### Training Day 3

The Jin Family’s Spear Technique again. I asked him to teach me another martial art and got beaten half to death. He said my mind was rotten.

While desperately dodging his attacks, the Jin Family’s Manoeuvre Technique rose to the eighth stage. Damn it. This is surprisingly effective.

### Training Day 4

Since starting training, I haven’t slept more than two hours in a day.

Most of my time is spent repeating training, sparring, training, and sparring with Jin Mukyung. Starting yesterday, I began using fasting pills instead of wasting time eating.

Even with the System, I’m reaching my physical limit.

### Training Day 5

My arms hurt, so I only ground a little ink.

The sky is yellow.

Going to sleep.

### Training Day 6

I don’t understand why the System doesn’t have a notepad function.

I got angry while grinding ink and broke the inkstone. Jin Mukyung beat me.

### Training Day 7

The Jin Family’s Manoeuvre Technique reached the ninth stage. My Level also increased by one.

I’ve practiced it so obsessively that these days, I even use the footwork when I’m simply walking around.

I got goose bumps.

### Training Day 8

My hands and feet keep getting tangled today. It feels like the martial arts I know, but not quite.

The martial arts I’ve performed thousands—even tens of thousands—of times feel unfamiliar. Jin Mukyung said it was a natural phenomenon.

*What the hell is he talking about?*

I got beaten because my expression was disrespectful.

### Training Day 9

I think I get it.

* * *

Bang!

Compressed air erupted from the tip of the wooden spear. Jin Mukyung skidded backward and clicked his tongue as he looked at his broken sword.

“That was a narrow success.”

I did not answer. I stood there blankly, gripping my spear.

*So that’s what it was.*

I thought I knew the martial arts I had learned inside and out. But I had been wrong. I had merely mistaken the middle of the mountain for the summit.

Whenever my martial arts rose to a new level, a new landscape came into view.

*Just like now.*

Ding. Ding. Ding.

> **System**
>
> - You have achieved mastery of **Jin Family’s Spear Technique**!
>
> - You have achieved mastery of **Jin Family’s Manoeuvre Technique**!
>
> - Achievement **Master a First Rate Martial Art** completed!
>
> - As a reward, a new Skill, **Martial Arts Manual Creation**, has been generated!
>
> - All Stats have increased significantly!
>
> - Level Up!
>
> - Level Up!

A wave of System notifications swept over me.

[^1]: *Junzi* is a Confucian ideal referring to a morally upright and cultivated gentleman.

[^2]: In Korean, *nam-saek* can refer both to male homosexuality and to the color navy blue, creating the misunderstanding between Jin Wikyung and Childeuk.
```
