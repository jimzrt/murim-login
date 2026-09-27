<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1155.txt",
      "sha256": "923ff84ed9b335f10499d827c2b6af34bbe4a05eac0ca6fe499a027806079eac",
      "bytes": 12507
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3b886a656e9aa6841b2a9f640e1d1d1bee4dedccddcb98c7b5ebca8784340c7c",
      "bytes": 1020
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "88a1b76647d767dc82cf4a47e15bbda9838c62ed98aa6d5f596709b3ac58dc67",
      "bytes": 246893
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b61293b96c32ae9dac4f833d6052203a201af2006adb4686ffe0b8f9ac55fd0b",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0e56d1c0ea22dc3e4284b6bd93dc1b0ba5d3591ca6a3bc50b36e32e2d1ef0390",
      "bytes": 1725
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "22d3a6b3236534634f743861bd9d526ecf2d80bfdd578fc1856feb1e871874e5",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "52d277957d0f8dcf634e6a194d82e99e1425b11336d44df255be2ba473fafc80",
      "bytes": 293106
    }
  ],
  "estimated_tokens": 8940
}
-->

# Durable State Update — Chapter 1155

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
1 and safe_through 1155. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1155. Profile updates may replace only one
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
  "chapter": 1155,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1155,
    "continuity_sources": [1155],
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
    "Morgoth destroyed Moscow and opened a Gate from the Demon Realm above its ruins; a vast monster army has invaded Earth and is advancing across Russia.",
    "Morgoth offers survival under his rule to those who surrender and demands Cheon Taemin and Jin Taekyung as tribute within three days.",
    "Cheon Taemin remains unconscious; Jin Taekyung has returned and is widely regarded by humanity as a new-age savior."
  ],
  "continuity_sources": [
    1154
  ],
  "open_questions": [
    "How will humanity respond to Morgoth’s surrender offer and demand for tribute?",
    "Can Jin Taekyung stop Morgoth and the invading army?",
    "What did the System notification shown to Jin Taekyung say?"
  ],
  "safe_through": 1154,
  "temporary_decisions": [
    "Render 은빛 산 as “Silver Mountains” and 마계의 대공 as “Archduke of the Demon Realm.”",
    "Render 모르고스’s command ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ as “Answer the call.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 힐러      | **healer**            |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 개봉 | **Kaifeng** | City where the preliminary competition will be held. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 대통령 | **President** | Title for Korea's head of state. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 힐러 | 진태경 | healer addressing the rescuer who stabilized the survivor | sir | deferential and grateful | The healer thanks Jin as 선생님 after witnessing his rescue and treatment. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 진태경 | 힐러 | invading Hunter to Ares healers | you people | profane and contemptuous | Uses 당신들이 while demanding that the healers save their fallen comrades and question Go Jun's order. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1154
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1154
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1154
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1155화



[러시아가 공식적으로 항복을 선언했습니다. 현 러시아 연방군 총참모장이자 모스크바 참극 직후 대통령 대행으로 임명된 바실리 게라시모프 대장은…….]

삑.

[전날 모스크바 참극의 여파로 극심한 피해를 입은 바 있는 우크라이나와 벨라루스를 중심으로 한 동유럽 국가는 모든 전력을 총동원하여 국경에 배치 중인 것으로…….]

삑.

[현재의 재난 상황에 대해 알려 드립니다. 전 세계를 기준으로 지난 11일간 하루 평균 네 건 이상의 몬스터 웨이브(Monster Wave)와 50여 건의 변이 게이트 현상이 발생했습니다.]

[정말이지 끔찍한 소식이군요. 그렇다면 에이미, 마력 분포도에 대한 소식은 어떻습니까?]

[유감이지만, 스티브. 금일의 마력 분포도는 2.8포인트 증가했습니다.]

[뭐라고요?]

[예. 무려 2.8 포인트입니다. 만약 이것이 어느 정도의 수치인지 가늠이 안 된다면, 이 자료 화면을 유심히 봐 주시길 바랍니다.]

[자, 여기 일일 5.0포인트 상승이라고 적혀 있군요. 네? 그래서 뭐가 문제냐고요? 참고로 이건 대격변 초기의 마력 분포도 변화를 그래프화한 자료입니다.]

[다시 말해서, 우리는 대격변 당시의 마력 수치를 절반 이상 따라잡았습니다. 특히나 몬스터 웨이브와 변이 게이트 현상이 집중적으로 발생한 중동 지역은 두 번째 대격변이 시작되었다고 해도 과언이 아니죠.]

[거기에 더해 모스크바 일대의 상황은 이미…… 모두가 아시리라 믿습니다. 제가 할 수 있는 말은 하나밖에 없군요.]

[부디 신의 가호가 함께하길.]

삑.

[속보입니다. 모르고스가 러시아의 항복을 받아들였습니다. 남부 표준시 기준 16:30부터 러시아 연방은 모든 무장을 해제하고, 앞서 항복했던 20여 개국과 같이 현재의 정부 체계를 유지하게 될 것입니다.]

[반면 이 결정에 반발한 상당수의 헌터 집단은 러시아 곳곳에서 몬스터와 맞서 교전을 벌이고 있는 것으로 확인…….]

삑.

[……당신의 의견에도 일부분 동의하오. 현재로서는 우리에게 매우 어려운 상황이지.]

[인류가 항복해야 한다는 뜻으로 이해해도 되겠습니까?]

[전혀. 나는 다만 통계학적 근거를 바탕으로 말한 것뿐이오.]

[하지만 앞서 박사님께서 하신 말씀대로라면, 인류가 모르고스를 상대로 승리할 수 있는 확률은 존재하지 않는 것이 아닙니까?]

[이쯤 되면 당신의 귀가 항문에 달린 것이 아닌지 의심이 되는군. 몇 번이나 말했듯이, 정확히 5.2퍼센트요.]

[민망할 정도로 낮은 확률이군요. 아마 이 방송을 보고 계시는 시청자분들도 저와 같은 생각을 하고 계시겠죠.]

[그래, 확률이 낮다는 걸 부정하진 않겠소. 그러나 똑똑히 알아두시오. 이건 대격변이 막 시작되었을 당시와 비교하면 비약적으로 높은 수치라는 걸.]

[압니다. 박사님께 노벨상까지 안겨 준 그 훌륭한 논문에 의하면, 0.2퍼센트로 명시되어 있더군요.]

[축하하오. 귀와 달리 눈은 제대로 된 위치에 달린 모양이군.]

[축하해 주셔서 감사합니다만, 저로서는 논문에 적힌 0.2퍼센트라는 수치가 어디까지나 스카이(Sky)의 등장 이전에 국한된 것이라는 사실을 짚고 넘어가지 않을 수 없겠네요.]

[맞소. 그렇지만 바로 그 스카이도-]

[마왕 아스모데우스와의 마지막 결전 직전까지도 승리 확률이 채 20퍼센트가 되지 않았죠. 예, 알고 있습니다. 하지만 그때와 달리 지금의 인류에게는 또 다른 선택지가 있지 않습니까?]

[당신!]

[입에 담기도 참담한 현실이지만, 그렇다고 해서 영원히 외면할 수는 없습니다. 더 늦기 전에 눈앞의 문제를 똑바로 직시해야죠. 안 그렇습니까?]

[…….]

[30여 년 전의 우리에게는 선택지가 없었습니다. 그저 온 힘을 다해 저항할 수밖에 없었죠. 그러나 모르고스는 지금 평화를 제안하고 있고, 실제로도 그에게 항복한 국가들은 정부를 유지한 채로 국민들을 안정시키고 있습니다.]

[……모르고스는 몬스터요. 빌어먹을 몬스터라고. 그 교활한 놈이 원하는 게 무엇인지 정말 모르겠소?]

[사람들이 원하는 게 무엇인지는 확실히 압니다. 바로 평화죠. 소중한 사람들의 목숨을 지킬 수 있는.]

[Bullshit. 이보게 젊은 친구, 헛소리는 집어치우게. 자네는 그저 비열한 겁쟁이에 불과해. 인류 전체를 위하는 척 스스로에게 최면을 걸면서 산 제물을 바치자고 주장하고 있지. 그것도 우리를 위해 누구보다 애써온 두 영웅을 말일세.]

[스카이와 진은 인류 역사에 영원토록 남을 만한 영웅들입니다. 저 역시 그들의 희생에 감사하고 있고요.]

[그게 사실이라면 지금 당장 그 염병할 아가리를 닥치고 집으로 가게. 그리고 가족들을 한 번씩 안아 준 뒤 서재로 가서 숨겨 뒀던 권총을 꺼내. 번거롭게 유서를 남길 필요까진 없을 걸세. 자네가 뒈져야 할 이유는 나를 포함해서 이 방송을 시청하고 있는 모두가 알고 있으니까.]

[이런, 정말 무례하시군요. 저는 다만 그 두 사람이 위대한 영웅답게 수십억 인류를 위하여 스스로 숭고한 희생을 선택하리라고 예상-]

[좋아, 그럼 어쩔 수 없군.]

[What?]

[지옥에나 떨어져라, 이 개자식아.]

탕! 타탕!

[꺄아아악!]

[Fuck! 힐러! 지금 당장 힐러 불러!]

[박사, 진정하고 권총 내려놓으십시오! 이건 경고…….]

삐이-!

[생방송 중 벌어진 불미스러운 사고에 대하여 사과의 말씀을 드립니다. 당사는 상황 수습에 최선을 다할 것이며-]

삑.

마침내 찾아온 정적 속, 흐릿한 빛만 내뿜고 있는 홀로그램 TV를 말없이 바라보던 스켈레톤 킹이 문득 입을 열었다.

“인간들이란.”

숨길 수 없는 혐오가 묻어 나오는 그 음성에, 탁자에 놓인 위스키병을 빤히 응시하고 있던 척 헤이글이 대꾸했다.

“같은 인간으로서 듣고 있자니 기분이 묘한데.”

“그럼 뭐라고 반박이라도 좀 해 보지 그래.”

“반박 안 해. 틀린 말도 아니니까. 특히 방금 그놈은 총맞을 만했어.”

스켈레톤 킹은 고개를 끄덕였다.

대격변과 마력에 관한 한 최고의 석학이라는 늙은 박사의 대처는 그가 생각하기에도 아주 훌륭했다.

한눈에 보기에도 각성은커녕 각성제라도 맞아야 움직일 수 있을 것 같은 90대 노인이었으나, 아메리카의 유구한 전통 무술인 건법(Gun法)에는 별다른 나이 제한도 없으니까.

“살았을까?”

“머리에 맞지는 않았으니까 그럴 확률이 높지.”

“아쉽군.”

“그 의견에는 매우 공감하지만, 저놈은 살아 있는 편이 나아. 저대로 죽어 버리면 오히려 여론 형성에 안 좋은 영향을 끼칠 수도 있거든.”

“……하긴.”

잠시 내려앉은 침묵 속, 스켈레톤 킹은 TV에서 보았던 여러 장면을 머릿속으로 되새겼다.

온 사방에서 들끓어 오르는 불안과 공포.

과거 대격변 당시의 상황을 따라잡을 기세로 폭등하는 마력 분포도와 이제는 버젓이 전파를 타고 세계 곳곳으로 퍼져 나가는 헛소리들까지.

스켈레톤 킹으로서는 도무지 이해할 수 없는 상황이 곳곳에서 벌어지고 있었다.

“술과 담배에 찌든 인간이여. 뭐 하나만 물어봐도 되나?”

“몇 시간 전에 술도 담배도 끊었지만, 일단 물어봐.”

“어떤 것이 인간의 본질이지?”

“대답하기 곤란한 질문이군. 아무래도 철학은 내 분야가 아니라서.”

“네가 그리 똑똑한 인간이 아니라는 사실은 이미 알고 있으니 걱정 말도록.”

“……뭐, 좋아.”

스켈레톤 킹을 노려보던 척 헤이글이 어깨를 으쓱했다.

“모두 다.”

“모두 다?”

“그래, 네가 지금까지 우리와 함께하며 보고 느낀 모든 게 인간의 본질이지. 적어도 나는 그렇게 생각해.”

“정수리를 쪼개서 뇌 구조를 살펴보고 싶을 정도로 멍청하고, 믿을 수 없을 만큼 탐욕스럽고 겁이 많은 게 인간의 본질이라고?”

“부정하고 싶지만, 그 또한 인간의 본질이야. 하지만 네가 느낀 점이 그것만은 아닐 텐데. 안 그래?”

물론이었다.

애초에 저런 지저분한 모습들만 봐 왔다면, 스켈레톤 킹이 지금껏 인간의 모습으로 그들과 함께할 일도 없었을 테니까.

그는 인간을 좋아했다.

처음부터 자신이 일반적인 몬스터와는 다르다고 느꼈고, 게이트 속 캄캄한 숲에서 어느 한 인간을 만난 후부터는 쭉 그들과 함께하게 되었다.

하지만…….

“아무리 그래도 이건, 있을 수 없는 일이잖나.”

“이봐, 해골 친구. 있을 수 없는 일이라는 건 이 세상에 존재하지 않아.”

스스로의 인내심을 시험하듯, 몇 시간째 개봉하지 않은 위스키병을 만지작거리며 척 헤이글이 덧붙였다.

“있어서는 안 되는 일들이 현실로 벌어지고 있을 뿐이지.”

“그렇다면.”

“맞아. 조금 전 총에 맞은 놈이 언급한 그 빌어먹을 ‘숭고한 희생’에 대해 동의하는 목소리가 더욱 커지겠지. 지금의 인류에게는 시간이 없지만, 선택지는 있거든.”

“제아무리 인간이 악한 면을 지니고 있다고 해도, 그들을 위해 목숨 걸고 싸운 영웅들을 제물로 바친다고?”

“제물로 바친다니, 무슨 소리지?”

“……?”

“말했잖나. ‘희생’이라고. 그게 저들이 진정으로 원하는 결과야. 손을 더럽히지도, 비난을 들을 필요도 없이 자연스럽게 외면하는 거지. 제물로 바쳐질 당사자들이 그런 선택을 내릴 수밖에 없도록.”

“……!”

“가장 큰 문제는, 진(Jin)은 충분히 그럴 만한 사람이라는 거고.”

일순간, 스켈레톤 킹은 자신도 모르게 입술을 깨물었다.

맞다.

자신이 아는 진태경은 그런 인간이다.

늘 그를 구박하고 놀려 대지만, 세상 누구보다 무거운 짐을 짊어지고 있는.

그렇기에 어느 때보다 큰 불안감이 엄습했다.

세상이 그의 죽음을 원한다면, 진태경은 스스로를 희생하고도 남을 만한 사람이니까.

“말도 안 돼. 만약 그 간악한 인간이…… 진태경이 스카이와 함께 희생한다고 해도 놈이 약속을 지킬 거라는 확신도 없지 않나.”

“인간은 보고 싶은 대로 보고, 믿고 싶은 대로 믿지. 그리고 모르고스는 그 사실을 너무나도 잘 알고 있어.”

사실이었다.

이미 뉴스에서 나왔듯, 모르고스는 약속을 지켰다.

러시아를 포함, 이미 그에게 항복 의사를 표한 20여 개국의 정부를 유지하고 몬스터들의 살인을 완벽하게 통제했으니.

그리고 그것은 사람들에게 희망을 심어 주었다.

모르고스는 마왕 아스모데우스와는 다르다는.

지금까지와 같은 자유를 누릴 수는 없겠지만, 수많은 이들의 목숨을 지킬 수 있을 것이라는 희망을.

“하지만 모르고스가 그 두 사람을 죽이고 약속을 깨트릴 가능성이…….”

“두말할 필요도 없이, 압도적으로 높지. 적어도 우리는 그 사실을 아주 정확하게 알고 있어. 그러나 공포에 반쯤 정신이 나가 버린 사람들이 그런 생각이나 하겠나?”

척 헤이글이 거칠어진 목소리로 말을 이었다.

“그 개자식들이 스스로의 잘못을 깨달았을 때는 모든 게 늦어 버린 후겠지. 현재 모르고스와 맞서 싸울 수 있는 유일한 헌터는 놈의 뱃속에 들어가 있을 테고.”

분노가 응어리져 있는 그 음성이 울려 퍼진 순간이었다.

불현듯 떠오른 한 가지 생각이, 스켈레톤 킹의 뇌리를 스쳐 지나간 것은.
```

## Final English reading copy

```markdown
# Chapter 1155

“Russia has officially declared its surrender. General Vasily Gerasimov, current Chief of the General Staff of the Russian Armed Forces and acting president appointed in the immediate aftermath of the Moscow catastrophe, has…”

Beep.

“Eastern European countries, particularly Ukraine and Belarus, which suffered severe damage in the aftermath of yesterday’s Moscow catastrophe, are mobilizing all available forces and deploying them along their borders…”

Beep.

“We now bring you an update on the current disaster. Over the past eleven days, the world has seen an average of more than four Monster Waves and around fifty cases of Gate mutations every day.”

“That’s truly horrifying news. Amy, what about the magical power distribution?”

“I’m afraid it’s bad news, Steve. Today’s magical power distribution rose by 2.8 points.”

“What?”

“Yes. A full 2.8 points. If you’re having trouble judging what that figure means, please take a close look at this graphic.”

“Here, it says the increase was 5.0 points per day. So what’s the problem, you ask? For reference, this graph shows the changes in magical power distribution at the beginning of the Great Cataclysm.”

“In other words, we’ve caught up to more than half of the magical power levels from the Great Cataclysm. In the Middle East, where Monster Waves and Gate mutations have been occurring in particularly high numbers, it’s no exaggeration to say that a second Great Cataclysm has begun.”

“And on top of that, the situation around Moscow is already… I’m sure everyone knows. There’s only one thing I can say.”

“May God be with you.”

Beep.

“Breaking news. Morgoth has accepted Russia’s surrender. Starting at 16:30 South Standard Time, the Russian Federation will disarm completely and, like the more than twenty countries that surrendered before it, retain its current system of government.”

“Meanwhile, a large number of Hunter groups opposed to this decision have reportedly engaged monsters in battles throughout Russia…”

Beep.

“…I agree with part of what you’re saying. Our situation is extremely difficult right now.”

“Should we understand that to mean humanity ought to surrender?”

“Not at all. I’m simply speaking on the basis of statistical evidence.”

“But according to what you said earlier, Doctor, there’s no chance of humanity defeating Morgoth, is there?”

“At this point, I’m beginning to wonder if your ears are attached to your anus. As I’ve said several times now, it’s exactly 5.2 percent.”

“That’s an embarrassingly low probability. I’m sure our viewers are thinking the same thing.”

“Yes, I won’t deny the odds are low. But remember this clearly: compared with when the Great Cataclysm first began, that figure is dramatically higher.”

“I know. According to that excellent paper that even won you a Nobel Prize, the figure was 0.2 percent.”

“Congratulations. Unlike your ears, your eyes seem to be in the right place.”

“Thank you. But I can’t help pointing out that the 0.2 percent in your paper applied only to the period before Sky appeared.”

“True. But even Sky—”

“—had less than a 20 percent chance of winning right up until the final battle with the Demon King Asmodeus. Yes, I know. But unlike then, humanity has another option now, doesn’t it?”

“You!”

“It’s a reality too appalling to say aloud, but that doesn’t mean we can keep ignoring it forever. Before it’s too late, we need to face the problem right in front of us. Don’t you agree?”

“……”

“Thirty years ago, we had no options. We could only resist with everything we had. But Morgoth is offering peace now, and the countries that surrendered to him really are keeping their governments and calming their people.”

“……Morgoth is a monster. A fucking monster. Do you really not understand what that cunning bastard wants?”

“I know exactly what people want. Peace. A chance to protect the lives of the people they love.”

“Bullshit. Listen, young man, cut the nonsense. You’re nothing but a despicable coward. You’re hypnotizing yourself into thinking you speak for all of humanity while arguing that we should offer up a living sacrifice. And not just anyone—two heroes who’ve done more for us than anyone else.”

“Sky and Jin are heroes who’ll be remembered throughout human history. I’m grateful for their sacrifices, too.”

“If that’s true, then shut your damn mouth and go home right now. Hug your family, one by one. Then go to your study and take out the pistol you’ve hidden there. No need to bother writing a will. Everyone watching this broadcast, myself included, knows why you need to die.”

“My, how rude. I’m simply saying that I expect those two to make a noble sacrifice of their own accord, as great heroes would, for the sake of billions of people—”

“Fine. Then I have no choice.”

“What?”

“Go to hell, you son of a bitch.”

Bang! Bang-bang!

“Aaah!”

“Fuck! Healer! Get a healer in here, now!”

“Doctor, calm down and put the gun down! This is a warn—”

BEEEEEP!

“We apologize for the unfortunate incident during our live broadcast. We will do everything we can to resolve the situation—”

Beep.

At last, silence settled over the room. The Skeleton King stared without a word at the holographic TV, now giving off only a dim glow. Then he spoke.

“Humans.”

The word dripped with unconcealed disgust. Chuck Hagel, who had been staring at the whiskey bottle on the table, answered him.

“As a human, I have to say, that’s a weird thing to listen to.”

“Why don’t you try arguing against it, then?”

“I’m not going to. He wasn’t wrong. Especially that last guy. He deserved to get shot.”

The Skeleton King nodded.

Even he had to admit that the old doctor—one of the foremost scholars on the Great Cataclysm and magical power—had handled the situation remarkably well.

The man looked to be in his nineties and, far from being Awakened, seemed to need a shot of stimulants just to move. But America’s venerable martial art of gun-fu had no age limit.

“Do you think he survived?”

“He wasn’t hit in the head, so probably.”

“Pity.”

“I agree completely. But it’s better for that guy to stay alive. If he died there, it could actually hurt public opinion.”

“……Fair enough.”

In the silence that followed, the Skeleton King replayed the scenes he’d seen on TV.

Anxiety and fear boiling over everywhere.

The magical power distribution soaring toward the levels of the Great Cataclysm—and the nonsense now being broadcast openly across the world.

Things were happening everywhere that the Skeleton King simply couldn’t understand.

“You human, steeped in alcohol and tobacco. May I ask you something?”

“I quit drinking and smoking a few hours ago, but go ahead.”

“What is the essence of humanity?”

“That’s a difficult question to answer. Philosophy isn’t really my field.”

“I already know you’re not particularly intelligent, so don’t worry.”

“……Fine.”

Chuck Hagel, who’d been glaring at the Skeleton King, shrugged.

“All of it.”

“All of it?”

“Yeah. Everything you’ve seen and felt while you’ve been with us. That’s what I think, anyway.”

“Humans are stupid enough to make me want to crack open their skulls and examine their brains, and so greedy and cowardly it’s hard to believe. That’s their essence?”

“I wish I could deny it, but that’s part of it, too. But that’s not all you’ve seen, is it?”

Of course it wasn’t.

If all the Skeleton King had ever seen were those ugly sides of humanity, he never would have lived among them in human form.

He liked humans.

He’d always felt that he was different from ordinary monsters. And ever since he’d met a human in the dark forest inside a Gate, he’d stayed with them.

But…

“Still, this… This shouldn’t be possible.”

“Listen, my bony friend. There’s nothing in this world that’s impossible.”

Chuck Hagel ran his fingers over the whiskey bottle, still unopened after several hours, as if testing the limits of his own patience. Then he added:

“Things that should never happen are just happening anyway.”

“Then…”

“Right. More people will start agreeing with that damn ‘noble sacrifice’ the guy who just got shot was talking about. Humanity’s running out of time, but we still have a choice.”

“Even if humans have evil in them, they’d offer up the heroes who risked their lives fighting for them as sacrifices?”

“Offer them up? What are you talking about?”

“……?”

“I said ‘sacrifice.’ That’s what they really want. To look away without getting their hands dirty or having to hear anyone blame them. To make the people being sacrificed feel like they have no choice but to choose it themselves.”

“……!”

“The biggest problem is that Jin is exactly the kind of person who’d do it.”

For a moment, the Skeleton King bit down on his lip without realizing it.

That was right.

Jin Taekyung was that kind of person.

He was always scolding and teasing him, but he carried a heavier burden than anyone else in the world.

And that was why an even greater unease came over him.

If the world wanted him dead, Jin Taekyung was exactly the sort of person who would sacrifice himself.

“That’s ridiculous. Even if that treacherous human, Jin Taekyung, sacrificed himself alongside Sky, how could we be sure Morgoth would keep his promise?”

“Humans see what they want to see and believe what they want to believe. Morgoth knows that better than anyone.”

It was true.

As the news had just reported, Morgoth had kept his promise.

He’d maintained the governments of the more than twenty countries that had already declared their surrender, Russia among them, and completely restrained the monsters from killing anyone.

And that had given people hope.

Hope that Morgoth was different from the Demon King Asmodeus.

Hope that, even if they couldn’t enjoy the freedom they’d had before, they could still save countless lives.

“But the chance that Morgoth will kill those two and break his promise…”

“Is overwhelmingly high. There’s no question about it. At least, we know that with absolute certainty. But do you think people, half-crazed with fear, are going to think that way?”

Chuck Hagel continued, his voice growing rougher.

“By the time those bastards realize what they’ve done, it’ll be too late. The only Hunter who can fight Morgoth right now will be inside that bastard’s stomach.”

The instant those words of tightly coiled anger rang out, a thought suddenly flashed through the Skeleton King’s mind.
```
