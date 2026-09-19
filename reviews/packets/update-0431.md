<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0431.txt",
      "sha256": "9b2436fb31ff77489e801af1f861bf752e3b36ab22bb1b9186fb22f94c9c9fb6",
      "bytes": 13057
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "85d8d6659b8ae5a4747be34cc9fb023d4ca76c3b46fb1fcdf5075b314aa433ab",
      "bytes": 2680
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "63a23715f5ad9b22a0a45f09af5ba17eb049e72f3afcc18c03f938db719596ab",
      "bytes": 142400
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "86de46bffaf12d173023a9efd56dc2df2ecb0ffcab6442f9c173f4e20217233e",
      "bytes": 533
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "7807fef332ab852d4ec547d371b12cb714fc257d70a6f1750ddc3681046dbf17",
      "bytes": 824
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "ab0cd57a7152415817515e5ae16fce89f93bf4dc066ac65a9c87ce254c9404f4",
      "bytes": 667
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "3640ea180668dec54430c1eace57ad6e886889a5c3c17a0f9b8172fb8f7b323a",
      "bytes": 1182
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "82931a0b750ea57438e4bf16cf4b330cbed9518d56e711611b28fbfc0ed20b9e",
      "bytes": 795
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6458583a734bbd765fa1212448f8751a654fec3de773343765b99a43576793a4",
      "bytes": 133462
    }
  ],
  "estimated_tokens": 10009
}
-->

