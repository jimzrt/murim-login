<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0861.txt",
      "sha256": "83bb251cee6cf46d6d6c6f387676fcbcb6723a35f99f6960eeaf596c5de217dd",
      "bytes": 12890
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0a73536d543b5c5082254ec1c611647975b8a1bcc5083099d2324decd5d5288d",
      "bytes": 2186
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "98ebb49424bfeaf4c25ba492300847dfabb4273b6af4462cc1c0c169a19d9167",
      "bytes": 229077
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "de239b96deaad445e1769581e89702d28512bd950895e39d69e2ea102487e9c3",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "633c7e2893b3bf6bb5e14351abcd5b890c8bf30afd68477dc4267caf8718dbe6",
      "bytes": 797
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "0ced88af408796e927d437fd157f3b8a4e1f81083db9f55a66e4dea3b44eff8d",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "a41512fa0c85bb16724e73f1d9abc220436b66ae9efbbdadc182f448d6587811",
      "bytes": 634
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "edee8aefb59a8db2eb2294f586b3eb75171ddd54981ef524079642d04fc3cc46",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "4ba1f3acd0d11205edcf6f1bed3d75777e0eb167890ab72efd42b582a7bb5962",
      "bytes": 883
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3fa73ffb475241a2f493481b1463b0fa3b2206da91bb48af9a0c8fb1c795a717",
      "bytes": 254400
    }
  ],
  "estimated_tokens": 10092
}
-->

# Durable State Update — Chapter 861

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
1 and safe_through 861. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 861. Profile updates may replace only one
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
  "chapter": 861,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 861,
    "continuity_sources": [861],
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
    "The Divine Physician secured the Blood Soul Gu from the deceased City Lord of Sichuan Province; it weakens hosts, causes madness, and eventually kills them.",
    "Jin suspects Dark Heaven killed the City Lord as part of a scheme against the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling to the imperial capital with Hong Jin, the Embroidered Uniform Guard, and Jin’s party; he is expected to meet the Emperor today.",
    "Hong Jin chose Jin Taekyung to protect Zhu Bao because he trusts him to defend the prince against any threat.",
    "Jeong Hogun commands the Embroidered Uniform Guard escorting Zhu Bao discreetly.",
    "The late Emperor entrusted Hong Jin with Zhu Bao’s care, and Zhu Bao trusts his elder brother.",
    "Zhu Bao gave Hyuk Mujin the joking title “Tenfold Man,” which Mujin inscribed on a bronze token.",
    "Jiangsu has no Murim sects: the founding emperor destroyed the Maoshan Sect and other sects that refused to relocate."
  ],
  "continuity_sources": [
    860
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord, and is it targeting the Emperor or imperial family?",
    "What does the Emperor intend for Prince Shangshan, and what prompted the imperial decree against Hong Jin?",
    "What does Zhu Bao’s secret letter to Jin contain?",
    "What do the Commander-in-Chief or Emperor know about the party, and who predicted that uninvited guests would interfere?",
    "Who trained the Embroidered Uniform Guard’s highly skilled martial artists, and for what purpose?"
  ],
  "safe_through": 860,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu”; 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard”; 금위군 as “Imperial Guards.”",
    "Render 강소 as “Jiangsu”; 절강성 as “Zhejiang Province.”",
    "Render 정호군 as “Jeong Hogun”; 정 천호 as “Commander Jeong.”",
    "Render 십상남자 as “Tenfold Man,” 茅山派 as “Maoshan Sect,” 太祖 as “Taizu,” 南京 as “Nanjing,” and 소주 as “Suzhou.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 산서     | **Shanxi**             |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 적통 | **orthodox lineage** | The legitimate succession of the Fire Gate Clan's tradition. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 남경 | **Nanjing** | Former imperial capital in Jiangsu Province. |
| 소주 | **Suzhou** | The party’s destination in Jiangsu Province. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 859
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 860
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch who served the late Emperor and has been entrusted with Prince Shangshan’s protection since the prince’s infancy.
- **Personality:** Composed and socially deft, Hong Jin is considerate toward those beneath him and dislikes excessive deference, which recalls his impoverished past.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung as the person best able to keep the prince safe.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 860
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 860
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Commands the Embroidered Uniform Guard force confronting Jin Taekyung and serves the Emperor's command.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 860
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 860
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, compassionate, and eager to emulate Jin Taekyung; he takes responsibility for his loyal subjects’ hardship, though his trust in his elder brother shows his youth.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃861화



