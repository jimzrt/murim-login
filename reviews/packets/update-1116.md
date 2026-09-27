<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1116.txt",
      "sha256": "b39d59c6252dfa4f5e875ff895def8f0e75471efd2030d364405c3275778ecf8",
      "bytes": 13336
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "96a69a2efed443cb3fd2fd2f23c8d7f4129b726250e415e684c3f2ab7c1de676",
      "bytes": 1348
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "31812534175ab90a1ae43243464f560a3462689ef66803e5cfefef29a922b435",
      "bytes": 244625
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "3c7caa2b7a1aa4e83343d6e8c149abe803cea1ec989137dcecc76692526720c2",
      "bytes": 915
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "88e174c8ce2f95ab1a1421741f45cb9776fabba516851e221056e06a876c7ecb",
      "bytes": 544
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "54b80543ac9dc90f178f0926c1d9dd59ae74a3b611ad36a90c75ce60f77b4f94",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "c0d94898223b2f39860ec2830174c092a21bb365f9144b3121e903df41deb089",
      "bytes": 554
    },
    {
      "path": "characters/Hak Su.md",
      "sha256": "7145124aae4f753df89720c79a8f832340260d22fbb5c5d2120e131725ea1b07",
      "bytes": 615
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "078c6bfad0a7e7d39db946de4e851489f9d1f936c87c625ec731e60a68fb0f72",
      "bytes": 289028
    }
  ],
  "estimated_tokens": 9489
}
-->

# Durable State Update — Chapter 1116

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
1 and safe_through 1116. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1116. Profile updates may replace only one
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
  "chapter": 1116,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1116,
    "continuity_sources": [1116],
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
    "The West Gate has fallen; more than half its garrison are casualties, and some survivors retreated to the Inner City.",
    "Jin Taekyung and Cheongpung are badly injured in the Inner City; Taekyung is alive and had forced himself to stand.",
    "Taekyung has rallied those around him to keep fighting for the Inner City's people.",
    "The South Gate defenders were ordered to retreat, with elites covering the rear; the outcome is unknown.",
    "The Slaughter Saint and Bow Saint are heading to the Inner City to join Taekyung.",
    "The Bow Saint destroyed an incoming rain of fireballs with an arrow of light.",
    "The Blood Lord's status after his earlier advance toward the Inner City is unknown."
  ],
  "continuity_sources": [
    1114,
    1115
  ],
  "open_questions": [
    "Will Jin Taekyung survive his injuries, and can he receive treatment from the Divine Physician?",
    "What is the Bow Saint hiding, and why did she accept the possibility of Taekyung’s death?",
    "Can the South Gate defenders retreat safely, and can the Inner City’s defenders stop the Blood Lord?"
  ],
  "safe_through": 1115,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 살성     | **Slaughter Saint**           | —              |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 신법     | **movement technique**                           |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 선배     | **Senior**                                   |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 학수 | **Hak Su** | Cheongheoja’s Senior Disciple and Hak Woo’s senior brother. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 장제자 | **Senior Disciple** | The Seafaring King's designated successor. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 남문 | **South Gate** | A gate that was never built because of the rear cliff. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |
| 서녕 | **Xining** | Capital of Qinghai. |
| 곤륜오선 | **Kunlun Five Immortals** | Collective name for five senior Kunlun elders. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 살성 | 청허자 | fellow martial master and former acquaintance | you | blunt and familiar | Recognizes him from a prior meeting. |
| 혈주 | 곤륜오선 | hostile opponent to elder martial masters | you old men | insulting and threatening | Threatens to tear them apart and orders them to leave. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1115
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and suspects the Lord wants Jin Taekyung above all else; he recognizes Cheongpung and remembers a debt to Sword Saint Mae Jonghak.

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1114
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1115
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1112
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hak Su.md

# Hak Su (학수)

- **Safe through:** Chapter 1090
- **Aliases:** None
- **Role:** Hak Su is Cheongheoja’s Senior Disciple and a senior brother to Hak Woo in the Kunlun Sect.
- **Personality:** Gracious and hopeful, he responds to Taekyung’s mistakes with patience and warmth.
- **Voice:** He speaks in courteous, formal phrases and tempers earnest reassurance with hearty, lightly humorous remarks.
- **Relationships:** Cheongheoja is his Master, and Hak Woo is his youngest Junior Brother; he treats Jin Taekyung warmly as a Fellow Daoist.

