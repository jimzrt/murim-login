<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1083.txt",
      "sha256": "a5cd798993c2c9099d0a0f2f60b1952c2cbd4afa2d52f352268923d370cca8cb",
      "bytes": 12554
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d1449be6b540116c88d7d3d8e1bfe8ad4240741100377cc0d46b94c730a164e5",
      "bytes": 1569
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cfb59cce7da7cabd0977b42265a02ef36c9d9d126e66ab5841bf51eff3ac3be8",
      "bytes": 243330
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8ee70186a227cb9039871a47e9cf14b45b09150f8b4842607b2eef134434560b",
      "bytes": 760
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "2e7efe332e1e9f480252bfc141a28ccfb0249588b05562091de2963d25a043d8",
      "bytes": 699
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "58a26ebc062bb2491d81493f3106d1710fa81b7f7ba862172b209911bfd6e6ec",
      "bytes": 286576
    }
  ],
  "estimated_tokens": 8735
}
-->

# Durable State Update — Chapter 1083

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
1 and safe_through 1083. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1083. Profile updates may replace only one
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
  "chapter": 1083,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1083,
    "continuity_sources": [1083],
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
    "Xining is Qinghai’s capital and a stronghold against Dark Heaven; crowds from across the province have gathered there.",
    "Xining’s food stores can sustain its people for at most fifteen days.",
    "Hak Su is Cheongheoja’s Senior Disciple, Hak Woo’s senior brother, and a possible successor to Kunlun Sect leadership.",
    "Taekyung believes the Lord of Heaven does not want him killed, but does not know why.",
    "The black-robed captive survived interrogation and treatment and can now speak; Mujin is to talk with him.",
    "Hak Eui investigated Qinghai’s affairs and presented his case to the gathered leaders.",
    "The City Lord of Qinghai and around a dozen other criminals were publicly executed; some in the crowd desecrated their bodies.",
    "Taekyung received a missive from the Murim Alliance in Henan.",
    "Potala Palace in Tibet has joined forces with Dark Heaven.",
    "Pa Ryun and Tae Gunak are working together on a plan to take control of the Yangtze in two days."
  ],
  "continuity_sources": [
    1081,
    1082
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "What did the Murim Alliance’s missive say, and who instructed Pa Ryun and Tae Gunak?"
  ],
  "safe_through": 1082,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 파륜     | **Pa Ryun**        |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 보상               | **Reward**                     |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쟁자수 | **caravan porter** | Porters who lead the escort caravan's horses and carts. |
| 살인멸구 | **Silencing the Witnesses** | Killing witnesses to prevent a secret from being exposed. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 인의대협 | **Great Hero of Benevolence and Righteousness** | Flattering epithet Mungyeong uses for Mu Song. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1082
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 1058
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

## Korean source