오늘 안에 황도에 도착할 것이라는 정호군의 말은 거짓이 아니었다.

행렬은 강소성의 성도이자 옛 황도였던 남경(南京)을 지나 마침내 소주(蘇州)에 다다랐고, 절강성으로 넘어가는 경계에서 일단의 병력과 맞닥트렸다.

“기다리고 있었습니다, 천호.”

전신을 빈틈없이 감싼 철갑과 투구 사이로 빛나는 안광.

한 사람, 한 사람이 무거운 기세를 흩뿌리는 그들의 머릿수는 자그마치 일천여 명에 육박했고, 바람을 받아 펄럭이는 황금색 깃발에는 황실을 상징하는 용이 마치 살아 있는 것처럼 꿈틀거리고 있었다.

금의위(錦衣衛).

이 세상에서 오직 한 존재, 천자의 명령에 따라 움직이는 충견들은 자신들의 상관인 정호군에게 군례를 올렸고 고귀한 황실의 핏줄을 이어받은 어린 왕과 대면했다.

“상산왕 전하시다. 예를 갖춰라.”

“천세(千歲)! 천세! 천천세!”

그리고 말에서 내리지도 않은 채 한목소리로 부르짖는 금의위들의 모습을 보며, 홍진은 문득 생각했다.

과연 이 수많은 이 중 몇 사람이나 저 외침에 진심을 실었을까.

아니, 한 사람이라도 있기는 한 것일까.

이미 그 의문에 대한 답을 알고 있는 홍진은 쓴웃음을 삼켰다.

‘저들이나 나나, 결국 한낱 축생(畜生)일 뿐. 중요한 것은 그 축생을 기르는 주인의 뜻이겠지.’

맞다. 천자는 지고지순하며 모두의 생사를 결정할 수 있는 만인지상(萬人之上)의 존재다.

그런 천자의 뜻을 막을 수 있는 것은 아무것도 없었다.

십여 년 전 그 끔찍한 숙청 속에서도 아슬아슬하게 스쳐 지나갔던, 어린 왕을 향한 칼날도.

그리고 다시 돌아온 천자의 칼날을 향해 나아가고 있는 이 마차도.

“속도를 올려라. 황도가 코앞이다.”

서서히 기울기 시작하는 태양과는 반대로, 마차는 바람처럼 내달렸다.

수천 리 동안 해진 무복으로 정체를 감추고 있던 정호군과 휘하의 금의위들은 그 이름에 어울리는 눈부신 금의(錦衣)와 갑옷을 걸쳤고, 황실의 깃발을 높게 세운 채 물결처럼 나아갔다.

마치 적장을 생포하여 귀환한 승리자처럼.

“길을 비켜라!”

일천의 금의위를 막아설 수 있는 것은 아무것도 없었다.

백성들은 두려움과 경외가 뒤섞인 눈빛으로 엎드렸고, 어린 왕을 앞세운 행렬은 위풍당당하게 활짝 열린 관문을 지나쳤다.

불과 반나절. 오직 그들만을 위해 비워진 대로(大路)와 물길을 따라 이동한 끝에, 마침내 홍진은 볼 수 있었다.

살아서는 두 번 다시 볼 수 없으리라 생각했던. 동시에 자신이 모시는 어린 왕을 위해서라도 절대 돌아오지 않으리라 다짐했던 거대한 성벽을.

‘황도(皇都)……!’

홍진은 새어 나오려는 탄식을 애써 억눌렀다.

보이지 않지만 보인다. 들을 수 없지만 들린다.

저 높은 성벽 뒤에 웅크린 용의 거처가. 단 하나의 옥좌를 둘러싸고 끊임없이 울려 퍼지던 무수한 비명이.

그것은 홍진의 뇌리에 깊숙이 틀어박힌 끔찍한 과거의 편린이었고, 한 사람을 대륙의 주인으로 거듭나게 한 역사이기도 했다.



