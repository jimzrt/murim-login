<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0866.txt",
      "sha256": "2940fb059ea60cae2c2cb31c4d418af1ad6aaf849b203b78f4bbb00fb82781eb",
      "bytes": 12807
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "598e88da59845a3a2ca3e9e626fffb22966020806208cf959a8382e10ee656b2",
      "bytes": 1592
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "254e3ed5b743b438f8b2efd684a89f59a630ff2ef07a9f703967ee02b375d05a",
      "bytes": 229368
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "971bbe9d19948fb4aea0e62b68fca58e2aae3869427a1c40653f0601221613df",
      "bytes": 819
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ec63215444fe42130f8c7b5d52890ab33b6b6931f2f782fb23ee38ac08b93004",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "02a15fd64a3c5d8163922f4aea207aea5e56383c49bde92113ebf606cde055c6",
      "bytes": 874
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "6af5d6c2e203d26c7f6a30d472a72bc2d9259b10a0e4a32d813762724a2fe10e",
      "bytes": 920
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2828ea7bee972440f65017b5509bb1115b51d80c6fc97bc319b084093d131e7f",
      "bytes": 255571
    }
  ],
  "estimated_tokens": 9298
}
-->

# Durable State Update — Chapter 866

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
1 and safe_through 866. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 866. Profile updates may replace only one
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
  "chapter": 866,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 866,
    "continuity_sources": [866],
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
    "Prince Shangshan and his party remain inside the imperial palace under surveillance; the Emperor postponed Shangshan’s audience until the next day.",
    "Baek Yeon helped the fourth prince seize the throne in a coup, betrayed the late Emperor and Crown Prince, and led a purge in which 30,000 people were arrested and killed.",
    "Hong Jin was unable to detect or stop the coup and is resolved to protect Shangshan in fulfillment of the late Emperor’s final wish and out of personal devotion.",
    "Shangshan is thirteen and has demonstrated composure in the face of death and the ability to make Baek Yeon bow his head.",
    "An unidentified guest has entered the pavilion at night, apparently brought there by Hong Jin past the guards."
  ],
  "continuity_sources": [
    865
  ],
  "open_questions": [
    "Who is the uninvited guest Hong Jin brought into the pavilion?",
    "What does the Emperor intend for Prince Shangshan, and why was his audience postponed?",
    "What does Hong Jin hope to accomplish by bringing the guest to the pavilion?",
    "What happened between Hong Jin and the old eunuch, and why did Hong Jin leave the East Depot?"
  ],
  "safe_through": 865,
  "temporary_decisions": [
    "Render 창위 as “Changwei,” the collective term for the East Depot and Embroidered Uniform Guard.",
    "Render 혈사자 as “Blood Envoy,” Baek Yeon’s sobriquet.",
    "Render 동창 as “East Depot.”",
    "Render 금의위 as “Embroidered Uniform Guard” and 금위군 as “Imperial Guards.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 일신     | **One God**         |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 산서     | **Shanxi**             |
| 공자      | **Young Master**                                                |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 은영술 | **concealment techniques** | Stealth arts associated with ninjas. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 창위 | **Changwei** | Collective term for the East Depot and Embroidered Uniform Guard. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 865
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he asserts imperial authority while tactically conceding the prince’s authority and enforcing protocol with ruthless decisiveness.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; he orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 865
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 865
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and sees protecting him as both a final imperial duty and a personal commitment; he trusts Jin Taekyung to keep the prince safe and has unresolved ties to former East Depot associates.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 865
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃866화



초대하지 않은 밤손님을 맞이하는 건 썩 달가운 상황이 아니다.

하물며 그가 대단한 수준의 은영술(隱映術)을 익힌 초절정 고수라면 더더욱.

“진 공자, 늦었지만 소개할게요. 이쪽은…….”

“아닐세. 이렇게 허락도 없이 불쑥 찾아왔으니, 내 입으로 직접 소개하는 것이 최소한의 도리겠지.”

스륵.

홍진의 말을 끊은 불청객이 복면을 내리자, 수염 하나 없는 매끈한 얼굴이 드러났다.

성별을 쉽게 짐작할 수 없을 만큼 중성적인 체구와 홍진과 비교했을 때 십 년은 어려 보이는 외모.

거기에 더해 초절정에 오른 일신의 무위(武威)까지.

이 모든 상황과 요소들을 머릿속에서 조합해 봤을 때, 불청객의 정체를 유추하는 것은 그리 어려운 일이 아니었다.

“동창(東廠)?”

불청객이 고개를 끄덕였다.

“제법 눈썰미가 있군.”

불쑥 찾아온 것으로도 모자라 자연스러운 하대까지.

맘에 들지는 않지만, 어떤 의미로는 차라리 편하다.

나도 똑같이 하면 그만이니까.

“뭐, 이 정도도 모르겠으면 나가 죽어야지.”

“말솜씨도 거침없고.”

“거침없는 게 주둥이뿐일까.”

“좋군. 좋아.”

소리 없이 웃은 불청객이 포권을 취하며 말했다.

“정식으로 인사하지. 동창 병필태감(秉筆太監), 마삼보(馬三保)라고 하네.”

동창 병필태감? 마삼보?

관직명을 보아하니 언뜻 들어도 고위직 같긴 한데, 이름은 어디 옆집 개똥이 수준이다.

추가 설명을 요구하는 내 눈빛에, 홍진이 입을 열었다.

“병필태감은 동창의 이 인자가 맡는 관직이에요. 서열로 따지자면 우두머리인 장인태감(掌印太監) 다음이죠.”

나는 놀란 눈으로 불청객, 아니 마삼보를 바라보았다.

그의 신분이 생각했던 것 이상으로 대단해서이기도 했지만, 동창의 이 인자씩이나 되는 거물이 왜 이 야심한 시각에 은밀하게 찾아왔는지에 대한 의문이 더욱 컸다.

더군다나 앞서 홍진을 대하던 늙은 환관의 태도가 어떠했는지 똑똑히 보고 느낀 후였으니까.

“동창과는 이미 사이가 틀어진 것 아니었습니까? 아까 전의 상황만 봐도 절대 좋아 보이진 않던데.”

홍진을 향한 내 물음에, 마삼보가 다시 한번 웃었다.

“확실히 보통은 아니로군. 그런 말을 내 면전에서 아무렇지 않게 꺼내다니.”

“그쪽한테 물어본 거 아닌데.”

“상관없네. 다만 그렇게 보였다니 다행일 뿐이야. 같은 편도 속아 넘어갈 정도였으니, 금의위 쪽은 말할 것도 없겠어.”

속아 넘어가?

그 의미심장한 말에 순간 멈칫한 내가 홍진을 바라보았다.

“……연기였다고요? 그게 전부?”

“정확히 말하자면 처음부터 의도했던 것은 맞아요. 연기는 아니었겠지만. 그 사람은 오래전부터 날 싫어했거든.”

홍진의 대답에 마삼보가 고개를 끄덕였다.

“음. 확실히 오래됐지. 얼추 기억하기로는 삼십 년도 넘은 것 같은데.”

“사람 잘 골랐더라, 마 첩형(貼刑). 아니, 이제는 태감 어른이라고 불러드려야 하나?”

“이런. 못 본 사이에 더 짓궂어졌군. 나 같은 사람이 언감생심 생각이나 했겠나. 잠시 자네 자리를 맡아 놓은 것뿐이지.”

“전혀.”

단호하게 대답한 홍진이 말을 이었다.

“자네라면 충분히 그 자리에 앉을 자격이 있어. 예전에도 그랬고, 지금도 마찬가지지.”

“……허 참. 그러고 보니 인사를 잊었군.”

고개를 절레절레 흔든 마삼보가 홍진의 어깨를 두드렸다. 씁쓸함과 반가움이 절반씩 뒤섞인 얼굴로.

“비록 시기가 좋지 않지만, 이렇게라도 다시 보게 되어 반갑네.”

“나 역시.”

불알 없는 두 사나이의 감동적인 재회를 지켜보고 있노라니, 나도 모르게 뜨거운 눈물이 흐르……지는 않았다.

감동적인 재회는 개뿔.

사정도 다 안 알려 주고 지들끼리만 떠드는데 뭔 놈의 눈물이 나온단 말인가.

하지만 마삼보와 홍진이 서로의 어깨를 맞잡고 있는 그 광경 자체는 내가 보기에도 썩 훈훈했다.

감동을 떠나서, 마삼보는 동창의 이 인자니까.

더불어 지금까지 오간 대화에 담긴 의미는 결코 부정적인 것이 아니었다.

‘밀약(密約).’

모두 사전에 약속되어 있던 부분이 틀림없다. 어디서부터 시작되어, 어디까지가 끝인지는 아직 모르지만.

그리고 내 기다림은 생각보다 금세 끝났다.

짧은 재회를 끝마친 두 사람이 차례대로 입을 열었으니까.

“마 태감과 저는 동기예요. 같은 날 처음으로 황궁에 발을 디뎠죠.”

“같은 날 자르기도 했지. 혹시 기억나나? 자네가 내 바로 앞 순번이었는데.”

“그랬었나?”

“확실하게 기억해. 비명 한 마디 내지르지 않는 걸 보고 참 독한 놈이라고 생각했었지.”

두 사람의 대화를 듣고 있던 내가 떨떠름하게 물었다.

처음보다는 조금 더 공손해진 어투로.

“그, 혹시 두 분이 같은 날 자르셨다는 게.”

“뭐겠어요. 그거지.”

“맞네, 그거.”

“……아.”

설마 했는데 이거 실화냐.

‘불알 동기라니.’

이것이 바로 어메이징 황궁인가.

불알친구. 입사 동기 정도는 명함도 못 내밀 것 같다.

물론 함께 자르고 들어온 사이인 만큼 그 끈끈함도 비교하지 못할 정도일 것이다.

“동창에 들어온 시기도 엇비슷했고, 같이 승승장구했었죠.”

“얼추 맞는 것 같군. 늘 자네가 나보다 한 걸음 앞섰던 것만 빼면.”

“물론 그랬을 때도 있었지. 하지만 창공(廠公) 어른께 가장 신뢰받던 건 항상 마 태감 그대였어. 특히 무공에 대한 자질은 비단 나뿐만이 아니라 동창 내의 그 누구도 따라올 자가 없었고.”

그들이 나누는 대화 중 무엇이 사실인지 모르겠지만, 적어도 마삼보의 무공에 관한 홍진의 평가에는 조금의 과장도 없을 것이라는 생각이 문득 들었다.

처음 보자마자 느꼈던 마삼보의 기운은 나나 백연과 비교해도 결코 아래가 아니었으니까.

‘물론 공력이 전부가 아니지만.’

내심 중얼거린 나는 마삼보의 전신을 훑었다.

전체적인 신장과 팔다리의 길이. 어느 부분의 근육이 유난히 발달했는지와 무슨 무기를 사용할 것 같은지.

이 정도면 정신질환에 가까운 직업병이지만, 마주한 상대를 미리 파악하는 건 중요한 습관이다.

단, 상대를 쓸데없이 불쾌하게 만들지 않는다는 가정하에.

“젊은 친구가 상당히 매서운 눈썰미를 지녔군.”

불쑥 들려온 마삼보의 목소리에, 나는 내심 입맛을 다시며 대답했다.

“그건 제가 할 말 같은데요.”

“왜, 너무 빨리 알아차려서 놀랐나?”

“음, 조금은.”

“오래된 습관일세. 내가 비록 자네와 같은 무림인은 아니지만, 언제 어디에서나 촉각을 곤두세우고 있어야 하거든.”

최대한 은밀히 살폈고, 눈치챌 수도 없을 만큼 짧은 시간이었다.

그러나 마삼보는 홍진과 대화를 나누는 사이에도 그 사실을 알아차렸다. 이는 그의 기감이 어지간한 초절정 고수보다도 뛰어나다는 것을 의미한다.

‘이게 동창인가?’

동창과 금의위.

합쳐 창위(廠衛)라 불리는 이 두 단체가 무슨 일을 하는지는 이미 들어서 알고 있다.

요인 암살. 감시와 첩보 및 기타 등등.

그들은 극한까지 단련된 첩보 요원이고, 뛰어난 암살자들이며 군인이다.

거기에 더해 천자라는 눈부신 후광을 등에 업고 사법기관으로서의 역할도 한다고 들었다.

그만큼 두 집단이 지닌 실권도, 무력도 엄청날 것이다.

‘당장 말단 금의위나 동창의 환관들만 봐도 범상치 않았지.’

사실, 범상치 않다는 표현조차 부족하다.

최소가 초일류, 과반수가 절정 고수였으니까.

황궁까지 오는 길에 내 두 눈으로 직접 확인한 절정 고수의 숫자만 무려 수백에 달한다.

이것마저도 그저 일부라는 것을 생각한다면, 아직 드러나지 않은 전력은 그야말로 무시무시할 정도였다.

‘그리고 이런 황궁이 암천과 손을 잡는다면, 만에 하나 정말로 그렇게 된다면…….’

차가운 한기가 등골을 타고 솟구친다. 앞에 선 마삼보의 눈동자에 비친 내 얼굴은 어느새 딱딱하게 굳어 있었다.

“자네, 나를 경계하고 있군.”

“경계가 아니라 의문이라고 해 둡시다. 아직까지는.”

“아직까지는?”

“두 분이 아주 끈끈한 사이인 건 더 말 안 해도 충분히 알겠고, 그보다는 아직 제가 듣지 못한 사실들이 많은 것 같은데요.”

“그래, 그렇겠지.”

마삼보가 빈 의자에 털썩 주저앉으며 말을 이었다.

“자네가 가진 의문을 풀어 주기 위해서, 어디서부터 어디까지 얘기해야 하겠나?”

“처음부터 끝까지. 전부.”

“전부는 곤란해. 오늘 이 자리에서 마무리하기에는 너무나도 긴 이야기가 될 테니까. 하지만 우선 한 가지는 말해 두지.”

“그럼 그것부터 들어 봅시다.”

“지금으로부터 약 한 달 전, 나는 한 사람 앞으로 밀서(密書)를 보냈네. 그 안에는 금의위 중 일부가 정체를 감추고 북상하고 있다는 정보와 그 종착지가 산서성일 것이라는 내 개인적인 추측이 담겨 있었지.”

홍진이 조용한 목소리로 마삼보의 말을 받았다.

“마 태감이 전해 준 정보 덕분에, 비록 짧지만 대비할 수 있는 시간이 있었어요. 제가 진 공자에게 도움을 청한 건…… 충분한 고민 끝에 내린 결정이었죠.”

“……!”

나로서도 처음 듣는 이야기다.

단지 홍진이 급해서, 손을 내밀 만한 사람이 마땅치 않아서 나를 선택한 줄만 알았다.

하지만 아니었다.

홍진은 신중하게 고민했고, 내게 구원을 요청했다.

그리고 그 과정에는 누군가의 보이지 않는 손길이 있었다.

홍진의 수완이 아무리 좋아도, 만 리도 넘게 떨어진 황도에서 벌어지는 일을 일일이 파악하는 것은 불가능하니까.

‘그러나 동창의 이 인자라면, 충분히 가능하지.’

천하 곳곳에 세작들을 심어 놓고 여러 동향을 감시하는 동창이다. 하물며 앞마당이라 할 수 있는 황도에서 벌어지는 일이라면 말할 필요도 없다.

단지 그것만으로 내 의문이 해결되는 것은 아니었지만.

“당신이 상산왕 전하를 구하기 위해 도움을 주었다는 것은 잘 알겠습니다. 하지만…….”

“무슨 말을 하려는지 알 것 같군. 그래, 자네 말이 맞아. 나는 이미 폐하께 충성을 맹세한 몸일세.”

내가 말을 이으려던 그 순간. 한발 앞서 입을 연 마삼보가 낮은 목소리로 덧붙였다.

“지금 옥좌에 앉아 있는 저 역적이 아닌, 선황(先皇) 폐하께 말이야.”

“……!”

“내가 왜, 어떻게 아직까지 황궁에 남아 있는 줄 아나?”

툭. 투둑.

하얗게 물든 주먹의 틈새로 핏방울이 점점이 떨어진다. 동창의 이 인자는 지금껏 들어 본 적 없는 성마른 목소리로 말을 이었다.

“해야 할 일이 있었으니까. 어떤 고난이 닥쳐도 참고 이겨 내며 때를 기다려야 했으니까……!”

미처 큰 소리로 토해 내지 못한 그 외침이, 사방을 둘러싼 내 공력에 가로막혀 덧없이 흩어진다.

지난 십여 년간 숨겨 왔던 감정을 드러낸 마삼보는 입술을 파르르 떨었다.

그리고 자신의 오랜 벗을 바라보며 끓어오르는 목소리로 말했다.

“홍진. 홍 첩형. 내 친구이자 동지여. 비로소 그때가 찾아왔네. 더 이상은 미룰 수 없어.”

“마 태감. 설마…….”

“그래.”

쿠궁.

난데없이 울려 퍼진 굉음과 함께 어두웠던 하늘이 눈부시게 물들었다. 창밖으로 쏟아지는 빗물과 낙뢰(落雷)를 뒤로한 채, 마삼보는 씹어뱉듯이 뇌까렸다.

“역적이 어지럽힌 저 하늘을, 우리의 손으로 바로 세우세.”
```

## Final English reading copy

```markdown
# Chapter 866

Having an uninvited guest show up at night is never a welcome situation.

Even less so when he’s a Supreme Peak master skilled in extraordinary concealment techniques.

“Young Master Jin, I know it’s late, but let me introduce you. This is…”

“No need. Since I’ve barged in without permission, the least I can do is introduce myself.”

*Slide.*

The uninvited guest interrupted Hong Jin and lowered his mask, revealing a smooth, clean-shaven face.

His build was so androgynous it was hard to guess his gender, and he looked a good ten years younger than Hong Jin.

On top of that, his personal martial prowess had reached Supreme Peak.

Put all those clues together, and it wasn’t hard to guess who the uninvited guest was.

“The East Depot?”

The guest nodded.

“You’ve got a sharp eye.”

As if barging in uninvited weren’t enough, he was addressing me casually, too.

I didn’t like it, but in a way, it made things easier.

I could just do the same.

“Well, if I couldn’t figure out something this obvious, I’d be better off going out and dying.”

“And you don’t mince words, either.”

“Is it only my mouth that doesn’t mince words?”

“Good. Very good.”

The uninvited guest smiled without making a sound, then clasped his hands in a formal salute.

“Allow me to introduce myself properly. I’m Ma Sanbao, Brush-Holding Eunuch of the East Depot.”

Brush-Holding Eunuch of the East Depot? Ma Sanbao?

Judging by the office, it sounded like a high-ranking position. But his name sounded like something you’d call the kid next door: Dogshit.

At the questioning look in my eyes, Hong Jin spoke up.

“The Brush-Holding Eunuch is the East Depot’s second-in-command. In terms of rank, he comes right after the Chief Eunuch.”

I stared at the uninvited guest—or rather, Ma Sanbao—with wide eyes.

His position was more impressive than I’d imagined, but I was even more curious why a big shot like the East Depot’s second-in-command had come here in secret at this late hour.

Especially after seeing for myself how that old eunuch had treated Hong Jin earlier.

“Hadn’t you already fallen out with the East Depot? Judging by what happened earlier, you two didn’t exactly seem to get along.”

Ma Sanbao laughed again at my question to Hong Jin.

“You’re certainly no ordinary young man. To bring that up so casually right in front of me…”

“I wasn’t asking you.”

“That doesn’t matter. I’m just glad it looked that way. If even our own side was fooled, the Embroidered Uniform Guard certainly won’t suspect a thing.”

Fooled?

I paused at his suggestive remark and looked at Hong Jin.

“……So it was an act? The whole thing?”

“To be precise, I did intend it from the start. But I wouldn’t call it an act. He’s disliked me for a long time.”

Hong Jin answered, and Ma Sanbao nodded.

“Mm. It’s been a long time, all right. If I remember correctly, it’s been over thirty years.”

“You picked a good man, Ma Constable. Or should I call you Eunuch now?”

“My, you’ve gotten even more mischievous since I last saw you. A man like me would never have dared dream of such a position. I was only holding yours for a while.”

“Not at all.”

Hong Jin answered firmly, then continued.

“You’re more than qualified to sit in that position. You were back then, and you still are now.”

“……Good grief. Come to think of it, I forgot to greet you.”

Ma Sanbao shook his head and patted Hong Jin on the shoulder, his face half bitter and half glad to see him.

“Even if the timing couldn’t be worse, I’m glad to see you again, even like this.”

“Likewise.”

Watching two men without balls have an emotional reunion, I felt hot tears begin to run down my face—

No, I didn’t.

An emotional reunion, my ass.

They hadn’t even filled me in on what was going on. Why the hell would I be crying?

Still, even I had to admit that the sight of Ma Sanbao and Hong Jin holding each other by the shoulders was pretty heartwarming.

And that was aside from the sentiment. Ma Sanbao was the East Depot’s second-in-command.

Besides, the meaning behind their conversation so far was definitely not a bad one.

*A secret pact.*

There was no doubt they’d arranged all of this beforehand. I just didn’t know where it had begun, or where it would end.

And my wait for an explanation ended sooner than I expected.

The two men finished their brief reunion and took turns speaking.

“Eunuch Ma and I are from the same cohort. We first set foot in the imperial palace on the same day.”

“And got cut on the same day, too. Do you remember? You were right before me in line.”

“Was I?”

“I remember it clearly. You didn’t let out a single scream. I thought you were one tough bastard.”

I’d been listening to them talk, and now I asked with a queasy look on my face.

My tone was a little more polite than before.

“Um, when you say you were both cut on the same day…”

“What do you think? That.”

“That’s right. That.”

“……Oh.”

I’d suspected as much, but was this for real?

*Ball-cutting buddies.*

Was this what made the imperial palace so amazing?

Childhood friends, coworkers who’d joined on the same day—they didn’t even come close.

And since they’d been cut and entered the palace together, their bond must have been on an entirely different level.

“We joined the East Depot around the same time and rose through the ranks together.”

“That sounds about right. Except you were always one step ahead of me.”

“That was true at times. But the Director always trusted you the most, Eunuch Ma. And when it came to martial arts talent, no one in the East Depot could match you—not just me.”

I didn’t know how much of their conversation was true, but it suddenly struck me that Hong Jin’s assessment of Ma Sanbao’s martial arts was probably not exaggerated in the slightest.

The energy I’d sensed from Ma Sanbao the moment I saw him was in no way inferior to mine or Baek Yeon’s.

*Of course, internal energy isn’t everything.*

I muttered to myself and looked Ma Sanbao over from head to toe.

His overall height and the length of his limbs. Which muscles were especially developed, and what kind of weapon he looked like he might use.

At this point, it was practically a mental disorder—an occupational hazard. But getting a read on the person in front of me was an important habit.

Provided it didn’t needlessly offend them.

“Young man, you’ve got a remarkably keen eye.”

At Ma Sanbao’s sudden remark, I answered, inwardly clicking my tongue.

“I was about to say the same about you.”

“What, surprised I noticed so quickly?”

“Mm. A little.”

“It’s an old habit. I may not be a Murim martial artist like you, but I have to stay alert, wherever I am.”

I’d examined him as discreetly as possible, in a fraction of a second—too quickly for him to have noticed.

And yet Ma Sanbao had caught on while talking with Hong Jin. That meant his Qi Sense was better than that of most Supreme Peak masters.

*So this is the East Depot.*

The East Depot and the Embroidered Uniform Guard.

I’d already heard what these two organizations, collectively known as the Changwei, did.

Assassinations of key figures. Surveillance, intelligence gathering, and so on.

They were intelligence agents trained to the limit, skilled assassins, and soldiers.

And with the Son of Heaven’s dazzling authority behind them, I’d heard they also served as a law enforcement agency.

Their influence and strength must be immense.

*Even the low-ranking Embroidered Uniform Guard and East Depot eunuchs I’ve seen so far were no ordinary people.*

“No ordinary” didn’t even begin to cover it.

Even the weakest were Supreme First Rate, and more than half were Peak masters.

On the way to the imperial palace, I’d seen hundreds of Peak masters with my own eyes.

And if that was only a fraction of their numbers, the strength they hadn’t yet revealed was truly terrifying.

*And if an imperial palace like this were to join hands with Dark Heaven—if, by some chance, it really came to that…*

A cold shiver ran up my spine. My face, reflected in Ma Sanbao’s eyes, had stiffened without me noticing.

“You’re wary of me.”

“Let’s call it a question mark, not wariness. For now.”

“For now?”

“I don’t need you to tell me you two are close. What I want to know is that there still seem to be a lot of facts I haven’t heard.”

“Yes, I suppose so.”

Ma Sanbao dropped into an empty chair and continued.

“How much do I need to tell you to clear up your questions?”

“Everything. From beginning to end.”

“Everything would be difficult. It’s far too long a story to finish here today. But I’ll tell you one thing first.”

“Let’s hear that, then.”

“About a month ago, I sent a secret letter to someone. It contained information that some members of the Embroidered Uniform Guard were heading north while concealing their identities, along with my personal suspicion that their destination was Shanxi Province.”

Hong Jin quietly picked up where Ma Sanbao left off.

“Thanks to the information Eunuch Ma gave me, I had some time to prepare, even if it wasn’t much. Asking Young Master Jin for help was a decision I made after thinking it through carefully.”

“……!”

This was the first I’d heard of it, too.

I’d thought Hong Jin had chosen me simply because he was desperate and had no one else he could turn to.

But that wasn’t it.

Hong Jin had thought it through carefully and asked me for help.

And somewhere along the way, someone had been lending a hand behind the scenes.

No matter how capable Hong Jin was, there was no way he could keep track of everything happening in the imperial capital, over ten thousand *ri* away.

*But the East Depot’s second-in-command could manage it.*

The East Depot had spies planted all over the land, watching for all sorts of developments. And if it was something happening in the imperial capital—practically its own front yard—there was no need to explain further.

That alone didn’t answer all my questions, though.

“I understand that you helped save His Highness Prince Shangshan. But…”

“I think I know what you’re about to say. Yes, you’re right. I’ve already sworn my loyalty to His Majesty.”

Just as I was about to continue, Ma Sanbao spoke first, then added in a low voice,

“Not the traitor sitting on the throne now. The late Emperor.”

“……!”

“Do you know why, and how, I’ve remained in the imperial palace all this time?”

*Tap. Tap.*

Drops of blood fell one by one through the gaps in his whitened fist. The East Depot’s second-in-command continued in a strained voice I’d never heard from him before.

“Because there was something I had to do. Because I had to endure whatever hardships came and wait for my moment……!”

The cry he couldn’t let out at full volume struck the barrier of my internal energy surrounding us and faded away.

Ma Sanbao’s lips quivered as he revealed emotions he’d kept hidden for over a decade.

Then he looked at his longtime friend and spoke in a voice boiling with feeling.

“Hong Jin. Hong Constable. My friend and comrade. The time has finally come. We can’t put it off any longer.”

“Eunuch Ma. Don’t tell me…”

“That’s right.”

*Rumble.*

A thunderous boom suddenly rang out, and the dark sky was flooded with blinding light. With the rain and lightning pouring beyond the window behind him, Ma Sanbao muttered as if spitting the words out.

“Let’s set right, with our own hands, the sky that traitor has thrown into chaos.”
```