# Durable State Update — Chapter 431

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 431. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 431. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 431,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 431,
    "continuity_sources": [431],
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
    "The Arch Lich's magic-circle fragments match the patterns and symbols of the Moving Formation Jin saw in Murim, and can be assembled into one enormous circle.",
    "The circle appears to have absorbed human life force to accumulate mana, but this remains the Skeleton King's inference rather than a confirmed decipherment.",
    "The circle at the Arch Lich's ruined base is inactive and retains traces of the deaths it once caused; Jin gains no interpretation from it and the System remains silent.",
    "Jin suspects that the Murim formation, the modern world's magic circle, the battle phenomena involving the Blood Lord and Western Heaven Demon Lord, and his junk capsule are connected.",
    "Magic Johnson is researching the circle on behalf of the coalition forces and brought Jin to the classified site for direct examination.",
    "The Skeleton King remains hidden in Jin's Inventory or an extradimensional pocket when necessary and continues pursuing a human-world identity as Stone-King.",
    "Chairman Shao is preparing a political reckoning against the Crown Prince Party after its persecution and forced-labor campaign.",
    "Jin's mother and Hayeon remain in China under Chairman Shao's protection.",
    "Lee Jungryong is publicly presumed dead without a surviving body, while Wu Heixing's corpse was recovered after the battle.",
    "Go Jun, Lee Jungryong's Disciple and Head of Security, has arrived in the ruins and confronted Jin."
  ],
  "continuity_sources": [
    430,
    429
  ],
  "open_questions": [
    "What do the shared patterns and symbols represent, and why did the Arch Lich possess a circle matching the Moving Formation?",
    "What connection links the two worlds, the battle phenomena, and the junk capsule?",
    "Why has Go Jun come to the ruins, and what does he intend to do about Jin?",
    "What final punishment will be imposed on Wu Heixing's father and the Crown Prince Party leadership?",
    "How will the Skeleton King's human identity and Stone-King name be formalized in the human world?"
  ],
  "safe_through": 430,
  "temporary_decisions": [
    "Render 샤오 쉔 as “Xiao Shen” and preserve “hyung” for his address to Jin.",
    "Render 매직 존슨 as “Magic Johnson,” 스켈레톤 킹 as “Skeleton King,” and 스톤-킹 as “Stone-King.”",
    "Render the suspected function of the circle as “life-force absorption” while preserving the uncertainty of the inference.",
    "Preserve Jin's dry, profane voice and the Skeleton King's grandiose, Internet-influenced insults.",
    "Render 아공간 포켓 as “extradimensional pocket.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 이정룡    | **Lee Jungryong** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 제자     | **Disciple**                                 |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 내가중수법 | **Inner-Family Heavy Hand** | Taekyung's joking comparison for his mother's painful palm strike. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 429
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 430
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong; leader of Lee's security detail; regarded by Lee as stronger than Park Tae Seop; after Go Jun's defeat by Jin Taekyung, Lee reaffirmed his faith in Go Jun and promised to give him the strength to defeat Taekyung.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 430
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 430
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 428
- **Aliases:** None
- **Role:** Wu Heixing was a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practiced martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts, before Jin Taekyung killed him.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃431화



- 간악한 인간. 저 인간은 누구냐?

있다. 그런 겁 없는 인간이.

마음속으로 뇌까린 나는 천천히 주위를 둘러봤다.

중심부에서 한참이나 벗어난, 인적이 끊긴 외곽. 대낮처럼 환하게 도시를 비추는 빛마저 미처 스며들지 못한 곳.

그리고 폐허 사이에서 그림자를 드리우며 걸어 나오는 한 사람.

“우리 사이에 인연이 있긴 한가 보다. 계속 마주치는 걸 보면.”

내 인사에 석고준이 차가운 목소리로 대꾸했다.

“인연이 아니라 악연이겠지.”

“그럼 하필 이런 곳에서 만나게 된 건 뭐라고 해야 하나. 우연?”

돌아온 것은 칼날 같은 한마디였다.

“필연(必然).”

“명쾌하네. 그래서 아까부터 떠돌이 개처럼 쫄래쫄래 따라온 건가?”

“언제부터 알고 있었지?”

“석기시대 때부터, 이 새끼야. 하도 쳐다보길래 면상에 구멍 뚫리는 줄 알았다.”

은밀한 감시의 시선을 느낀 것은 마법진을 확인하고 나온 직후였다.

다른 이들이 보내는 호기심과 선망의 눈빛과는 다른, 불쾌하면서도 끈적한 시선.

그리고 지금 같은 상황에서 내게 적대감을 보이는 부류는 극소수다.

“너 아니면 태자당 짱깨 놈들이지 뭐. 그런데 후자는 여기저기 싸질러 놓은 똥 치우기 바쁘니까…… 뻔한 거 아냐?”

분명히 정곡을 찌르는 한마디였을 텐데, 석고준에게는 조금의 당황도 엿보이지 않았다.

“역시. 그랬군.”

“역시?”

“너라면 알아챌 것이라 생각했다. 아니었다면 매직 존슨을 떼어 놓고 굳이 여기까지 혼자 올 이유가 없겠지.”

이놈 봐라?

그제야 석고준이 당황하지 않는 이유를 알았다. 놈은 내게 신호를 보낸 거다. 따라오라는 신호를.

이건 감시도, 유인도 아니었다. 석고준과 나. 우리 두 사람 모두가 원했던 그림이다.

물론 이 만남의 결과는 크게 어긋나겠지만.

“묻고 싶은 게 있다.”

석고준은 대답을 기다리지 않았다. 나를 똑바로 노려보며 자신이 해야 할 말을 이어 갈 뿐이었다.

“네 짓이냐?”

짧고 간결한 질문이었지만 그에 담긴 뜻을 알아듣기에는 차고 넘친다. 하지만 나는 고개를 갸우뚱거리며 천연덕스럽게 되물었다.

“뭐가?”

“알고 있을 텐데.”

“너 혹시…… 지금 내가 정룡 아저씨를 죽였다, 이런 생각 하고 있는 건 아니지?”

이정룡. 그 이름을 듣자 석고준의 눈빛이 격동으로 흔들렸다. 나는 대답을 기다리지 않고 두 손으로 입을 틀어막았다.

“세상에, 어떻게 그런 끔찍한 생각을 할 수가. 진심이야?”

“가증스러운 연기는 집어치워. 지금 몰라서 묻는 것 같나?”

“그럼 왜 묻는 건데? 기자 회견 안 봤어?”

“봤지. 처음부터 끝까지 헛소리와 거짓말을 늘어놓더군.”

툭, 투둑.

하얗게 물들 만큼 꽉 움켜쥔 주먹에서 핏방울이 떨어진다. 석고준은 분노로 타오르는 눈동자로 나를 노려보았다.

“이곳에는 너와 나, 단 두 사람뿐이다. 네 입으로 진실을 말해라.”

- 노옴! 감히 애틀랜타 태생인 이 몸, 스톤 킹을 빼놓다니!

여기 몬스터 하나 추가요.

정확히는 두 사람에 몬스터 하나다. 스켈레톤 킹을 더 이상 몬스터라고 부를 수 있을지는 모르겠지만.

“흠.”

석고준을 바라보며 뒷머리를 벅벅 긁던 내가 입을 열었다.

“맞아. 내가 죽였어.”

“……!”

“이정룡도, 우헤이싱도. 전부 내가 해치웠다. 미친놈들이 말도 안 되는 시나리오를 써 왔더라고. 나만 죽이고 아크 리치는 건드리지도 않을 생각이었지. 그리고 결과는…… 알지?”

추측과 진실은 엄연히 다르다.

이미 충분히 짐작하고 있던 사실이라고 해도, 원수의 입에서 확답을 듣는 건 전혀 다른 문제다.

나는 몸을 파르르 떠는 석고준을 향해 마지막 쐐기를 박았다.

“그런 놈들인데 내가 뭘 어쩌겠냐. 둘 다 미국행 티켓 끊어 줬어. 아, 정룡 아저씨는 특별히 퍼스트 클래스로.”

“네가, 네가 감히 그분을……!”

쏴아아악!

석고준의 전신에서 솟구친 살기에 공기가 차갑게 얼어붙는다.

나는 검자루를 향해 움찔거리는 놈의 손가락을 빤히 바라보다, 불쑥 입을 열었다.

“너, 지금 뭐 하냐?”

“……!”

석고준의 눈이 부릅떠진다. 동시에 주위에 휘몰아치던 살기가 씻은 듯이 사라졌다.

아니, 내게서 흘러나온 기파(氣波)에 짓눌렸다.

순식간에 지배자가 뒤바뀐 공간 속, 나는 천천히 걸음을 뗐다.

“확실히 전보다 실력이 일취월장했네. 따져 보면 우헤이싱보다도 훨씬 나아. 이정룡 그 인간이 곁에 두고 키운 제자다워.”

저벅.

“그런데…….”

저벅.

내딛는 걸음만큼, 석고준의 안색도 창백하게 질려 간다.

압도적인 힘의 격차. 토끼는 호랑이를 이길 수 없다. 검을 뽑기 위해 조금이라도 움직이는 순간, 내 이빨은 놈의 목덜미를 파고들 것이다.

“누울 자리는 보고 다리를 뻗어야지. 묫자리에 자리를 잡으면 어떡하냐.”

파앙-!

느긋하게 들어 올린 손가락 끝에서 압축된 공기가 터져 나갔다.

날카로운 파공성과 함께 한 줄기의 지풍(指風)이 석상처럼 굳어 버린 석고준을 향해 쏘아졌다. 그리고…….

따앙!

놈의 허리춤에 매여진 검을 저 멀리 튕겨 냈다.

눈을 부릅뜬 채 굳어 있던 석고준의 표정이 일그러지는 것을 보며, 나는 피식 웃었다.

“왜, 죽일 것 같았냐?”

“……어째서?”

“그렇게 죽고 싶으면 좀 더 은밀하게, 진짜 죽을 각오를 하고 찾아와. 오늘처럼 어중간하게 함정 파놓지 말고.”

나는 번개처럼 손을 뻗었다. 석고준이 반응할 새도 없었다.

팡! 다시 한번 쏘아진 세 줄기의 지풍이 짙은 어둠 너머 어딘가를 관통한 다음 순간.

퍼퍼퍽!

저 멀리, 미세한 타격음과 함께 의식을 잃은 검은 그림자 셋이 허공으로부터 투두둑 떨어졌다.

각각 은신 특성을 단련한 상위 헌터인 데다 각종 마법으로 모습을 감췄지만, 중단전의 개방으로 더욱 날카로워진 내 기감을 피할 수는 없었다.

“도촬 중이었니? 몰카충 새끼야.”

툭, 툭.

나는 혀를 차며 석고준의 뺨을 두드렸다. 치욕감에 이를 악문 놈의 잇새 사이로 악에 받친 목소리가 흘러나왔다.

“이러고도…… 너희가 무사할 것 같으냐?”

“너희?”

“우리는, 아레스 길드는 무너지지 않는다. 반드시 그분의 죽음에 대한 복수를…….”

쫙!

이빨과 함께 핏물이 튀었다. 나는 석고준의 멱살을 단단히 틀어쥔 채 다시 한번 귀싸대기를 날렸다.

쫙!

한 번 더.

쫙!

다시 한번 더.

쫙!

내가중수법(內家重手法).

손바닥에 실린 공력은 놈의 뼈와 살을 찢는 대신 석고준의 내부로 파고들어 뇌를 뒤흔들었다.

나는 만취한 사람처럼 중심을 잡지 못하고 비틀거리는 석고준의 목울대를 움켜쥐었다.

“지금부터 하는 말. 똑똑히 기억해라.”

“커헉……!”

신음과 함께 터져 나온 피거품이 얼굴에 튄다. 초점을 잃어버린 눈동자에 비친 낯선 누군가가 무감각한 표정으로 말을 이었다.

“시작한 건 너희지만, 끝내는 건 나야.”

결국 현대도 힘의 논리에 지배되는 세상이다.

헌터라는 초인이 가진 능력, 혹은 그만한 권력을 지닌 이들이 자신들의 입맛에 맞춰 규칙을 정하고 거리낌 없이 반칙을 저지른다. 그들이 무슨 짓을 하건 옐로카드도, 레드카드도 주어지지 않는다.

이정룡이 견제를 위해 꺽정 아저씨의 팔을 잘랐던 것 역시, 그들에게는 당연했던 일이었다. 하지만…….

“그러지 말았어야지.”

이제 새로운 심판이 들어섰으니 규칙도 바뀌어야 한다. 그리고 새로운 규칙의 내용은 매우 간단하다.

나는 석고준의 아혈(啞穴)을 짚으며 작게 뇌까렸다.

“눈에는 눈. 이에는 이.”

빨래를 쥐어짜듯, 놈의 두 팔을 비트는 동시에 힘껏 당겼다.

콰드드득!

끔찍한 파육음과 함께 육신으로부터 떨어져 나온 두 개의 팔.

엄청난 양의 핏물이 쏟아지고 부릅뜬 눈에서 흰자위가 드러난다. 아혈이 봉해진 입에서는 소리 없는 비명이 쏟아졌다.

“아직 안 끝났다.”

너덜거리는 양팔의 단면에 손가락을 쑤셔 박았다. 손에 실린 열양지기가 살을 지지며 더욱 큰 고통을 안겨 준다. 고통으로 몸부림치는 놈의 몸을 짓누르며 발목을 잡았다.

“이 정도로는 부족하겠지. 넌 그런 놈이니까.”

우두둑!

천근거석도 가루로 만들어 버리는 근력이다. 두 다리를 이루는 뼈가 단번에 으스러지고 수백 조각으로 나뉘었다.

“……!”

소리 없는 몸부림.

나는 상상하지 못할 고통으로 까무러치는 석고준의 몸에 공력을 불어 넣었다.

흐릿해져 가던 눈동자에 빛이 돌아온 뒤에, 주먹으로 부서진 다리를 후려쳤다.

쿵! 쿵! 쿵!

문득 주먹을 멈췄을 때, 지면에 널브러져 있는 것은 인간이 아닌 커다란 고깃덩어리였다.

코와 입으로 새어 나오는 옅은 숨결만이 살아 있다는 유일한 증거였다.

인벤토리에서 이 모든 광경을 지켜본 스켈레톤 킹이 떨리는 목소리로 말했다.

- 이, 인간.

나는 메마른 목소리로 대답했다.

“왜?”

- 아, 아니. 그…….

녀석은 말꼬리를 흐렸지만, 나는 스켈레톤 킹이 하고자 하는 말을 이미 알고 있었다.

“그래, 잔인하지.”

- …….

“하지만 필요한 일이었어.”

아무것도 할 수 없다는 무력감. 차라리 죽는 게 백 배, 천 배 낫다고 생각할 만큼의 고통.

그리고 상대가 마음만 먹으면 언제든지 같은 상황에 처할 수도 있다는 공포까지.

이 모든 것들을 적의 가슴에 심고, 뼈에 새겨 두어야 한다.

물론 가장 뒤탈이 없는 것은 따로 있지만.

‘죽음.’

나도 모르게 손가락 끝이 움찔거렸다.

아주 조금, 조금의 힘을 가한다면 석고준을 죽일 수 있다.

혹시 모를, 아주 약간의 가능성마저 없애 버릴 수 있는 절호의 기회다.

하지만…….

‘시기가 좋지 않아.’

진실을 둘러싼 의심은 사라지지 않는다.

인류가 처음 달에 간 것도, 역사에 기록된 수많은 유명인사가 살아 있다는 음모론도 그와 같은 맥락이다.

이정룡에 이어 우헤이싱, 거기에 더해 석고준까지 사라진다면. 때마침 이곳에 내가 ‘우연히’ 있었다는 사실이 밝혀진다면 나를 둘러싼 소문들은 더 이상 음모론이 아니게 된다. 그러니 이쯤에서 끝내야 한다.

압도적인 힘의 격차와 나에 대한 공포를 심어 준 바로 지금.

“마지막으로 말한다.”

“……!”

석고준의 신형이 움찔 떨렸다. 나는 어느 때보다 낮고 무감정한 목소리로 한 글자, 한 글자를 씹어 뱉었다.

“이정룡, 한 사람으로 끝내.”

용암처럼 뜨거운 숨이 닿자 엎어진 몸뚱어리가 경련을 일으킨다.

마치 자신의 목을 파고드는 호랑이의 이빨을 느낀 토끼처럼.

“이빨 감추고, 손톱 숨겨. 그렇게 한다면…… 아무 일도 일어나지 않는다.”

죽이고자 했다면 죽을 각오도 했어야 옳다.

이정룡은 가장 큰 적이자 걸림돌이었고, 결국 자신이 저지른 짓에 대한 대가를 치렀다.

지금의 내 제안은 화해의 권고다. 아니, 요구다.

그리고 석고준에게 남은 선택지는 단 하나뿐이었다.

스윽.

아주 미세하게 끄덕여지는 고개. 공포와 두려움으로 젖은 두 눈동자를 응시하던 나는, 석고준의 수혈(睡穴)을 짚고 인벤토리에서 상급 포션 몇 개를 꺼내 몸에 부었다.

치이이익.

그리고 빠르게 치유되어 가는 놈을 바라보다, 문득 고개를 돌렸다.

“그래서…… 대충 이렇게 된 겁니다.”

그 순간, 공간이 한 꺼풀 벗겨지며 거구의 흑인이 모습을 드러냈다. 복잡한 눈빛으로 나를 바라본 매직 존슨이 입을 열었다.

「할 얘기가 많을 것 같군.」

“제 생각이랑 같네요.”

그런 우리의 대화에, 스켈레톤 킹이 작게 중얼거렸다.

- 클럽은?

거기 게이 바야, 인마.
```

## Final English reading copy

```markdown
# Chapter 431

“Vile human. Who is that human?”

So there is one. A human with no sense of fear.

I muttered inwardly and slowly looked around.

The desolate outskirts were far from the center, abandoned by everyone. Even the light illuminating the city as brightly as day had yet to reach this place.

And from among the ruins, a single person came walking out, casting a shadow.

“There must be some kind of connection between us. We keep running into each other.”

Go Jun answered my greeting in a cold voice.

“Not a connection. Bad blood.”

“Then what should we call the fact that we happened to meet in a place like this? Coincidence?”

The answer that came back was as sharp as a blade.

“Inevitability.”

“Clear enough. So have you been following me around like a stray dog since earlier?”

“When did you realize?”

“Since the Stone Age, you bastard. You stared at me so much that I thought you were going to bore holes in my face.”

I had felt the gaze of someone secretly watching me immediately after I came out from examining the magic circle.

It was an unpleasant, sticky gaze, completely different from the curious and admiring eyes of the others.

And at a time like this, there were very few people who would show hostility toward me.

“Either you or those Crown Prince Party Chinese bastards. But the latter are too busy cleaning up the shit they’ve scattered everywhere… It was obvious, wasn’t it?”

That had clearly struck the mark, but there was not the slightest trace of surprise on Go Jun’s face.

“As expected. So that’s how it was.”

“As expected?”

“I thought you would notice. Otherwise, you wouldn’t have left Magic Johnson behind and come all the way out here alone.”

Well, look at this bastard.

Only then did I understand why Go Jun hadn’t been surprised. He had sent me a signal. A signal to follow him.

This wasn’t surveillance, nor was it a lure. It was the scene both Go Jun and I had wanted.

Of course, the outcome of this meeting would be very different from what he expected.

“There’s something I want to ask.”

Go Jun didn’t wait for an answer. He stared straight at me and simply continued with what he had come to say.

“Was it you?”

It was a short, simple question, but there was more than enough meaning packed inside it. I tilted my head and asked back with an innocent expression.

“What was?”

“You know.”

“You don’t happen to think that I killed Uncle Jungryong, do you?”

At the sound of Lee Jungryong’s name, Go Jun’s eyes shook violently. Without waiting for his answer, I covered my mouth with both hands.

“My God, how could you have such a horrible thought? Are you serious?”

“Stop that disgusting act. Do you think I’m asking because I don’t know?”

“Then why are you asking? Didn’t you watch the press conference?”

“I did. You spouted nothing but nonsense and lies from beginning to end.”

Drip. Drip.

Drops of blood fell from the fist he had clenched so tightly that it had turned white. Go Jun glared at me with eyes burning with rage.

“There are only two people here—you and me. Tell me the truth with your own mouth.”

“Vile human. How dare you leave this Atlanta-born Stone-King out of it!”

One more monster for the count.

More precisely, two people and one monster. Though I wasn’t sure whether the Skeleton King could still be called a monster.

“Hm.”

I scratched the back of my head while looking at Go Jun, then opened my mouth.

“That’s right. I killed him.”

“……!”

“Lee Jungryong and Wu Heixing. I took care of both of them. Those lunatics came up with a ridiculous scenario. They planned to kill only me without even touching the Arch Lich. And the result… You know what happened, right?”

An assumption and the truth were two entirely different things.

Even if he had already guessed the truth, hearing a definite answer from the mouth of his enemy was a completely different matter.

I drove the final nail into the coffin for Go Jun, whose body was trembling violently.

“They were that kind of people. What else was I supposed to do? I bought both of them tickets to the United States. Ah, I gave Uncle Jungryong first class.”

“You—you dared to do that to him…!”

Whoosh!

The killing intent erupting from Go Jun’s entire body froze the air around us.

I stared at his fingers twitching toward the hilt of his sword, then abruptly opened my mouth.

“What do you think you’re doing?”

“……!”

Go Jun’s eyes widened. At the same time, the killing intent swirling around us vanished as if it had been washed away.

No—it had been crushed beneath the wave of qi flowing from me.

In the space where the dominant force had changed in an instant, I slowly began to walk.

“You’ve improved by leaps and bounds since the last time I saw you. If you think about it, you’re far better than Wu Heixing. Just what I’d expect from the Disciple Lee Jungryong trained at his side.”

Step.

“With that said…”

Step.

With every step I took, Go Jun’s face grew paler.

The gap between our powers was overwhelming. A rabbit could not defeat a tiger. The moment he made even the slightest movement to draw his sword, my teeth would sink into his neck.

“You should look at where you’re lying before you stretch out your legs. What are you doing, settling into a grave?”

Bang!

Compressed air exploded from the tip of a finger I had raised leisurely.

With a sharp crack, a single stream of Finger Qi shot toward Go Jun, who had frozen like a stone statue. And then—

Clang!

It sent the sword strapped to his waist flying far into the distance.

Watching Go Jun’s frozen expression twist while his eyes remained wide open, I let out a short laugh.

“What? Did you think I was going to kill you?”

“……Why?”

“If you want to die that badly, come more secretly and be ready to truly die. Don’t set up a half-assed trap like you did today.”

I thrust out my hand like lightning. Go Jun didn’t even have time to react.

Bang!

The three streams of Finger Qi I fired pierced somewhere beyond the thick darkness. A moment later—

Thud-thud-thud!

Three unconscious black shadows fell from the air in the distance, accompanied by faint impacts.

Each one was a high-level Hunter who had trained in stealth abilities and concealed himself with various kinds of magic, but none of them could evade my Qi Sense, sharpened even further by the opening of my Middle Dantian.

“Were you secretly filming me, you hidden-camera bastard?”

Tap. Tap.

Clicking my tongue, I tapped Go Jun on the cheek. A voice full of spite slipped between his clenched teeth.

“Do you think you people will get away with this?”

“You people?”

“We—the Ares Guild—will not fall. We will definitely avenge that person’s death…”

Smack!

Blood spattered together with teeth. I gripped Go Jun tightly by the collar and slapped him across the face again.

Smack!

One more time.

Smack!

Again.

Smack!

Inner-Family Heavy Hand.

Rather than tearing through his bones and flesh, the internal energy in my palm burrowed into Go Jun’s body and rattled his brain.

I grabbed the throat of Go Jun, who staggered helplessly, unable to keep his balance like a drunken man.

“Remember what I’m about to say. Remember it clearly.”

“Ghk!”

A bloody foam burst out with his groan and splattered across my face. An unfamiliar man was reflected in his unfocused eyes, his expression numb as he continued speaking.

“You started this, but I’ll be the one to finish it.”

In the end, the modern world was also ruled by the logic of power.

The abilities possessed by superhumans called Hunters—or the power held by those with equivalent authority—allowed them to set the rules according to their own tastes and break them without hesitation. No matter what they did, they were never given a yellow card or a red card.

When Lee Jungryong cut off Uncle Kkeokjeong’s arm to keep him in check, that had been perfectly natural to people like them. But—

“You shouldn’t have done that.”

Now that a new referee had entered the game, the rules had to change as well. And the new rules were very simple.

I pressed Go Jun’s Mute Acupoint and muttered quietly.

“An eye for an eye. A tooth for a tooth.”

I twisted both his arms and pulled with all my strength, as though wringing out laundry.

Crack-crack-crack!

With a horrible tearing sound, two arms came away from his body.

An enormous amount of blood poured out, and the whites of his bulging eyes showed. A silent scream spilled from his mouth, its Mute Acupoint sealed.

“It’s not over yet.”

I shoved my fingers into the ragged stumps of his arms. The Scorching Yang Qi in my hand seared his flesh, inflicting even greater pain. I pinned down his writhing body and grabbed him by the ankles.

“This won’t be enough for someone like you.”

Crack!

The Strength in my body could grind even a thousand-geun boulder into powder. The bones forming both his legs shattered in an instant, splitting into hundreds of pieces.

“……!”

He struggled without making a sound.

I poured internal energy into Go Jun’s body as he passed out from unimaginable pain.

When the light returned to his fading eyes, I smashed his shattered legs with my fist.

Boom! Boom! Boom!

By the time I finally stopped punching, what lay sprawled across the ground was no longer a human being but a large lump of meat.

The faint breath leaking from his nose and mouth was the only proof that he was still alive.

The Skeleton King, who had watched the entire scene from inside my Inventory, spoke in a trembling voice.

“Human.”

I answered in a dry voice.

“What?”

“N-No, it’s just…”

His voice trailed off, but I already knew what the Skeleton King wanted to say.

“Yeah. It’s cruel.”

“……”

“But it was necessary.”

The helplessness of being unable to do anything. Pain so unbearable that death would seem a hundred or a thousand times better.

And the fear that they could find themselves in the same situation at any time if their opponent simply put his mind to it.

I needed to plant all of those things in the enemy’s heart and engrave them into his bones.

Of course, there was another option that would leave the fewest loose ends.

*Death.*

The tips of my fingers twitched before I realized it.

If I applied just a little—just a tiny bit more—force, I could kill Go Jun.

It was the perfect opportunity to eliminate even the slightest possibility.

But…

*The timing isn’t right.*

The doubts surrounding the truth would not disappear.

The conspiracy theory that humanity’s first trip to the moon was a lie, and the conspiracy theories claiming that countless famous people recorded in history were still alive, all followed the same pattern.

If Lee Jungryong disappeared, followed by Wu Heixing and then Go Jun as well—and if it came to light that I had “happened” to be here at exactly the right time—the rumors surrounding me would no longer be conspiracy theories.

So I had to end it here.

Right now, after planting fear of me and the overwhelming gap between our powers.

“I’ll say this one last time.”

“……!”

Go Jun’s body flinched. In a voice lower and more emotionless than ever, I bit out each word one by one.

“Let it end with Lee Jungryong. No one else.”

My breath, hot as lava, touched his body, and the figure lying facedown began to convulse.

Like a rabbit sensing the tiger’s teeth digging into its neck.

“Hide your teeth. Hide your claws. If you do that… nothing will happen.”

If he had intended to kill, he should have been prepared to die.

Lee Jungryong had been my greatest enemy and obstacle, and in the end, he had paid the price for what he had done.

What I was offering now was a proposal of reconciliation.

No—a demand.

And Go Jun had only one choice left.

His head gave the faintest nod.

As I stared into his two eyes drenched in fear and terror, I pressed his Sleep Acupoint, took several high-grade potions from my Inventory, and poured them over his body.

Hissssss.

I watched him heal rapidly, then suddenly turned my head.

“So… that’s more or less what happened.”

At that moment, a layer of space peeled away, revealing a huge Black man. Magic Johnson looked at me with a complicated expression before opening his mouth.

“I think there’s a lot we need to talk about.”

“I was thinking the same thing.”

As we spoke, the Skeleton King muttered quietly.

“What about the club?”

“That’s a gay bar, dumbass.”
```