‘살려 주마, 이번만큼은.’



문득 귓가에 울려 퍼지는 누군가의 냉엄한 목소리에, 홍진은 자신도 모르게 이를 악물었다.

‘폐하의 뜻대로 되진 않을 겁니다. 이번만큼은.’

저 멀리 서쪽으로부터 시작된 노을이, 황도의 성벽을 물들이고 있었다.



* * *



처음 본 항주(杭州)는 좋은 도시였다.

운하를 타고 절강성 곳곳으로 운반되는 풍부한 물자와 빼어난 풍광(風光).

오는 길에 지나친 드넓은 평야에는 온갖 곡식들이 황금빛 물결처럼 굽이치고 있었고, 사람들의 입가에는 웃음이 떠나지 않았다.

‘천하에서 가장 아름다운 도시라더니.’

언젠가 스치듯이 들었던 그 말은 틀림없는 사실이었다.

바로 그렇기에 남경이라는 유구한 역사를 간직한 대도시를 버리고 항주로 천도(遷都)을 감행했을지도 모르겠다.

다만 한 가지 문제는 이 아름다운 도시가, 내가 생각했던 것 이상으로 흉흉하다는 점이었다.

철컥. 철컥.

날붙이가 토해 내는 서늘한 마찰음.

어느 방향으로 고개를 돌려도 군사들이 보인다. 그것도 지금껏 내가 알던 어설픈 잡졸들이 아니라, 철저한 무장을 갖춘 정예군이.

오죽하면 그 속 편한 혁무진마저 웃음기를 싹 지운 채 이렇게 말할 정도였다.

“조장님. 이건 좀…… 심한데요?”

평소였으면 습관처럼 한마디 쏘아붙이기라도 했을 텐데, 그런 나조차도 이번만큼은 십분 공감할 수밖에 없었다.

‘뭐 이렇게 많아.’

그냥 많은 게 아니다. 정말 더럽게 많다.

어느 정도냐 하면 절강성 특산품이 용정차(龍井茶)가 아니라 금위군이 아닐까 의심이 갈 정도다.

“평소에도 이렇게 경계가 삼엄합니까?”

항주에 접어들면서 웃음기를 잃은 것은 혁무진만이 아니었다.

내 물음을 들은 홍진은 낯설게 느껴질 만큼 딱딱한 음성으로 대답했다.

“황도인 만큼 평상시 경계도 철저한 편이에요. 물론 이 정도까지는 아니었지만.”

“그렇다면…….”

“모종의 명령을 받은 게 틀림없어요. 그리고 아마도…… 우리와 어떻게든 연관이 있을 테고.”

홍진이 붉게 칠한 입술을 핥으며 중얼거렸다.

“이미 짐작하고는 있었지만, 생각보다 환영 인사가 과하네요.”

나는 문득 십만 대군이 창칼을 들이대는 장면을 떠올렸지만, 이내 고개를 저었다.

‘그럴 가능성은 희박하지.’

이렇게 쉽게 죽일 거였다면 상산왕 주표는 산서성을 벗어나지도 못했을 것이다.

천자가 휘하의 금의위들을 보내 자신의 어린 동생을 데려온 이유가 정확히 무엇인지는 모르나, 적어도 대의명분(大義名分)에 어긋나지 않는 선에서 상산왕을 처리할 것은 분명했다.

황제란 그런 자리니까.

‘더군다나 이미 대외적으로 알려진 이미지도 좋지 않고.’

민심(民心)은 곧 천심(天心)이라는 말이 괜히 나왔을까.

대국에 앞서 대륙을 제패했던 초원의 유목 민족 역시 무너진 민심과 함께 몰락했다.

백성을 다스리는 것은 황제지만, 백성이 없다면 황제도 존재하지 못한다.

그런 의미에서 작금의 천자를 향한 세인들의 시선은 상당히 부정적인 편이었다.

‘유능하지만 잔혹한 황제.’

무림에서도 종종 들었고, 오는 길에서 홍진과 은밀히 대화를 나누며 더욱 자세히 알게 된 사실이었다.

