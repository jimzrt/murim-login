<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1172.txt",
      "sha256": "33aba5feaf7381fee4bed440731089f32e47d3d178336982184bedcf5ce05f61",
      "bytes": 11542
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f26e3a76216d86a41d0be5cdc0573b9530bbabe4822c2ac431347d9b81a1db85",
      "bytes": 845
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6e9de10cb86d235cdc20ec9eddcaa1edc2bda70493e7635975354014596de37a",
      "bytes": 248454
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "432579d7be418479b158870ea0e1445f3f9c3178c169db4ded922128358c787e",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "9619e7c1fffc6594b5a931d6ee0f33aa102afd31adf316892028213da7f7b3a6",
      "bytes": 545
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "e83b2eb1dd7afea1658f3e0be9eac340d25b598b75eaf214f1dc3b10add64301",
      "bytes": 853
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "11fb0f7e4f16c27bbc134493c04626c2dbb21eec0e8c23eabc96857e6602e5fc",
      "bytes": 703
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9888fa34f76fb43f17128ef707d756cad1ad61b59610e952577b341a16beda3f",
      "bytes": 294710
    }
  ],
  "estimated_tokens": 8067
}
-->

# Durable State Update — Chapter 1172

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
1 and safe_through 1172. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1172. Profile updates may replace only one
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
  "chapter": 1172,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1172,
    "continuity_sources": [1172],
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
    "Morgoth was killed when Jin pierced his Dragon Heart; its immense magical power burst across the battlefield.",
    "Jin’s injuries and status effects were healed, but he fell unconscious from severe exhaustion.",
    "The Skeleton King revived as the Lv. 180 Undead King after absorbing the spreading darkness and magical power.",
    "Magic Johnson and the Undead King recognized that another catastrophe had begun or been completed; the pillar of magical power exploded."
  ],
  "continuity_sources": [
    1171
  ],
  "open_questions": [
    "What catastrophe was completed by Morgoth’s death, and what will follow the explosion of the magical-power pillar?",
    "How will Jin fare after his exhaustion-induced unconsciousness?"
  ],
  "safe_through": 1171,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 최민우    | **Choi Minwoo**   |
| 생도     | **cadet**                                    |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 화산     | **Huashan**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 미합중국 | **United States** | Formal Korean reference used during the Defense Minister's imperialist rant. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 마법진 | **Magic Formation** | The formation that transports Ma Sanbao and his followers. |
| 흑룡공 | **Black Dragon Duke** | Title in Morgoth's System announcement. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1171
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1171
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1171
- **Aliases:** None
- **Role:** Morgoth was a Dragon Lord and sovereign of a vast palace, slain by Jin Taekyung when Jin pierced his Dragon Heart.
- **Personality:** Composed and intellectually curious, Morgoth spent millennia seeking God and regards powerful beings as sources of amusement, willing to aid a worthy rival when it promises greater future entertainment.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth returned the Skeleton King to Jin to help him grow stronger and commands seven soul-stolen S-rank Hunters as Guardians.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 1157
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and resolute under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, whom he regards as a model of taking responsibility in a crisis; he is the maternal grandson of Cheon Taemin.

## Korean source