```text
1083화




선(善)과 악(惡)이 처음으로 갈라선 그 순간부터, 세상에는 결코 사라지지 않는 것들이 탄생했다.

도적이라 불리는 자들 또한 그중 일부다.

재물을 강탈하거나 훔치고, 혹은 그 과정에서 타인의 생명마저 해치는 그들은 까마득한 과거부터 늘 존재해왔고 결코 뿌리 뽑을 수 없는 종류의 인간군상이었다.

빛이 존재하는 곳에 그림자가 드리워지는 것처럼, 그것은 사람이라면 누구나 느끼는 오욕칠정(五慾七情)의 감정을 제거하지 않는 이상 멈출 수 없는 수레바퀴였으니까.

아마도 그래서였을 것이다.

사람들이 마침내 이 불쾌한 순리를 인정하기로 결심한 것은.

끊을 수 없는 고리를 부수기 위해 애꿎은 피를 흘리는 것보다, 서로 간의 대화를 통하여 어느 정도 공생(共生)하는 관계를 묵인하게 된 것은.

하지만 제법 긴 시간 동안 이어져 왔던 그 공생의 시간도, 이제는 끝을 향해 달려가고 있음을 사람들은 직감하고 있었다.

“이봐들, 그 소식 들었나?”

불길함은 늘 희망보다 한 걸음 앞질러 나아가는 법.

그중에서도 산과 강에 인접한 현읍(縣邑)의 백성들은 심상치 않은 분위기를 피부로 느끼고 있었다.

“지난밤에 갑자기 밀어닥친 토사(土砂)로 인해 산 너머로 가는 통행로가 완전히 막혔다는군. 약초꾼들 말로는 평범한 산사태가 아닌 것 같다던데…….”

“평범한 산사태가 아니라니, 그게 무슨 소린가?”

“나야 오십 평생 쟁기질만 해 온 놈이라 잘은 모르지만, 그네들 눈에는 훤히 보이지 않나.”

“그래서?”

“토사에 휩쓸려 온 나무들의 잘린 단면을 슥 보아하니, 이게 확 꺾이고 부러진 게 아니라 어째 누가 도끼질이라도 깔짝거린 것 같다 이 말일세. 애당초 산사태의 징조도 딱히 없었고.”

“잠깐, 그렇다는 건.”

“누구 짓이겠나. 귀신의 조화가 아닌 이상 십중팔구 그 염병할 산적 놈들이겠지.”

“쉿. 염병할 산적 놈들이라니. 말조심하게. 그럴 리는 없겠지만 만에 하나 녹림맹도들의 귀에 들어가기라도 하면…….”

“녹림맹도는 얼어 죽을. 산적 놈들을 산적이라고 부르는데 뭐가 문제라고. 산길 한번 넘어갈라치면 이틀 치 품삯을 뜯어 가는 날강도들 아닌가?”

“어허, 이 사람이 그래도. 심정은 이해하지만 지금은 녹림맹 역시 엄연한 아군일세. 황명에 따라 무림맹과 손잡고 서쪽의 흉적(凶賊)들과 맞서는.”

“저 친구 말이 옳네. 산적들이 질 나쁜 놈들인 거야 세상 사람들이 다 알지만, 그렇다고 암천처럼 아주 막 나가는 종자들은 아니야. 우리가 코흘리개였을 때도 한번 비슷한 일이 있었지 않나.”

“맞지. 물론 그때는 암천이 아니라 마교였지만, 여하튼 당시 무림맹과 손을 잡아서 맞서 싸운 것으로 기억하네. 그 후에 녹림맹이 만들어진 거고.”

제법 나이가 지긋해진 중년인들에게 있어 정마대전(正魔大戰)은 잊을 수 없는 유년 시절의 기억 중 하나다.

비록 일반 백성들은 별다른 피해를 입지 않았으나, 사악한 교리를 믿는 살인귀들이 중원을 침범했다는 소식에 온 천하가 들썩이지 않았던가.

그렇기에 녹림맹을 둘러싼 이 석연치 않은 불길한 소문 속에서도, 사람들은 반신반의할 수밖에 없었다. 

그들이 기억하는 녹림맹은 그래도 비교적 말이 통하는 도적놈들이 모여 만든 집단이자, 일상의 한 조각이 되어 버린 지 오래였으니까.

하지만 이에 관한 소문은 그뿐만이 아니었다.

“이틀 전. 어두컴컴한 밤에 우리 마을을 지나갔던 그 작자들 기억나나?”

“알지. 그 외지인들 말하는 것 아닌가. 청화(靑花) 표국이라고 했던 것 같은데.”

“그래. 그자들. 나도 웬 황소처럼 커다란 쟁자수 한 놈이 그 무거운 깃발을 눈 하나 깜짝 안 하고 들고 있길래 깜짝 놀랐었지. 얼굴은 덩치보다 더 살벌해서 두 번 놀랐고.”

“그런데 그 얘기는 갑자기 왜? 상단이며 표국이며 달에 몇 번씩 오가니 별다를 것도 없을 텐데.”

주위 사람들의 의아한 반응에, 맨 처음 이야기를 꺼냈던 중년인이 한껏 목소리를 낮추며 입을 열었다.

“왔지. 오긴 왔는데……결국 어디로 갔느냐가 중요한 거 아니겠나.”

“뭐?”

“직접 보게. 오늘 새벽에 약초꾼 홍씨가 토사에서 끄집어낸 걸세.”

그리고 다음 순간, 중년인이 품에서 꺼내어 펼친 천 뭉치를 확인한 사람들은 눈을 부릅뜰 수밖에 없었다.

정확히는, 때마침 말라붙은 흙과 모래알이 떨어지면서 드러난 두 글자를 보며.

청화(靑花).

“이, 이건.”

“그 몸집 큰 쟁자수를 기억한다면 놈이 들고 있었다던 깃발도 알겠군. 맞네, 그가 들고 있던 표기(鏢旗)일세.”

사람들은 서로를 바라보며 마른 침을 꿀꺽 삼켰다.

깃발은 어느 집단에서나 커다란 상징적인 의미를 가지는 법.

군대에서 대장기(大將旗)를 목숨을 바쳐 지키는 것처럼, 그들이 아는 상단이나 표국 역시 자신들의 깃발을 하나의 자긍심으로 여겼다.

그런데 불과 이틀 전, 깊은 밤에 산길을 지나갔을 표국의 깃발이 토사물 속에서 발견되었다면.

그리고 하루 만에 미심쩍은 산사태로 인해 유일한 통행로가 막혔다면.

“이게 무엇을 뜻하는 것인지, 대충 감이 오지 않나?”

“……설마?”

“설마가 아니고 역시야. 녹림맹, 그 빌어먹을 산적 놈들이 뭔가 일을 벌인 것이 분명하네. 모종의 이유로 살인멸구(殺人滅口)를 하고 산사태를 빙자해 은폐하려 한 거야.”

일순간 숨 막히는 침묵이 좌중을 짓눌렀다.

어느덧 선명하게 실체화된 불안감이, 앞뒤가 딱딱 들어맞는 현재의 상황이 그들을 숨통을 옥죄이고 있었다.

“하, 하지만 저들이 뭐가 아쉬워서 그런 일을 벌이겠나. 과거에도 마교와 맞서 싸웠고, 그에 대한 보상으로 장강의 수적들처럼 맹(盟)까지 자처하며 나름대로 호의호식할 수 있게 되었는데.”

누군가가 애써 불안감을 물리치기 위한 말을 내뱉었지만, 돌아오는 음성은 무섭도록 현실적이었다.

“재작년 추수 때, 자네가 했던 말 기억하나?”

“재작년? 갑자기 그게 무슨.”

“아쉬워했었네. 근 십 년 중에서도 최고의 대풍(大豐)이었는데도 이 정도로는 안 된다며 한숨을 내쉬었었지. 한데 저놈들이라고 다를까?”

“……!”

“뻔하지. 농사나 짓는 우리도 욕심이 있는데, 남의 것을 빼앗는 걸 업으로 삼는 놈들이면 어떻겠나.”

비록 궤(軌)가 다르더라도 들어맞는 것이 있다.

한낱 소작농인 중년인은 스스로 깨달은 바와 산적들에 대한 부정적인 인식을 바탕으로 말하고 있을 뿐이었지만, 사실 그 의견에 대한 당위성은 충분했다.

마교는 단지 중원 무림을 원했으나, 지금의 암천은 천하 그 자체를 얻고자 하니까.

누구든 이 도박에서 성공한다면 십왕(十王)이라는 별호 대신, 진정한 일국의 왕으로 거듭날 수도 있을 테니까.

새로운 천하.

새로운 주인 아래에서.

그리고 이 작은 마을까지 흘러 들어간 여러 가지 소식 중에는, 아직 확실시 되지 않은 녹림맹의 배반보다 훨씬 더 충격적인 이야기도 있었다.

“인의대협들만 모였다는 바로 그 정파의 모용세가(慕容世家)도 흉적과 손을 잡았는데, 도적놈들이라고 오죽할까.”

천하 오대세가의 일원이었음에도 북방 일대에 피바람을 불러일으켰다는 모용세가가 입에 오르자, 나머지 사람들은 약속이라도 한 듯이 굳게 입을 닫았다.

맞다.

천성이 도적이요, 삶의 목적이 빼앗는 것인 그들에게 배신이 무슨 대수란 말인가.

이 거대한 도박판에서 승리할 수만 있다면, 끝까지 살아남을 수만 있다면 과거와는 비교도 할 수 없는 영광과 재물을 얻게 될 것이다.

“실로 난세(亂世)로군.”

한구석에 앉아있던 노인의 나지막한 뇌까림은 모두의 마음을 대변하는 것이었고, 뒤이어 한숨처럼 흘러나온 한 마디는 들끓는 불안감에 기름을 부었다.

“산자락이 이리도 들썩이니, 강물도 요동치겠어.”

그리고 그 말은 곧 현실이 되었다.

흑도의 두 거인이 서로를 마주한 지 이틀이 지난 어느 날에.



* * *



이 아득하고도 광활한 장강(長江)이 누구의 것이냐 묻는다면, 무림에 몸담은 이들은 망설임 없이 대답할 것이다.

오대세가도, 구파일방도 아닌 바로 장강수로맹이라고.

그러나 무림에 속하지 않은 이들의 대답은 다를 것이다.

그들에게 있어 그 대상이 산이건, 강이건 저 드높은 하늘 아래 만물의 주인은 오직 한 사람.

천자(天子)뿐이니까.

그리고 해상왕(海上王) 파륜은, 오래전부터 그 사실이 썩 마음에 들지 않았다.

“노부가 어릴 적, 옆집에 살던 노인이 그러더군. 천자는 용의 핏줄을 이어 받은 하늘의 자손이니, 몸과 마음을 다해 섬겨야 한다고.”

음성은 나직했으나 힘이 실려 있었고, 심후한 공력은 공간을 떨어 울렸다.

“성격은 괴팍했지만, 뭐 그럭저럭 괜찮은 노인이었지. 잇따른 흉년에 부모를 잃고 고아가 되어 버린 노부를 잠시나마 거두어 주었으니.”

파륜은 상념에 잠긴 눈빛으로 자신의 과거를 돌아보았다.

이미 수백, 수천 번도 넘게 되짚어 보았지만 온통 좋지 않은 기억들뿐이다.

수염이 나기도 전에 양친을 잃고 노인에게 거둬져, 호된 종살이로 입에 풀칠이라도 할 수 있었던 시간이 그나마 가장 괜찮은 축에 들었을 정도니까.

물론, 그마저도 얼마 가지 않았지만.

“빌어먹을 시절이었다. 열 명이 넘는 얼간이들이 왕을 자처하고, 관군이란 것들이 대낮에 마을로 쳐들어와 약탈과 살인을 일삼아도 아무런 문제가 되지 않을 만큼.”

파륜은 성긴 수염을 쓰다듬었다.

뻔한 이야기다.

노인은 바로 그때 죽었다.

패잔병 무리도, 도적도 아닌 예리한 창칼과 높은 깃발을 치켜세우며 진군하던 관군에 의해서.

그리고 노인에게 고마움을 품고 있던 열두 살의 소년은, 그의 노쇠한 육신에 창날을 찔러넣은 관군을 죽이고 도망쳤다.

“사흘 밤낮을 쉬지 않고 달렸지. 결국 놈들의 추격을 벗어나 강가에 다다라 쓰러졌는데, 문득 그런 생각이 들더군.”

파륜은 하늘을 가리키며 말을 이었다.

“천하가 제 것이라 주장하는 것들이 이토록 많은데, 하늘의 자손이라는 것들이 저 모양이라면 난 누구를 섬겨야 하나?”

결국 길었던 난세도 끝났다.

주씨 성을 지닌 영웅은 대륙을 일통했고, 오직 그 자신만이 천자임을 만천하에 알렸다.

그리고 그사이 소년에서 청년이, 하인에서 수적이 된 파륜은 새로운 천자의 등극을 보며 의문에 대한 답을 찾을 수 있었다.

“그때 알았다. 모든 것은 창칼로 얻을 수 있다는 사실을. 오직 최후의 승자가, 결과로 입증한다는 것을.”

하지만 파륜은 자신의 한계를 누구보다 잘 알고 있었다.

그에게는 천하를 얻을 명분도, 그럴만한 무력도 없었으니까.

다만, 이 거대한 강을 얻을 수 있었다.

지금 이 순간, 저 멀리 모습을 드러낸 대국의 군함과 맞설 수백 척의 선박과 수천이 넘는 수하들도 함께.

“돛을 펴라. 시간이 왔다.”

촤아악.

선명하게 웃는 파륜의 머리 위로 나부끼는 거대한 천자락.

그에 따라 나아가는 무수한 뱃머리를 보며, 파륜의 곁에 있던 흑의인이 조용히 입꼬리를 말아올렸다.
```