젊어서부터 여러 반란과 이민족의 난을 진압하며 큰 군공(軍功)을 쌓았고, 맡은 지역을 다스림에 있어서 한 치의 빈틈도 없다는 평을 들었던 이가 바로 작금의 황제였다는 것을.

홍진은 만약 그가 선황의 첫 번째 아들로 태어났다면, 혹은 맏형이었던 황태자가 조금이라도 부족한 인물이었다면 자연스럽게 다음 황위(皇位)를 물려받았을 것이라고 했다.

‘하지만 현실은 달랐지.’

황제가 되기 전의 그는 후계 구도와는 상당한 거리가 있었다.

위로는 자그마치 세 명의 형이 있었고, 장자 계승의 원칙에 따라 자연스럽게 황태자로 우뚝 선 맏형은 그에 못지않게, 아니 보는 시선에 따라서는 그 이상으로 출중한 인물이었다.

신분의 고하에 상관없이 오직 인의(人意)로 사람을 대하며, 능히 대국을 이끌기에 충분한 자질을 보여 준 훌륭한 재목.

홍진은 당시의 황태자를 이렇게 평했다.

‘준비된 천자.’

기나긴 전란은 이미 오래전에 끝났다.

천하 각지에 흩뿌려져 있던 불온한 반란의 씨앗도, 대국을 호시탐탐 넘보던 이민족들도 모조리 뿌리 뽑았다.

기틀을 마련한 대국에게 필요한 것은 정복이 아닌 안정이었고, 조금의 흠결도 없는 완벽한 적통(嫡統)과 자질을 갖춘 황태자는 그야말로 모든 면에서 준비된 후계자였다.

이미 후계 구도에서 멀찍이 밀려난, 황실의 사 황자가 그림자 속에서 검을 뽑아 들기 전까지는.

다그닥.

유난히도 또렷하게 울려 퍼진 말발굽 소리와 함께, 상념에서 깨어난 나는 주위를 둘러보았다.

‘여긴.’

의문에 대한 답은 금세 나왔다.

어느새 마차는 멈췄고, 사방을 빽빽하게 감싸던 금의위의 사이로는 지금껏 무림에서 단 한 번도 보지 못했던 거대한 건축물들이 늘어서 있었으니까.

마치 현대의 마천루(摩天樓)를 떠올릴 만큼 높고, 그와 비교할 수도 없을 만큼 고풍스럽고 화려하게 치장된 건물들은 오직 한 장소를 의미하고 있었다.

‘황궁(皇宮).’

용의 거처이자, 천하라는 거대한 톱니바퀴를 움직이는 중심지.

창 틈새로 보는 것만으로도 압도되는 듯한 황궁의 입구를 말없이 바라보던 내게, 홍진이 한껏 숨죽인 목소리로 작게 속삭였다.

“진 공자. 내가 지금까지는 잘 참고 있었는데…… 이제는 말해 줄 때가 된 것 같지 않아요?”

그 말을 듣는 순간, 나는 홍진이 무엇을 물어보려 하는지 알아차렸다.

나와 혁무진을 제외한 다른 이들.

지금 홍진은 아직도 모습을 드러내지 않은 또 다른 조력자들의 위치를 궁금해하고 있었고, 내 대답은 정해져 있었다.

- 걱정 마세요. 머지않아 곧 알게 될 테니까.

기대에 어긋난 대답이었는지 홍진은 살짝 미간을 찌푸렸지만, 그렇다고 불만을 표하지는 않았다.

그들을 돕기 위해 그 먼 거리를 쉬지 않고 달려온 나다.

지금 같은 상황에서 서로를 향한 신뢰마저도 없다면 불안과 위험은 더욱더 커질 수밖에 없다.

그리고 그런 의미에서, 나 역시 묻지 않을 수 없었다.

- 어떻게 그 많은 것들을 알고 있는 겁니까?

그것은 제법 오래전부터 이어져 왔던 의문이었다.

상산왕 주표가 제아무리 이름뿐인 왕이라고는 하나, 황위를 둘러싼 끔찍한 암투 속에서 살아남은 유일한 직계 황족이자 번왕(藩王).

