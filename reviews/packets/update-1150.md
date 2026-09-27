<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1150.txt",
      "sha256": "264a01ec91160278441766e77d5a75813a63d8c377f89728ced9693a30e05126",
      "bytes": 12026
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2935ddcf1e97d7e3803e8323afeab7d93dd16154eb4a79f1814c8c6840369c84",
      "bytes": 1072
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "43462be5eea22f76b3f427491db9c94d53de518aa1f3a03787e88e23427d0f2f",
      "bytes": 246289
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cb744fcc0eb5de663368f75538a73d28eea7c98b99d396212a916da4bf67858e",
      "bytes": 760
    },
    {
      "path": "characters/Michael.md",
      "sha256": "144e28332690d7aa80ceb6e3adf19611f1284693b9925c370ee7b9a1505b462c",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bf7859ae1f94bc4cd95e13e452647f001d596b267e8e1a51602d9cd5390de154",
      "bytes": 292059
    }
  ],
  "estimated_tokens": 8035
}
-->

# Durable State Update — Chapter 1150

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
1 and safe_through 1150. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1150. Profile updates may replace only one
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
  "chapter": 1150,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1150,
    "continuity_sources": [1150],
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
    "Taekyung has been unconscious for ten days; Magic Johnson's last contact with the group was twenty-four hours ago.",
    "The Main Quest Cataclysm failed despite the Doppelganger's defeat; the Demon Realm's boundaries have partially opened and a rift is in progress.",
    "Black Dragon Duke Morgoth has answered a summoning; Taekyung recognizes his wings and roar from his last night in Murim.",
    "Morgoth destroyed Red Square and entered Vladimir Furin's office in Russia.",
    "Taekyung and the Skeleton King are allies and friends."
  ],
  "continuity_sources": [
    1149
  ],
  "open_questions": [
    "Why has Taekyung's ten days of unconsciousness corresponded to only twenty-four hours since the last contact?",
    "What conditions change the rift's progress?",
    "What does Morgoth intend in Russia?"
  ],
  "safe_through": 1149,
  "temporary_decisions": [
    "Render 흑룡공 as “Black Dragon Duke” and 모르고스 as “Morgoth.”",
    "Render 균열과 붕괴 as “Rift and Collapse.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 평화 | **Peace Guild** | Guild name. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1149
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 843
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃1150화



악수.

두 사람이 서로 한 손을 건네어 잡는 행위이자, 전 세계적으로 가장 보편적인 인사법.

하지만 서로의 손과 손이 맞닿은 그 순간, 블라디미르 푸린은 일평생 수만 번도 넘게 해 왔던 모든 악수가 뇌리에서 지워지는 것을 느꼈다.

“……!”

차갑고, 단단하다.

강철?

아니다.

사내. 아니, 모르고스의 손은 지금껏 세상에 존재하지 않았던 물질처럼 그의 손을 감싸 안았고, 이내 천천히 위아래로 흔들었다.

마치 손안의 개미를 다루듯 조심스럽게.

그리고 짧은 악수를 끝마쳤을 때, 괴물의 입가에는 만족스러운 미소가 맺혀 있었다.

“역시 흥미롭군. 이 세상의 인간들은.”

짧지만 많은 것이 담겨 있는 한 마디.

푸린은 자신의 귀를 의심하며 입을 열었다.

“그게…… 무슨 뜻이지?”

“글쎄, 굳이 부연 설명이 필요한가?”

자연스럽게 맞은편 자리에 앉은 모르고스가 신기한 눈빛으로 탁자 위의 집기들을 훑었다.

“봐도 봐도 놀라운 문명이야. 한때 내가 머물렀던 세상의 인간들은 꿈도 꿀 수 없을 만큼.”

“……!”

“이 정도의 반응이 나올 줄은 몰랐는걸. 너희도 이미 짐작하고 있었지 않나. 저 어딘가에는 마계(魔界)와 같은 또 다른 세상이 존재하리라는 것을.”

모르고스의 말은 틀림없는 사실이었다.

대격변 이후, 세계 각국은 마계가 아닌 또 다른 이계(異界)의 존재 유무에 관하여 물밑으로 수많은 연구를 계속해 왔고 그건 지금까지도 현재 진행형이었다.

하지만 짐작과 확신은 다른 법.

지금 모르고스는, 어디까지나 가설에 불과하던 이계의 존재를 확인시켜 주었다.

자신이 어디에서 왔는지도.

‘혹시?’

푸린은 생각했다.

어쩌면 눈앞의 이 괴물이 단순히 피에 미친 몬스터가 아닐 수도 있지 않을까 하고.

만약 그렇다면, 지난 열흘 동안 이어졌던 악몽 같은 재앙도 뒤늦게나마 수습할 수 있을 가능성이 충분했다.

“그렇다면 너, 아니 당신은 지금 말한 그 이계에서 온 건가?”

모르고스가 선선히 대답했다.

“그럴 수도 있고, 아닐 수도 있네.”

“무슨 뜻이지?”

“말했잖나. 한때 머물렀던, 이라고.”

“그럼…….”

“물론 그 세상의 인간들도 제법 흥미로운 구석이 많았지. 하지만 시간이 흐르자 어느 순간 모든 것이 지루해지더군. 변화가 필요한 시점이었어. 아주 강렬하고 확실한 변화가.”

그 말에 담긴 뜻을 알아차린 듯, 눈을 부릅뜬 푸린을 향해 모르고스가 부드럽게 웃었다.

“그래서 떠났지. 마계로.”

“……!”

“누군가의 밑에 들어가는 건 썩 유쾌한 일은 아니었지만, 결과적으로는 매우 훌륭한 선택이었네. 이처럼 흥미로운 유희까지 경험하게 되었으니. 안 그런가?”

그 순간, 푸린은 자그마한 모닥불처럼 타오르던 희망이 흔적도 사그라지는 것을 느꼈다.

“……유희?”

“그래, 유희.”

“그럼, 지금까지 벌인 모든 일도 그 잘난 유희였나?”

숨길 수 없는 떨림이 묻어나는 목소리에, 모르고스가 작게 한숨을 내쉬었다.

“역시 인간은 인간이로군.”

“뭐?”

“세상에, 유희라니. 그런 저급한 사고방식으로 나를 판단하지 말게. 그건 단지 징벌이었어.”

“징벌이라니, 그게 무슨……!”

“무지한 것도 죄일세. 만약 처음부터 엎드려 복종했다면 그와 같은 일은 벌어지지도 않았겠지. 하지만 그들은 내 관대한 제안을 거절했고, 나로서는 합당한 벌을 내릴 수밖에 없었네. 그게 전부야.” 

마침내 푸린은 깨달았다.

자신이 마주하고 있는 존재가 얼마나 깊은 어둠을, 광기(狂氣)를 품고 있는지.

유희? 징벌?

둘 다 틀렸다.

모르고스가 행한 모든 것은 대격변이 종결된 이래 찾아볼 수 없었던 재앙이자 학살이었으니까.

약 일 년 전, 아크 리치의 출현을 시작으로 여러 대사건이 있었지만, 지난 열흘간 벌어진 일들에 비하면 새 발의 피에 불과했다.

현재까지의 추정 사상자만 무려 5천만.

중동, 정확히는 북아프리카와 서아시아 일대는 이미 흑룡의 등장과 함께 죽음의 땅으로 변모했다.

저항한 자들은 서서히 썩어 가고 있거나 언데드가 되었고, 살아남은 자들은 절대적인 복종을 맹세하며 노예가 되었다.

신의 선택을 받았다는 헌터도, 철저히 무장한 군대도.

그 누구도 흑룡의 거대한 날개를 꺾을 수 없었다.

이 세상은 이미 그의 것이었다.

“미쳤군. 완전히 미쳤어.”

블라디미르 푸린이 힘없이 뇌까렸다.

그때였다.

모르고스의 입가에 맺혀 있던 미소가 한층 진해진 것은.

“미쳤다고? 내가?”

“왜, 부정할 셈인가? 그토록 많은 사람을 죽였음에도?”

“그럴 리가. 다만 실망스럽기 그지없군.”

심연을 닮아 있는 흑룡의 두 눈동자가, 눈앞의 독재자를 꿰뚫듯 응시했다.

“어떻게 자네 같은 인간이, 감히 그런 말을 입에 담을 수 있지?”

“……!”

“물론 어느 정도는 이해해. 인간의 얄팍함에 대해서는 익히 겪어 알고 있으니까. 부와 권력이 얼마나 너희를 타락시키는지도. 하지만.”

팅.

길고 새하얀 손가락이 찻주전자를 두드리자, 한때 푸린을 상징하는 대명사처럼 여겨졌던 홍차가 찰랑거렸다.

“어설픈 위선은 집어치우게. 그건 내 지성에 대한 모독이야.”

“너, 너는.”

“그래, 이미 많은 것을 알고 있지. 너희를 통해 알게 되었다는 것이 가장 정확한 표현이겠지만.”

실로 긴 세월을 살았다.

아득하리만치 기나긴 세월을.

하지만 그런 모르고스에게도 21세기의 현대는 매우 흥미로운 세상이었다.

지난 인류의 역사는 물론 마법과 과학 기술의 융합, 정부의 체계와 사상.

그로 인해 전 세계 곳곳에 뿌리내린 크고 작은 분쟁까지.

지금껏 보지 못한 새로운 형태의 문명은 학구열을 자극하기에 충분했고, 망각도 한계도 모르는 그의 두뇌는 보고 듣는 모든 것을 순식간에 흡수해 냈다.

그리고 그중에는 이 세상에서 가장 광활한 영토를 다스리는 어느 독재자에 관한 정보 역시 포함되어 있었다.

“인상 깊더군. 여러 가지 의미로.”

그 순간, 블라디미르 푸린은 되레 마음이 차분해지는 것을 느꼈다.

살아 있는 재앙이나 다름없는 저 괴물, 드래곤(Dragon)은 이미 자신에 대한 모든 것을 알고 있었다.

아니, 어쩌면 그가 상상하는 것 이상으로 많은 것을.

그것이 중동을 포함한 전 세계 곳곳을 초토화시키는 과정에서 입수한 정보든, 손바닥만 한 스마트폰 하나에 담겨 있던 정보든 더 이상 중요하지 않았다.

남은 것은 운명과 선택뿐.

그렇게 러시아 연방의 늙은 독재자는, 마지막까지 쓰고 있던 위선의 가면을 내려놓았다.

“그래서? 사인이라도 받으려고 찾아왔나.”

“오, 제법 의연해졌는걸.”

“떳떳하지 못할 이유가 없으니까.”

“그래, 좋아. 이제야 자네를 만난 보람이 느껴지는군.”

재밌다는 표정으로 푸린을 바라본 모르고스가 말을 이었다.

“그럼 단도직입적으로 말하지. 항복하게.”

“노예가 되어라?”

“뭐, 이 세계에는 국민이라는 좋은 단어가 있지 않나.”

“하지만 실상은 노예지. 당신에게 항복한 이들이 어찌 되었는지는 모두가 알고 있어.”

“그렇다면 더 이야기가 쉽겠군. 항복이라는 평화롭고도 현명한 판단 덕분에 수많은 인간들이 살아남았다는 것도 알고 있을 테니까.”

“당신은 아직 인간에 대해 잘 모르는군. 우리는 한낱 개미처럼 하루하루 연명하는 걸 살아 있다고 하진 않아. 울타리 안 가축처럼 길러지다 도축당하는 건 더더욱 싫어하고.”

장장 오십여 년에 달하는 집권 기간 동안 강력한 통제와 억압에 몰두해 온 독재자의 말이라고 하기에는 부끄러울 정도였으나, 푸린은 조금도 신경 쓰지 않았다.

아니, 오히려 노회한 눈빛을 번뜩이며 모르고스를 향해 말을 이어갈 뿐이었다.

“이만하면 충분한 대답이 되었으리라 믿고, 다시 묻겠네. 나를 찾아온 진짜 이유가 뭔가?”

“뭐?”

“사실 줄곧 이해가 되지 않았지. 당신 같은 존재가 왜 굳이 이런 수고로움을 감수하는 것인지. 아, 미리 말해 두겠는데 유희의 일종이니 하는 헛소리는 하지 말아 주게.”

푸린은 탁자 위에 가지런히 놓여 있던 시가를 집어 들고 불을 붙였다.

서서히 피어오르는 연기 사이로 보이는 모르고스를 똑바로 응시하며.

“이렇게 대화를 나누어 보니 더 이해가 되지 않거든. 인간을 가축이나 개미쯤으로 취급하는 당신이 이런 방식으로 외교와 협상을 시도한다? 글쎄, 진심이야 어떻든 나로서는 믿음이 안 가는 게 사실이지.”

종(種)이 다르더라도 궤(軌)는 같을 수 있는 법.

그런 의미에서 블라디미르 푸린은 자신과 모르고스가 서로 퍽 닮아 있다고 여겼다.

그들은 지배자였으니까.

비록 그 격차가 하늘과 땅만큼의 차이일지언정, 모르고스 역시 강력한 힘을 바탕으로 수많은 이들의 머리 위에 군림해 온 폭군이었을 테니까.

그리고 그가 알고 있는 한, 압도적인 힘을 가진 자에게는 대화라는 수단이 필요 없었다.

뻔뻔함은 당연한 덕목이요, 부끄러움은 낡은 서랍장 속 할아버지의 편지처럼 케케묵은 뭔가가 되어 버린다.

한낱 인간에 불과한 그가 이럴진대, 기본적인 관념부터가 다른 드래곤이라면 오죽할까.

더군다나 이 세상에 처음으로 발을 디딘 드래곤은 모르고스가 처음이 아니었다.

“과거 대격변 당시에 파리를 잿더미로 만들었던 당신의 동족 역시 마찬가지였지. 놈은 그 어떤 몬스터보다 포악했고, 무자비했어.”

모르고스가 담담하게 대꾸했다.

“누군지 알 것도 같군. 드물게 그런 녀석들이 있지.”

“놈과의 전투가 있던 날, 백만에 달하는 인명 피해가 있었지. 무려 네 명의 S급이 지휘하던 천 명의 헌터들도 함께 죽었고.”

드래곤이 쓰러진 자리에서 미카엘 실베르트라는 또 다른 괴물이 탄생했지만, 그것은 최근에서야 밝혀진 일.

끝부분을 골고루 태운 푸린이 시가를 물며 덧붙였다.

“그런데, 그때의 어린 드래곤보다도 훨씬 강한 힘을 지닌 당신이 이렇게까지 하는 이유는 무엇일까.”

찰나의 침묵이 내려앉았으나, 그 침묵은 그리 오래가지 않았다.

질문을 받은 이가 대답하지 않더라도, 질문한 이는 이미 그 물음에 대한 답을 알고 있었으니.

“당신도 느낀 거지. 모든 인간과 싸울 수는 없다는 걸. 아니, 정확히는…….”

후욱.

짙은 시가 연기를 내뱉으며, 이미 모든 것을 잃을 준비를 끝낸 늙은 독재자가 웃었다.

“아직 찾아내지 못한 누군가를 두려워해서겠지.”

그 순간.

달칵. 구구구궁.

주름진 손아귀에 줄곧 숨겨져 있던 작은 버튼이 눌림과 동시에, 크렘린 궁 지하 깊숙한 곳에서 거대한 울림이 솟아올랐다.
```

## Final English reading copy

```markdown
# Chapter 1150

A handshake.

The act of two people reaching out and clasping one another’s hand—a greeting practiced more widely than any other around the world.

But the moment their hands met, Vladimir Furin felt every handshake he’d exchanged tens of thousands of times over the course of his life vanish from his mind.

“……!”

Cold. Hard.

Steel?

No.

The man—no, Morgoth’s hand closed around his as if it were made of a substance that had never existed in this world. Then it began to move slowly up and down.

Carefully, as if handling an ant in his palm.

When the brief handshake ended, a satisfied smile touched the monster’s lips.

“Just as I thought. The humans of this world are fascinating.”

A short sentence, but one that carried a great deal.

Furin wondered if he’d heard correctly, then opened his mouth.

“What… do you mean?”

“Is an explanation really necessary?”

Morgoth sat down naturally in the seat across from him and swept his gaze over the items on the table, his eyes full of wonder.

“An astonishing civilization, no matter how many times I see it. The humans in the world where I once stayed could never have dreamed of anything like this.”

“……!”

“I didn’t expect you to react like that. You already suspected it, didn’t you? That somewhere out there, another world like the Demon Realm existed.”

Morgoth was stating an undeniable fact.

Since the Great Cataclysm, countries around the world had continued to conduct countless behind-the-scenes studies into whether other worlds existed—worlds apart from the Demon Realm. Those studies were still ongoing.

But a suspicion was not the same as certainty.

Morgoth had just confirmed that another world, previously nothing more than a hypothesis, truly existed.

And told him where he had come from.

*Could it be?*

Furin thought.

What if the monster before him wasn’t simply a creature mad with bloodlust?

If that were true, there was a very real chance they might still be able to contain the nightmare that had been unfolding for the past ten days, even at this late hour.

“Then you—no, sir. Did you come from the other world you mentioned?”

Morgoth answered readily.

“That may be true, or it may not.”

“What does that mean?”

“I told you. I said I once stayed there.”

“Then…”

“Of course, the humans of that world had their share of interesting qualities. But as time went on, everything began to bore me. It was time for a change. A powerful, decisive change.”

As if he understood the meaning behind those words, Furin’s eyes widened. Morgoth smiled gently at him.

“So I left. For the Demon Realm.”

“……!”

“Entering someone else’s service wasn’t especially pleasant, but in the end, it was an excellent choice. I’ve had the chance to experience such an interesting game, after all. Don’t you agree?”

In that moment, Furin felt the hope that had been burning like a tiny flame disappear without a trace.

“……A game?”

“Yes. A game.”

“Then everything you’ve done up to now was this grand game of yours?”

At the unmistakable tremor in Furin’s voice, Morgoth let out a small sigh.

“Humans really are human.”

“What?”

“Good heavens, a game? Don’t judge me by such a base way of thinking. It was simply punishment.”

“Punishment? What are you—”

“Ignorance is a sin, too. If they had bowed down and obeyed from the start, none of this would have happened. But they rejected my generous offer, so I had no choice but to give them a fitting punishment. That’s all.”

At last, Furin understood.

Just how much darkness—how much madness—lay within the being before him.

A game? Punishment?

Both were wrong.

Everything Morgoth had done was a catastrophe and a massacre on a scale unseen since the Great Cataclysm had ended.

There had been several major incidents since the Arch Lich appeared about a year ago. But compared with what had happened over the last ten days, they were a drop in the bucket.

Estimates already put the number of dead and injured at fifty million.

The Middle East—more precisely, North Africa and West Asia—had already become a land of death with the Black Dragon’s arrival.

Those who resisted were slowly rotting or had become undead. The survivors became slaves, swearing absolute obedience.

Not Hunters chosen by God. Not even heavily armed armies.

No one could break the Black Dragon’s massive wings.

This world already belonged to him.

“You’re insane. Completely insane.”

Vladimir Furin muttered weakly.

Then Morgoth’s smile deepened.

“Insane? Me?”

“Are you going to deny it? After killing so many people?”

“Of course not. I’m simply disappointed beyond words.”

The Black Dragon’s eyes, like the depths of an abyss, fixed on the dictator before him as if to pierce straight through him.

“How can someone like you dare to say such a thing?”

“……!”

“Of course, I understand to some extent. I know from experience how shallow humans can be—and how wealth and power corrupt you. But…”

Ting.

A long, pale finger tapped the teapot. The tea once considered almost synonymous with Furin rippled inside.

“Spare me the half-baked hypocrisy. It’s an insult to my intelligence.”

“You—you…”

“Yes, I already know a great deal. Though it would be more accurate to say I learned it through you.”

He had lived for an immensely long time.

A time beyond imagining.

Yet even to Morgoth, the modern world of the twenty-first century was deeply fascinating.

Human history. The fusion of Magic and technology. The structures and ideologies of governments.

And the countless conflicts, large and small, that had taken root all over the world as a result.

This new form of civilization, unlike anything he had seen before, was more than enough to stir his thirst for knowledge. His mind, which knew neither forgetfulness nor limits, absorbed everything he saw and heard in an instant.

Among it all was information about a certain dictator who ruled the largest territory in the world.

“I found it impressive. In more ways than one.”

In that moment, Vladimir Furin felt his mind grow strangely calm.

The monster before him, a living calamity, the Dragon, already knew everything about him.

No—perhaps even more than he could imagine.

Whether that knowledge came from information Morgoth had gathered while laying waste to the Middle East and other parts of the world, or from what was stored on a tiny smartphone, no longer mattered.

All that remained were fate and choice.

And so the old dictator of the Russian Federation finally lowered the mask of hypocrisy he’d worn to the very end.

“So? Did you come here hoping to get my autograph?”

“Oh, you’ve become quite composed.”

“I have no reason to feel ashamed.”

“Good. Now I feel my visit was worthwhile.”

Morgoth looked at Furin with amusement, then continued.

“Then I’ll be direct. Surrender.”

“Become a slave?”

“Well, this world has a fine word for it: citizen.”

“But in reality, they’re slaves. Everyone knows what happened to those who surrendered to you.”

“Then this will be easy. You must know that countless humans survived thanks to the peaceful, wise decision to surrender.”

“You still don’t understand humans very well. We don’t consider scraping by day after day like mere ants to be living. And we certainly don’t want to be raised like livestock behind a fence and then slaughtered.”

It was a shameful thing for a dictator to say—one who had spent more than fifty years in power tightening his grip through control and oppression—but Furin didn’t care in the slightest.

No. His shrewd eyes gleamed as he continued to address Morgoth.

“I trust that’s answer enough. So let me ask again. Why did you really come here?”

“What?”

“Truthfully, I’ve been wondering this all along. Why would someone like you go to all this trouble? And let me make this clear in advance: don’t give me any nonsense about it being a game.”

The cigar had been lying neatly on the table. Furin picked it up and lit it.

Through the slowly rising smoke, he stared straight at Morgoth.

“After talking to you, it makes even less sense. You treat humans like livestock or ants, yet you’re trying to negotiate and conduct diplomacy this way? Well, whatever your true intentions, I find it hard to believe you.”

Different species could still follow the same path.

In that sense, Vladimir Furin thought that he and Morgoth were rather alike.

They were rulers.

Even if the gap between them was as wide as the sky and the earth, Morgoth, too, must have tyrannized countless people from a position of power.

And as far as Furin knew, anyone with overwhelming power had no need for conversation.

Shamelessness became a natural virtue, while shame turned into something as old and musty as a grandfather’s letter forgotten in a drawer.

If a mere human like him was that way, then what about a Dragon whose basic sense of the world was different?

Besides, Morgoth wasn’t the first Dragon to set foot in this world.

“Your kind destroyed Paris during the Great Cataclysm. That one was more vicious and merciless than any monster.”

Morgoth replied calmly.

“I think I know who you mean. There are a few like that.”

“The day of the battle against it, there were a million casualties. A thousand Hunters led by no fewer than four S-ranks died as well.”

Another monster, Michael Silbert, was born where the Dragon fell—but that had only been discovered recently.

Furin put the cigar, its tip now evenly lit, between his lips and added:

“So why would you, with power far greater than that young Dragon had, go to such lengths?”

A moment of silence settled over them, but it didn’t last long.

Even if the one asked didn’t answer, the one who’d asked already knew the answer.

“You’ve realized it, too. That you can’t fight every human. No, to be precise…”

Fwoosh.

Exhaling a thick cloud of cigar smoke, the old dictator, already prepared to lose everything, smiled.

“You’re afraid of someone you haven’t found yet.”

At that moment—

Click. Rrrrrumble.

As the small button that had been concealed in Furin’s wrinkled hand was pressed, a tremendous rumble rose from deep beneath the Kremlin.
```
