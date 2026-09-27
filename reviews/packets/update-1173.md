<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1173.txt",
      "sha256": "6bcb96d4b7c6876bc34f6c7ff3ec77bdafd039ecee73fc3247a4b48275ab0452",
      "bytes": 13522
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9205f677debb2de6a3a7c4170bafd30ffed6cbca9df570d203dd2ba2e55cb4ee",
      "bytes": 945
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6e9de10cb86d235cdc20ec9eddcaa1edc2bda70493e7635975354014596de37a",
      "bytes": 248454
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "006a5648e57fb716eb549826b266e6e1a954e699991cf3f9b12372699e68a383",
      "bytes": 760
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "8c9d10caac9f1c361facfa97282ee11dc7c5e1e00ba1119b678b7b71dcdadbfe",
      "bytes": 1775
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "29e1dff441ec843df6e4525e48422d2d0ae87c397e2aec4577e5492129128542",
      "bytes": 853
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9888fa34f76fb43f17128ef707d756cad1ad61b59610e952577b341a16beda3f",
      "bytes": 294710
    }
  ],
  "estimated_tokens": 9134
}
-->

# Durable State Update — Chapter 1173

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
1 and safe_through 1173. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1173. Profile updates may replace only one
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
  "chapter": 1173,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1173,
    "continuity_sources": [1173],
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
    "The Great Cataclysm has begun, with darkness spreading from Moscow and magical power surging worldwide.",
    "Gates across Eurasia are mutating simultaneously; at least 20% have reached levels that could lead to Monster Waves.",
    "The System reported Rift progress at 90%; Main Quest Rift and Collapse failed, and Predestined Collapse was created.",
    "The U.S. President ordered Code Black activated.",
    "Jin is unconscious from exhaustion and is being carried by the Undead King as they leave the battlefield.",
    "Choi Minwoo attended a gathering of world leaders and declared that they would end the war."
  ],
  "continuity_sources": [
    1172
  ],
  "open_questions": [
    "What will happen as the Great Cataclysm and Predestined Collapse unfold?",
    "How will Jin fare after his exhaustion-induced unconsciousness?"
  ],
  "safe_through": 1172,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 임꺽정 | **Im Kkeokjeong** |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 테스 | **Tess** | Figure invoked through Taekyung's quotation of “Know thyself.” |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실드 | **Shield** | Spell used by the Doppelganger to create layered barriers. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 팀원 | 팀장 | team member to team leader | Team Leader Kim | casual, familiar, and dialectal | Team members use forms including 햄 and informal greetings when addressing Kim. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 팀장 | 팀원 | freelance team leader to subordinate team member | asshole/punk | insulting-casual | The Team Leader addresses the subordinate with 새꺄 and 인마 while joking and complaining over drinks. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1172
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 1156
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter and veteran tank in the Peace Guild; after recovering from the Black Hunters’ attack and having both arms reattached, he continues as a Hunter while nearing the end of rehabilitation.
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1172
- **Aliases:** None
- **Role:** Morgoth was a Dragon Lord and sovereign of a vast palace, slain by Jin Taekyung when Jin pierced his Dragon Heart.
- **Personality:** Composed and intellectually curious, Morgoth spent millennia seeking God and regards powerful beings as sources of amusement, willing to aid a worthy rival when it promises greater future entertainment.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth returned the Skeleton King to Jin to help him grow stronger and commands seven soul-stolen S-rank Hunters as Guardians.

## Korean source