그런 상산왕의 심복인 홍진 역시 평범한 환관일 리 없다는 생각은 전부터 품고 있었지만, 그가 알고 있는 정보와 어디에서나 두려움의 대상인 금의위를 아무렇지 않게 대하는 태도는 생각했던 것 이상이었다.

이런 식으로라도 직접 물어볼 수밖에 없을 만큼.

- 저 역시 목숨을 건 이상, 이 물음에 대한 답은 반드시 들어야겠습니다. 지금 당장.

덜컥.

단호함이 묻어나오는 전음에 말없이 나를 응시하던 홍진이 돌연 마차의 문을 열어젖혔다.

그리고 황궁으로 이어지는 아득한 높이의 계단을 내려오는 일단의 무리를 바라보며 입을 열었다.

“진 공자. 내가 왜 환관이 되기로 결심했는지, 말해 준 적이 있었죠?”

나는 고개를 끄덕였다.

산서성에서 홍진과 처음 인연을 맺었을 무렵, 그는 스쳐 가듯 자신의 과거를 말해 준 적이 있었다.

“가난이 싫었고, 가족을 살리고 싶었어요. 하지만 선택할 방법이 그리 많지는 않더라고. 아니, 당시로써는 유일했지.”

홍진은 천천히 말을 이었다.

원하는 바를 얻기 위해서는, 또 다른 무언가를 희생해야 한다고.

굶주림을 이기지 못한 가난뱅이 소년은 그렇게 환관이 되었고, 스스로 새로운 이름을 지었다.

“홍진(洪進). 큰물로 나아가고 싶었어요. 악취 풍기는 시궁창을 벗어나서, 넓고 맑은 바다로.”

그 바람이 현실이 되기까지는, 그리 오랜 시간이 필요하지 않았다.

가난을 벗어난 젊은 환관은 전에 없던 야망을 품게 되었고, 그만한 능력을 갖추었으니까.

그리고 언제나 철두철미하고 냉철한 그의 모습은, 곧 선황의 눈에 띄게 되었다.

“어느 날 선황께서 나를 불러 말씀하셨지. 내 능력을 중히 쓰일 만한 곳이 있다고.”

홍진이 또렷한 음성으로 말을 이었다.

“진 공자. 혹시 동창(東廠)이라고 들어 봤어요?”

“……!”
```

## Final English reading copy

```markdown
# Chapter 861

Jeong Hogun hadn’t been lying when he said they would reach the imperial capital today.

The procession passed through Nanjing, the capital of Jiangsu Province and the former imperial capital, and finally arrived in Suzhou. At the border crossing into Zhejiang Province, they came face-to-face with a force of soldiers.

“We’ve been waiting for you, Commander.”

Gleaming eyes shone between their full suits of iron armor and helmets.

Each man radiated a heavy aura. There were nearly a thousand of them, and on the golden banners fluttering in the wind, the dragon that symbolized the imperial family writhed as if alive.

The Embroidered Uniform Guard.

The Emperor’s loyal hounds—who answered to only one person in this world, the Son of Heaven—saluted their superior, Jeong Hogun, then faced the young prince who carried the noble blood of the imperial family.

“His Highness Prince Shangshan is here. Pay your respects.”

“Long live the prince! Long live the prince! Long, long live the prince!”

Watching the Embroidered Uniform Guard shout in unison without even dismounting, Hong Jin found himself wondering:

How many of them truly meant those words?

No—did even one?

Hong Jin already knew the answer. He swallowed a bitter smile.

*They and I are nothing more than beasts. What matters is the will of the master who raises those beasts.*

That was right. The Son of Heaven was supreme, above all others, and could decide who lived and died.

Nothing could stand in the way of his will.

Not even the blade that had narrowly missed the young prince amid that terrible purge more than a decade ago.

Nor could anything stop this carriage as it headed toward the Son of Heaven’s returning blade.

“Pick up the pace. The imperial capital is just ahead.”

As the sun began to sink, the carriage raced like the wind.

After hiding their identities in worn martial artists’ clothes for thousands of li, Jeong Hogun and the Embroidered Uniform Guard under his command now wore dazzling brocade and armor befitting their name. They advanced like a wave, imperial banners held high.