```text
＃1172화



활화산이라는 표현은 결코 과장이 아니었다.

아니, 되레 턱없이 부족했다.

지난 수천 년간 뭇 세상을 공포로 몰아넣었던 악룡의 마지막 숨결이 흩어진 그 순간부터 누구도 막을 수 없는 재앙은 정해진 길을 따라 내달리고 있었으니까.

분출(噴出), 혹은 폭발.

무어라 정의해도 상관없었다.

그저 이것밖에는 남지 않았다는 듯, 처음으로 주인의 통제를 벗어난 드래곤 하트는 아득한 세월 동안 쌓여 있던 모든 것을 세상 밖으로 토해 냈다.

마침내 최후를 맞이한 용의 사체를 장작 삼아, 이제 막 깨어난 활화산보다도 맹렬하게.

콰아아아아!

천지를 떨어 울리는 굉음이 귓가에 닿기도 전에, 전장의 모두는 그 무시무시한 파동을 느낄 수 있었다.

모르고스의 죽음과 함께 안식을 맞이한 일곱 기의 가디언. 아니, 옛 동료들의 시신을 수습하고 있던 S급 헌터들도.

이미 전의를 상실하고 사방으로 흩어진 몬스터들을 추격하던 수천 명의 헌터도.

본능을 자극하는 그 거대한 울림을 느낀 그들은 약속이라도 한 것처럼 한 방향으로 고개를 돌렸고, 이내 석상처럼 굳어 버렸다.

화아아아아.

바람을 타고 전해지는 소름 끼치는 냉기와 거무스름한 안개.

그리고 그 너머로 우뚝 선 아득하고도 거대한 칠흑빛 기둥.

“저게 무슨…….”

누군가의 입술 사이로 흘러나온 외마디 신음은, 아연한 눈빛으로 눈앞의 광경을 바라보던 모두의 마음을 대변하는 것이었다.

악룡은, 모르고스는 분명 죽었다.

그들은 오늘 이 자리에서 승리했고, 당장의 위험은 제거되었다.

그런데 어째서일까.

왜 하늘을 가르고 대지를 향해 죽음의 숨결을 쏟아내던 미증유의 괴물보다, 저 깊고 컴컴한 어둠이 두렵게 느껴지는 것일까.

그러나 이 의문에 대한 답을, 그들은 이미 알고 있었다.

다만 서릿발 같은 마력에 얼어붙은 오감과 정신이 미처 제때 반응하지 못했을 뿐이다.

지금으로부터 불과 수십 년 전, 한 마디의 예고도 없이 찾아온 ‘그날’의 기억을.

하지만 그들 중 가장 먼저, 또한 누구보다 선명하게 이 현상의 정체를 깨달은 두 존재는 달랐다.

“……막아야 해.”

보이지 않는 무언가에 홀린 듯, 넋이 나간 음성으로 뇌까리는 대마도사를 향해 망자들의 군주가 입을 열었다.

“막을 수 없어.”

매직 존슨의 그것과 달리 언데드 킹은 어조는 담담했다.

마치 이미 모든 것을 포기한 것처럼.

하지만 틀렸다.

그 안에는 아직 꺼지지 않은 희망이 담겨 있었다.

비록 한 줌에 불과하지만, 여전히 빛을 잃지 않은 불씨와 같은 희망이.

“적어도 지금 당장은.”

나직한 목소리와 함께, 의식을 잃은 친구를 품에 안은 언데드 킹은 손끝을 타고 전해지는 온기를 느꼈다.

그래.

아직 그들의 희망은 꺼지지 않았다.

또한 이 불씨를 지키는 것만이 지금 그들이 할 수 있는 최선이었다.

“돌아간다. 지금 당장.”

더는 돌이킬 수 없는 일이 벌어지기 전에.

목 끝까지 차오른 그 한마디를 차마 토해 내지 못한 채, 언데드 킹과 매직 존슨은 돌아섰다.

어느덧 먹구름 따위가 아닌, 순수한 어둠으로 물들어가는 하늘이 그들의 머리 위로 차디찬 그림자를 드리우고 있었다.

대격변(大激變).

인류가 지난 수십 년간 잊고 있었던, 세 글자를 모두의 뇌리에 낙인처럼 되새기며.

그리고 잠시 후, 대마도사를 중심으로 발현된 대규모 워프 마법진이 눈부신 섬광과 함께 사라진 이후에도 주인에게 닿지 못한 딱딱한 기계음은 세상 어디에선가 울려 퍼지고 있었다.

삐빅.



- [마력]의 분포도와 농도가 폭등하고 있습니다. 지금 당장 조치를 취하십시오.

- [균열]의 현재 진행도 : 73%

- [균열]이 특정 수치에 도달함에 따라, [몬스터]들의 흉포함과 힘이 크게 증가합니다.

- [균열]의 현재 진행도 : 85%

- [균열]이 특정 수치에 도달함에 따라, [게이트]의 위험성과 [몬스터 웨이브]의 확률이 크게 증가합니다.

- [균열]의 현재 진행도 : 90%



.

.

.



- 퀘스트 성공 요건을 충족하지 못했습니다.

- 임무 : [“흑룡공” 모르고스] 처치 (완료)



[균열]의 진행도 저지 (미완료)



- 메인 퀘스트, [균열과 붕괴]가 실패했습니다.

- 새로운 메인 퀘스트, [예정된 붕괴]가 생성되었습니다.

- 부디, 무운을 빕니다.



* * *



시스템은 거짓말을 하지 않았다.

그리고 시스템의 존재를 모르는 이들조차 그 경고 메시지가 필요 없었을 만큼, 모든 변화는 극적으로 찾아왔다.

혹은, 예고도 없이 들이닥친 약탈자처럼.

“마력 수치가……! 마력 수치가 폭등하고 있습니다!”

“모스크바 일대뿐만이 아닙니다! 상트페테르부르크와 노보시비르스크는 물론, 카잔 지역까지……!”

파도가 파도를 만나 부서지듯, 온 사방에서 비명과도 같은 외침이 서로를 집어삼켰다.

붉게 실핏줄이 선 눈동자와 한껏 도드라진 목의 핏대.

이 끔찍한 혼란의 구렁텅이는 어느 한 장소에만 국한되지 않았다.

한 나라를 좌지우지하는 권력자들이 모인 전 세계의 지하 벙커에서, 국무 회의실에서, 그리고 좁게는 인터넷이 통하는 곳이라면 어디서든 벌어지고 있었다.

그 믿을 수 없는 기현상을 목격한 이들은 비단 전장에 남아 있던 헌터들 뿐만이 아니었다.

화염을 머금은 창날이 모르고스와 함께 모스크바의 하늘을 뒤덮고 있던 짙은 먹구름을 베어 가른 그때, 수십억 인류는 그 틈새 사이로 자신들의 운명을 결정지을 전투를 잠시나마 지켜볼 기회를 얻었다.

그들은 추락하는 악룡의 모습을 보며 전율을, 또 한 번 자신들을 구해 낸 젊은 영웅의 업적에 환호했다.

하나 인류는 몰랐다.

깊은 절망에 빠져 있던 인류에게 비춘 이 한 줄기의 빛이, 그들이 흘린 눈물이 마르기도 전에 사그라지리라는 것을.

구구구궁.

위성으로부터 송출된, 그 불안정한 노이즈 낀 화면을 지켜보던 사람들은 불현듯 무언가 잘못되었음을 깨달았다.

마치 모든 것을 빨아들이는 블랙홀처럼, 이질적일 만큼 선명한 어둠을 흩뿌리는 거대한 기둥.

그것으로 끝이었다.

눈부신. 어둠이라는 단어와는 도저히 함께할 수 없는 그 먹먹한 빛줄기가 하늘을 닫았고 이번에는 두 번 다시 열리지 않았다.

그리고 모스크바를 집어삼킨 어둠은, 증식(增殖)했다.

콰아아아아.

광야를 달리는 한 마리의 말과 같이 어둠은 침묵에 잠긴 세상을 고요히 질주했다.

동, 서, 남, 북.

말발굽이 스쳐 지나간 곳에는 빛이 사라졌다.

모스크바를 비추던 노을빛을 가렸듯이 어둠은 모든 빛을 집어삼켰다.

강렬한 태양도 어둠을. 아니, 그 깊고도 순수한 마력을 뚫지 못했고 하늘의 별도 지워졌다.

마침내 모든 힘을 토해 낸 드래곤 하트가 가루가 되어 흩어진 뒤에도 비로소 만개한 재앙은 이미 세상 곳곳에 포자(胞子)를 흩뿌리고 있었다.

바로 지금처럼.

“코드 레드! 코드 레드! 변이 게이트 발생!”

“변이 게이트? 제기랄, 고작 그따위로 코드 레드라니! 몬스터 웨이브(Monster Wave)만 추려서 보고해!”

상급자의 일갈은 어쩌면 당연했다.

수년 전이었다면 조간신문의 1면과 각종 뉴스 속보로 도배되었을 변이 게이트 발생도, 이제는 ‘따위’가 될 만큼 상황은 긴박하게 흘러가고 있었으니까.

하지만 뒤이어 날아든 외침은, 혼잡하게 뒤섞인 그의 뇌리를 단숨에 비워 낼 만큼 명료하면서도 충격적이었다.

“유, 유라시아(Eurasia) 전역의 모든 게이트가 일제히 변이하고 있습니다.”

“뭐?”

“그중 약 20퍼센트 이상의 게이트가 몬스터 웨이브로 진행될 정도의 수치로…….”

뒷말은 들리지 않았다.

상급자는 갑작스럽게 찾아온 이명(耳鳴)에 사로잡힌 채 침묵했고, 온 힘을 쥐어짜 내어 간신히 한 마디를 내뱉었다.

“지금 즉시 상부에 알려.”

“상부라면 정확히 어디로…….”

대답할 시간도 없었다.

유럽과 아시아 전역에 흩어진 게이트의 숫자는 천 개 이상.

머뭇거리는 부하를 거칠게 밀쳐내며, 상급자는 자신이 이곳의 책임자로 임명된 지 십 년이 넘는 기간 동안 단 한 번도 건드리지 않았던 특수 통신기를 집어 들었다.

오직 한 곳으로만 이어진 직통 연락 수단.

그리고 영원처럼 길게 느껴지는 신호음 끝에 연락이 닿은 수신자는, 숨길 수 없는 떨림이 묻어나오는 목소리로 이 상황을 정리했다.

- 코드 블랙을 발동시키시오.

통화는 그것으로 끝났다.

하지만 1분도 채 되지 않는 이 짧은 통화가 역사에 남을 것이라는 사실을, 두 사람 모두가 알고 있었다.

아니, 코드 블랙이라는 용어의 뜻에 담긴 의미를 아는 사람들이라면 누구나.

그리고 지금 막 수화기를 내려놓은 수신자, 아니 미합중국의 대통령을 화면을 통해 마주하고 있던 이들은 그 극비 정보를 알고 있는 극소수의 인류에 속했다.



- 시작됐군요.

- ……예, 결국.



인종도 성별도 다르지만, 한 나라를 이끈다는 점에서만큼은 동일한 신분을 지닌 이백여 명의 사람들은 한동안 말없이 서로를 바라보았다.

다만 그들 중 유일한 예외가 있다면 오직 한 사람, 유독 젊은 동양인 청년뿐이었다.

일국을 이끄는 지도자도 아니요, 그들처럼 노회하거나 닳고 닳은 정치력을 지닌 것도 아니지만 그는 이 자리에 참석할 수 있는 충분한 권한을 지니고 있었다.

오늘 이 자리에 참석하지 못한 누군가의 뜻을 가장 잘 알고 있는 사람이기도 했으니.

- 시작되었지만, 끝난 것은 아닙니다.

상처가 회복되지 않은 얼굴과 핏물이 달라붙은 머리카락.

그러나 누구도 이와 같은 모습을 한 그에게 예의를 지키지 않는다며 비판하지 않는다.

아니, 감히 할 수조차 없다.

그들이 마주한 저 젊은 청년은 그들을 대신하여 이 세상을 위해 피 흘려 싸운 영웅이다.

인류의 역사에 기록된 그의 조부가, 그리고 오늘 모스크바에서 스러져 간 이들이 그러했듯이.

그리고 지금의 이 자리는 자신의 것이 아니라는 듯, 홀로 서 있던 최민우는 횃불처럼 타오르는 두 눈과 음성으로 말을 이었다.

- 이 전쟁을 끝내는 것은, 우리입니다.

지난 수십 년간 어디에서도 불린 적 없던 그 불길한 암호, 코드 블랙.

아니, 대격변.

돌이킬 수 없는 전쟁은 이미 시작되었고, 영웅은 아직 죽지 않았다.
```