## Korean source

```text
＃1116화



청해성 최후의 보루라고 할 수 있는 서녕성은 익히 알려져 있듯 수성전에 있어 매우 유리한 이점을 가졌다.

그러나 지난 세월에 걸쳐 벌어진 수십 차례의 전투를 돌이켜 보자면, 침입자들에게 가장 큰 악몽을 선사한 것은 단단하면서도 높은 성벽뿐만이 아니었다.

“역시, 저 악귀 같은 놈들도 해자(垓字)만큼은 쉽게 넘지 못하는군요.”

중년 도사의 감탄 섞인 뇌까림에, 곤륜파의 장문인인 청허자가 고개를 끄덕였다.

“만약 저 해자가 없었다면 지금보다 곱절은 힘든 싸움이 되었을 것이다. 진즉 성문이 뚫리고도 남았을 터이니.”

청허자의 말은 사실이었다.

그 폭만 무려 십여 장이요, 깊이 또한 상당한 해자는 지금 이 순간에도 적들에게 크나큰 희생을 강요하고 있었으니까.

뿐인가.

해자를 넘는다 하더라도 엄청난 두께의 묵철(墨鐵)로 이루어진 성문이 기다리고 있었니, 제아무리 무공을 익힌 암천의 광신도들이라 한들 성문을 노리기보다 피해를 감수하고 성벽을 오를 수밖에 없었다.

물론 압도적인 머릿수와 잠력단을 이용한 힘의 증폭 덕분인지 때때로 성벽이 위태로울 때도 있었지만, 적어도 그들이 지키는 동문(東門)은 다른 어느 곳보다 순조로운 수성전을 이어 가고 있었다.

어쩌면, 지금의 상황만 잘 유지한다면 승리할 수 있지 않을까 하는 마음을 품을 정도로.

그리고 그것은 청허자의 곁에 서 있던 중년의 도사 역시 크게 다르지 않은 듯했다.

“만약 이 전투에서 승리한다면, 모두 함께 본산(本山)으로 돌아갈 수 있겠지요?”

“모두 함께라, 그리된다면 얼마나 좋을까.”

어느 때보다 깊게 가라앉은 청허자의 음성에, 중년의 도사 역시 씁쓸한 표정을 지었다.

“둘째를…… 생각하고 계십니까?”

그 조심스러운 물음에, 잠시 침묵하던 청허자가 고개를 가로저었다.

“아니다.”

“하면.”

“제자를 바른길로 이끌지 못한, 어느 어리석은 스승의 부족함을 생각하고 있었다.”

“……!”

“빈도의 잘못이다. 처음부터 끝까지. 그 모든 것이.”

“스승님…….”

중년의 도사, 아니 청허자의 장제자인 학수(學水)는 안타까운 얼굴로 자신의 스승을 바라보았다.

“자책하지 마십시오. 스승님의 잘못이 아닙니다.”

“그리 생각하느냐?”

“저는 압니다. 아니, 곤륜의 모두가 알지요. 스승님께서 그 누구보다 둘째를 가장 가까이에 두고 각별히 보살피셨다는 사실을.”

“그럴 수밖에 없었다. 늘 온순했던 너나 활기찬 셋째와 달리, 그 아이는 늘 어딘가 거칠고 불안해 보였으니까.”

“스승님께서 학의(學意)라는 도호를 내리신 것도, 그런 이유에서였지 않습니까.”

“그래, 분명 그랬었지.”

어둡고 험한 뒷골목에서 성장한 소년은 그렇게 새로운 이름과 가족을 얻었고, 청허자는 거친 기질을 타고난 자신의 둘째 제자에게 늘 말해왔다.

학의라는 두 글자에 담긴 뜻처럼, 조금 더 의로운 사람이 되라고.

단 한시도 스스로 도사라는 사실을 망각하지 말라고.

“하지만…… 감히 그 누가 짐작이나 할 수 있었겠습니까. 녀석이 암천과 내통하던 간자(間者)였다는 사실을.”

지그시 입술을 깨문 학수가 고개를 내저었다.

“사실 저 역시 아직도 믿기지 않습니다. 믿고 싶지도 않고요.”

그의 시선이 문득 옆을 향했다.

지금은 텅 비어 있는 그 자리에, 자신의 둘째 사제가 여느 때와 같은 삐딱한 얼굴로 서 있을 것처럼.

그러나 그런 일은 벌어지지 않는다.

아니, 불가능했다.

학의는 이미 죽었으니까.

그는 오늘 동이 트기 전, 깊은 밤을 노려 간자를 포박하고자 했던 이들에게 맞서 저항하던 끝에 결국 목숨을 잃었다.

그리고 뒤늦게 현장에 도착한 학수는, 잘려 나간 사제의 목과 피가 흐르는 검을 들고 있던 스승의 모습을 볼 수 있었다.

지금처럼, 어느 때보다 슬픈 눈빛을 한 그를.

“……스승님.”

학수가 복잡한 눈빛으로 청허자를 바라보던 그때.

쐐애애액!

공간을 가로지르는 날카로운 파공성과 함께, 온 힘을 다해 경신법을 펼쳐 달려온 전령이 다급한 외침을 토해 냈다.

“장문인!”

피투성이나 다름없는 행색에 더하여 백지장처럼 새하얗게 질린 얼굴.

반사적으로 흘러나오려는 침음성을 삼킨 청허자가 무거운 어조로 입을 열었다.

“어디서 오는 길인가?”

“남문, 후욱. 남문입니다.”

“그렇다는 건, 두 선배께서 내성으로의 퇴각을 명하신 겐가?”

“그걸 어찌…….”

“알겠네. 다른 곳의 상황 역시 다르지 않겠군.”

더 이상의 말은 필요 없었다.

전령의 모습만으로 어렴풋이 상황을 짐작한 청허자가 침착하게 말을 이었다.

“속히 가서 전하게. 곧 동문의 병력을 이끌고 내성으로 합류하겠다고.”

“부디, 무운(武運)을 빕니다.”

짧은 목례와 함께 전령이 떠나자, 학수가 딱딱하게 굳은 얼굴로 입을 열었다.

“먼저 가십시오. 제가 일부 병력과 함께 시간을 벌겠습니다.”

결의로 가득한 눈빛과 음성.

하지만 청허자는 즉각 고개를 가로저었다.

“너를 남겨 두고 떠날 수는 없다.”

대답에 묻어나오는 듯한 스승의 우려에, 학수가 흐릿하게 미소지었다.

“내성까지 가는 길도 결코 쉽지 않을 겁니다. 아니, 어쩌면 이곳보다도 더 위험할 수 있겠지요. 저들에게는 저보다 스승님이 필요합니다.”

충분히 가능성 있는 예측이었다.

혈주의 맹공에 의해 서문이 무너졌다는 비보는 전고(戰鼓)가 무너지기 직전 동문으로 전달된 상황.

다른 세 곳에 비해 비교적 전력이 약한 적들이 배치된 동문과 달리, 대책 없이 퇴각했다가는 서문을 통해 무인지경으로 성 내부를 휩쓸고 있을 혈주와 광신도들을 맞닥트릴지도 모르는 일이었으니까.

그러나 그런 학수의 의견에도 불구하고, 청허자는 좀처럼 뜻을 굽히지 않았다.

“불허(不許)한다.”

“스승님, 시간이 없습니다!”

조바심을 참지 못한 학수가 다급하게 외친 그때.

“누구에게 말이냐?”

이상하리만치 착 가라앉은 청허자의 음성이, 그의 귓가를 파고들었다.

“……스승님?”

“누구에게 시간이 없느냐 물었다.”

학수는 당황한 얼굴로 눈을 깜빡였다.

아니, 이와 같은 반응을 보이는 것은 비단 그뿐만이 아니었다.

갑작스럽게 뒤바뀐 노 도사의 기세에, 그의 평소 모습을 아는 곤륜파의 제자들은 물론 주위의 수비군들 모두가 청허자를 바라본 그 순간이었다.

그 누구도 예상치 못한 누군가의 음성이 빗줄기를 뚫고 울려 퍼진 것은.

“어찌 대답을 망설이는 거요. 하늘 같은 스승님께서 묻고 계시지 않소.”

철벅.

딱딱한 음성과 함께 비 웅덩이를 밟는 발걸음.

그와 동시에 깊게 눌러쓴 초립(草笠)을 벗은 이립 어림의 사내가, 차가운 눈빛으로 학수를 응시하며 말을 이었다.

“대답하시오, 대사형(大師兄).”

“……!”

“……!”

일순간, 보이지 않는 격동이 성벽 위를 휩쓸었다.

아니, 그것은 경악을 넘어선 무언가였다.

이미 돌아올 수 없는 강을 건넜다고 알려진 망자(亡者)가, 모두의 앞에 모습을 드러냈으니.

그러나 쉽사리 충격에서 벗어나지 못하는 대부분의 사람들과 달리, 말없이 자신의 사제를 바라보던 학수는 이내 침착한 어조로 입을 열었다.

“죽은 줄 알았는데?”

“그리 보였다면, 맞소.”

갑작스럽게 나타난 이립 어림의 사내, 학의가 딱딱하게 굳은 얼굴로 대답했다.

간밤에 잘려 나갔던, 아니 그리 알려졌던 자신의 목을 쓰다듬으면서.

“당신을 진심으로 아꼈던 그 멍청한 놈은 이미 죽었소. 그리고 동이 트기 전에 새로 태어났지.”

“그럼 내가 보았던 그 수급은…….”

“잊은 모양이구려. 서녕의 뇌옥(牢獄)이 얼마나 붐비는지.”

그제야 학수는 문득 떠올릴 수 있었다.

며칠 전 청해성주를 비롯한 몇몇 수뇌부는 저잣거리로 끌려 나와 즉결 처형되었지만, 그들을 제외하더라도 물경 일백이 넘는 죄인들이 뇌옥에서 판결을 기다리고 있었다는 것을.

그리고 그중 학의와 체형이 흡사한 자를 찾아, 모두의 이목을 속일 정도로 완벽한 인피면구(人皮面具)를 제작할 수 있는 누군가의 존재를.

“살성(殺星).”

혼잣말처럼 뇌까린 학수가 작게 고개를 끄덕였다.

“그래, 그렇게 된 거로군.”

모든 것을 인정하는 것이나 다름없는 그의 담담한 태도에, 설마 하는 마음으로 상황을 지켜보던 사람들 사이로 침음성이 흘러나왔다.

학수, 바로 그였다.

암천과 결탁한 배신자의 정체는.

다른 누구도 아닌 곤륜파 장문인의 장제자가, 무려 삼십 년간 몸담았던 사문을 저버린 것이다.

그리고 마지막까지 믿고 싶었던 제자의 이와 같은 모습을, 청허자는 형용할 수 없는 시선으로 바라보고 있었다.

“무슨…… 이유에서였느냐.”

그 짤막한 물음에, 학수가 천천히 입술을 뗐다.

“이유도, 의문도 필요 없다. 오직 주어진 임무만을 생각하라.”

그것은 대답이었고, 동시에 기억이었다.

저 머나먼 사막 너머의 땅에서 태어난 한 갓난아이가, 열세 살의 소년으로 자라날 때까지 수도 없이 들었던.

그렇기에 수십 년이 지나도 거역할 수 없는, 뼛속까지 각인된 의무이자 사명.

“천상천하(天上天下), 만마앙복(萬魔仰伏).”

“……!”

“오직 그것만이 전부요. 더 이상의 이유는 필요 없지.”

파르르 떨리는 스승, 아니 스승이라 불렀던 자의 눈빛을 똑바로 응시하며 학수가 말을 이었다.

지금까지와는 전혀 다른 표정과 목소리로.

“종종 당신에게 그런 말을 하곤 했었지. 청해호(靑海湖)에서 당신을 만난 건, 내 인생 최고의 행운이었다고.”

진심이었다.

청허자는 그 누구보다 도인이라 불릴 자격이 있는 사람이었고, 우연을 가장한 채 청해호 인근을 떠돌던 어느 소년과의 만남을 운명으로 받아들였으니까.

“고마웠소. 딱히 특출난 무재(武才)가 있었던 것도 아니었기에, 지금과 같은 위치에 오르리라는 건 나 자신조차도 몰랐거든.”

하지만 청허자는 신분과 재능을 따지지 않았다.

설령 곤륜파가 정마대전의 여파로 극심한 피해를 입지 않았더라도, 그는 기꺼이 학수를 제자로 받아들였을 것이다.

학수가 간자로서 길러졌듯이, 청허자 역시 본래 그런 사람이었으니까.

“청허자, 모두 당신 덕분이오.”

그의 입가에 선명한 미소가 떠오른 순간.

“학수, 네놈이 감히-!”

보다 못한 학의가 분노에 찬 고함을 터트리며 신형을 내쏘았다.

아니, 지금 이 순간 사문을 등진 배신자를 향해 달려드는 것은 비단 학의 혼자만이 아니었다.

쐐애애액!

표횰한 신법과 범상치 않은 기세.

곤륜십객(崑崙十客)이라 불리며, 향후 곤륜오선의 뒤를 이을 장로들이자 작금의 곤륜파에서 빼놓을 수 없는 중추로 여겨지는 그들은 한 치의 망설임 없이 검을 뽑았고.

서걱!

적의 몸통을 파고든 검광(劍光)과 함께, 뜨거운 핏물이 솟구쳤다.

촤악, 투두둑.

성벽 위에 흩뿌려지는 선혈(鮮血).

그리고 어느덧 앞을 가로막은 청허자의 어깨너머로 보이는 믿을 수 없는 광경에, 학의는 눈을 부릅떴다.

“이게 무슨……!”

“학수라, 그리 불리는 것도 이제 지긋지긋해지던 참이었지.”

목이 베이고 심장이 관통되어 숨이 끊어진 다섯 구의 시신 들을 바라보던 학수가, 아니 암천의 간자가 천천히 고개를 들었다.

자신보다 앞서, 혹은 비슷한 시기에 걸쳐 곤륜파에 스며들었던 또 다른 그림자들과 함께.

“육호(六號). 그게 내 이름이다.”

그 순간.

와득.

이제는 다섯으로 줄어든 곤륜오객이, 정확히는 암천에 의해 길러졌던 간자들이 품에 숨기고 있던 잠력단을 꺼내어 씹어 삼켰다.

스아아아아!

들불처럼 일어나는 거대한 기파 속, 청허자의 나직한 한 마디가 공간을 울렸다.

“진정으로, 너를 남겨두고 떠날 수는 없겠구나.”
```