Like victors returning with an enemy general in chains.

“Make way!”

Nothing could stand in the way of a thousand members of the Embroidered Uniform Guard.

The commoners bowed low, their eyes mixed with fear and awe, as the procession led by the young prince passed through the gates, flung wide open before them.

In just half a day, they had traveled along the great roads and waterways cleared exclusively for them. At last, Hong Jin saw it.

A massive wall he’d thought he would never see again in his lifetime. A wall he had sworn never to return to, if only for the sake of the young prince he served.

*The imperial capital…!*

Hong Jin forced down the sigh that nearly escaped him.

He could see what lay out of sight. He could hear what no longer made a sound.

The dragon’s lair crouched behind those towering walls. The countless screams that had echoed endlessly around a single throne.

They were horrific fragments of the past, lodged deep in Hong Jin’s mind—and the history that had made one man the ruler of the continent.

*“I’ll spare you. Just this once.”*

At the sudden memory of someone’s cold voice ringing in his ears, Hong Jin clenched his teeth without realizing it.

*It won’t go as Your Majesty wishes. Not this time.*

The sunset, beginning far to the west, stained the walls of the imperial capital.

* * *

Hangzhou made a fine first impression.

It had an abundance of goods carried by canal throughout Zhejiang Province, and its scenery was beautiful.

The wide plains we’d passed on the way were covered in every kind of grain, rippling like golden waves. Smiles never left the people’s faces.

*They say it’s the most beautiful city under heaven.*

Something I’d once heard in passing. And it was absolutely true.

Maybe that was why they’d abandoned a great city with Nanjing’s long history and moved the capital to Hangzhou.

There was just one problem: this beautiful city was a lot more threatening than I’d expected.

Clank. Clank.

The cold scrape of weapons.

Whichever way I turned, I saw soldiers. And not the half-trained grunts I was used to—these were elite troops, fully armed.

Even the easygoing Hyuk Mujin had lost his smile and said,

“Captain. This is a bit… much, isn’t it?”

Normally, I’d have shot back at him out of habit. But this time, even I had to agree.

*Why are there so many?*

It wasn’t just a lot. There were a downright disgusting number of them.

There were so many I was starting to wonder if Zhejiang Province’s specialty wasn’t Longjing tea but Imperial Guards.

“Is security always this tight?”

Hyuk Mujin wasn’t the only one who’d lost his smile after we entered Hangzhou.

Hong Jin answered my question in a voice so stiff it hardly sounded like him.

“As the imperial capital, it’s always been well guarded. Of course, it’s never been like this before.”

“Then…”

“They must have received some sort of order. And it’s probably… connected to us somehow.”

Hong Jin licked his red-painted lips and murmured,

“I had my suspicions, but this welcome is more intense than I expected.”

For a moment, I pictured a hundred thousand soldiers pointing their spears and blades at us. Then I shook my head.

*That’s unlikely.*

If they’d wanted to kill him that easily, Prince Shangshan Zhu Bao wouldn’t have made it out of Shanxi Province.

I didn’t know exactly why the Son of Heaven had sent the Embroidered Uniform Guard to bring his young brother here. But one thing was certain: the prince would be dealt with in a way the emperor could publicly justify.

That was the nature of an emperor.

*Besides, the emperor’s public image is already bad.*

Was it for nothing that people said the people’s will was the will of Heaven?

The nomadic people of the steppe, who had ruled the continent before the Great Nation, had fallen alongside the people’s waning support.

The emperor ruled the people, but without the people, there could be no emperor.

In that sense, the public’s view of the current Son of Heaven was quite negative.

*A capable but ruthless emperor.*

I’d heard it now and then in Murim, and learned more about him through quiet conversations with Hong Jin on the way here.

The current emperor had built up an impressive record of military service from a young age, putting down several rebellions and uprisings by foreign peoples. He was also praised as a ruler who left no detail unattended in governing the regions under his charge.

Hong Jin said that if the emperor had been born the late Emperor’s eldest son—or if his eldest brother, the Crown Prince, had been even a little less capable—he would naturally have inherited the throne.

*But things hadn’t worked out that way.*

Before becoming emperor, he’d been nowhere near the line of succession.

