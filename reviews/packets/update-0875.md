<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0875.txt",
      "sha256": "d18c5f076b784a64a51ef4440f7352ef6957106ce9fca0aef08897ab8045eb32",
      "bytes": 13100
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ba0bcb79d28187b5eb08ca791f5a078fa84ad7a78d1c115758fc2f8faa645fac",
      "bytes": 959
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5fcfff91f26cce7ac511fc77cf79a7bc31a55cf3ddb32bd047b04b32a5d42b10",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "e71a0b8266808016c3efe58c9303ccc410bbdc52b3624a9ca444a313cb742417",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7d156ac456ffef9914890d50c787e2c4391cb31d269b947b8011f4b9a6979c40",
      "bytes": 1511
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "cbdac721eef619d3e6fbcf24cb37aa2a8070fe08ddbe39373feb12fc4a1c708f",
      "bytes": 554
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "132a4a0c39ea14902173a51d1a7a554bd323d1a03a7cc5bdacb1df91af986da3",
      "bytes": 952
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "49f03bde03d6b073c132fb8eea89af08fc3766de20d2b8ae4974acf3230bb6b0",
      "bytes": 258007
    }
  ],
  "estimated_tokens": 9972
}
-->

# Durable State Update — Chapter 875

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
1 and safe_through 875. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 875. Profile updates may replace only one
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
  "chapter": 875,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 875,
    "continuity_sources": [875],
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
    "Prince Shangshan has agreed to follow the Emperor’s will and remains in the imperial capital under the care of palace attendants led by So Gyo.",
    "Taekyung gave Shangshan the Myriad-Poison Ring for protection against poisoning; Shangshan promised to keep it hidden and return it.",
    "The Emperor has a concealed Supreme Peak assassin, No Shadow.",
    "The palace attendants assigned to Shangshan are First Rate martial artists who carry flexible swords."
  ],
  "continuity_sources": [
    874
  ],
  "open_questions": [
    "What does the Emperor intend for Shangshan, and what are the palace attendants’ true orders?",
    "Can Taekyung and Hong Jin devise a way to protect Shangshan?"
  ],
  "safe_through": 874,
  "temporary_decisions": [
    "Render 삼영 as “Third Shadow,” 일영 as “First Shadow,” 무영 as “No Shadow,” and 관내후 as “Marquis Within the Passes.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 일신     | **One God**         |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 사천     | **Sichuan**            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 은잠술 | **concealment technique** | Technique used by Hidden Shadow Pavilion agents to hide their presence. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 애향 | **Aehyang** | The City Lord’s favored concubine. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 874
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 871
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 874
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 848
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 874
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

## Korean source

```text
＃875화



이별의 시간은 짧았다.

얼마 지나지 않아 돌아온 궁인들은 상산왕을 둘러싼 채 미로처럼 복잡하고 넓은 건청궁의 복도 어딘가로 이끌었다.

‘당장으로서는 이게 최선이야.’

내심 중얼거린 나는 궁인들 사이로 언뜻언뜻 드러나는 어린 왕의 뒷모습을 지켜보았다.

과연 저 아이에게 남은 시간이 어느 정도일까.

나도 모르겠다.

그나마 이번 알현을 통해 얻은 것이 있다면, 황제가 아주 물불 안 가리는 미친놈은 아니라는 사실을 재확인한 것이었다.

‘이미 역모를 통해 많은 반발을 샀으니, 어린 막냇동생마저 같은 방식으로 쳐낼 수는 없겠지.’

모든 일에는 최소한의 명분이 필요하다.

황제가 만인 위에 군림하는 절대왕정의 시대에도 이는 예외가 아니었고, 이미 십여 년 전 황궁에 피바람을 불러일으킨 황제에게는 보이지 않는 위험 요소들이 있었다.

선황을 그리워하는 옛 신하들.

그리고 어린 왕을 동정하는 백성들.

이런 상황에서 상산왕이 부자연스러운 방법으로 죽음을 맞이한다면, 그것이야말로 또 다른 역모의 빌미가 될 것이다.

‘가장 자연스러운 방법은 독살뿐인데…… 쉽지는 않을 거다.’

만독지환(萬毒指環)의 효력이 어디까지인지는 정확히 밝혀진 바가 없다.

그러나 과거 적천강의 체내를 잠식했던 무형지독마저 흡수한 귀물(貴物)이니 제아무리 황제라 해도 그만한 독을 구하기는 쉽지 않을 것이다.

뒤늦게 만독지환의 존재를 눈치채고 강제로 빼앗지 않는 한은.

‘하지만 이것으로 최소한의 시간은 벌었다.’

상산왕에게 만독지환을 맡긴 것?

후회하지 않는다.

지금까지의 상황을 보았을 때 황제와 암천은 분명 어떤 방식으로든 깊게 연관되어 있었고, 이대로 놈들의 손아귀에 황실이 넘어간다면 끝장이다.

그렇기에 만독지환을 잃을 위험을 감수하고서라도 상산왕을 지켜야 했다.

그는 반(反) 황제파의 유일한 희망이자 강력한 구심점이었으니까.

그리고 내가 이곳에서 사귄 친구 중 하나니까.

‘물론 친구라고 하기에는 나이 차이가 좀 나는 편이지만.’

나는 쓴웃음을 지으며 상산왕 일행이 사라지는 것을 끝까지 지켜보았다.

그리고 무거운 마음으로 돌아선 그곳에는 아직 익숙해지지 않은, 하지만 한 번 본 것만으로도 꽤 오랫동안 기억에 남을 법한 어느 여인이 나를 조용히 응시하고 있었다.

“오래 기다렸습니까?”

여인, 소교(小嬌)가 차분한 목소리로 대답했다.

“아닙니다. 천녀는 황제 폐하의 명을 수행 중인 몸이니, 어찌 길고 짧음이 있을 수 있겠습니까.”

충성심 하나는 끝내주는군. 내심 중얼거린 나는 떨떠름하게 고개를 끄덕였다.

“그럼 갑시다.”

앞서 소교가 언급한 황제의 명이란 바로 나를 건청궁 밖으로 인도하는 것이었다.

물론 말이 인도지, 사실상 감시 겸 쫓아내는 것이었지만 그게 뭐 대수겠는가.

“제가 앞장서겠습니다. 따라오시길.”

하지만 나는 소교를 따라 몇 걸음 걷기도 전에 눈살을 찌푸렸다.

“잠깐만요. 이 방향이 아닌 것 같은데?”

“맞습니다. 기억하고 계시는군요.”

당연히 기억할 수밖에 없다. 최악의 상황이 닥쳤을 때를 대비해 퇴로를 봐 두는 건 필수였으니까.

나는 담담하게 대구하는 소교를 보며 황당한 얼굴로 되물었다.

“아니, 맞습니다 하고 넘어갈 게 아니라 방향이 틀렸다니까?”

“건청궁은 들어올 때와 나갈 때가 다릅니다.”

“예?”

“생문(生門)이 사문(死門)이 되고, 사문이 생문이 되기도 하지요. 진 공자께서는 강호를 주유하시는 무림인이시니, 그 의미를 이해하시리라 생각합니다만.”

“……!”

나는 입을 다물었다. 머릿속에서 섬광처럼 떠오른 한 단어가 뇌리를 스쳤다.

“설마…… 기관진식(機關陣式)?”

대답 대신 작게 고개를 끄덕인 소교는 앞서 걷기 시작했고, 그 모습을 멍하니 바라보던 나는 황급히 그 뒤를 따랐다.

앞서 들은 이야기에 대한 충격을 곱씹으면서.

‘빌어먹을. 아무리 황제여도 그렇지. 이건 처소가 아니라 철옹성 수준인데.’

황제를 제외하고 건청궁에 배치된 초절정 고수만 무려 셋.

그중 하나는 황제를 가장 가까운 거리에서 보호하는 은잠술의 달인이고, 그밖에도 궁 곳곳에 배치된 최정예 살수들의 숫자만 낮게 잡아도 일백을 넘어간다.

그런데 거기에 더해 기관진식까지?

‘확실히 정상은 아니야.’

황제의 신변 보호가 철저한 건 당연한 일이지만, 그래도 정도라는 것이 있는 법.

그러나 이 궁의 경계는 확실히 비이상적이었다.

마치 조금 전 만났던 황제의 모습을 고스란히 투영하는 것처럼.

‘아마도 그 역시 불안했던 거겠지. 수많은 적을 만들었으니.’

지난 역모로 사지가 찢기고 목이 달아난 이들의 숫자만 무려 삼만 명이라고 했다.

그중에는 피가 이어진 황족들은 물론, 대국의 기틀을 다진 개국공신도 있었고 청렴한 관리와 명망 높은 학자들도 있었다.

한데 그들 모두가 죽었다.

순리(順理)를 거스른 역모로. 단 한 사람의 명령에 의해.

그런 황제에게 적이 없다면 그것이야말로 어불성설이었다.

‘그렇다면 혹시?’

나는 소교의 뒤를 따라 걸으며 문득 떠올렸다. 만인지상의 황제이기 이전에 초절정 고수였던 그를.

드높은 일신의 무위와 젊은 나이에 비하면 십 년. 아니 족히 이십 년은 늙어 보이던 황제의 얼굴을.

‘그것 때문이었나.’

초절정은 타고난 재능 하나만으로는 결코 들어설 수 없는 지고의 영역.

그런데 남 부러울 것 없는 대륙의 지배자는 피땀 흘려 가며 무공을 익혔다.

자신이 무뢰배라 칭하는 강호의 무림인들처럼 쉴 새 없이 병장기를 휘두르고, 때로는 전신을 엄습하는 고통에 신음도 흘렸을 것이다.

하지만 그럼에도 밤마다 암살에 대한 두려움과 악몽을 완전히 떨쳐 내지는 못했던 모양이다.

‘어디까지나 짐작이지만, 충분히 가능성 있는 이야기지.’

나 역시 이 두 손으로 직접 숱한 목숨을 거둬들인 장본인이기에 그 감정을 어렴풋이 짐작할 수 있을 것 같았다.

정당한 살인은 없다. 명분 있는 살인만이 있을 뿐이다.

나로서는 어쩔 수 없는 싸움이었고, 반드시 쓰러트려야 하는 이들이었다며 스스로 자위하고는 했지만 그 사실은 변하지 않았다.

그렇게 죽어 간 수많은 망자(亡子)는 종종, 어쩌면 꽤 자주 찾아와 나를 괴롭혔고 나는 식은땀에 흠뻑 젖은 채 잠에서 깨어나곤 했다.

하물며 명분 없는 역모로 수만 명을 죽인 황제라면 어떻겠나.

‘매일 밤이 아주 불타오르겠구만.’

쓴웃음을 지은 나는 계속해서 걸음을 옮겼다. 줄곧 말없이 앞서가던 소교는 더욱 깊고, 알 수 없는 곳으로 나를 이끌었다.

슬슬 찝찝한 생각이 들 정도로.

“그, 뭐 좀 여쭤봐도?”

문득 걸음을 멈춘 소교가 돌아섬과 동시에 불쑥 입을 열었다.

“괜찮습니다.”

“예?”

“진 공자께서 우려하시는 불상사는 없을 테니, 안심하시고 따라오시라는 말씀입니다.”

잠시 침묵하던 나는 입맛을 다셨다.

“아주 그냥 정곡을 찌르시네. 혹시 독심술이라도 익혔어요?”

“아닙니다. 다만 어느 순간부터 호흡이 조금 흐트러지시더군요.”

“아. 티 났구나. 눈치 빠르시네.”

“저 역시 무공을 익혔으니까요. 무인에게 호흡을 조절하는 것만큼 중요한 것도 없겠지요.”

맞는 말이다. 경지가 높은 고수들일수록 한 호흡도 되지 않는 짧은 순간 만에 승부가 결정 나는 경우가 허다하니까.

하지만 그런 것과는 별개로 소교의 말투는 사뭇 도전적이기까지 했고, 나는 그 말을 끝으로 돌아선 그녀의 뒷모습을 보며 생각했다.

‘그러니까 지금, 나한테 시비를 건 건가.’

아마도 그런 것 같다. 아니, 거의 확실하다.

기껏해야 일류 정도의 무위를 갖춘 소교가 나를 가르치려는 듯한 모습에 어이가 없었지만, 나는 소리 없이 실소를 흘리는 것으로 마무리 지었다.

따지고 보면 소교는 황제의 충복 중 한 사람이고, 이곳은 적군의 진영이다. 이런 상황에서 뭘 기대하겠나.

‘습격이라도 안 하는 걸 다행으로 여겨야지.’

말해 봤자 입만 아프다. 절레절레 고개를 흔든 내가 잠시 멈췄던 발걸음을 재차 떼려던 그 순간이었다.

쨍그랑.

“……!”

희미하지만 똑똑히 들었다. 마치 교차로처럼 이어진 여러 개의 길 중, 컴컴한 복도 어딘가에서 들려오는 그 소음을.

그리고 짜증 가득한 누군가의 목소리를.

- 이 미천한 것들이 감히 누구에게……!

“따라오시지요.”

신속한 움직임으로 다가온 소교가 내 앞을 가로막았지만, 나는 개의치 않고 공력을 일으켜 오감(五感)을 더욱 곤두세웠다.

‘여자. 분명 여자 목소리였어.’

뭔가 있다. 아직 내가 모르는 무언가가.

그리고 이 빌어먹을 황궁에서 목표한 바를 이루기 위해서는, 조금이라도 더 많은 단서를 알아내야 한다.

저벅.

“진 공자!”

어둠에 잠긴 그곳을 향해 걸음을 떼자마자 귓가를 파고든 나직한 외침.

명백한 경고의 의미를 띤, 서늘한 눈빛으로 나를 노려보는 소교의 모습에, 나는 더욱더 큰 확신을 얻었다.

그녀가 이토록 강경하게 막아선다는 것은 결코 외부인에게 보여서는 안 되는 무언가가 있다는 뜻.

그러나 이곳은 황제의 거처다. 나는 아무것도 모르는 척 능청맞게 웃으며 입을 열었다.

“아니, 무슨 일이 생긴 것 같길래. 잠깐 가 봐야 하지 않을까요?”

“따라오시라고, 말씀드렸습니다.”

“거참. 황궁 인심 한번 퍽퍽하네. 근데 방금 누구예요? 대충 듣기로는 여자 목소리 같던데.”

“그쯤 하시지요. 경고했습니다.”

“경고 한 번이면 아직까지는 괜찮구만, 뭘. 그런데 진짜 누구예요? 내가 너무 궁금해서 오늘 밤에 잠 못 잘까 봐 그래.”

“영원히 잠드시는 것보다야 낫겠지요.”

굳은 얼굴로 대답한 소교가 불현듯 외쳤다.

“출(黜)!”

쉬쉬쉬쉭!

그야말로 한순간이었다.

높은 천장에서 뚝 떨어져 내린 십여 개의 날붙이가 내 전신을 에워쌌다.

어둠을 닮은 새카만 복면과 그 위로 드러난 살인자의 눈동자.

순식간에 건청궁의 살수들에게 둘러싸인 나는 무겁게 가라앉은 목소리로 입을 열었다.

“불상사는 없을 거라더니?”

소교가 허리춤에 찬 연검에 손을 가져가며 대답했다.

“없을 겁니다. 이대로 얌전히 돌아간다면.”

“그냥 이상한 소리가 나길래 본 것뿐인데. 뭐가 그렇게 예민하지?”

“폐하의 뜻에 불응(不應)하겠다는 뜻으로 받아들이면 될까요?”

“그건 좀 곤란한데.”

“그럼 돌아서서 천녀를 따라오시지요. 아주 조용히.”

“싫다면?”

스아아아.

나는 소리 없이 공력을 끌어올렸다.

그리고 사방을 짓누르는 내 기세 탓인지, 혹은 곧 다가올 혈전(血戰)을 예상하는지 빙하처럼 차갑게 굳은 소교와 살수들의 얼굴을 차례대로 훑어본 뒤, 조용히 두 팔을 들어 올렸다.

“좋아. 항복.”

“……!”

“길 안내나 마저 해 줘요. 빨리 돌아가서 밥 먹어야 하니까.”

나는 작게 한숨을 내쉰 소교가 살수들을 물리는 것을 바라보며 내심 웃었다.

여기서 더 큰 위험을 초래할 필요는 없었다.

비록 금세 가로막히긴 했지만, 이미 소기의 목적을 달성한 후였으니까.

나는 똑똑히 들었다.

어느 여인이 내지른 그 앙칼진 외침을.

그리고 그건 몇 달 전, 사천성주가 기거하는 성주부에서 들었던 누군가의 목소리를 떠올리게 만들었다.

너무나도 간드러지고 교태가 넘쳐흘러 기억할 수밖에 없던 그 목소리를.

‘그 여자 이름이…….’

그래. 애향(愛香).

사천성주가 황제에게 빼앗긴, 사랑해 마지않았던 그의 애첩.
```

## Final English reading copy

```markdown
# Chapter 875

The farewell was brief.

Before long, the palace attendants returned and led Prince Shangshan away, surrounding him as they guided him through some part of Qianqing Palace’s vast, maze-like corridors.

*For now, this is the best I can do.*

I thought to myself as I watched the young prince’s back, glimpsed now and then between the attendants.

How much time did that child have left?

I didn’t know.

If I’d gained anything from this audience, it was the confirmation that the Emperor wasn’t a complete madman who’d stop at nothing.

*He’s already made plenty of enemies through his coup. He can’t just get rid of his youngest younger brother the same way.*

Everything needs at least some pretext.

Even in an era of absolute monarchy, with the Emperor ruling over all, that was no exception. And the Emperor, who’d brought a bloody storm to the imperial palace more than a decade ago, had dangers lurking out of sight.

Old retainers who longed for the late Emperor.

And the people, who pitied the young prince.

If Prince Shangshan died under unnatural circumstances in this situation, it would provide the perfect excuse for another rebellion.

*The most natural method would be poisoning…but that won’t be easy.*

No one knew exactly how far the Myriad-Poison Ring’s power extended.

But it was a divine treasure that had even absorbed the Formless Ultimate Poison that once spread through Jeok Cheongang’s body. Even the Emperor wouldn’t have an easy time obtaining poison of that caliber.

Unless he eventually discovered the Myriad-Poison Ring and took it by force.

*But this has bought us at least a little time.*

Giving the Myriad-Poison Ring to Prince Shangshan?

I didn’t regret it.

From everything I’d seen so far, the Emperor and Dark Heaven were definitely connected somehow, and if the imperial family fell into their hands, it was all over.

That was why I had to protect Prince Shangshan, even if it meant risking the ring.

He was the anti-Emperor faction’s only hope, and the powerful figure who could rally them.

And he was one of the friends I’d made here.

*Though there’s a bit of an age gap for me to call him a friend.*

I smiled bitterly and watched until Prince Shangshan and his party disappeared from sight.

When I turned away, heavy-hearted, a woman was quietly watching me. I still wasn’t used to seeing her, but one look was enough to make her face linger in my memory for quite some time.

“Have you been waiting long?”

The woman, So Gyo, replied in a calm voice.

“No. This humble woman is carrying out His Majesty the Emperor’s orders. How could I measure the wait as long or short?”

*That’s some serious loyalty,* I murmured to myself and nodded awkwardly.

“Then let’s go.”

The Emperor’s order So Gyo had mentioned was to escort me out of Qianqing Palace.

Of course, “escort” was just a polite way of saying she was keeping an eye on me and kicking me out, but what did it matter?

“I’ll lead the way. Please follow me.”

But I’d barely taken a few steps after So Gyo when I frowned.

“Wait. I don’t think this is the right way.”

“It is. You remember.”

Of course I remembered. In case the worst happened, it was essential to scout an escape route.

I stared at So Gyo, who’d answered so matter-of-factly, and asked incredulously,

“Don’t just say it is. I’m telling you we’re going the wrong way.”

“Qianqing Palace has different paths in and out.”

“What?”

“The life gate can become the death gate, and the death gate can become the life gate. Since you’re a martial artist who travels the martial world, Young Master Jin, I thought you would understand what that means.”

“……!”

I fell silent. A word flashed through my mind like a bolt of lightning.

“Don’t tell me…mechanisms and formations?”

So Gyo gave a slight nod instead of answering, then started walking ahead. I stared after her blankly before hurrying to follow.

I was still absorbing the shock of what I’d just heard.

*Damn it. Even for an Emperor, this is ridiculous. This isn’t a residence; it’s an impregnable fortress.*

There were no fewer than three Supreme Peak masters stationed in Qianqing Palace, not counting the Emperor.

One of them was a master of the concealment technique, guarding the Emperor from the closest possible distance. And even if I lowballed it, there were more than a hundred elite assassins stationed throughout the palace.

And on top of that, mechanisms and formations?

*He’s definitely not normal.*

It was only natural for the Emperor’s security to be thorough, but there had to be limits.

The defenses of this palace were decidedly abnormal.

As though they were a perfect reflection of the Emperor I’d met just moments ago.

*He must have been afraid, too. He’s made so many enemies.*

They said as many as thirty thousand people had been torn limb from limb and beheaded in the last coup.

Among them were members of the imperial family, bound to him by blood; founding heroes who had laid the foundations of the Great Nation; upright officials; and renowned scholars.

Every one of them had died.

In a rebellion against the natural order. At the command of a single man.

It would have been absurd if an Emperor like that had no enemies.

*Then could it be…?*

I followed So Gyo and found myself thinking of the Emperor—not as the ruler above all, but as a Supreme Peak master.

His formidable martial prowess. His face, which looked ten years older than it should have—no, a good twenty years older, considering how young he was.

*Was that why?*

Supreme Peak was a lofty realm no one could enter through innate talent alone.

And yet the ruler of the continent, who had everything anyone could want, had sweated blood to learn martial arts.

He must have swung weapons without pause, like the martial artists of the martial world he called ruffians. At times, he must have groaned under pain that racked his whole body.

But even then, it seemed he couldn’t completely shake off his fear of assassination and the nightmares that came with it.

*It’s only a guess, but it’s certainly possible.*

I’d taken countless lives with these very hands, so I thought I could vaguely understand how he felt.

There was no such thing as a justifiable killing. Only a killing with a pretext.

I’d comforted myself by saying I’d had no choice, that they were people I had to defeat. But that didn’t change the truth.

The countless dead would come to torment me from time to time—maybe even quite often—and I’d wake up drenched in cold sweat.

What about an Emperor who’d killed tens of thousands through a rebellion with no pretext at all?

*His nights must be a real inferno.*

I smiled bitterly and kept walking. So Gyo had led me on in silence the whole time, deeper and deeper into places I couldn’t make sense of.

It was starting to feel unsettling.

“Um, can I ask you something?”

So Gyo stopped and turned around. At the same time, she spoke without hesitation.

“Of course.”

“What?”

“I’m saying you can follow me without worry. Nothing unfortunate will happen, Young Master Jin.”

I fell silent for a moment, then clicked my tongue.

“Wow, right to the heart. Have you learned mind reading or something?”

“No. I simply noticed your breathing become slightly uneven at some point.”

“Oh. I gave it away, huh? You’re perceptive.”

“I’ve learned martial arts as well. Controlling one’s breathing is one of the most important things for a martial artist.”

She was right. The higher a master’s realm, the more often a fight was decided in a split second—not even a full breath.

But regardless, So Gyo’s manner had been almost provocative. Watching her turn away after saying that, I thought,

*So she’s picking a fight with me?*

Probably. No, almost certainly.

It was absurd to have So Gyo, who had no more than First Rate martial prowess, act as if she were teaching me a lesson. But I let it end with a silent chuckle.

Come to think of it, So Gyo was one of the Emperor’s loyal servants, and this was enemy territory. What else could I expect?

*I should be grateful she’s not attacking me.*

There was no point talking about it. I shook my head and was just about to start walking again when—

Crash.

“……!”

It was faint, but I heard it clearly. From somewhere along the dark corridor, among several paths branching off like a crossroads.

And then a voice, full of irritation.

—How dare you, you lowly wretches…!

“Please follow me.”

So Gyo hurried over and stood in my way, but I didn’t care. I raised my internal energy and sharpened my senses.

*A woman. That was definitely a woman’s voice.*

Something was going on. Something I didn’t know about yet.

And if I wanted to accomplish what I’d come to do in this damn imperial palace, I needed to uncover as many clues as I could.

Step.

“Young Master Jin!”

A low shout cut into my ears as soon as I stepped toward the darkness.

So Gyo glared at me with a cold look that was unmistakably a warning, and I became even more certain.

If she was blocking me this firmly, there had to be something here that outsiders absolutely weren’t allowed to see.

But this was the Emperor’s residence. I put on an easy, innocent smile and spoke as if I knew nothing.

“It sounded like something happened. Shouldn’t we go take a look?”

“I told you to follow me.”

“Come on. The imperial palace is a pretty unfriendly place. Who was that just now? From what I could tell, it sounded like a woman.”

“That’s enough. I’ve warned you.”

“One warning means I’m still fine for now, right? But seriously, who was it? I’m so curious I might not be able to sleep tonight.”

“Better that than sleeping forever.”

So Gyo answered with a stern face, then suddenly cried out,

“Out!”

Shhk-shhk-shhk!

It happened in an instant.

A dozen or so blades dropped from the high ceiling and surrounded me.

Black masks as dark as the shadows, with the eyes of killers visible above them.

Surrounded in a flash by the assassins of Qianqing Palace, I spoke in a low, heavy voice.

“You said nothing unfortunate would happen.”

So Gyo put a hand on the flexible sword at her waist. “It won’t. As long as you turn around and leave quietly.”

“I just heard a strange noise and came to take a look. Why are you so touchy?”

“Should I take that as defying His Majesty’s will?”

“That would be a problem.”

“Then turn around and follow me. Quietly.”

“And if I don’t?”

Ssshhh.

I silently drew up my internal energy.

Then, perhaps because my aura pressed down on them from every direction, or perhaps because they anticipated the bloodbath about to come, So Gyo and the assassins’ faces hardened like ice. I looked over them one by one, then quietly raised both hands.

“Fine. I surrender.”

“……!”

“Just finish showing me the way. I need to get back and eat.”

So Gyo let out a small sigh and ordered the assassins to withdraw. I watched them go and smiled to myself.

There was no need to stir up even more trouble here.

Though I’d been stopped in no time, I’d already accomplished what I’d set out to do.

I’d heard it clearly.

That sharp cry from a woman.

And it reminded me of someone’s voice I’d heard a few months ago at the residence of the City Lord of Sichuan Province.

It had been so sweet and dripping with seduction that I couldn’t have forgotten it.

*That woman’s name was…*

Right. Aehyang.

The beloved concubine the City Lord of Sichuan Province had lost to the Emperor.
```