## Final English reading copy

```markdown
# Chapter 1083

From the moment good and evil first split apart, things that would never disappear from the world were born.

Those called bandits were among them.

They robbed and stole wealth, and sometimes even took other people’s lives in the process. They had existed since time immemorial and were the kind of people who could never be rooted out completely.

Just as shadows fell wherever there was light, the wheel could not be stopped unless people were rid of the desires and emotions everyone felt.

Perhaps that was why people had finally decided to accept this unpleasant natural order.

Rather than spill innocent blood trying to break an unbreakable cycle, they had come to tolerate a certain degree of coexistence through talking things out.

But people could sense that the long stretch of coexistence was now rushing toward its end.

“Hey, have you heard the news?”

Foreboding always ran a step ahead of hope.

The people of county towns near mountains and rivers felt the unusual atmosphere keenly.

“They say a sudden landslide last night completely blocked the road over the mountain. The herb gatherers say it doesn’t look like an ordinary landslide…”

“What do you mean, it wasn’t an ordinary landslide?”

“I’ve spent my whole fifty years plowing fields, so I can’t say for sure. But those folks can tell at a glance.”

“And?”

“The herb gatherers took one look at the cut ends of the trees swept down with the earth and sand. They hadn’t been bent and snapped clean off—it looked as though someone had given them a few halfhearted chops with an axe. Besides, there weren’t any real signs of a landslide to begin with.”

“Wait. Does that mean…”

“Who else could it be? Unless ghosts did it, it was those damn bandits.”

“Shh! ‘Those damn bandits’? Watch your mouth. It’s unlikely, but if the Green Forest Alliance hears you…”

“Green Forest Alliance, my ass. What’s wrong with calling bandits bandits? They’re highwaymen who take two days’ wages just to let you cross a mountain pass!”

“Now, now. I understand how you feel, but the Green Forest Alliance is officially on our side. By imperial decree, they’ve joined forces with the Murim Alliance against the vicious enemies in the west.”

“That man’s right. Everyone knows bandits are no good, but they’re not completely out of control like Dark Heaven. Something like this happened when we were kids, too, didn’t it?”

“Right. Though it wasn’t Dark Heaven back then, it was the Demonic Cult. Anyway, I remember the Green Forest Alliance joining forces with the Murim Alliance to fight them. The Green Forest Alliance was formed afterward.”

For middle-aged men who were getting on in years, the Great Faction War was one of those childhood memories they would never forget.

Ordinary people had suffered little harm, but the news that bloodthirsty murderers who believed in an evil doctrine had invaded the Central Plains had thrown the whole land into turmoil.

So even with these ominous rumors about the Green Forest Alliance, people couldn’t help but remain skeptical. The Green Forest Alliance they remembered was a group formed by bandits who were at least willing to talk. They had long since become a part of everyday life.

But that wasn’t the only rumor going around.

“Do you remember those men who passed through our village in the dead of night two days ago?”

“Of course. You mean those strangers? I think they called themselves the Blue Flower Escort Bureau.”

“Right, those men. I was shocked to see one of their porters, big as an ox, holding up that heavy flag without even blinking. Then I got a second shock when I saw his face—it was even more terrifying than his build.”

“Why bring that up now? Merchants and escort bureaus pass through here several times a month. It’s nothing unusual.”

At the others’ puzzled looks, the middle-aged man who’d started the conversation lowered his voice.

“They did come through, but where they went in the end—that’s what matters, isn’t it?”

“What?”

“See for yourself. Herb Gatherer Hong pulled this out of the landslide early this morning.”

The next moment, the middle-aged man pulled a bundled piece of cloth from his robe and unfolded it. Everyone who saw it widened their eyes.

More precisely, they stared at the two characters revealed as the dried mud and grains of sand fell away.

Blue Flower.

“T-This is…”

“If you remember that big porter, you’ll remember the flag he was carrying, too. That’s right. It’s their escort flag.”

The villagers looked at one another and swallowed hard.

A flag held great symbolic meaning for any group.

Just as soldiers would give their lives to protect a general’s banner, the merchants and escort bureaus they knew took pride in their own flags.

But what if an escort bureau’s flag, carried along the mountain road in the dead of night just two days ago, had turned up in the landslide?

And what if a suspicious landslide had blocked the only road through the mountains a day later?

“You can guess what this means, can’t you?”

“…You don’t think?”

“I’m not guessing. That’s exactly what happened. The Green Forest Alliance—those damned bandits—must have pulled something. For some reason, they killed to silence whoever knew, then tried to cover it up by passing it off as a landslide.”

A suffocating silence pressed down on the group.

Their unease, now unmistakably real, tightened like a noose around their necks as the pieces of the situation fell neatly into place.

“B-But what would they have to gain from doing that? They fought the Demonic Cult in the past. As a reward, they got to call themselves an alliance, like the river pirates on the Yangtze, and live pretty comfortably.”

“Do you remember what you said during the harvest two years ago?”

“Two years ago? What does that have to do with anything?”

“You were disappointed. It was the best harvest in nearly ten years, but you sighed and said it still wasn’t enough. Would those men be any different?”

“…!”

“It’s obvious. Even we farmers get greedy. What about men who make their living taking what belongs to others?”

Even if their paths were different, some things still fit.

The middle-aged tenant farmer was only speaking from what he’d learned himself and his prejudice against bandits. But his argument made plenty of sense.

The Demonic Cult had wanted only the Central Plains Murim. Dark Heaven wanted the world itself.

Anyone who won this gamble could become a true king of a nation, instead of merely being called one of the Ten Kings.

A new world.

Under a new ruler.

Among all the news that had reached this little village, there was also a story far more shocking than the still-unconfirmed rumors of the Green Forest Alliance’s betrayal.

“Even the Murong Family of the orthodox faction—the one supposedly full of Great Heroes of Benevolence and Righteousness—joined forces with those vicious enemies. What do you expect from a bunch of thieves?”

At the mention of the Murong Family, one of the Five Great Families, which had unleashed a bloodbath across the northern lands, the others shut their mouths as if on cue.

That was right.

For people born bandits, whose whole purpose in life was to take what they wanted, why would betrayal matter?

If they could win this enormous gamble and survive to the end, they would gain wealth and glory beyond anything they’d known before.

“What a turbulent age we live in.”

The old man’s quiet murmur from his place in the corner spoke for everyone. Then his next words, breathed out like a sigh, fanned the unease already boiling inside them.

“With the mountains in such an uproar, the rivers will be in turmoil, too.”

And soon enough, his words became reality.

Two days after the two giants of the dark-path Murim faced one another.

* * *

If you asked whose the vast, boundless Yangtze was, those in the Murim would answer without hesitation.

Not one of the Five Great Families or the Nine Sects and One Gang—but the Yangtze River Channel League.

But those outside the Murim would give a different answer.

To them, whether you were talking about mountains or rivers, there was only one master of all things beneath the lofty sky.

The Son of Heaven.

And the Seafaring King, Pa Ryun, had never liked that one bit.

“When this old man was a child, an old man who lived next door told me that the Son of Heaven was descended from dragons, a child of Heaven who must be served with all one’s heart and soul.”

His voice was low, but full of force. His profound internal energy made the air tremble.

“He had a bad temper, but he was a decent enough old man. When I was orphaned by one bad harvest after another, he took me in for a while.”

Pa Ryun looked back on his past, lost in thought.

He had gone over it hundreds, thousands of times already, but it was full of nothing but bad memories.

He had lost both parents before he could grow a beard, and the time he spent in harsh servitude under the old man, just managing to keep food in his mouth, had been the best part of his life.

Of course, even that didn’t last long.

“It was a damnable time. More than ten fools called themselves kings, and the so-called imperial troops could raid villages in broad daylight, looting and killing, without facing any consequences.”

Pa Ryun stroked his sparse beard.

It was the same old story.

The old man had died then.

Not at the hands of a defeated army or bandits, but the imperial troops marching forward with sharp spears and tall banners.

The twelve-year-old boy, grateful to the old man, killed the soldier who had driven a spear into the old man’s frail body, then ran.

“I ran for three days and nights without stopping. In the end, I escaped their pursuit, reached a riverbank, and collapsed. Then a thought came to me.”

Pa Ryun pointed to the sky as he continued.

“There were so many people claiming the world belonged to them. If the so-called children of Heaven were like that, who was I supposed to serve?”

In the end, the long age of chaos came to an end.

A hero of the Zhu family unified the continent and announced to all under Heaven that he alone was the Son of Heaven.

By then, the boy had become a young man, and Pa Ryun had become a river pirate instead of a servant. Watching the new Son of Heaven ascend the throne, he found the answer to his question.

“That was when I learned that anything could be won with spears and swords. That only the last one standing could prove himself by the outcome.”

But Pa Ryun knew his own limits better than anyone.

He had neither the right to claim the world nor the strength to take it.

Still, he had been able to claim this great river.

And with it, hundreds of ships and thousands of men—enough to stand against the Great Nation’s warships, now visible in the distance.

“Raise the sails. The time has come.”

*Whoosh.*

Above Pa Ryun’s bright smile, a great sheet of cloth snapped in the wind.

As countless ships surged forward beneath it, the black-robed man at Pa Ryun’s side quietly curled his lips into a smile.
```