He had three older brothers. And his eldest, who had naturally become Crown Prince under the principle of primogeniture, was every bit as outstanding as he was—perhaps even more so, depending on whom you asked.

A fine man who treated people with kindness and integrity regardless of their status, and showed every quality needed to lead the Great Nation.

Hong Jin had described the Crown Prince of that time as:

*A Son of Heaven prepared for the throne.*

The long wars had ended long ago.

The seeds of rebellion scattered across the land and the foreign peoples who had constantly eyed the Great Nation had all been uprooted.

The Great Nation had been established on firm foundations. What it needed now wasn’t conquest, but stability. With his perfect orthodox lineage and all the qualities a ruler could need, the Crown Prince was a successor prepared in every respect.

That was until the Emperor, then the imperial family’s fourth son, had drawn his sword from the shadows—already pushed far from the line of succession.

Clip-clop.

The sound of hooves rang out unusually clearly, snapping me out of my thoughts. I looked around.

*Where are we?*

The answer came quickly.

The carriage had stopped, and beyond the Embroidered Uniform Guard packed tightly around us stood enormous buildings the likes of which I’d never seen in Murim.

They were so tall they reminded me of modern skyscrapers, and so richly and classically decorated that those skyscrapers couldn’t compare. They could only mean one place.

*The imperial palace.*

The dragon’s lair, and the center that kept the enormous gears of the world turning.

I stared silently at the entrance to the palace, so overwhelming that even the sight of it through the narrow gap in the window was enough to make me feel small. Hong Jin leaned close and whispered, barely above a breath.

“Young Master Jin, I’ve held it in until now, but… don’t you think it’s time to tell me?”

The moment he said it, I knew what he was asking.

The others besides Hyuk Mujin and me.

Hong Jin wanted to know where our other helpers were—the ones who still hadn’t shown themselves. I already had my answer.

—Don’t worry. You’ll find out soon enough.

It wasn’t the answer he’d hoped for. Hong Jin furrowed his brow slightly, but didn’t complain.

I’d traveled all this way, without stopping, to help them.

If we couldn’t even trust one another in a situation like this, the anxiety and danger would only grow.

And with that in mind, I couldn’t help asking him something, too.

—How do you know all of this?

It was a question I’d been carrying for quite some time.

Prince Shangshan Zhu Bao might have been a prince in name only, but he was the only direct imperial relative to have survived the horrific struggle over the throne—and a prince who ruled a fief.

I’d long suspected that Hong Jin, the prince’s trusted aide, couldn’t be an ordinary eunuch. But the breadth of his knowledge and the way he faced the Embroidered Uniform Guard, feared wherever they went, without a hint of unease exceeded even my expectations.

I had to ask him directly, even if it meant asking like this.

—Since I’ve risked my life, I deserve an answer to this question. Right now.

Clunk.

At my firm Sound Transmission, Hong Jin stared at me in silence. Then, without warning, he flung open the carriage door.

Looking toward a group of people descending the impossibly high stairs that led down from the imperial palace, he spoke.

“Young Master Jin, I’ve told you why I decided to become a eunuch, haven’t I?”

I nodded.

Back when Hong Jin and I first met in Shanxi Province, he’d briefly told me about his past.

“I hated being poor, and I wanted to save my family. But I didn’t have many options. No—at the time, I only had one.”

Hong Jin continued slowly.

To get what you wanted, you had to sacrifice something else.

So the poor boy, unable to overcome his hunger, became a eunuch and chose a new name for himself.

“Hong Jin. I wanted to reach the great waters. To leave that stinking sewer behind and go somewhere wide and clear, like the sea.”

It hadn’t taken long for that wish to come true.

The young eunuch had escaped poverty and developed ambitions he’d never had before. He also had the ability to fulfill them.

And his usual thoroughness and cool judgment soon caught the eye of the late Emperor.

“One day, the late Emperor summoned me and told me there was a place where my talents could be put to good use.”

Hong Jin continued in a clear voice.

“Young Master Jin. Have you ever heard of the East Depot?[^1]”

“……!”

[^1]: The East Depot was an imperial secret-police agency in Ming China.
```