```text
＃1173화



인간은 학습의 동물이다.

물론 종종 중요한 것들을 망각하곤 하지만, 무엇 하나 배우는 것 없이 매번 잊기만 했다면 현재의 인류는 존재할 수 없었을 것이다.

그들은 언제나 조금씩 배워 나갔다.

그렇게 수백만 년에 걸쳐 끊임없이 발전했다.

불을 다루고, 돌을 깎으며, 마침내 구름 위 무한한 공허의 세상까지 엿보았다.

그리고 이처럼 아득한 세월에 걸쳐 위대한 문명을 이룩한 인류가 대격변(大激變)이라 명명된 그 끔찍했던 대재앙을 잊기에, 지난 삼십여 년은 너무나도 짧은 시간이었다.

위이이이잉-!

강렬한 사이렌 소리가 도시를, 아니 온 세상을 뒤덮었다.

얼어붙은 극동의 땅에서 솟구쳐 오른 마력이 하늘을 물들이는 속도보다 빠르고, 그와는 비교도 할 수 없을 정도로 다급하게.

당연하게도 가용할 수 있는 모든 인력과 자원이 아낌없이 퍼부어졌다.

각 정부는 계엄령과 동시에 군대를 동원하여 자국민들을 안전 구역으로 대피시켰고, 그 일련의 상황은 매우 신속하고 간결하게 진행되었다.

불행인지 다행인지, 모르고스의 등장 이후 공포에 사로잡힌 사람들은 이미 대피를 완료했거나 당장이라도 대피할 모든 준비를 끝마친 상태였으니까.

하지만 아직 푸른 하늘 아래 놓인 이들이라 할지라도, 그들 앞에 놓인 위험의 크기는 결코 줄어들지 않았다.



- 동서쪽 3.2km 밖에서 몬스터 웨이브 발생!

- 해당 위치와 규모 전송하겠음. 즉각 출동 바람!



시스템은 이번에도 옳았다.

균열의 단계를 넘어 붕괴가 시작되었다.

걷잡을 수 없는 마력의 폭주에 세상 곳곳에 흩어진 무수한 게이트는 하나둘씩 그 컴컴한 아가리를 벌렸고, 저주받은 세상에서 뛰쳐나온 몬스터들은 더욱 강해진 힘과 흉포함으로 날뛰었다.

바로 지금처럼.

드드드득.

저 멀리서부터 전해지는 진동에, 지면이 부르르 몸을 떨었다.

제 몸집보다 큰 타워 실드(Tower Shield)의 손잡이를 으스러질 듯이 움켜쥐고 있는 누군가의 손 역시도.

턱.

불현듯 어깨에 닿은 묵직한 감촉에, 불에 덴 사람처럼 화들짝 놀랐던 청년은 이내 안도의 한숨을 내쉬었다.

“……팀장님.”

“자식, 쫄기는.”

밤송이 같은 수염 사이로 이를 드러내며 씩 웃는 중년인의 모습에 순간적으로 부아가 치밀만도 했지만, 청년은 마른침을 꿀꺽 삼키며 대답했다.

“아, 아닙니다.”

“아니긴, 딱 보면 알지. 그냥 솔직하게 말해.”

“그, 사실 조금은.”

“이놈 보게. 명색이 헌터라는 놈이 싸우기 전에 겁부터 집어 먹어?”

“……죄송합니다.”

순식간에 울상이 된 청년의 모습에 짐짓 엄한 표정을 짓고 있던 중년인은 물론, 주위의 헌터들까지 피식피식 실소를 흘렸다.

“팀장아. 그러다 애 울것다. 그만혀.”

“어허, 사내놈이 뭐 이런 걸로 울어. 다 한 번씩 겪어 보는 거지. 나 때는…….”

“염병, 그놈의 라떼 또 나왔네. 허구헌날 모카 골드만 처먹는 양반이.”

“얼마 전에 바꿨어, 화이트 골드로.”

“그건 잘했네.”

“고마워.”

“넣어 둬. 뭘 이런 것 가지고.”

나이 지긋한 아저씨들이 주고받는 대화를 듣고 있던 청년은 머리가 터질 것 같았다.

이곳은 어디이며 난 누구인가.

무조건 긴장해야만 하는 이 심각한 상황에서, 듣는 것만으로도 맥이 탁 풀려 버리는 저 대화의 흐름은 무엇인가.

‘나, 혹시 팀 잘못 고른 건가.’

물론 문득 청년의 뇌리를 스친 그 생각에는 상당한 어폐가 있었다.

애초부터 청년에게는 선택권 자체가 없었으니까.

그리고 불과 스무 살밖에 되지 않은 이 청년을 무려 평균 연령 41.5세에 달하는 고인물 파티로 ‘집어’ 온 장본인이 불쑥 입을 열었다.

“어때?”

“예?”

“이제 좀 낫지?”

잠시 눈을 깜빡이던 청년이 이내 대답했다.

조금 전과는 달리 훨씬 차분하고, 더 얼떨떨해진 목소리로.

“어, 예.”

“하도 얼어 있길래 그냥 장난 한번 쳐 봤다. 이 나이 처먹고 허튼 짓거리 한다고 너무 뭐라 하지는 말고.”

“아, 아닙니다. 그런 생각은 절대 안 했습니다.”

“뭐 그거야 어떻든 이해해. 처음에는 원래 떨리는 게 당연한 거거든. 신경도 날카로울 수밖에 없지.”

청년의 어깨를 격려하듯 두드린 중년인이 소리내어 웃었다.

어지간한 흉악범도 한 수 접고 들어갈 인상이라는 게 믿어지지 않을 만큼 사람 좋아 보이는 웃음.

아마도 그 때문이었을 것이다.

이 고인물 파티에서 입 벙긋할 수도 없는 위치인 청년이, 조금 용기를 내기로 마음먹은 것은.

“그, 한 가지 여쭤봐도 됩니까?”

다행히도 앞서 느낀 그 웃음은 흉악범의 일반인 코스프레가 아니었다.

중년인이 선선히 고개를 끄덕이자, 청년이 조심스럽게 말을 이었다.

“왜 굳이 저를…….”

몇 음절 내뱉지도 못하고 조금씩 흐려지는 말꼬리.

하지만 말에 담긴 뜻을 알아차리기에는 충분했고, 중년인은 생각할 필요도 없다는 듯이 대답했다.

“닮았거든.”

“닮았다는 건…….”

“그래. 내가 아는 사람이랑.”

사실, 이틀 전 처음 본 청년의 모습은 중년인이 숱하게 봐왔던 초짜들의 전형이었다.

잔뜩 굳어 있는 팔과 다리. 바짝 마른 입술과 초조하게 굴러가는 눈동자.

그러나 단지 그뿐만이었다면, 굳이 자신의 목숨을 맡길 만한 팀원으로 그를 선택하진 않았을 것이다.

“훈련하고 있는 거, 다 봤다.”

“훈련이요?”

“응. 아주 열심히 하던걸. 필사적이라고 느껴질 만큼.”

“하지만 그건…….”

“알아, 너뿐만 아니라 그 자리의 모든 신입들이 하고 있던 거였지. 그렇게라도 눈에 띄어서 조금이라도 괜찮은 팀에 들어가려고.”

맞다.

이틀 전, 두 사람이 처음 만난 그곳에는 이제 막 지역 헌터 훈련소를 수료한 신입들 수백 명이 있었고 팀 배정을 기다리며 자신을 보여 주고 있었다.

조금이라도 생존률이 높은 팀으로 가기 위해서.

이전처럼 더 많은 돈을 벌기 위해서가 아니라, 그 무엇과도 바꿀 수 없는 목숨을 지키기 위해서.

그리고 청년은, 그 많고 많았던 신입 중 유일하게 자리를 비웠던 사람이었다.

“그때 어디에 있었지?”

“밖에 있었습니다. 사람 없고, 좀 넓은 곳을 찾아야 했거든요.”

“이유는?”

“그야, 훈련을 해야 했으니까요.”

“다른 사람들처럼 본인 어필 겸 그곳에서 했어도 됐었을 텐데? 관계자들이 모니터 룸 통해서 대기실까지 지켜보고 있는 건 이미 일반인들 사이에서도 모르는 사람이 없는 이야기고.”

“그건 맞지만…….”

머뭇거리던 청년이 말을 이었다.

“그곳에서는 제대로 된 훈련이 불가능할 것 같았습니다.”

당연한 이야기다.

그곳은 정식 테스트를 치르는 트레이닝 룸도 아닌 대기실. 공간이 상당히 넓다고는 해도, 그 많은 사람이 날붙이를 휘둘러 대면 집중력이 흐트러질 수밖에 없으니까.

그러나 청년만큼은 예외였다.

훈련이라는 행위 자체는 같을 수 있었지만, 그 목적은 전혀 달랐다.

그는 진심을 다해 노력하고 있었다.

좋은 팀에 들어가기 위해서가 아니라, 그렇게라도 조금이나마 강해지기 위해서.

그리고 그날, 청년의 뒤를 몰래 뒤쫓아갔던 중년인은 아무도 없는 공터에서 홀로 훈련에 매진하고 있는 그의 뒷모습에서 몇 년 전의 기억을 떠올릴 수 있었다.

“그 녀석도 그랬어.”

“네?”

“아까 말했던 그 친구 말이야. 헌터 인력 사무소에서 마주친 녀석이었지. 너처럼 젊었, 아니 어렸어. 딱 봐도 초짜였는데 곧 못 보게 될 얼굴이구나 싶었지.”

“그렇게 생각하신 이유가 있었습니까?”

“F급이었거든.”

“아.”

F급.

그 짧은 단어에 청년은 납득했다.

헌터계의 불가촉천민.

등급 뒤에 UCK를 붙여도 전혀 이질감이 없다는 밑바닥 아래의 지하.

오죽하면 청년도 생애 첫 등급 측정을 하던 날, 모니터에 선명히 뜬 E를 보며 이런 생각을 했을 정도다.

아, 그래도 F는 아니라서 다행이라고.

하지만 청년이 그랬듯, 중년인이 말하는 ‘그 녀석’도 남들과는 다른 부분이 있었다.

“처음에는 몰랐지. 그후로 반년 넘게 보게 될 줄은.”

“그래도 다행히 일거리가 잡히긴 한 모양이네요.”

“무슨 소리야? F급이었다니까. 나야 그래도 나름 짬바도 있고 인연이 있어서 가끔 짐꾼으로라도 불러 주는 곳이 있었지만 F급 신입? 어림도 없지.”

“하지만 방금은…….”

“봤다고 했지. 같이 일했다고는 안 했어.”

청년이 눈을 동그랗게 떴다.

“그럼 인력 사무소에 나오기만 한 겁니까? 일도 없는데?”

“그래, 거의 반년 내내 그랬지. 단 하루도 안 빼놓고, 꼭두새벽부터 저녁까지.”

아마 보통 사람이면 그쯤 해서 관뒀을 것이다.

그러니까, 어디까지나 보통 사람이었다면.

“녀석은 아니었어. 멀쩡한 소파를 놔두고 사무소 뒷산까지 올라가서 매일 같이 죽어라 훈련만 했지. 내가 이틀 전에 봤던 어떤 놈처럼.”

“……!”

“우선 번호표부터 뽑고, 훈련하고, 순번 돌아오는 시간 맞춰서 돌아오면 매번 그랬듯이 빠꾸 먹고, 다시 번호표 뽑고, 훈련하고……. 게이트는 입구 근처도 못 가봤는데 사무소 문 닫을 시간만 되면 하루 다섯 탕 뛴 사람보다 더 지쳐 있었지.”

멍하니 이야기를 듣고 있던 청년이 솔직히 말했다.

“저였으면 도중에 멘탈 터졌을 것 같습니다.”

“그렇지? 와중에 참 웃긴 게, 얼굴은 항상 죽상에다가 입 모양은 씨발씨발 거리고 있는데 훈련은 내가 본 누구보다 열심히 하더라고. 그 친구는 할 만해서 한 게 아니라 힘든데도 한 거야. 그것도 매일같이.”

“굉장하네요.”

“그래, 굉장한 친구야.”

“아니, 팀장님도요.”

“응?”

“반년 동안 매일 같이 보셨다는 건, 팀장님도 그분처럼 하셨다는 거 아닌가요?”

잠시 침묵하던 중년인이 너털웃음을 흘렸다.

“맞네, 흐흐. 하지만 난 절대 그 친구처럼은 못 될 거야.”

“저는 아니라고 생각합니다. 이미 대단하신걸요.”

그저 아부를 위한 말이 아니다. 

중년인이 청년의 모습을 지켜보았듯이, 청년 역시 상관의 행동을 빠짐없이 지켜보고 있었다.

지켜보았다고 하기에는 고작 이틀밖에 되지 않았지만, 그가 충분히 존경할 만한 사람이라는 사실만큼은 차고 넘칠 만큼 느끼고 있었다.

“저는 팀장님처럼 되는 게 꿈입니다.”

“……어, 나?”

“예. 인품, 실력. 그리고 노력까지 갖추셨잖아요. 예전에 팀장님과 관련된 뉴스 기사도 본 적 있습니다. 제목도 기억나요. F급에서 B급까지. 누구보다 가팔랐던 어느 헌터의 인생 굴곡.”

잊고 싶은 흑역사를 뒤집어 까 버리는 청년의 말에 곳곳에서 폭소가 터졌고, 중년인은 붉게 달아오른 얼굴로 덥수룩한 수염을 긁적였다.

그리고 더듬거리는 목소리로 막 입을 열려던 그때, 돌연 얼굴을 굳혔다.

구구구구궁.

십여 분 전보다 더욱 강해진, 아니 이제는 발바닥뿐만이 아니라 온몸으로 전해지는 진동.

‘온다.’

모두가 동시에 느꼈고, 새삼 깨달았다.

자신들이 그 누구보다 죽음과 가까이 서 있음을.

하지만 결코 물러설 수 없었다.

그들은 인류 최후의 저지선이니까.

오직 이 순간을 위해, 지금의 능력을 선물 받은 것일 테니까.

“이봐, 신입.”

“예, 팀장님.”

어느덧 등 뒤에서 들려오는 부름에 청년은 마른 음성으로 대답했다.

언제부터인가 그의 손도, 타워 실드도 더는 떨리지 않았다.

“고맙다.”

“예?”

“나도 누군가의 꿈이라고 해 줘서, 그게 고맙다고.”

이 순간에도 웃음을 잃지 않은 중년인, 아니 아레스 길드 32팀장 임꺽정은 투구를 깊게 눌러쓰며 생각했다.

‘그 친구처럼 될 수는 없어도, 나 역시 헌터지.’

그리고 수백여 미터 밖에서 피어오른 먼지 구름을 응시하며, 온 힘을 다해 부르짖었다.

“포메이션-!”

그 순간.

하늘을 찌를듯한 함성에 맞춰, 임꺽정의 가슴팍에 달린 통신기가 메시지를 수신했다.

- 전 헌터들에게 알린다. 알파, 알파가 깨어났다.

칼날 같은 바람이 전장을 휘감고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1173

Humans are animals that learn.

Of course, they often forget important things. But if they forgot everything without ever learning a thing, humanity as we know it wouldn’t exist.

They kept learning, little by little.

And over millions of years, they developed without end.

They learned to use fire and chip away at stone, until at last they glimpsed the boundless world of empty space above the clouds.

But for humanity, which had built a great civilization over such an unfathomable stretch of time, the past thirty-odd years were far too short to forget the horrific catastrophe named the Great Cataclysm.

*Wheeeeeee!*

A blaring siren swept over the city—no, over the entire world.

Faster than magical power rising from the frozen lands of the Far East could stain the sky, and with an urgency that couldn’t even be compared to it.

Naturally, every available person and resource was thrown into action without restraint.

Governments declared martial law and deployed the military to evacuate their citizens to safe zones. The whole process moved swiftly and efficiently.

For better or worse, ever since Morgoth appeared, people had been gripped by fear. They’d already evacuated, or made all the preparations to do so at a moment’s notice.

But even those still beneath the blue sky faced no less danger.

—Monster Wave detected 3.2 kilometers away to the east and west!

—Sending location and scale. Deploy immediately!

The System was right again.

The rift stage was over. The Collapse had begun.

As magical power spiraled out of control, countless Gates scattered around the world began opening their dark maws, one after another. Monsters poured out of that cursed world, rampaging with greater strength and savagery.

Just like now.

*Rumble, rumble.*

The ground trembled at the vibrations coming from far away.

So did the hand gripping the handle of a Tower Shield bigger than its owner, tight enough to crush it.

*Thump.*

At the heavy touch that suddenly landed on his shoulder, the young man jumped as if burned. Then he let out a sigh of relief.

“…Team Leader.”

“You’re jumpy, kid.”

The middle-aged man grinned, showing his teeth between bristly whiskers. The young man might have been annoyed for a moment, but instead he swallowed hard and answered.

“N-no, I’m not.”

“Sure you are. It’s obvious. Just be honest.”

“Well, the truth is, a little.”

“Look at this guy. You call yourself a Hunter, and you’re already scared before the fight’s even started?”

“…I’m sorry.”

The young man’s face fell in an instant. The middle-aged man, who’d been putting on a stern expression, and the Hunters around them all chuckled.

“Team Leader, you keep that up and the kid’ll cry. Give it a rest.”

“Now, now. A grown man shouldn’t cry over something like this. We’ve all been through it once. Back in my day…”

“Jesus, here comes his ‘back in my day’ latte again.[^1] And all he ever drinks is Mocha Gold.”

[^1]: The Korean phrase for “back in my day” sounds like “latte,” setting up the instant-coffee joke.

“I switched a while ago. White Gold now.”

“Good for you.”

“Thanks.”

“Don’t mention it. It’s nothing.”

Listening to the old guys chatter, the young man felt like his head was about to burst.

*Where am I, and who am I?*

In this serious situation, where he should have been on edge, what was this conversation that made him lose all his nerve just listening to it?

*Did I pick the wrong team?*

Of course, there was a serious flaw in that thought.

The young man hadn’t had a choice in the first place.

And the person who’d “picked up” this twenty-year-old and brought him into a veteran party with an average age of 41.5 suddenly spoke.

“How about it?”

“Huh?”

“Feeling a little better?”

The young man blinked for a moment, then answered.

His voice was much calmer than before, but even more bewildered.

“Uh, yes.”

“You were so stiff I figured I’d mess with you a little. Don’t be too hard on me for fooling around at my age.”

“N-no, not at all. I’d never think that.”

“Good. But I understand either way. It’s natural to shake at first. Your nerves are bound to be on edge.”

The middle-aged man patted the young man’s shoulder encouragingly and laughed out loud.

It was a friendly laugh, hard to believe coming from a face that could make even the most vicious criminal think twice.

Maybe that was why the young man, who was at the bottom of the pecking order in this veteran party, decided to work up the courage to speak.

“Um, could I ask you something?”

Thankfully, that laugh hadn’t come from a vicious criminal pretending to be an ordinary person.

When the middle-aged man readily nodded, the young man cautiously continued.

“Why did you choose me…”

His words trailed off after only a few syllables.

But that was enough for the middle-aged man to understand. He answered without a moment’s hesitation.

“You reminded me of someone.”

“Reminded you of someone…?”

“Yeah. Someone I know.”

Truth be told, when the middle-aged man first saw the young man two days ago, he’d looked like every other rookie he’d ever seen.

Arms and legs locked stiff. Lips parched. Eyes darting around anxiously.

But if that had been all there was to him, the middle-aged man wouldn’t have chosen him as a teammate to entrust with his life.

“I saw you training.”

“Training?”

“Yeah. You were working really hard. Hard enough to look desperate.”

“But that was…”

“I know. All the rookies there were doing it. Trying to stand out so they’d get into a decent team.”

That was right.

Two days ago, when the two of them first met, hundreds of rookies who’d just graduated from the regional Hunter training center had gathered there, showing off as they waited for their team assignments.

They wanted to get into a team with a better chance of survival.

Not to earn more money like before, but to protect the one thing they couldn’t trade for anything: their lives.

And of all those rookies, the young man had been the only one who wasn’t there.

“Where were you then?”

“Outside. I needed to find somewhere without people, somewhere with a little space.”

“Why?”

“Because I had to train.”

“You could’ve done it there, like everyone else, and used it to show off, couldn’t you? Everyone knows the people in charge watch the waiting room through the monitor room.”

“That’s true, but…”

The young man hesitated, then continued.

“I didn’t think I could train properly in there.”

Naturally. It was a waiting room, not a training room for the official test. It was fairly spacious, but with so many people swinging around bladed weapons, it would have been hard to concentrate.

But the young man was different.

The act of training might have been the same, but his reason for doing it was entirely different.

He was working with all his heart.

Not to get onto a good team, but to become even a little stronger.

That day, after secretly following the young man, the middle-aged man had watched him train alone in an empty lot. The sight brought back a memory from a few years ago.

“That guy was like that, too.”

“Who?”

“The friend I mentioned earlier. I ran into him at a Hunter manpower office. He was young, like you—no, younger. A rookie at a glance. I figured I wouldn’t be seeing him for long.”

“Was there a reason you thought that?”

“He was F-rank.”

“Ah.”

F-rank.

At the word, the young man understood.

An untouchable in the Hunter world.

So far beneath the bottom that you could tack UCK onto the F and it would fit perfectly.

The young man had even thought the same thing on the day he got his first rank assessment, when he saw the E on the monitor:

*At least I’m not F-rank.*

But just as the young man was different, so was the “guy” the middle-aged man was talking about.

“At first, I didn’t know I’d keep seeing him for over half a year.”

“At least he managed to find work, then.”

“What are you talking about? I said he was F-rank. I had some experience and connections, so there were places that’d occasionally call me in as a porter. But an F-rank rookie? Not a chance.”

“But you just said…”

“I said I saw him. I didn’t say we worked together.”

The young man’s eyes widened.

“So he just kept showing up at the manpower office? Even when there was no work?”

“Yeah. For nearly half a year. From the crack of dawn until evening, without missing a single day.”

Most people would’ve quit by then.

That is, if they’d been ordinary people.

“He wasn’t. He’d leave a perfectly good sofa behind and climb the hill behind the office, training like hell every day. Like some guy I saw two days ago.”

“...!”

“He’d take a number, train, come back when his turn was up, get turned down like always, take another number, train again… He never even got near a Gate, but by closing time at the office he’d be more exhausted than someone who’d done five runs in a day.”

The young man listened, dazed, then answered honestly.

“I think I would’ve lost it halfway through.”

“Right? And here’s the funny part: his face always looked miserable, and his mouth was going *fuck, fuck, fuck*, but he trained harder than anyone I’d ever seen. He wasn’t doing it because it was easy. He did it even though it was hard. Every single day.”

“That’s incredible.”

“Yeah. He was an incredible guy.”

“No, I mean you, too, Team Leader.”

“Me?”

“If you saw him every day for half a year, doesn’t that mean you were doing the same thing he was?”

The middle-aged man was quiet for a moment, then let out a hearty laugh.

“You got me. Heh. But I’ll never be like that guy.”

“I don’t think that’s true. You’re already amazing.”

It wasn’t just flattery.

Just as the middle-aged man had watched the young man, the young man had been watching his superior closely, too.

He’d only known him for two days, so it was a stretch to say he’d watched him for long. But he’d seen more than enough to know he was someone worth respecting.

“My dream is to become like you, Team Leader.”

“...Me?”

“Yes. You have character, skill, and you work hard. I even saw a news article about you once. I remember the headline: *From F-rank to B-rank: A Hunter’s Life of Extraordinary Ups and Downs.*”

The young man had dredged up an embarrassing chapter of his life that the middle-aged man would rather forget. Laughter broke out around them, and the middle-aged man scratched his bushy beard, his face turning red.

Just as he started to stammer out a reply, his expression suddenly hardened.

*Rrrrrumble.*

The vibrations were stronger than they’d been ten minutes ago. Now they weren’t just coming up through the soles of their feet; they were shaking their whole bodies.

*It’s coming.*

Everyone felt it at once, and realized anew how close they were to death.

But they couldn’t back down.

They were humanity’s last line of defense.

They must have been given their powers for this very moment.

“Hey, rookie.”

“Yes, Team Leader.”

The young man answered hoarsely when the call came from behind him.

At some point, his hand and his Tower Shield had stopped shaking.

“Thanks.”

“What?”

“Thanks for saying I’m someone’s dream.”

Even now, the middle-aged man—Im Kkeokjeong, Team Leader of Ares Guild’s Team 32—hadn’t lost his smile. He pulled his helmet down low and thought:

*I may not be able to become like that guy, but I’m a Hunter, too.*

Then he fixed his gaze on the dust cloud rising a few hundred meters away and shouted with all his might:

“Formation—!”

At that moment, as a roar pierced the sky, the communicator on Im Kkeokjeong’s chest received a message.

—All Hunters, listen. Alpha—Alpha has awakened.

A blade-sharp wind swept across the battlefield.
```