## Final English reading copy

```markdown
# Chapter 1116

As everyone knew, Xining Fortress—the last line of defense in Qinghai—had an enormous advantage when it came to defending against a siege.

But looking back over the dozens of battles fought over the years, it wasn’t just the fortress’s high, sturdy walls that had given invaders their worst nightmares.

“As expected, even those Fiends can’t cross the moat easily.”

At the middle-aged Daoist’s admiring murmur, Cheongheoja, the Sect Leader of the Kunlun Sect, nodded.

“If we didn’t have that moat, this fight would be twice as hard as it is now. The gates would have been breached long ago.”

Cheongheoja spoke the truth.

Even now, the moat—which was more than ten jang wide and quite deep—was forcing the enemy to pay a terrible price.

And that wasn’t all.

Even if they crossed the moat, they would face the fortress gates, made of immensely thick black iron. No matter how skilled in martial arts Dark Heaven’s fanatics were, they had no choice but to accept the losses and climb the walls rather than attack the gates.

Of course, the walls had occasionally been in danger, perhaps because of the enemy’s overwhelming numbers and the power boost from their Temporary Strength Pills. But at least at the East Gate, which they were defending, the siege was going more smoothly than anywhere else.

So smoothly, in fact, that they could almost believe they might win if they just kept things as they were.

The middle-aged Daoist standing beside Cheongheoja seemed to feel much the same.

“If we win this battle, we can all return to the main sect together, can’t we?”

“All of us together…… How wonderful that would be.”

At the deep, heavy note in Cheongheoja’s voice, the middle-aged Daoist’s expression turned bitter as well.

“Are you thinking about your Second Disciple?”

At the cautious question, Cheongheoja was silent for a moment, then shook his head.

“No.”

“Then……”

“I was thinking about the shortcomings of a foolish master who failed to guide his Disciple down the right path.”

“……!”

“It was my fault. From beginning to end. All of it.”

“Master……”

The middle-aged Daoist—Cheongheoja’s Senior Disciple, Hak Su—looked at his master with sorrow.

“Don’t blame yourself. It wasn’t your fault.”

“Is that what you think?”

“I know it. No—everyone in Kunlun knows. You kept your Second Disciple closer than anyone else and cared for him especially well.”

“I had to. Unlike you, who were always gentle, and your Third Junior Brother, who was full of energy, that child always seemed rough and unsettled.”

“And wasn’t that why you gave him the Daoist name Hak Eui?”

“Yes. That was certainly why.”

The boy had grown up in the dark, treacherous back alleys and gained a new name and a family. Cheongheoja had always told his rough-tempered Second Disciple to become a more righteous person, just as the name Hak Eui implied.

To never forget, even for an instant, that he was a Daoist.

“But…… who could ever have guessed? That he was a spy who’d been conspiring with Dark Heaven.”

Hak Su pressed his lips together and shook his head.

“To be honest, I still can’t believe it. And I don’t want to.”

His gaze suddenly shifted to the side.

For a moment, it seemed as if his Second Junior Brother might be standing there in his usual crooked pose.

But that wasn’t going to happen.

No. It was impossible.

Hak Eui was already dead.

Before dawn today, he had fought against those trying to capture a spy under cover of night, and in the end, he’d lost his life.

Hak Su had arrived at the scene too late. He’d seen his master holding his Junior Brother’s severed head and a sword dripping with blood.

He’d seen his master with eyes sadder than ever—just like now.

“……Master.”

Just as Hak Su was looking at Cheongheoja with a complicated expression—

Whoooosh!

A messenger came racing in, using his movement technique with all his might. His cry burst through the sharp whistle of air as he cut across the space.

“Sect Leader!”

He was covered in blood, and his face was as white as a sheet.

Cheongheoja swallowed the groan that almost escaped him and spoke in a heavy voice.

“Where have you come from?”

“South Gate. Hah…… South Gate.”

“Then the two Seniors ordered a retreat to the Inner City?”

“How did you……?”

“I understand. The situation must be the same elsewhere.”

There was no need to say more. From the messenger’s appearance, Cheongheoja had a rough idea of what had happened. He calmly continued:

“Go at once and tell them. I’ll lead the East Gate forces and join them in the Inner City shortly.”

“May you have good fortune in battle.”

The messenger left with a brief bow. Hak Su spoke, his expression stiff.

“Go ahead without me. I’ll buy you some time with part of the force.”

His eyes and voice were full of resolve.

But Cheongheoja immediately shook his head.

“I can’t leave you behind.”

At the concern in his master’s reply, Hak Su gave a faint smile.

“The road to the Inner City won’t be easy. No—it may be even more dangerous than here. They need you more than they need me.”

It was a perfectly reasonable prediction.

The dire news that the West Gate had fallen to the Blood Lord had reached the East Gate just before the war drums were about to be destroyed.

Unlike the East Gate, where the enemy forces were comparatively weaker than at the other three gates, a retreat without a plan might lead them straight into the Blood Lord and his fanatics, who could be rampaging unchecked through the fortress from the West Gate.

Even so, Cheongheoja would not yield.

“I forbid it.”

“Master, we’re out of time!”

Just as Hak Su shouted in desperation—

“Who is out of time?”

Cheongheoja’s voice sank strangely low, piercing Hak Su’s ear.

“……Master?”

“I asked who’s out of time.”

Hak Su blinked, bewildered.

And he wasn’t the only one who reacted that way.

The old Daoist’s presence had changed so suddenly that the Kunlun Disciples who knew him well—and all the soldiers nearby—were staring at Cheongheoja.

Then, through the rain, a voice no one expected rang out.

“Why hesitate to answer? Your Master, who’s as lofty as the heavens, is asking you.”

Splash.

A foot came down in a puddle, accompanied by a hard-edged voice.

At the same time, a man who looked to be around thirty took off his low-pulled straw hat. He stared at Hak Su with cold eyes and continued:

“Answer me, Senior Brother.”

“……!”

“……!”

A shock rippled across the wall.

No—it was more than shock.

Someone everyone had believed had crossed the point of no return had appeared before them. The man they had believed dead stood before them.

Unlike most of the people, who could not recover from the shock, Hak Su silently looked at his Junior Brother. Then he spoke in a calm voice.

“I thought you were dead.”

“If it looked that way, then I was.”

The man who had appeared so suddenly—Hak Eui—answered with a face set in stone.

He rubbed his neck, which had supposedly been severed last night.

“The fool who truly cared about you is already dead. And before dawn, I was born anew.”

“Then the head I saw……”

“You must have forgotten how crowded Xining’s underground prison is.”

Only then did Hak Su recall.

A few days ago, the Qinghai City Lord and several other leaders had been dragged into the streets and executed on the spot. But even after they were gone, well over a hundred prisoners had remained in the underground prison, waiting for judgment.

And there had been someone who could find a prisoner built like Hak Eui and craft a human-skin mask so perfect it deceived everyone.

“The Slaughter Saint.”

Hak Su murmured the words as if to himself, then gave a slight nod.

“So that’s what happened.”

His calm acceptance of what had happened left the onlookers who had been watching in disbelief murmuring.

Hak Su. It was him.

The traitor who had sided with Dark Heaven.

No one else but the Kunlun Sect Leader’s Senior Disciple had betrayed the sect he’d belonged to for thirty years.

Cheongheoja looked at his Disciple—whose actions he’d wanted to disbelieve until the very end—with an expression beyond words.

“Why……?”

At the brief question, Hak Su slowly parted his lips.

“Don’t seek reasons or question the mission you’ve been given. Think only of your assigned task.”

It was an answer—and a memory.

A newborn child, born on a land beyond a distant desert, had heard those words countless times before he grew into a thirteen-year-old boy.

A duty and a mission etched into his bones, impossible to defy even after decades.

“Heaven above and earth below, let ten thousand demons bow in homage.”

“……!”

“That is all there is. No further reason is needed.”

Hak Su met the eyes of the trembling man who had been his master, and continued.

His expression and voice were utterly unlike what they had been before.

“I used to tell you from time to time that meeting you by Qinghai Lake was the greatest luck of my life.”

He had meant it.

Cheongheoja was more deserving of being called a Daoist than anyone else. He had accepted his meeting with a boy wandering near Qinghai Lake as fate, never knowing the boy had made it look like chance.

“Thank you. I wasn’t especially gifted in martial arts, so even I didn’t know I’d reach a position like this.”

But Cheongheoja had never cared about status or talent.

Even if the Kunlun Sect hadn’t suffered devastating losses in the wake of the Great Faction War, he would have gladly accepted Hak Su as his Disciple.

Just as Hak Su had been raised to become a spy, Cheongheoja had always been that kind of person.

“It was all thanks to you, Cheongheoja.”

The instant a clear smile came to Hak Su’s lips—

“You dare, Hak Su—!”

Unable to watch any longer, Hak Eui roared in anger and shot forward.

And he wasn’t the only one charging at the traitor who had turned his back on his sect.

Whoooosh!

Their movement techniques were swift, their auras extraordinary.

The Kunlun Ten Guests, regarded as future Elders who would succeed the Kunlun Five Immortals and as indispensable pillars of the Kunlun Sect, drew their swords without a moment’s hesitation.

Slice!

A sword flash pierced the enemy’s torso, and hot blood gushed out.

Splatter. Thud, thud.

Blood sprayed across the wall.

Cheongheoja had stepped into his path. Over his master’s shoulder, Hak Eui caught sight of something unbelievable, and his eyes widened.

“What is this……!”

“I was getting tired of being called Hak Su.”

Hak Su watched the five corpses, their throats cut and hearts pierced, their breathing stopped. Then he—or rather, the Dark Heaven spy—slowly raised his head.

With the other shadows who had infiltrated the Kunlun Sect before him, or around the same time.

“Number Six. That’s my name.”

At that moment—

Crack.

The Kunlun Five Guests, now reduced to five—or, more precisely, the spies raised by Dark Heaven—pulled out the Temporary Strength Pills hidden in their robes and chewed them.

Sssssss!

Amid the enormous aura rising like a wildfire, Cheongheoja’s low voice rang out.

“I truly can’t leave you behind.”
```