## Final English reading copy

```markdown
# Chapter 1172

“Active volcano” was no exaggeration.

If anything, it fell woefully short.

From the moment the last breath of the evil Dragon that had terrorized the whole world for thousands of years dispersed, an unstoppable catastrophe had been racing along its predetermined course.

An eruption—or an explosion.

It didn’t matter what you called it.

As if this were all it had left to do, the Dragon Heart had, for the first time, slipped beyond its master’s control and vomited everything it had accumulated over an unfathomably long time out into the world.

Using the body of the Dragon that had finally met its end as kindling, it raged more fiercely than a newly awakened active volcano.

*Roooar!*

Before the deafening roar that shook heaven and earth even reached their ears, everyone on the battlefield felt the terrifying shock wave.

The S-rank Hunters were gathering the bodies of the seven Guardians who had found peace with Morgoth’s death—their former comrades.

Thousands of Hunters were chasing monsters that had lost the will to fight and scattered in every direction.

At that enormous, instinct-stirring rumble, they all turned their heads in the same direction as if on cue. Then they froze like statues.

*Fwoooosh.*

A chilling cold carried on the wind. A dark, ashen mist.

And beyond it, a towering pillar of pitch-black darkness, vast beyond comprehension.

“What is that…?”

The solitary groan that slipped from someone’s lips spoke for everyone staring at the scene before them in stunned disbelief.

The evil Dragon—Morgoth—was definitely dead.

They had won here today. The immediate danger was gone.

So why?

Why did that deep, pitch-black darkness feel more frightening than the unprecedented monster that had split the sky and poured its deathly breath down upon the earth?

They already knew the answer.

Their senses and minds, frozen by the icy magical power, simply hadn’t reacted in time to the memory of *that day*—the day that had arrived without a word of warning just a few decades ago.

But two beings realized what was happening first—and more clearly than anyone else.

“…We have to stop it.”

The Lord of the Dead spoke to the Grand Mage, who was muttering as though possessed by something unseen, his voice vacant.

“We can’t stop it.”

Unlike Magic Johnson’s, the Undead King’s tone was calm.

As if he’d already given up on everything.

But that wasn’t true.

There was still hope in his words, however faint—a tiny ember that had yet to lose its light.

“At least, not right now.”

With those quiet words, the Undead King held his unconscious friend in his arms and felt warmth pass into his fingertips.

That was right.

Their hope hadn’t gone out yet.

And protecting that ember was the best they could do now.

“We’re leaving. Right now.”

Before something happened that couldn’t be undone.

Unable to force out the words that had risen to the back of his throat, the Undead King and Magic Johnson turned away.

The sky above them was no longer filled with mere storm clouds. It was turning to pure darkness, casting a cold shadow over them.

The Great Cataclysm.

The three ominous syllables humanity had forgotten over the past few decades were branded into everyone’s minds once more.

And even after the Grand Mage’s large-scale Warp Magic Formation appeared and vanished in a dazzling flash, a hard mechanical beep—one that hadn’t reached its owner—continued to ring out somewhere in the world.

*Beep.*

> **System**
>
> The distribution and concentration of **magical power** are skyrocketing. Take action immediately.
>
> **Current Rift Progress:** 73%
>
> When the **Rift** reaches a certain level, the ferocity and strength of **monsters** increase significantly.
>
> **Current Rift Progress:** 85%
>
> When the **Rift** reaches a certain level, the danger posed by **Gates** and the probability of a **Monster Wave** increase significantly.
>
> **Current Rift Progress:** 90%

.

.

.

> **System**
>
> You have failed to meet the Quest success requirements.
>
> **Mission:** Defeat “Black Dragon Duke” Morgoth (Complete)
>
> Halt the Rift’s progress (Incomplete)
>
> Main Quest Rift and Collapse has failed.
>
> A new Main Quest, Predestined Collapse, has been created.
>
> Good luck.

* * *

The System never lied.

And even people who didn’t know it existed had no need for its warning messages. Every change came dramatically.

Or like a marauder who barged in without warning.

“The magical power levels…! They’re skyrocketing!”

“It’s not just the Moscow area! St. Petersburg and Novosibirsk—and even the Kazan region…!”

Like waves crashing into one another, panicked shouts from all directions swallowed each other up.

Eyes webbed with red veins. Veins bulging along people’s necks.

The pit of this dreadful chaos wasn’t confined to any one place.

It was happening in underground bunkers around the world, where the people who ran entire nations had gathered; in cabinet meeting rooms; and, on a smaller scale, anywhere with an internet connection.

The Hunters still on the battlefield weren’t the only ones who witnessed the unbelievable phenomenon.

When a spearhead wreathed in flames cut through Morgoth and the thick storm clouds covering Moscow’s sky, billions of people had been given a brief chance to watch a battle that would decide their fate.

They shuddered at the sight of the evil Dragon falling, then cheered the young hero who had saved them once again.

But humanity didn’t know that the single ray of light shining on them in their deepest despair would fade before the tears they shed had even dried.

*Rumble.*

Those watching the unstable, grainy feed transmitted from a satellite suddenly realized something was wrong.

A gigantic pillar, spewing darkness so vivid it looked unnatural—like a black hole sucking everything in.

That was all they saw.

Dazzling. That oppressive beam, so bright it seemed impossible to call it darkness, closed the sky. This time, it never opened again.

And the darkness that had swallowed Moscow began to multiply.

*Roooar.*

Like a horse galloping across the wilderness, the darkness raced silently through a world steeped in quiet.

East, west, south, north.

Wherever its hooves passed, the light vanished.

Just as it had blotted out the sunset over Moscow, the darkness devoured every light.

Even the blazing sun couldn’t pierce the darkness. No—the pure, profound magical power. The stars in the sky vanished, too.

By the time the Dragon Heart, having poured out all its strength, crumbled to dust, the catastrophe that had finally blossomed had already scattered its spores across the world.

Just like now.

“Code Red! Code Red! Mutation Gate detected!”

“Mutation Gate? Shit, we’re calling that Code Red now? Report only Monster Waves!”

The superior’s bark was understandable.

A few years ago, the appearance of a Mutation Gate would have covered the front page of morning papers and dominated every breaking-news broadcast. Now the situation was so urgent that even that had become something to dismiss.

But the shout that came next was so clear and shocking that it wiped his jumbled thoughts clean in an instant.

“A-all Gates across Eurasia are mutating at once.”

“What?”

“At least twenty percent of them have reached levels high enough to progress into Monster Waves…”

He didn’t hear the rest.

Seized by the sudden ringing in his ears, the superior fell silent. He squeezed out every last bit of strength and managed to say one thing.

“Tell the higher-ups immediately.”

“Which higher-ups, exactly…?”

There was no time to answer.

There were more than a thousand Gates scattered across Europe and Asia.

Shoving aside his hesitant subordinate, the superior picked up a special communications device he hadn’t touched once in the more than ten years since he’d been appointed head of this place.

A direct line that connected to only one place.

After a signal that seemed to ring on forever, someone answered. The tremor in the recipient’s voice was impossible to hide as they summed up the situation.

“Activate Code Black.”

That was the end of the call.

But both of them knew that this brief conversation, lasting less than a minute, would go down in history.

Or rather, anyone who understood what the words *Code Black* meant knew.

And those facing the recipient on-screen—the person who had just set down the receiver, the President of the United States—belonged to the tiny fraction of humanity privy to that top-secret information.

“It's begun.”

“…Yes. In the end.”

Though they differed in race and gender, these two hundred people shared one thing: they all led a nation. For a while, they looked at one another in silence.

There was only one exception among them: a distinctly young East Asian man.

He wasn’t a national leader, nor did he have the seasoned, battle-hardened political instincts they did. But he had every right to attend this gathering.

He was also the person who best understood the wishes of someone unable to attend today.

“It’s begun, but it isn’t over.”

His face was still healing, his hair matted with blood.

But no one criticized him for appearing before them like that without showing proper respect.

No—they wouldn’t dare.

The young man before them was a hero who had bled and fought for the world in their place.

Just as his grandfather, recorded in humanity’s history, had—and just as those who had fallen in Moscow today had.

As if this place didn’t belong to him, Choi Minwoo stood alone and continued, his voice and eyes burning like torches.

“We will end this war.”

The ominous code name that hadn’t been spoken anywhere for decades: Code Black.

No—the Great Cataclysm.

The irreversible war had already begun, and the hero was not dead yet.
```
