# Retrospective Patch Plan — Chapters 9–13

Create bounded exact-text patches; do not return complete chapters. Every `old`
string must occur exactly once in the identified current chapter. `new` must be
finished replacement prose. Combine adjacent findings when useful, never alter
unreported text, and disposition every finding.

Return exactly one JSON object with no Markdown fence:

{
  "summary": "brief patch summary",
  "patches": [
    {"chapter": 1, "finding_ids": ["R0000-01"], "old": "exact old text", "new": "exact replacement"}
  ],
  "dispositions": [
    {"finding_id": "R0000-01", "status": "applied|rejected|unresolved", "reason": "specific reason"}
  ]
}

Reject a finding only when its proposed change is not supported by the supplied
source. Leave genuinely uncertain findings unresolved. Do not intensify or
sanitize register.

## Audit rubric

# Retrospective Translation Audit Rubric

Audit accepted chapters for defects likely to survive an ordinary review. Do
not retranslate acceptable prose or optimize merely for difference.

Prioritize in this order:

1. Reversed or altered actions, negation, subjects, identities, kinship,
   quantities, causal relations, and physical direction.
2. Omitted source beats, explanatory mechanisms, pragmatic cues, ambiguity,
   jokes, and characterization.
3. Established terminology, Murim concepts, hierarchy, and address.
4. Register mismatch: intensified or sanitized profanity, euphemisms made more
   explicit, stiffness, or flattened comic timing.
5. Clear English defects that materially impede voice or meaning.

Semantic fidelity outranks polish. Preserve the source's degree of explicitness.
Do not report optional synonyms, generic praise, or whole-chapter rewrites.
Every finding must quote an exact current-English span and provide a finished,
bounded replacement. Mark a finding critical only when it changes a scene
fact, action, identity, negation, or consequence; major for meaningful lost
hierarchy, mechanism, characterization, ambiguity, or register; minor for clear
localized defects without changed meaning.

## Structured findings

```json
{
  "summary": "9 findings in chapters 9-13",
  "findings": [
    {
      "chapter": 9,
      "confidence": 0.98,
      "current": "The hereditary martial art created by some fellow called the founder—or was it the family’s founding granddad?—was unbelievably complicated.",
      "defect": "The replacement joke about a “founding granddad” loses the source’s explicit wordplay between 시조, “founder,” and 시조새, “Archaeopteryx.”",
      "id": "R0009-01",
      "rationale": "The source deliberately turns “founder” into the similar-sounding “Archaeopteryx,” a comic beat characterizing Taekyung’s irreverent narration.",
      "replacement": "The hereditary martial art created by some fellow called the founder—or was it Archaeopteryx?—was unbelievably complicated.",
      "severity": "major",
      "source": "시조인가 시조새인가 하는 양반이 만들었다는 가전 무공은 더럽게 복잡했다."
    },
    {
      "chapter": 9,
      "confidence": 1.0,
      "current": "I thought the game’s language system had glitched. Fortunately, it meant exactly what I thought it meant.",
      "defect": "This repeats the preceding thought about the language system and omits the source beat in which the warriors accompanying Wipeng join Taekyung’s laughter.",
      "id": "R0009-02",
      "rationale": "The omitted group laughter establishes the falsely convivial atmosphere immediately before Wipeng resumes reading the arrest order.",
      "replacement": "Laughter was contagious. The warriors who had come with Wipeng began laughing along with me.",
      "severity": "major",
      "source": "원래 웃음은 전염되기 마련이다. 위팽과 같이 온 무사들도 나를 따라 웃기 시작했다."
    },
    {
      "chapter": 9,
      "confidence": 1.0,
      "current": "Elder Council",
      "defect": "The established name of the family body is rendered with a non-glossary variant throughout the scene.",
      "id": "R0009-03",
      "rationale": "The supplied glossary fixes 장로원 as “Council of Elders,” and consistent naming matters because it is a specific political body within the Jin Family.",
      "replacement": "Council of Elders",
      "severity": "major",
      "source": "장로원"
    },
    {
      "chapter": 10,
      "confidence": 1.0,
      "current": "**Excellent Grain-Repelling Pill**",
      "defect": "The item name does not use the established translation for 벽곡단.",
      "id": "R0010-01",
      "rationale": "The supplied glossary fixes 벽곡단 as “fasting pills”; this is a recurring named consumable whose terminology continues into the following chapter.",
      "replacement": "**Excellent Fasting Pill**",
      "severity": "major",
      "source": "[뛰어난 벽곡단]"
    },
    {
      "chapter": 11,
      "confidence": 1.0,
      "current": "- Your fatigue has been restored.",
      "defect": "The English reverses the System effect by saying that fatigue itself is restored rather than relieved.",
      "id": "R0011-01",
      "rationale": "The pill removes Taekyung’s fatigue; the current line literally indicates that his fatigue returns, contradicting both the source and his immediately improved condition.",
      "replacement": "- Your fatigue has been relieved.",
      "severity": "critical",
      "source": "- 피로가 회복됩니다."
    },
    {
      "chapter": 12,
      "confidence": 0.99,
      "current": "I launched into the form.",
      "defect": "The translation omits that Taekyung begins the second form.",
      "id": "R0012-01",
      "rationale": "Here 이 is the Sino-Korean numeral “two,” following the earlier identification of 일 초식 as the first form; the number tracks his progression through the spear technique.",
      "replacement": "I launched into the second form.",
      "severity": "minor",
      "source": "이 초식이 시작됐다."
    },
    {
      "chapter": 13,
      "confidence": 0.96,
      "current": "“Is it true that you tried to rape the daughter of the Mount Heng Sword Sect?”",
      "defect": "The translation turns a woman affiliated with the sect into the sect’s literal “daughter” and makes the source’s euphemistic allegation more explicit.",
      "id": "R0013-01",
      "rationale": "항산검문의 여식 identifies the alleged victim as a woman of the Mount Heng Sword Sect, while 범하려 한 uses the euphemistic “tried to violate”; the replacement preserves both the relationship and degree of explicitness.",
      "replacement": "“Is it true that you tried to violate a woman of the Mount Heng Sword Sect?”",
      "severity": "critical",
      "source": "“항산검문의 여식을 범하려 한 것이 사실입니까?”"
    },
    {
      "chapter": 13,
      "confidence": 0.99,
      "current": "*Attempted rape?*",
      "defect": "The translation narrows the allegation from attempted sexual assault to attempted rape.",
      "id": "R0013-02",
      "rationale": "성폭행 denotes sexual assault and does not by itself specify the narrower offense of rape.",
      "replacement": "*Attempted sexual assault?*",
      "severity": "major",
      "source": "‘성폭행 미수?’"
    },
    {
      "chapter": 13,
      "confidence": 0.96,
      "current": "They all said roughly the same thing: Jin Taekyung had gotten thoroughly drunk, gone to the wrong room, and found that the room belonged to the daughter of the Mount Heng Sword Sect.",
      "defect": "The witness-summary passage again changes a woman of the sect into the sect’s literal daughter.",
      "id": "R0013-03",
      "rationale": "The source identifies the room’s occupant by her affiliation with the Mount Heng Sword Sect, not by assigning a literal parent-child relationship to the sect.",
      "replacement": "They all said roughly the same thing: Jin Taekyung had gotten thoroughly drunk, gone to the wrong room, and found that the room belonged to a woman of the Mount Heng Sword Sect.",
      "severity": "critical",
      "source": "진태경이 거나하게 취해서 방을 잘못 찾았고, 그 방의 주인이 항산검문의 여식이었다는 것."
    }
  ]
}
```

## Chapter 9

### Korean source

```text
＃9화



띠링.



- [진가보법]을 습득하셨습니다.

- 해당 무공을 대성할 시 여러 효과를 얻을 수 있습니다.

- 업적, [무공을 익히다]를 달성하셨습니다.

- 업적 달성 보상으로 칭호, [초보 수련자]를 획득합니다.



“어이고.”

시스템 알림이 뜬 순간 털썩 주저앉았다. 먼지가 풀풀 피어올랐지만 무슨 상관이냐, 어차피 이미 거지꼴이다.

‘뭐가 이렇게 빡세냐.’

진태경의 서재에는 단 두 종류의 책이 존재했다.

야설. 그리고 야설이 아닌 것. 사백여 권에 달하는 책 중 야설을 제외하니 백여 권이 남았다.

‘대단한 놈.’

한국에서 태어났으면 불법 성인 사이트 운영자, 미국에서 태어났다면 징역을 살았을 놈이다. 어쨌든 그렇게 분류를 끝내 놓으니 무공 비급은 삼십여 권에 불과했다.

‘비급을 야설의 절반만 모았어도.’

나로서는 애석한 일이었지만 수확은 있었다. 당장 필요한 무공 비급을 발견했으니까.

진가창법과 진가보법. 너무 오랫동안 수련을 하지 않아 잊고 있었다는 태원진가의 가전 무공이다.

‘진가보법 확인.’

띠링.



스킬창



[진가보법]

종류 : 보법

등급 : 일류

제한 : 태원진가의 직계

경지 : 일 성

설명 : 태원진가의 시조가 창안한 보법. 변화가 적고 단조로우나 실전적이다.





진가창법의 설명도 크게 다르지 않았다. 다만.

‘변화가 적고 단조롭긴 개뿔.’

시조인가 시조새인가 하는 양반이 만들었다는 가전 무공은 더럽게 복잡했다. 어젯밤 일만 생각하면 저절로 이가 갈릴 정도다.



- [진가보법]의 습득을 시작합니다.

- 구결을 암기 중입니다. 무공의 등급과 지력 수치에 따라 속도가 달라집니다.



그래, 딱 여기까지는 괜찮았다. 문제는 그다음부터였다.



- [진가보법]의 투로를 표시합니다. (0 / 100)



시스템이 표시한 발자국을 따라 보법을 밟는데, 얼마나 꼬장꼬장하고 칼 같은지 표시한 발자국에서 조금이라도 벗어나면 실패. 다음 동작이 늦어도 실패다.

그렇게 전체 투로를 정확히 밟아야 1회 완수다.

‘미친 좆망겜.’

현실에서의 나와 지금의 캐릭터는 체격의 차이가 크다. 키는 반 뼘 가까이 줄어들었고 리치도 짧다. 세밀한 조정이 안 되니 실수가 연이어 터졌다.

‘성공한 게 기적이다.’

100회를 채우고 나니 손발이 덜덜 떨렸다.

‘그래도 하나는 얻었어.’

오랜 헌터 생활로 전투, 특히 집단전이라면 이골이 났다. 생사를 오가는 싸움에서 가장 중요한 것은 첫째가 운, 둘째가 발이다.

전진. 후퇴. 혹은 정지. 팔이 잘려도 다리만 움직이면 살 수 있다. 하지만 다리가 잘리면 그걸로 끝이다.

발이 나가야 팔이 나간다. 내가 겪은 전투들은 그랬고, 그것이 보법을 먼저 익힌 이유였다.

‘하지만…….’

너무 느리다. 시스템의 힘을 빌렸음에도 반나절이 훌쩍 흘렀는데 창술까지 익히려면 얼마나 더 시간이 필요할까.

‘오늘로 5일째.’

가상현실 게임은 현실에 비해 시간이 빠르게 흐른다고 했다. 하지만 시간 배율을 감안하더라도 5일은 긴 시간이다.

“후우.”

나는 한숨과 함께 잡념을 애써 털어 버렸다.

구조? 로그아웃? 지금은 가능성에 매달리기보다 혼자서라도 계속 나아가야 할 때다.

‘그럼 오늘은 여기까지.’

나는 무공 비급들을 챙겨 일어났다.

그리고 2층 침실에 도착했을 때, 비급들 사이에 이색적인 책 한 권이 끼어 있다는 사실을 깨달았다.



[야왕 대물남]



“크흠.”

아이고, 이런 실수를.



* * *



“벌써 기침하셨습니까?”

하인은 휘둥그레진 눈으로 나를 바라봤다. 그의 손에는 아침 식사가 놓인 쟁반이 들려 있었다.

“잠이 잘 안 와서…….”

내 대답은 사실이다. 그 원인은 운기조식에 있었다.

‘이거 효과 죽이네.’

운기조식은 정신과 오감을 맑게 하는 것 외에도 피로를 해소하는 효능이 있었다. 곰곰이 생각해 보니 운기조식을 하게 된 이후로 피곤한 적은 없었던 것 같다.

‘통증도 거의 사라졌고.’

“상처가 덧날 수도 있으니 너무 무리하지 마십시오.”

하인의 말에 가슴 한구석이 따뜻해진다. 이 거지 같은 게임에도 한 줄기 빛 같은 NPC가 있구나. 드디어 정상인을 만났어.

‘이게 뭐라고 울컥하냐.’

나는 먹먹해진 얼굴로 아침 식사를 시작했다.

하나같이 짜거나 싱거운 반찬들이었지만 허기를 반찬 삼아 해치우고 탕약 그릇을 한 번에 들이켰다.

“크으.”

저절로 눈살이 찌푸려지는 맛이다. 이윽고 상을 모두 치운 하인이 고개를 조아렸다.

“그럼 소인은 이만.”

“아, 잠깐만요.”

“말씀 낮추십시오. 어찌 제게 말을 높이십니까?”

생각해 보니 그러네.

처음에는 그래픽과 인공지능이 너무 현실적이라 만나는 NPC마다 존대를 썼지만 이제는 어느 정도 익숙해진 상태.

비로소 유저의 존엄성을 되찾을 때가 온 것이다. 나는 준엄하게 대답했다.

“당분간은 저 편한 대로 할게요.”

시바, 차마 말을 못 놓겠다. 딱 봐도 마흔은 넘어 보이는 아저씨한테 이놈 저놈 할 수는 없는 일 아닌가.

망할 게임, 쓸데없이 그래픽만 좋아서 반말도 못 하겠다.

‘이러다가 NPC랑 친구도 먹겠네.’

내가 머리를 다쳤다는 사실을 어필하자 하인도 마지못해 고개를 끄덕였다.

“어쩔 수 없군요. 한데 시키실 일이?”

“비는 방 없나 해서요.”

하인이 고개를 갸웃했다.

“구해 드릴 수는 있습니다만, 혹 용도가 어찌 되시는지.”

“무공 수련을 하려고요.”

“예?”

“여기 있는 방들은 죄다 더럽거나 답답해서…… 그런데 표정이 왜 그러세요?”



* * *



전각을 나온 하인이 곧장 달려간 곳은 가주 집무실이었다.

하인의 보고가 끝나자 서류 탑 너머로 진위경의 근엄한 목소리가 울렸다.

“수고했네.”

하인이 떠나기가 무섭게 벌떡 일어난 진위경이 서류를 허공에 흩뿌렸다.

“경사다! 오늘 일 안 해!”

“누구 맘대로요?”

흩날리는 서류를 남김없이 잡아챈 위팽이 한숨을 내쉬었다.

“이러시는 거 다른 사람들이 알면 또 말 나옵니다.”

“지금 셋째가 본격적으로 무공을 익히겠다는데 뭐가 더 중요한가!”

“그것보다는 장로원에서 벼르고 있다는 사실이 중요하죠.”

장로원. 그 단어에 진위경의 표정이 가라앉았다.

“망할 노친네들.”

“조만간 가로회의가 열릴지도 모르겠습니다. 저들 입장에서는 틈이 보이니 물어뜯는 것이 당연하지요.”

회의 안건은 보나 마나 뻔하다. 진태경의 평소 행실로 시작해서 소문주인 자신에 대한 공격으로 끝날 것이다.

“그 작자들도 참 끈질겨.”

“하루 이틀 일입니까? 오래된 기둥에는 벌레가 끓는 법입니다.”

“방법이 없을까?”

“결국 또 삼공자의 방패 역할을 자처하시는군요.”

위팽이 한숨을 내쉬었다.

“주군. 속하가 한 말씀 올려도 되겠습니까?”

“거절하겠네.”

“그럼 저도 거절하겠습니다. 문파 공금 횡령만 다섯 번쨉니다. 다른 것들은 셀 수도 없어요. 본가의 문규대로 집행했으면 삼공자는 살아 있는 게 기적입니다.”

“어허. 이 사람.”

“말이 나왔으니 하는 얘긴데, 본가 식솔 아무나 붙잡고 물어보십쇼. 주군 입장에서야 사랑하는 동생이지, 다른 사람들은…… 어휴, 말도 못 합니다.”

“자네 우리 막내한테 무슨 불만 있나? 말투가 왜 그래?”

“답답해서 그럽니다. 답답해서. 삼공자가 사고 치면 주군이 수습하고, 그거 막아 주느라 장로원 요구 들어주고. 이렇게 야금야금 주도권을 뺏기고 있잖습니까. 요즘 어떤 소문까지 도는 줄 아십니까?”

“어떤 소문?”

“삼공자가 장로파라는 말도 있습니다. 장로원 쪽에서 용돈 받아서 쓰고 일부러 사고 치는 거라고요.”

진위경의 눈꺼풀이 파르르 떨렸다.

“이런 천인공노할!”

“저는 차라리 그랬으면 좋겠습니다. 장로원 쪽에서 은전이라도 찔러 주면 공금 횡령은 안 할 테니까요.”

“자네…….”

“할 말 다 했습니다. 자를 거면 자르십쇼.”

끙. 진위경이 깊은 한숨을 내쉬었다.

“나도 슬슬 이대로는 안 된다고 생각하고 있네.”

“생각 좋죠. 실행에 안 옮기시니 문제죠.”

“그래도 이번만큼은 최대한 힘써 봐야지.”

“아이고, 주군…….”

“이번이 마지막일세. 내 분명히 약속하지.”

진위경이 정색하고 말했다. 위팽이 의뭉스러운 목소리로 물었다.

“정말이십니까?”

“아직 기억도 온전치 않은 아이야. 게다가…… 하루아침에 다른 사람처럼 변했어. 자네도 느끼고 있잖은가.”

“그거야 그렇지만…….”

위팽이 말꼬리를 흐렸다.

확실히 삼공자는 변했다. 기억을 잃은 것이 거짓말이든, 사실이든 현재 보여 주는 모습은 확실히 희망적이다.

잠시 생각에 잠겨 있던 진위경이 입을 뗐다.

“위팽.”

“예.”

“내 이름으로 명령서 하나 만들게.”

“어떤……?”

“적당한 죄목 몇 개 가져다 쓰고 처벌로 수련동에 강제 폐관 시켜.”

“아하.”

위팽은 이마를 탁 쳤다. 다분히 보여 주기식이지만 현재 상황에서는 훌륭한 응급 처치다. 곧 있을 가로회의에서 받을 압박을 해소하면서 진태경에 대한 처벌 수위를 낮출 수 있기 때문이다.

거기에 덧붙여…….

“삼공자의 부탁도 들어주게 됐군요. 수련할 곳을 찾고 있었으니 말입니다.”

이거야말로 일석삼조 아닌가. 위팽은 진심으로 감탄했다.

“역시 주군이십니다.”

“우리 집안사람들이 이래. 아, 내가 그거 말했나? 태경이도 어릴 때 참 영특했는데, 어느 하루는…….”

“……명령서 작성하러 가 보겠습니다.”



* * *



“하여, 열네 가지 법규를 어겨 문내 기강을 흐트러트린 삼공자 진태경에게 무기한의 수련동 폐관을 명한다.”

이름이…… 위팽이라고 했던가? 밥맛없게 생긴 놈의 말을 잠자코 듣고 있다가 번쩍 손을 들었다.

“저, 질문 있는데요.”

“하십시오.”

“무기한의 뜻이 뭡니까?”

위팽이 떨떠름하게 대답했다.

“정해진 기한이 없다는 겁니다.”

“아.”

난 또 게임 언어 시스템이 오류 난 줄 알았지. 다행히 내가 아는 뜻이랑 같다. 하하.

“하하하.”

“허허허.”

원래 웃음은 전염되기 마련이다. 위팽과 같이 온 무사들도 나를 따라 웃기 시작했다.

그렇게 훈훈해진 분위기에서 위팽이 마지막 줄을 읊었다.

“죄인 진태경은 오라를 받들라.”

“싫어.”

“……?”

“……?”

“싫다고. 시바.”

포승줄을 들고 다가오던 두 놈이 이게 아닌데, 하는 눈으로 위팽을 바라봤다. 그러거나 말거나 나는 내 할 말을 했다.

“내가 수련하게 방 하나만 구해 달랬지 감옥에 넣어 달랬냐?”

완전히 정신병자 새끼들 아냐, 이거?

“자, 삼공자. 진정하고 내 말을 들어 보시오.”

“듣기는 시벌, 수련동에는 수련에 필요한 모든 것이 있습니다. 복지도 나쁘지 않습니다. 이딴 말이나 할 거 아냐.”

표정을 보니 제대로 짚었다. 나는 쐐기를 박아 넣었다.

“군인 월급 오르니까 행복하게 군대 다녀오라고 할 놈들이네, 이거. 몰라, 나 안 들어가. 그냥 방이나 마당에서 나 혼자 수련할래.”

솔직히 수련동이라는 곳, 단편적으로 생각해 봤을 때는 나쁘지 않다.

하지만 무기한이라는 말이 가시처럼 걸린다. 당장 무공 익히고 레벨 업이 시급한데 수련동에서 백날 천날 목 빼고 꺼내 주기만 기다릴 수는 없으니까.

나는 그대로 벌렁 누워 버렸다.

“배 째!”

“삼공자. 적당히 하고 일어나시지요.”

위팽이 인상을 쓰고 노려보았다.

“다 공자를 위해 소가주께서 결정하신 겁니다.”

“진위경, 아니 형님이?”

그 동생 바보가 이런 명령을 내렸다고?

그때 위팽의 입술이 달싹였다. 동시에 귓가로 어떤 음성이 들려왔다. 육성과는 다른 기묘한 느낌이었다.

- 전음입니다. 놀라지 말고 들으십시오.

전음. 무협지에서 본 기억이 있다. 고수들만 사용한다는 일종의 텔레파시.

- 기억을 잃어서 잘 모르시겠지만, 삼공자는 요주의 인물입니다. 조만간 더 큰 처벌이 내려질 수 있어 그전에 소가주께서 미리 조치하시는 겁니다.

27년 한평생 열심히 살았는데 가중 처벌이 웬 말이냐.

슬퍼하는 내 귓가로 위팽의 전음이 이어졌다.

- 말이 무기한이지, 소가주께서 공자를 평생 수련동에 처박아 놓으실 거라 생각하십니까?

나는 고개를 저었다. 그 양반이라면 그럴 리가 없다. 수련동에 단둘이 처박히기를 원한다면 모를까.

- 길어도 칠주야(七晝夜) 안에 꺼내 드리겠습니다. 어떻습니까?

위팽의 눈에서 강렬한 의지가 엿보였다. 이것까지 거절하면 두들겨 패서라도 데려갈 것 같다.

‘시벌, 여기 NPC들은 죄다 깡패야, 뭐야.’

야, 이 새끼야. 니가 그렇게 싸움을 잘해?

나는 [기감]을 끌어올려 위팽의 레벨을 확인했다.



[Lv.???]



“…….”

깡패 맞네. 레벨 깡패. 저놈도 진위경 못지않은 인간 백정일 것이다. 위팽이 눈을 부릅뜨고 물었다.

- 어쩌시렵니까?

나는 두려움에 떨면서도 손가락 세 개를 펴 보였다.

- ……사흘 안에 빼 달라고요?

뭐 이런 새끼가 다 있냐. 그런 얼굴로 나를 노려보던 위팽이 이내 한숨과 함께 말했다.

“뫼셔라.”

#수련동 #폐관 #협상 #성공적.
```

### Current accepted English

```markdown
# Chapter 9

Ding.

> **System**
>
> - You have acquired **Jin Family’s Manoeuvre Technique**.
>
> - You can obtain various effects upon mastering this martial art.
>
> - You have completed the achievement **Learn a Martial Art**.
>
> - As an achievement completion reward, you have acquired the title **Novice Trainee**.

“Good grief.”

The moment the System notification appeared, I slumped to the floor. Dust billowed into the air, but who cared? I already looked like a bum anyway.

*Why is this so damn hard?*

There were only two kinds of books in Jin Taekyung’s study.

Erotic novels. And books that weren’t erotic novels.

Of the more than four hundred books, only about a hundred remained after I took out the erotic novels.

*What an incredible bastard.*

If he’d been born in Korea, he would’ve been running an illegal adult website. If he’d been born in America, he’d be serving a prison sentence.

At any rate, once I finished sorting them, there were only about thirty martial arts manuals.

*If only he’d collected half as many manuals as erotic novels.*

It was a shame from my perspective, but I had still made a worthwhile discovery. I’d found the martial arts manuals I needed right now.

The Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique. They were hereditary martial arts of the Jin Family of Taiyuan—arts I’d forgotten because I hadn’t practiced them in far too long.

*Let’s check the Jin Family’s Manoeuvre Technique.*

Ding.

> **System**
>
> Skill Window
>
> **Jin Family’s Manoeuvre Technique**
>
> **Type:** Manoeuvre Technique
>
> **Grade:** First Rate
>
> **Restriction:** Direct descendants of the Jin Family of Taiyuan
>
> **Realm:** First Stage
>
> **Description:** A manoeuvre technique devised by the founder of the Jin Family of Taiyuan. It has few variations and is monotonous, but it is practical.

The description of the Jin Family’s Spear Technique wasn’t much different. Except…

*“Few variations and monotonous,” my ass.*

The hereditary martial art created by some fellow called the founder—or was it the family’s founding granddad?—was unbelievably complicated. Just thinking about last night made my teeth grind.

> **System**
>
> - You are beginning to acquire **Jin Family’s Manoeuvre Technique**.
>
> - You are memorizing the formula. The speed varies according to the martial art’s grade and your Intelligence stat.

Right. Everything was fine up to that point.

The problem started after that.

> **System**
>
> - The movement sequence for **Jin Family’s Manoeuvre Technique** is being displayed. (0 / 100)

I followed the footprints displayed by the System and practiced the manoeuvre technique. But the footprints were so fussy and razor-precise that stepping even slightly outside them meant failure. Taking too long to perform the next movement also meant failure.

I had to follow the entire sequence perfectly to complete it once.

*What a fucking garbage game.*

There was a major difference between my real-world physique and the character’s. My height was shorter by nearly half a handspan, and my reach was shorter too. I couldn’t make the fine adjustments I needed, so one mistake followed another.

*It’s a miracle I succeeded at all.*

After completing the sequence one hundred times, my hands and feet were trembling.

*Still, I gained something.*

After years of working as a Hunter, I was thoroughly familiar with combat—especially group battles. In fights where life and death were on the line, the most important thing was luck first and your feet second.

Moving forward. Retreating. Or stopping.

Even if your arm was cut off, you could survive as long as your legs still moved. But if your legs were cut off, it was over.

Your feet had to move before your arms. That was how all my battles had gone, and it was why I had chosen to learn a manoeuvre technique first.

*But…*

It was too slow. Even with the System’s help, half a day vanished in the blink of an eye. How much longer would it take if I also had to learn spear techniques?

*Today makes five days.*

I’d heard that time passed faster in virtual-reality games than in the real world. But even after accounting for the time multiplier, five days was a long time.

“Fuu…”

I forced away my distractions with a sigh.

Rescue? Logout?

This wasn’t the time to cling to possibilities. I had to keep moving forward, even if I had to do it alone.

*That’s enough for today.*

I gathered up the martial arts manuals and stood.

When I reached the bedroom on the second floor, I realized that one unusual book had been mixed in among the manuals.

**The Night King: Well-Endowed Man**

“Ahem.”

Oh dear. What a mistake.

* * *

“Are you up already?”

The servant stared at me with wide eyes. He was holding a tray with breakfast on it.

“I couldn’t sleep…”

My answer was the truth. That was because I’d been circulating my qi.

*This is ridiculously effective.*

Circulating my qi didn’t just clear my mind and sharpen my senses. It also relieved fatigue. Looking back, I didn’t think I’d felt tired even once since I started circulating my qi.

*The pain is almost gone too.*

“Your wounds could worsen, so please don’t push yourself too hard.”

A warm feeling spread through one corner of my chest at the servant’s words.

*Even this shitty game has an NPC who’s like a ray of light. I’ve finally met a normal person.*

*Why does this make me feel so emotional?*

Feeling strangely choked up, I began eating breakfast.

Every side dish was either too salty or too bland, but I demolished the entire meal because hunger was the best seasoning, then downed the bowl of herbal decoction in one gulp.

“Ugh.”

The taste made me frown instinctively. Once the servant had cleared away the table, he bowed his head.

“Then I shall take my leave.”

“Ah, wait a second.”

“Please speak less formally. Why are you using honorifics with me?”

Come to think of it, he had a point.

At first, the graphics and artificial intelligence had been so realistic that I had used polite speech with every NPC I met. But by now, I had grown somewhat accustomed to them.

The time had finally come to reclaim the dignity of a user.

I answered sternly.

“For now, I’ll speak however I’m comfortable.”

*Fuck, I can’t bring myself to drop the honorifics.*

I couldn’t exactly talk down to a man who clearly looked over forty and call him “you bastard” or “you punk.”

*Damn game. The graphics are so good I can’t even speak informally.*

*At this rate, I’ll end up becoming friends with an NPC.*

When I emphasized the fact that I had suffered a head injury, the servant reluctantly nodded.

“I suppose it can’t be helped. Is there something you require?”

“I was wondering if there was an empty room.”

The servant tilted his head.

“I can arrange one for you, but what might you need it for?”

“I want to practice martial arts.”

“Pardon?”

“All the rooms here are either dirty or stuffy… Why do you look like that?”

* * *

After leaving the pavilion, the servant went straight to the Family Head’s office.

Once his report was finished, Jin Wikyung’s solemn voice rang out from beyond a tower of documents.

“You’ve done well.”

The instant the servant left, Jin Wikyung sprang to his feet and scattered the documents into the air.

“It’s cause for celebration! I’m not working today!”

“Who said you could decide that?”

Wipeng caught every last one of the fluttering documents and sighed.

“If the others find out you’re acting like this, they’ll start talking again.”

“The Third Young Master says he’s going to take up martial arts in earnest. What could possibly be more important than that?”

“The fact that the Elder Council is waiting to pounce on you is more important.”

At the words *Elder Council*, Jin Wikyung’s expression darkened.

“Damn old men.”

“A family council meeting may be held soon. From their perspective, they’ve spotted an opening, so naturally they’ll sink their teeth into it.”

The agenda was obvious. It would begin with Jin Taekyung’s usual conduct and end with an attack on Jin Wikyung himself, the Lesser Family Head.

“Those bastards are persistent.”

“Is this something that started yesterday? Old pillars always end up crawling with bugs.”

“Isn’t there any way around it?”

“So you’re volunteering to serve as the Third Young Master’s shield again.”

Wipeng sighed.

“My lord, may I offer a word?”

“I refuse.”

“Then I refuse as well. This is the fifth time he’s embezzled the family’s public funds. I’ve lost count of the other things. If we had enforced the family rules properly, it would be a miracle if the Third Young Master were still alive.”

“Now, now.”

“Since we’re on the subject, grab anyone in the family and ask them. From your perspective, he’s your beloved little brother. To everyone else…”

Wipeng shook his head.

“Honestly, I can’t even say it.”

“Do you have some complaint against our youngest? Why are you speaking like that?”

“I’m frustrated. That’s all. I’m frustrated. The Third Young Master causes trouble, you clean it up, and you accept the Elder Council’s demands to keep them from making things worse. They’re slowly taking away your authority. Do you know what kind of rumor is going around these days?”

“What rumor?”

“Some people say the Third Young Master is part of the Elder faction. That he gets pocket money from the Elder Council and deliberately causes trouble.”

Jin Wikyung’s eyelids began to tremble.

“That’s an outrage!”

“I’d actually prefer that to be true. If the Elder Council slipped him even a few silver coins, he wouldn’t have to embezzle the family’s funds.”

“You…”

“I’ve said my piece. Fire me if you want.”

With a groan, Jin Wikyung let out a deep sigh.

“I’ve been thinking things can’t go on like this, either.”

“Thinking is good. The problem is that you never put it into action.”

“Even so, I should do my best this time.”

“Oh, my lord…”

“This will be the last time. I give you my word.”

Jin Wikyung spoke with a serious expression. Wipeng asked, sounding skeptical,

“Do you really mean it?”

“He’s still a child whose memory hasn’t fully returned. And besides… he changed into an entirely different person overnight. You’ve noticed it too.”

“That’s true, but…”

Wipeng let his voice trail off.

The Third Young Master had definitely changed. Whether the memory loss was a lie or the truth, the way he was behaving now was undeniably hopeful.

Jin Wikyung thought for a moment before speaking.

“Wipeng.”

“Yes.”

“Prepare an order in my name.”

“What sort of…?”

“Use a few appropriate charges and order him to undergo indefinite confinement in the training hall.”

“Ah.”

Wipeng slapped his forehead.

It was mostly for show, but under the circumstances, it was an excellent emergency measure. It would relieve the pressure Jin Wikyung was about to receive at the upcoming family council meeting while lowering the severity of the punishment imposed on Jin Taekyung.

And on top of that…

“It fulfills the Third Young Master’s request too. He was looking for somewhere to train.”

Wasn’t this three birds with one stone? Wipeng was genuinely impressed.

“As expected, you’re my lord.”

“That’s how my family is. Oh, did I ever tell you? Taekyung was a clever child when he was young, but one day…”

“…I’ll go write the order.”

* * *

“Therefore, for violating fourteen regulations and disrupting discipline within the family, the Third Young Master, Jin Taekyung, is hereby ordered to undergo indefinite confinement in the training hall.”

Was his name Wipeng? I listened silently to the sour-looking bastard, then raised my hand.

“I have a question.”

“Go ahead.”

“What does ‘indefinite’ mean?”

Wipeng answered reluctantly.

“It means there is no set deadline.”

“Oh.”

I’d thought the game’s language system had malfunctioned. Fortunately, it meant the same thing I knew it meant.

Ha ha.

“Ha ha ha.”

“Ho ho ho.”

I thought the game’s language system had glitched. Fortunately, it meant exactly what I thought it meant.

In that warm atmosphere, Wipeng read the final line.

“The convict, Jin Taekyung, shall submit to the bonds.”

“No.”

“…”

“…”

“I said no. Fuck.”

The two men approaching with rope restraints looked at Wipeng as if to say, *This isn’t how it was supposed to go.*

I ignored them and said what I had to say.

“I asked you to find me a room so I could practice, not put me in prison. Are you people completely fucking insane?”

“Now, Third Young Master. Calm down and listen to me.”

“Listen to what, for fuck’s sake? You’re going to say the training hall has everything needed for practice and the living conditions aren’t bad. You’ll spout that kind of nonsense.”

Judging by Wipeng’s expression, I’d hit the nail on the head. I drove the point home.

“You people would tell someone to go happily serve in the army because military pay had gone up. Forget it. I’m not going in. I’ll practice by myself in my room or in the yard.”

Honestly, on the surface, the training hall didn’t sound so bad.

But the word *indefinite* stuck in my mind like a thorn. I needed to learn martial arts and Level up immediately. I couldn’t spend day after day in the training hall, craning my neck and waiting to be let out.

I flopped onto the floor.

“Go ahead and gut me!”

“Third Young Master, that’s enough. Please get up.”

Wipeng scowled at me.

“The Lesser Family Head made this decision entirely for your sake.”

“Jin Wikyung—I mean, my brother?”

That brother-obsessed idiot had given this order?

At that moment, Wipeng’s lips moved.

At the same time, a voice reached my ears. It felt strange, unlike an actual spoken voice.

> “This is Sound Transmission. Don’t be alarmed—just listen.”

Sound Transmission. I remembered seeing it in martial arts novels. A kind of telepathy that only masters could use.

> “You may not know this because you’ve lost your memory, but the Third Young Master is a person of concern. A harsher punishment may be handed down soon, so the Lesser Family Head is taking action beforehand.”

I had worked hard for twenty-seven years. What did I do to deserve an aggravated sentence?

As I lamented, Wipeng’s Sound Transmission continued in my ear.

> “It may be called indefinite confinement, but do you really think the Lesser Family Head intends to bury you in the training hall for the rest of your life?”

I shook my head.

*There’s no way he’d do that.*

Not unless he wanted the two of us locked up together in the training hall.

> “I’ll get you out within seven days and nights at the latest. How does that sound?”

There was fierce determination in Wipeng’s eyes. If I refused this too, he looked ready to beat me and drag me there if he had to.

*Fuck, are all the NPCs here thugs or what?*

*Hey, you bastard. Are you really that good at fighting?*

I raised my Qi Sense and checked Wipeng’s Level.

> **System**
>
> - **Lv. ???**

“…”

*He really is a thug.*

A Level thug, at least.

He was probably every bit the human butcher Jin Wikyung was.

Wipeng opened his eyes wide and asked,

> “What will you do?”

Even as I trembled with fear, I held up three fingers.

> “…You want me to get you out in three days?”

*What kind of bastard is this?*

Wipeng glared at me with that exact look, then finally sighed.

“Escort him.”

#TrainingHall #ClosedDoorTraining #Negotiation #Successful.
```
## Chapter 10

### Korean source

```text
＃10화



십여 분을 걸어 도착한 곳은 태원진가의 후방을 가로막은 절벽이었다. 커다랗게 아가리를 벌린 동공(洞空). 그 앞에 한 사람이 있었다.

“음. 왔느냐?”

불곰 같은 덩치에 근엄한 말투. 진위경이다. 나는 엉거주춤하게 고개를 숙여 보였다.

“안녕하십니까, 형……님.”

진위경은 껄끄러운 존재다. 졸지에 NPC 가족이 생긴 것도 모자라 나한테 엄청 관심이 많기 때문이다.

저 봐라, 남들 보는 눈이 있다고 티 내지 않으려고 무지 애쓰는 거. 하지만 자세히 보면 눈동자가 촉촉하게 젖어 있다.

‘감수성 실화냐.’

외관상으로는 삼합회 두목도 한 수 접고 들어갈 것 같은데, 이 게임 캐릭터들은 어째 다 요지경인지 모르겠다.

“네 행실을 더 이상 묵과할 수 없어 소가주이자 가주 대행의 직분으로 폐관을 명했다. 하고 싶은 말이 있느냐?”

‘당연히 있지.’

그러나 짜고 치는 고스톱이다. 수련동으로 오는 길에 위팽에게 돌아가는 사정을 들었다. 태원진가 내에서 권력층 간의 힘 싸움이 있고, 진위경이 내 방패 역할을 해 주고 있다는 것.

이번 강제 폐관 행은 그러니까, 쇼인 거다.



‘어차피 공자도 수련 공간이 필요하다고 하지 않았습니까? 사흘만 참으십시오.’



나는 위팽의 마지막 말을 떠올리며 반성하는 척 고개를 숙였다.

“죗값을 달게 받겠습니다.”

이 연극의 장점은 대사가 짧다는 것이다. 진위경은 애잔한 눈빛으로 마지막 대사를 읊었다.

“죄인을 수련동에 가둬라. 출관 날짜는 차후 통보하겠다.”

말이 끝나기가 무섭게 수련동 입구를 지키던 무사 두 명이 다가와 내 양팔을 붙들었다. 연극이 끝났으니 퇴장할 차례.

나는 수련동 입구에 섰다.

- 필요한 것은 가져다 놨다. 막내야, 무리하지 말거라.

진위경의 전음과 함께 첫발을 내디뎠다.



* * *



수련동은 한마디로 동굴이었다. 그것도 절벽을 파서 만든 인공 동굴. 높고, 넓었다. 그리고 축축했다.

철벅철벅.

수련동 소속 무사를 따라 얼마나 걸었을까. 내가 신은 것이 가죽신인지 물걸레인지 헷갈릴 때쯤 거대한 철문이 나타났다.

‘와…….’

보는 순간 입이 벌어졌다. 통로를 빈틈없이 채운 그것은 문이라기보다 모든 출입을 금지하는 벽처럼 보였다.

안내해 준 무사가 횃불을 들고 외쳤다.

“개문!”

그그긍-

거대한 철문이 천천히 아가리를 벌렸다. 무슨 열려라 참깨 같은 마법 주문은 아니고, 미리 대기하고 있던 NPC 한 명이 삐죽 튀어나와 있는 개폐 장치를 잡아당긴 것뿐이었지만 압도적인 광경이었다.

그리고 내부가 눈에 들어온 순간.

“우와.”

이번만큼은 나도 새어 나오는 탄성을 숨기지 못했다.

처음 수련동에 들어올 때만 해도 축축한 지하 동굴을 생각했는데…….

“이게 다 뭐야.”

넓은 침상에 보기만 해도 기분이 좋아지는 털 이불. 축축하고 울퉁불퉁한 돌바닥 대신 깔끔한 회색 지면이 펼쳐져 있다.

‘시멘트……는 당연히 아니겠고 석회석인가?’

냉기가 감도는 것만 빼면, 아니, 그걸 감안해도 상상 이상으로 괜찮은 환경이다.

‘이게 처벌이라고?’

얼떨떨하게 주위를 바라보는데 등 뒤에서 헛기침 소리가 들렸다. 돌아보니 안내역을 한 수련동 무사다.

“필요한 것들은 모두 갖춰 놓았습니다. 그럼 저는 이만.”

그그긍. 천천히 닫히는 철문을 바라보다가 문득 수련동 입구에서 들었던 전음이 생각났다.



‘필요한 것은 가져다 놨다. 막내야, 무리하지 말거라.’



아아, 그것은 동생을 생각하는 NPC의 마음.

이 못난 유저는 목 놓아 웁니다.



* * *



현실에서도 숱하게 일어나는 일이다. 비리를 저지른 고위층들이 휠체어를 타고 검찰을 드나들고, 수사를 피하기 위해 병원 특실에 입원하는 것.

조금 다르긴 해도 내가 지금 그 모양새다. 나는 감동한 얼굴로 수련동 특실을 바라봤다.

“이런 게 금수저의 삶이구나.”

그래픽, 인공지능만 현실적인 게 아니다. 아무리 날고 기어도 금수저가 최고라는 사회적 메시지를 담고 있다.

세상에, 이 캐릭터 아니면 어쩔 뻔했어. 아빠가 가주, 큰형이 소가주에 둘째 형은 무공의 천재다. 마음 놓고 기루 죽돌이 짓 할 만하다.

‘진태경 이 새끼…….’

알고 보니 어린 나이에 세상 돌아가는 이치를 깨달은 대현자가 아닌가.

나는 현실적인 갓-수저 시스템에 전율하며 백여 평에 달하는 수련동을 돌아다녔다. 그리고 수련동 무사가 말한 ‘필수품들’을 찾을 수 있었다.

‘우선 식량.’

식량은 항아리 두 개에 나뉘어 보관되어 있었다. 속을 들여다보니 약재 냄새가 진하게 풍기는 주먹밥이다.



아이템창



[뛰어난 벽곡단]

종류 : 단환

등급 : 일류

제한 : 없음

설명 : 온갖 좋은 약재를 무식하게 때려 박아 만든 벽곡단. 섭취 시 원기를 회복하며, 장복할 경우 추가적인 효과를 얻는다.





“아, 이게 바로 그 벽곡단?”

무협 소설에서 많이 봤다. 가볍고 부피가 작아서 휴대하기 편한 데다 영양 보충까지 된단다. 나머지 항아리에도 벽곡단이 그득했다.

‘일단 인벤토리에 넣어 둬야지.’

양손으로 항아리를 잡고 중얼거렸다.

“아이템 습득.”

다른 사람이 이 모습을 봤다면 놀라 자빠졌을 거다. 멀쩡하게 놓여 있던 항아리 두 개가 증발한 듯이 사라졌으니까.

나는 인벤토리에 수납된 항아리를 흐뭇하게 바라봤다.

‘이걸로 식량 문제는 해결됐고.’

그다음으로 발견한 두 번째 필수품은 물이다. 수련동 내부는 엄연히 동굴이라, 한쪽 구석에 차가운 지하 샘물이 있어 식수 문제를 해결해 주었다.

그리고 마지막 세 번째.

“흠.”

여러 개의 병기가 나란히 걸려 있는 무기 거치대. 당연하게도 가장 먼저 손에 쥔 것은 단단해 보이는 목창(木槍)이다.

‘아이템 감정.’

띠링.



아이템창



[수련용 목창]

종류 : 병장기

등급 : 삼류

제한 : 없음

설명 : 초보자용으로 제작되었다.





“오.”

초보자를 대상으로 만들어진 수련용 목창. 지금의 내게 딱 맞는 물건이다. 여기에 하나만 더 있으면 완벽하지.

“인벤토리 오픈.”

나는 씩 웃으며 인벤토리에서 [진가창법]이 적힌 비급을 꺼냈다.

띠링.



- [진가창법]을 습득하시겠습니까? (3 / 10)



“당연히 예스지.”

나는 시스템이 참 좋다. 가끔은 사랑스럽다.



* * *



어제 진가보법을 익히며 처음 알게 됐다. 시스템 알림은 띠링, 하나만이 아니라는 사실을.

그리고 저 소리가 얼마나 듣기 싫은 소리인지를.

삑!



- 동작이 실패했습니다.

- 남은 성공 횟수 (2 / 100)



실패 메시지. 일명 삑사리가 나면 어김없이 뜨는 시스템창이다. 도대체 몇 번째 보는 메시지인지 모르겠다.

나는 손에 쥔 [수련용 목창]을 바라봤다.

‘잘못 생각했네.’

목창이라 그런가, 가볍다. 찌르면 찌르는 대로, 휘두르면 휘두르는 대로 빠르게 움직인다. 그래서 문제다.

‘너무 가벼워서 조절하기가 힘들어.’

미세한 조정이 어렵다 보니 자꾸만 삐끗한다. 더럽게 깐깐한 시스템이 그런 사소한 실수를 눈감아 줄 리가 없다.

삑.



- 동작이 실패했습니다.

- 남은 성공 횟수 (5 / 100)



“아오. 시발.”

결국 [수련용 목창]을 내던지고 [예리한 창]을 인벤토리에서 꺼냈다. 길이나 창대의 굵기가 내가 현실에서 쓰던 창과 얼추 맞아떨어진다.

그런데 왜 처음부터 꺼내지 않았냐고?

“더럽게 무겁네. 진짜.”

통짜 강철로 만들었다 보니 무게가 장난이 아니다. 체감상 느껴지는 무게만 얼추 50kg에 육박하는 괴물인 것이다.

이런 걸 몇 시간이고 휘둘렀다가는 내 체력이 못 버틴다.

현재 내 경지는 이류, 시스템의 힘을 빌렸다지만 쌀 반 가마니가 넘는 무게를 팔랑개비처럼 휘두르는 건 무리다.

‘어디서 호랑이 기운이 솟아나는 것도 아니고.’

그런 생각을 했을 때였다.

“……어?”

내가 방금 뭐라고 했지? 호랑이 힘?

“있네?”

이곳은 게임이다. 시스템이 있고 능력치가 있다. 그리고 공력이 있다. 심법을 통해 이끌어 낼 수 있는 10년의 공력이!

잠깐이나마 잊고 있었다는 게 쪽팔릴 정도다.

“내가 그런 걸 써 봤어야지…….”

고기도 먹어 본 놈이 안다고 했다. F급 헌터가 괜히 F급이겠나. 마나라고는 쥐뿔도 없이 맨몸으로 때우니까 헌터들 사이에서도 반푼이 취급받는 거다.

‘그래도 문제 하나는 해결했네.’

허허, 나는 어이없게 웃으며 창을 집어 들었다. 그리고 천천히, 신중하게 공력을 끌어 올렸다.

머릿속에서는 시스템이 각인시킨 진가심법의 구결이 빠르게 되감기며 공력을 정해진 길로 이끈다.

찌릿.

반응은 즉각적이었다.

단전에 웅크리고 있던 10년 공력이 전신으로 퍼져 나간다. 게임이라서, 무림인이라서 느낄 수 있는 그 기운이 사지백해로 뻗어 나가는 것이 느껴졌다.

‘이건…….’

온몸에 힘이 넘쳐흐른다. 월등히 상향된 신체 능력과 감각은 F급 헌터로 살아온 내게 다시 한번 황홀함을 선사해 주었다.

‘이렇게 달라질 수 있다니.’

나는 창을 잡고 [진가창법]을 펼쳤다. 더 이상 무겁게 느껴지지 않는 50kg의 철창은 내가 원하는 길을 따라 허공을 찌르고 베었다.

이윽고.

띠링.



- 남은 성공 횟수 (6 / 100)



기다리던 알림이 울리기 시작했다.



* * *



진위경이 근심 섞인 얼굴로 입을 열었다.

“잘하고 있겠지?”

“잘하고 있겠지요. 염치가 있으면.”

“아직 몸도 성치 않은데…… 괜찮겠지?”

“모르는 사람이 보면 삼공자가 오늘내일하는 줄 알겠습니다. 저 정도면 침 발라도 나아요.”

“아니야. 막내가 어릴 때부터 얼마나 허약했는지 자네가 몰라서 하는 말이야.”

위팽이 기가 찬 얼굴로 대답했다.

“삼공자 입으로 들어간 영약과 보양제만 해도 방 하나를 채울 겁니다. 그리고 벌써 잊으셨습니까? 작년에 있었던 백년설삼 절도 사건!”

“어허. 그건…….”

“그때 약왕당주가 대노해서 삼공자 배를 갈라 보겠다고 날뛰는데, 솔직히 말리면서도 그런 생각이 들더군요. 갈라도 정당방위라고.”

진위경은 슬쩍 시선을 회피했다. 결국 진위경의 개인 사재를 털어 보상하는 것으로 마무리됐지만 당시 약왕당주의 분노는 대단했다.

“그 정도 영약을 꿀꺽했으니 모르긴 몰라도 죽을 때까지 잔병치레는 안 할 겁니다.”

“그래도 부족해. 자네는 딱 보면 모르나? 나는 막내 볼 때마다 안쓰러워. 애가 뼈다귀에 살점 몇 개 붙어 있는 꼴이잖나. 아침마다 비리비리해서 힘도 없고.”

“힘이 없다고요?”

위팽은 순간 과거에 들었던 소문을 떠올렸다. 태원 홍등가 기녀들 사이에서 진태경이 야왕(焲王)이라는 별명으로 불린다는 소문이었다.

‘도대체 어느 정도길래.’

약발 하나는 제대로 받은 모양이군. 위팽은 자신도 모르게 팔뚝을 들어 크기를 상상해 보았다.

“자네 뭐 하나?”

“아, 아닙니다.”

진위경은 산더미처럼 쌓인 서류 더미를 보며 한숨을 내쉬었다.

“막내도 그렇고, 가문 안팎으로 신경 쓸 일 천지야. 특히…… ‘그들’이 접선해 온 것도 꺼림칙하고.”

“항산검문 말씀이시군요.”

항산검문. 그 이름이 갖는 무게는 결코 가볍지 않았다.

수십 년 전, 어느 불패(不敗)의 낭인이 현판을 내건 이래 무서운 속도로 성장해 왔고, 작금에 이르러서는 태원진가의 입지를 위협할 정도가 되었다.

“무슨 의도일까?”

“수하들을 풀어 알아보고 있습니다.”

진위경은 항산검문에서 온 서신을 만지작거렸다.

왜? 어떤 목적으로 그들이 오는가? 꼬리에 꼬리를 무는 의문 끝에 내린 결론은 하나였다.

“산서성 각 지부에 알리게. 항산검문의 목적이 무엇이든 간에 만반의 준비를 갖추라고.”

이곳은 무림이다.

준비된 자만이 살아남아 내일을 맞이할 수 있으리라.
```

### Current accepted English

```markdown
# Chapter 10

After walking for more than ten minutes, we arrived at a cliff that blocked off the rear of the Jin Family of Taiyuan. A massive cavern gaped open in its face. One person stood in front of it.

“Hmm. You came?”

He had the build of a brown bear and spoke in a solemn tone.

Jin Wikyung.

I gave an awkward bow.

“Hello, big… brother.”

Jin Wikyung was an awkward presence. As if suddenly gaining an NPC family wasn’t enough, he also paid an absurd amount of attention to me.

Just look at him. He was trying so hard not to show it in front of everyone else. But if you looked closely, his eyes were moist.

*Is this guy seriously that sentimental?*

With his appearance, he looked like the kind of man who could make even a triad boss back down. Yet somehow, every character in this game was completely bizarre.

“I can no longer overlook your conduct. As the Lesser Family Head and acting Family Head, I have ordered you to undergo closed-door training. Do you have anything to say?”

*Of course I do.*

But this was all a staged performance. On the way to the training hall, Wipeng had explained what was really going on. There was a power struggle among the upper ranks of the Jin Family of Taiyuan, and Jin Wikyung was acting as my shield.

This forced confinement was, in other words, a show.

*The Young Master needed a place to train anyway, didn’t he? Just endure it for three days.*

Remembering Wipeng’s final words, I bowed my head as if repenting.

“I will gladly accept my punishment.”

The advantage of this play was that the lines were short.

Jin Wikyung delivered his final line with a sorrowful look in his eyes.

“Confine the criminal to the training hall. The release date will be announced later.”

The moment he finished speaking, two warriors guarding the entrance to the training hall approached and grabbed me by both arms.

The play was over. Time for me to exit the stage.

I stood at the entrance to the training hall.

*I’ve had everything you need brought there. Little brother, don’t overdo it.*

Along with Jin Wikyung’s Sound Transmission, I took my first step inside.

* * *

The training hall was, in a word, a cave. An artificial cave dug into a cliff, at that. It was tall, spacious, and damp.

Splash. Splash.

How long had I been walking behind the warrior assigned to the training hall? By the time I could no longer tell whether I was wearing leather shoes or wet mops, a massive iron gate appeared.

*Wow…*

My mouth fell open the moment I saw it. Filling the passageway without leaving a gap, it looked less like a door and more like a wall blocking all entry and exit.

The warrior leading me raised his torch and shouted,

“Open the gate!”

Grrrnnng—

The massive iron gate slowly opened its jaws. It wasn’t some magical command like “Open, Sesame.” One NPC who had been waiting nearby simply grabbed and pulled the protruding gate mechanism.

Even so, it was an overwhelming sight.

And the moment I saw what lay beyond it—

“Whoa.”

This time, I couldn’t hide the exclamation that escaped me.

When I had first entered the training hall, I had imagined a damp underground cave.

“What is all this?”

A broad bed covered in a furry blanket lifted my spirits just by looking at it. Instead of a damp, uneven stone floor, a neat gray surface stretched out before me.

*Cement… Obviously not. Limestone?*

Even with the chill in the air, the environment was far better than I had imagined.

*This is supposed to be a punishment?*

I looked around in a daze, then heard someone clear his throat behind me. It was the warrior who had guided me here.

“We’ve prepared everything you need. I’ll be going now.”

I watched the iron gate slowly close with another grinding sound, then suddenly remembered the Sound Transmission I had heard at the entrance to the training hall.

*I’ve had everything you need brought there. Little brother, don’t overdo it.*

Ah. The heart of an NPC who cared about his little brother.

This pathetic user was bawling his eyes out.

* * *

It was something that happened all the time in the real world, too. High-ranking officials who had committed corruption showing up at the prosecutors’ office in wheelchairs, or checking themselves into private hospital rooms to avoid investigation.

My situation was a little different, but I looked much the same. I gazed at the private suite of the training hall with a deeply moved expression.

“So this is the life of a gold spoon.”[^1]

It wasn’t only the graphics and artificial intelligence that were realistic. The game also carried the social message that, no matter how high you flew or how low you crawled, gold spoons had it best.

What would I have done without this character? His father was the Family Head, his eldest brother was the Lesser Family Head, and his second brother was a martial arts prodigy. He could spend his days loafing around pleasure houses without a care.

*Jin Taekyung, you bastard…*

Now that I thought about it, wasn’t he actually some great sage who had grasped the ways of the world at a young age?

Shuddering at the realistic God-Spoon System, I walked around the training hall, which covered well over three thousand square feet. Before long, I found the “necessities” the warrior had mentioned.

*Food first.*

The food was stored in two jars. When I looked inside, I found rice balls that gave off a strong medicinal scent.

> **System**
>
> **Item Window**
>
> **Excellent Grain-Repelling Pill**
>
> **Type:** Pill
>
> **Grade:** First Rate
>
> **Restriction:** None
>
> **Description:** A grain-repelling pill made by crudely cramming in all kinds of beneficial medicinal ingredients. Restores vitality when consumed and grants additional effects when taken over a long period.

“Oh, so this is the famous grain-repelling pill?”

I had seen them plenty of times in martial arts novels. They were light, compact, easy to carry, and apparently provided nutritional supplementation, too.

The other jar was packed full of grain-repelling pills as well.

*I should put these in my inventory for now.*

I gripped the jars with both hands and muttered,

“Item acquisition.”

If someone else had seen me, they would have fallen over in shock. The two perfectly ordinary jars had vanished as if they had evaporated.

I gazed fondly at the jars stored in my inventory.

*That takes care of food.*

The second necessity I found was water. Since the training hall was, after all, a cave, a cold underground spring in one corner took care of my drinking water.

And then there was the third and final necessity.

“Hmm.”

A weapons rack held several weapons in a neat row. Naturally, the first thing I picked up was a sturdy-looking wooden spear.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Training Wooden Spear**
>
> **Type:** Weapon
>
> **Grade:** Third Rate
>
> **Restriction:** None
>
> **Description:** Made for beginners.

“Oh.”

A training wooden spear made for beginners. It was exactly what I needed right now.

If I had just one more thing, everything would be perfect.

“Open inventory.”

Grinning, I took a martial arts manual titled *Jin Family’s Spear Technique* out of my inventory.

Ding.

> **System**
>
> - Would you like to learn the Jin Family’s Spear Technique? (3 / 10)

“Obviously.”

The System was great.

Sometimes, it was even adorable.

* * *

I had learned something for the first time yesterday while practicing the Jin Family’s Manoeuvre Technique.

The System’s notification sound wasn’t always ding.

I had also learned just how much I hated the other sound.

Beep!

> **System**
>
> - The movement failed.
>
> - Successful attempts (2 / 100)

It was the failure message. The System window that appeared without fail whenever I botched a movement.

I had no idea how many times I had seen it by now.

I stared at the *Training Wooden Spear* in my hand.

*I was thinking about this all wrong.*

Maybe it was because it was made of wood, but the spear was light. Whether I thrust or swung it, it moved as quickly as I wanted.

That was the problem.

*It’s too light to control.*

Because it was so difficult to make minute adjustments, I kept making mistakes. There was no chance that such a filthy, ridiculously picky System would overlook minor errors.

Beep.

> **System**
>
> - The movement failed.
>
> - Successful attempts (5 / 100)

“Ah, fuck.”

In the end, I tossed the *Training Wooden Spear* aside and pulled a *Sharp Spear* from my inventory. Its length and shaft thickness were roughly similar to the spear I had used in the real world.

But why hadn’t I taken it out from the beginning?

“It’s insanely heavy. Seriously.”

Since it had been made entirely of steel, its weight was no joke. By feel alone, it was a monster weighing nearly fifty kilograms.

My Stamina couldn’t withstand swinging something like this for hours.

My current realm was second-rate. Even with the System’s help, swinging around more than half a sack of rice as if it were a pinwheel was impossible.

*It’s not like I suddenly have tiger power or something.*

That was when it hit me.

“…Huh?”

What had I just said?

Tiger power?

“It’s here?”

This was a game. There was a System and stats. And there was internal energy.

Ten years of internal energy that could be drawn out through a cultivation technique!

It was embarrassing that I had forgotten about it even for a moment.

“I should’ve tried using that…”

They say you only know what something is like once you’ve experienced it. Was it any wonder an F-rank Hunter was F-rank? With barely any mana to speak of, I made do with my bare body. Even among Hunters, I was treated like a half-baked amateur.

*At least that solves one problem.*

I let out a dumbfounded laugh, then picked up the spear. Slowly and carefully, I began drawing out my internal energy.

The formula of the Jin Family’s Cultivation Technique, imprinted in my mind by the System, played rapidly through my thoughts, guiding my internal energy along its prescribed path.

A prickling sensation ran through me.

The response was immediate.

The ten years of internal energy coiled in my dantian spread throughout my body. Because this was a game and I was a martial artist, I could feel it spreading through every part of me.

*This is…*

Strength overflowed through my entire body. My vastly improved physical abilities and senses once again filled me with exhilaration after a lifetime as an F-rank Hunter.

*How can a person change this much?*

I gripped the spear and began practicing the *Jin Family’s Spear Technique*. The fifty-kilogram iron spear no longer felt heavy. It thrust and slashed through the air along the paths I wanted it to follow.

Before long—

Ding.

> **System**
>
> - Successful attempts (6 / 100)

The notification I had been waiting for began to ring.

* * *

Jin Wikyung spoke with a worried expression.

“He’s doing well, right?”

“He should be, if he has any sense of shame.”

“He’s still not fully recovered… He’ll be all right, won’t he?”

“Anyone who didn’t know better would think the Third Young Master was on death’s door. At that point, even spit would cure him.”

“No. You don’t know how weak the youngest was when he was little.”

Wipeng answered with an incredulous look.

“The elixirs and tonics that have gone into the Third Young Master alone would be enough to fill an entire room. And have you already forgotten about the hundred-year snow ginseng theft last year?”

“Ahem. That was…”

“At the time, the Medicine King Hall Master was so furious that he ran around shouting that he was going to cut open the Third Young Master’s stomach. To be honest, even while I was stopping him, I found myself thinking that it would qualify as self-defense.”

Jin Wikyung subtly averted his gaze.

In the end, the matter had been settled by paying compensation out of Jin Wikyung’s personal fortune, but the Medicine King Hall Master’s rage had been extraordinary.

“He swallowed that much elixir. Whatever else may be true, he probably won’t suffer from minor ailments until the day he dies.”

“It still isn’t enough. Can’t you tell just by looking at him? Every time I see the youngest, I feel sorry for him. He looks like a skeleton with a few scraps of flesh stuck to it. He’s so feeble and weak every morning.”

“Weak?”

Wipeng suddenly remembered a rumor he had heard in the past.

Among the courtesans of Taiyuan’s red-light district, Jin Taekyung was supposedly known by the nickname Night King.

*Just how impressive is he?*

The medicine must have worked properly, after all. Without realizing it, Wipeng raised his forearm and began imagining the size.

“What are you doing?”

“Ah, nothing.”

Jin Wikyung sighed as he looked at the mountain of documents piled before him.

“There’s so much to worry about, both inside and outside the family. Especially… I don’t like the fact that ‘they’ have made contact.”

“You mean the Mount Heng Sword Sect.”

Mount Heng Sword Sect. The weight of that name was anything but light.

Since an undefeated wandering martial artist first hung its signboard decades ago, it had grown at a frightening pace. By now, it had become strong enough to threaten the position of the Jin Family of Taiyuan.

“What could their intentions be?”

“I’ve sent my subordinates out to find out.”

Jin Wikyung fidgeted with the letter from the Mount Heng Sword Sect.

Why were they coming? For what purpose?

After one question led to another, he reached a single conclusion.

“Notify every branch in Shanxi. Whatever the Mount Heng Sword Sect’s purpose may be, tell them to make every possible preparation.”

This was Murim.

Only those who prepared themselves would survive and live to see tomorrow.

[^1]: In Korean, “gold spoon” is shorthand for someone born into wealth; “God-Spoon” is a pun that escalates the expression.
```
## Chapter 11

### Korean source

```text
＃11화



쉬익. 후웅-

허공에서 반짝이는 수십 개의 점을 창끝이 차례차례 관통한다.

한 번의 동작이 끝날 때마다 창날 아래 매달린 붉은 수실이 요동쳤다. 그저 멋으로 달아 놓은 것이 아니라, 적의 시선을 분산시키기 위한 용도다.

팡!

다시 한번 바람이 찢어지는 소리가 들렸다. [진가창법]을 이루는 일곱 개의 초식. 그중 마지막인 천관일(天貫軼)이다.

그리고 이번 천관일은 앞서 성공시킨 아흔아홉 번의 천관일보다 정확하고, 강력했다.

‘이거지.’

손끝이 짜릿하다. 진가창법의 일곱 개 초식은 끊어서 펼쳐도 충분히 파괴적이지만, 이어졌을 때 진정한 효과가 드러난다.

자동차 경주에 비교하자면 일 초식은 시동. 마지막 천관일은 골인이라 할 수 있겠다.

“후.”

더운 숨을 내뱉으며 창을 바로 세운 순간이었다.

띠링.



- 남은 성공 횟수 (100 / 100)

- [진가창법]을 습득했습니다.

- 반복된 수련의 결과로 관련 스탯이 상승합니다!

- 근력, 체력, 민첩이 각각 1씩 올랐습니다.



“오. 스탯 상승.”

이런 방법으로 능력치를 올릴 수도 있구나. 나는 신기해하며 상태창을 띄웠다.

띠링.



상태창



[Lv.11 진태경]

직업 : 이류 무인

명성 : 10

칭호 : 3개 (칭호 효과 적용 중)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 –5, 명성 –50)

- 초보 수련자 (수련 속도 +10%)

근력 : 41체력 : 51

민첩 : 51 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 0





이 정도면…….

“훌륭한 이류 나부랭이네.”

하지만 현실보다는 낫다. 더욱더 위로 올라갈 수 있으니까. F급으로 각성한 날부터 매일매일 느꼈던 한계와 사회가 덮어 놓은 유리천장이 느껴지지 않으니까.

“그럼 뭐 하냐. 마음대로 로그아웃도 못 하는데.”

나는 한숨을 내쉬며 바닥에 주저앉았다. 몇 시간 동안 쉬지 않고 수련했더니 몸이 물먹은 솜처럼 무겁다.

“어이고. 힘들다.”

띠링.



- 당신은 피로와 허기를 느낍니다. 음식물을 섭취하여 몸 상태를 회복시키십시오.



그래. 그럴 것 같더라.

“피로와 허기라.”

답은 휴식밖에 없다. 잘 먹고, 잘 자는 거다. 하지만 태평하게 배나 긁으면서 쉬기에는 시간이 아깝다.

이럴 때 회복 아이템 같은 거라도 하나 있으면…….

“아, 맞다. 벽곡단.”

인벤토리에 넣어 두었던 벽곡단을 꺼냈다. 희한한 냄새를 풍겼지만 찬밥 더운밥 가리면 프로 헌터가 아니다.

나는 입을 크게 벌리고 벽곡단을 한입 가득 베어 물었다.

그리고 생각했다.

‘그냥 뱉을까.’

맛이 없는 정도가 아니다. 혀가 살려 달라고 비명을 지르고 위장이 출입 금지 팻말을 걸 정도의 맛이다.

하지만 인간은 때때로 초인적인 의지를 발휘하는 법. 나는 눈을 질끈 감고 벽곡단을 남김없이 씹어 삼켰다.

꿀꺽.

“으어어. 먹었어. 진짜 먹었어.”

다음 순간 시스템 알림이 울리지 않았다면 한참을 그렇게 뒹굴었을 것이다.

띠링.



- [뛰어난 벽곡단]을 섭취했습니다.

- 당신은 포만감을 느낍니다.

- 피로가 회복됩니다.

- 한 시간 동안 모든 능력치가 2씩 상승합니다.



“뭐?”

황급히 상태창을 열어 보니 공력을 제외한 모든 능력치가 2씩 올라 있었다. 거기에 피로와 허기 회복까지. 나는 쌩쌩한 몸 상태와 포만감을 느끼며 중얼거렸다.

“완전 사긴데?”

더럽게 맛없는 곡물 덩어리에 이런 엄청난 효능이 있을 줄이야. 아니, 잠깐만.

“이거, 중복 효과 있나?”

고작 하나를 먹었는데 총합 10포인트가 올랐다. 두 개, 세 개, 아니 열 개를 먹는다면?

‘저게 고블린 똥이라도 먹어야지.’

왠지 고블린 똥이 더 맛있을 것 같긴 한데…… 확실히 시도해 볼 만한 일이다.

‘할 수 있다. 할 수 있다. 진태경.’

떨리는 손으로 두 번째 벽곡단을 집어 들었다.

그리고 잠시 뒤.



- [뛰어난 벽곡단]을 섭취했습니다.

- 효과가 중복되지 않습니다.

- 당신은 과한 포만감을 느낍니다.

- [과식]의 영향으로 한 시간 동안 움직임이 둔화됩니다!



나는 시스템 알림과 함께 무릎을 꿇었다.

“우웨에에엑!”



* * *



[과식]으로 빵빵해진 배가 겨우 꺼진 뒤에야 다시 수련을 시작할 수 있었다. 수련동에 머무는 시간은 사흘. 그동안 최대한 힘을 키워서 나가야 한다.

“하!”

짧은 기합과 함께 창날이 묵직한 궤적을 그렸다.

‘자세는 낮게, 발은 무겁게, 창은 빠르게.’

진가창법은 공격적이다. 끊임없이 적을 압박하며 나아간다. 창의 궤적은 단순하지만 치명적이다.

‘군대에서 파생되었다고 했나?’

게임의 설정이 어떤지는 몰라도 일개 병졸이 익힐 만한 무공은 아닌 것 같다.

명색이 일류 무공인 데다 펼치려면 상당한 신체 능력이 필요하기 때문이다. 정예병, 혹은 지휘관들이 익혔던 무공이 아니었을까 싶다.

‘헌터 훈련소 시절 배웠던 거랑 비교하면 천지 차이지.’

그런 생각을 했을 때였다. 체력의 고갈인지, 아니면 잡념 때문인지 발이 꼬였다. 발이 꼬이니 손도 흐트러진다. 잔뜩 힘을 머금은 창날이 기세를 잃고 바람을 갈랐다.

쉬익-

시스템이 울린 것도 동시다.



- [진가창법]의 숙련도가 1 오릅니다. (6 / 100)



“겨우 1?”

방금처럼 무공을 처음부터 끝까지 펼칠 때마다 숙련도가 오른다. 시스템의 판정에 따라 얻는 숙련도도 다른데, 이번에는 발이 자주 꼬여서 1이 오른 게 전부였다.

“어떻게 갈수록 못하지?”

습득 후 세 번째로 펼친 진가창법은 점점 형편없어지고 있었다. 처음에 얻은 숙련도는 3. 두 번째는 2. 세 번째인 지금은 1이다.

“삼, 이, 일. 카운트 세는 것도 아니고 뭐야, 이게?”

네 번째는 아예 숙련도를 1도 안 줄 기세다. 나는 한숨과 함께 다시 창을 잡았다. 호흡이 점점 달리는 게 느껴졌지만 다시 진가창법을 펼쳐 냈다.

그리고 사 초식을 펼칠 무렵 균형을 잃고 쓰러졌다.

띠링.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



“돌겠네.”

그대로 누워 종유석이 매달린 수련동 천장을 바라봤다.

자꾸 발이 꼬인다. 내가 익힌 그대로 했는데 도대체 왜? 습득할 때도 이런 일은 없었다.

“뭐가 문제지?”

계속 턱, 하고 걸리는 부분이 있다. 그걸 알아내야 한다.

나는 오뚝이처럼 일어나 다시 진가창법을 펼쳤고, 이번에는 삼 초식 만에 넘어졌다.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



창이 아니라 발에 집중해서 펼치자 문제점이 희미하게 모습을 드러낸다. 좋아, 한 번 더.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



이제 알겠다. 그런데…….

“여기서 진가보법이 왜 튀어나와?”

처음 익힐 때 고생하긴 했다. 한나절 내내 보법만 밟았으니까. 하지만 창법을 펼칠 때 나도 모르게 섞어 쓸 정도냐, 물어보면 그건 아니다.

‘그렇게 따지면 7년 동안 익힌 동작 다 섞었지.’

나도 창술을 배우긴 했다. 헌터 훈련소에 입소하면 기본적으로 배우는 건데, 마나를 사용할 수 없는 F급을 대상으로 보급된 거라 우리끼리는 좆밥 창술이라고 불렀다.

그거에 비하면 진가창법은 중급 헌터용은 된다.

“한번 해 볼까?”

머리 싸매고 생각해 봤자 원형 탈모만 생긴다. 기술은 일단 몸으로 부딪쳐 봐야 아는 법.

나는 천천히 진가창법을 펼치기 시작했다. 그리고 하체로는 진가보법을 펼쳤다.

‘동작이 부자연스러워.’

자꾸만 어긋난다. 하지만 다르다. 지금까지는 실이 뒤죽박죽 얽혀 있었다면 이번에는 톱니바퀴가 미세하게 비껴가는 느낌이랄까. 그렇게 몇 번을 시도했을까.

쉬익- 팡!

단순한 찌르기 동작. 나도 모르는 사이에 마지막 일곱 번째 초식까지 펼쳤나 생각했지만 오 초식의 한 동작이다.

“방금 뭐야?”

등줄기가 찌릿했다. 한순간, 보법과 창법이 완벽하게 맞물린 결과였다. 손에 쥔 창이 부르르 떨렸다.



- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)



이제 시스템 알림은 저 구석으로 처박고, 다시 창을 단단히 말아 쥔다. 조금 전의 느낌을 떠올리며 발을 내디뎠다. 그리고 다시 한번.

쉭- 쉬쉭-

이거다. 창을 뻗는 순간 느꼈다. 보법과 창법. 이 두 톱니바퀴가 정확히 맞물린다.

이루 말할 수 없는 쾌감에 휩싸여 두 개의 톱니바퀴를 굴리고, 또 굴렸다. 내딛는 걸음이, 찌르고 베고 휘두르는 창날이 빠르고 정확했으며 강했다.

단전이 뜨겁다. 공력은 하나의 불덩어리가 되어 창에 스며들었다. 토해 내야 했다.

바로 지금!

“합!”

천관일. 하늘을 뚫는다는 진가창법의 마지막 일격이 뻗어 나갔다. 먹먹한 굉음이 터져 나왔다.

쾅-!

먼지가 피어오르고 돌이 사방으로 비산한다. 수련동의 벽에 박힌 창이 몸을 떨었다. 깊숙이 박혀 보이지도 않는 창날을 중심으로 커다란 구멍이 생성되어 있었다.

구멍? 아니다. 이건 크레이터다. 숨 막히는 광경이다.

“헉, 헉…….”

쾌감에 등골이 오싹했다. 시발, 나야. 내가 해냈다고!

트롤도 한 방에 끝장낼 수 있는 저런 미친 일격을 내가……!

휘청.

‘어?’

떠나가라 소리를 지르고, 인증 사진도 찍어야 하는데. 쌀벌레라고 놀리던 진호 형 코를 납작하게 만들어 줘야 하는데.

‘아, 여기. 게임이었지.’

눈앞이 흐릿하다. 몸에 힘이 빠진다. 견딜 수 없는 졸음이 밀려와 나를 덮쳤다.

‘졸려.’

나는 생각하는 것을 멈추고 본능에 몸을 맡겼다. 어디선가 많이 듣던 소리가 아스라이 멀어진다.

띠링. 띠링. 띠링.

.

.

.

- 공력이 모두 소진되었습니다.

- 극도의 피로감을 느낍니다.

- 업적, [물아일체]를 달성하셨습니다. 보상이 주어집니다!

- 무공의 연계를 스스로 깨달았습니다. 보상으로 무공의 경지가 크게 상승합니다.

- [진가심법]의 경지가…….

- [진가보법]의 경지…….

- [진가창법]의…….

- 레벨 업!

- 레벨 업!



* * *



- 수면 모드가 종료되었습니다.



눈을 떴다. 종유석이 매달린 동굴 천장이 보인다.

‘수련동.’

얼마나 기절해 있었던 걸까. 반나절? 아니면 하루?

모르겠다. 중요한 건 내가 아직 게임 속이고, 충분히 쉬었다는 사실이다.

‘컨디션도 최상이고.’

이상할 정도로 몸 상태가 좋다. 그러고 보니 기절하기 직전에 시스템 알림을 들었던 것도 같다.

“메시지창 오픈.”

다음 순간 확인 안 한 메시지들이 시야를 가렸다. 메시지를 다 읽고 생각을 정리했을 때는 십여 분이 훌쩍 흐른 뒤였다. 나는 짧게 소감을 중얼거렸다.

“대박 났네.”

진가보법, 창법은 삼 성으로 무려 두 단계나 뛰었고 진가심법은 이 성으로 올랐다. 거기에 더해…….

“2레벨이나 올랐다고?”

기쁘면서도 얼떨떨하다. 사실 수련동에서 레벨을 올릴 수 있으리란 기대는 거의 하지 않았기 때문이다.

“보통 퀘스트 깨거나 몬스터를 잡아야 오르는 거 아니었어?”

무공을 익히고 지금처럼 어떤 깨달음을 얻는 것으로도 레벨 업이 된다니. 게임 장르가 무협이라 그런가? 확실히 종잡을 수가 없다.

“아, 어쩐지 몸이 가뿐하더라.”

레벨 업 효과로 몸이 회복된 모양이다. 레벨 업 전까지 남아 있던 타박상과 약간의 통증도 모두 깨끗이 사라져 있었다.

“상태창 오픈.”

상태창에도 변화가 있었다. 13레벨로 오르면서 스무 개의 잔여 포인트를 얻었고, 수련의 영향으로 근력, 체력, 민첩이 소량 오른 상태다.

“13레벨이라.”

퀘스트 완료 조건은 일류 경지와 레벨 30, 명성 500 달성.

빠르지는 않지만 수련만으로도 착실히 레벨을 올리고 있으니 순항하고 있는 셈이다.

‘수련동만 나가면 돛을 피고 쭉쭉 나아가는 거지.’

나는 흐뭇하게 웃으며 포인트를 분배했다.

이제 [물아일체]의 업적을 이루면서 받은 보상 확인만이 남았다.

“인벤토리 오픈.”



- 신규 아이템이 1개 존재합니다. 확인하시겠습니까?



어, 내놔.
```

### Current accepted English

```markdown
# Chapter 11

Whoosh. Fwoom—

The spearhead pierced dozens of sparkling points in the air one after another.

Each time I completed a form, the red tassel hanging beneath the spearhead whipped around. It wasn’t just for show; it was meant to draw the enemy’s eye.

Bang!

Again, the sound of wind being torn apart rang out. It was the seventh and final form of the Jin Family’s Spear Technique: the Sky-Piercing Strike.

This Sky-Piercing Strike was more precise and powerful than the ninety-nine I had successfully performed before it.

*This is it.*

My fingertips tingled. Each of the seven forms in the Jin Family’s Spear Technique was destructive enough when performed separately, but its true effect emerged when they flowed together.

If I compared it to a car race, the first form was starting the engine. The final Sky-Piercing Strike was crossing the finish line.

“Whew.”

I exhaled a hot breath and raised the spear upright.

Ding.

> **System**
>
> - Successful attempts: (100 / 100)
>
> - You have acquired **Jin Family’s Spear Technique**.
>
> - As a result of repeated training, related stats have increased!
>
> - Strength, Stamina, and Agility have each increased by 1.

“Oh. My stats went up.”

So this was another way to improve my stats. Intrigued, I opened my Status Window.

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 11 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
>
> **Fame:** 10
>
> **Titles:** 3 (Title effects active)
>
> - **Child of a Prestigious Family:** All stats +5, Fame +50
>
> - **Shame of the Family:** All stats –5, Fame –50
>
> - **Novice Trainee:** Training speed +10%
>
> **Strength:** 41  
> **Stamina:** 51
>
> **Agility:** 51  
> **Intelligence:** 10
>
> **Charm:** 10  
> **Internal Energy:** 10 years
>
> **Remaining Points:** 0

This was…

“What a fine second-rate nobody.”

Still, it was better than reality. I could keep climbing higher. I no longer felt the limitations I’d sensed every day since awakening as an F-rank, or the glass ceiling society had placed over me.

“So what? I can’t even log out whenever I want.”

I sighed and sank to the floor. After several hours of nonstop training, I felt as heavy as a waterlogged cotton blanket.

“Ow. I’m exhausted.”

Ding.

> **System**
>
> - You feel fatigued and hungry. Consume food to restore your physical condition.

Yeah. I figured that would happen.

“Fatigue and hunger…”

The only answer was rest. Eat well and sleep well. But I didn’t have time to lie around leisurely scratching my belly.

If only I had some kind of recovery item…

“Oh, right. Grain-repelling pills.”

I took one of the grain-repelling pills from my inventory. It gave off a strange smell, but a professional Hunter couldn’t afford to be picky about whether his rice was hot or cold.

I opened my mouth wide and took a huge bite.

Then I thought,

*Should I just spit it out?*

It wasn’t merely tasteless. It tasted bad enough that my tongue screamed for mercy and my stomach hung up a no-entry sign.

Every now and then, humans could summon superhuman willpower. I squeezed my eyes shut, chewed the grain-repelling pill thoroughly, and swallowed every last bit.

Gulp.

“Uuugh. I ate it. I actually ate it.”

If the System notification hadn’t sounded the next moment, I probably would have kept rolling around on the floor for quite a while.

Ding.

> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - You feel full.
>
> - Your fatigue has been restored.
>
> - All stats increase by 2 for one hour.

“What?”

I hurriedly opened my Status Window. Every stat except Internal Energy had increased by 2. On top of that, my fatigue had lifted and my hunger was gone.

Feeling energized and full, I muttered,

“This is completely broken.”

Who would have thought such a foul-tasting lump of grain could have such incredible effects? Wait a second.

“Do the effects stack?”

Just one had increased my stats by a total of 10 points. What if I ate two? Three? No, ten?

*I’d eat goblin shit if I had to.*

Goblin shit might actually taste better… but it was definitely worth a try.

*I can do this. I can do this. Jin Taekyung.*

With trembling hands, I picked up a second grain-repelling pill.

And a short while later—

> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - The effects do not stack.
>
> - You feel excessively full.
>
> - Your movements will be slowed for one hour due to **Overeating**!

I dropped to my knees as the System notification sounded.

“Bleaaargh!”

* * *

I could only resume training after my bloated stomach finally went down. I had three days to stay in the training hall. I needed to grow as strong as possible before leaving.

“Hah!”

With a short battle cry, the spearhead traced a heavy arc.

*Keep my stance low, my feet heavy, and my spear fast.*

The Jin Family’s Spear Technique was aggressive, constantly advancing while pressuring the enemy. Its spear movements were simple but lethal.

*Was it derived from the military?*

I didn’t know what the game’s setting was, but it didn’t seem like a martial art an ordinary foot soldier could learn.

After all, it was a first-rate martial art and required considerable physical ability to perform. Perhaps it had been practiced by elite soldiers or commanders.

*Compared with what I learned at the Hunter training camp, it’s like heaven and earth.*

That was when my foot tangled—whether from exhaustion or distraction, I wasn’t sure. Once my foot got tangled, my hands lost their rhythm too. The spearhead, loaded with strength, lost its momentum and sliced through the air.

Whoosh—

The System sounded at the same time.

> **System**
>
> - Jin Family’s Spear Technique Mastery increased by 1. (6 / 100)

“Only 1?”

My Mastery increased each time I performed the martial art from beginning to end. The amount I gained depended on the System’s evaluation, and this time, all I got was 1 because my feet had tangled so often.

“Why am I getting worse the more I do it?”

The third time I performed the Jin Family’s Spear Technique after acquiring it, I was getting worse and worse. The first time, I gained 3 Mastery. The second time, 2. This third time, 1.

“Three, two, one. It’s not even a countdown. What is this?”

The fourth attempt looked like it would yield no Mastery at all. I sighed and took hold of the spear again. My breathing was becoming increasingly ragged, but I performed the Jin Family’s Spear Technique once more.

Around the fourth form, I lost my balance and fell.

Ding.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

“This is driving me insane.”

I lay there and stared at the training hall’s ceiling, where stalactites hung overhead.

My feet kept getting tangled. I was performing the technique exactly as I had learned it, so why was this happening? Nothing like this had happened when I acquired it.

“What’s the problem?”

Something kept throwing me off. I had to figure out what it was.

I got back up like a roly-poly and performed the Jin Family’s Spear Technique again. This time, I fell after only the third form.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

When I focused on my feet instead of the spear, the problem started to come into focus.

Good. One more time.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

Now I understood. But…

“Why is the Jin Family’s Manoeuvre Technique showing up here?”

I had struggled when I first learned it. I’d spent half a day practicing nothing but footwork. But if you asked whether it was enough to make me unconsciously mix it into my spear technique, the answer was no.

*If that were the case, I’d have mixed in every movement I’ve learned over seven years.*

I had learned spear fighting before, too. It was one of the basics taught at the Hunter training camp. Since it was distributed to F-ranks who couldn’t use mana, we called it shitty spear fighting among ourselves.

Compared with that, the Jin Family’s Spear Technique was good enough for intermediate Hunters.

“Should I give it a try?”

No matter how hard I racked my brain, all I’d get was a bald spot. The only way to understand a technique was to try it with my whole body.

I began performing the Jin Family’s Spear Technique slowly. At the same time, I performed the Jin Family’s Manoeuvre Technique with my lower body.

*The movements don’t flow naturally.*

They kept falling out of sync. But it was different. Until now, it had felt as if tangled threads were being pulled in every direction. This time, it felt as if gears were slipping past each other by a hair.

How many times had I tried?

Whoosh—Bang!

It was a simple thrust. For a moment, I wondered if I had performed all the way through the seventh and final form without realizing it, but it was only one movement from the fifth form.

“What was that?”

A shiver ran down my spine. For one brief moment, the footwork and spear technique had meshed perfectly. The spear in my hand trembled.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

I shoved the System notification into a corner of my mind and tightened my grip on the spear. Recalling the sensation from a moment ago, I stepped forward.

And again.

Swish—Whoosh—

*This is it.*

I felt it the instant I thrust the spear. The footwork and the spear technique. The two gears meshed perfectly.

Overwhelmed by indescribable pleasure, I turned those two gears again and again. My steps were fast and precise. The spearhead that thrust, slashed, and swung was fast, precise, and powerful.

My dantian grew hot. My internal energy became a ball of fire and seeped into the spear.

I had to release it.

*Right now!*

“Hah!”

The Sky-Piercing Strike—the final blow of the Jin Family’s Spear Technique, said to pierce the heavens—shot forward.

A deep, muffled boom erupted through the cavern.

Bang!

Dust rose, and stones scattered in every direction. The spear embedded in the training hall’s wall trembled. A massive hole had formed around the spearhead, which had plunged so deeply that it was no longer visible.

A hole? No.

This was a crater.

The sight was breathtaking.

“Huff, huff…”

The exhilaration sent a shiver down my spine.

*Fuck, it was me. I did it!*

I had unleashed that insane strike—the kind that could take down a troll in one blow.

Me!

I staggered.

*Huh?*

I needed to shout my head off and take a proof photo. I needed to put Big Brother Jinho in his place—he used to call me a freeloader.

*Oh, right. This was a game.*

My vision blurred. The strength drained from my body. An unbearable wave of sleepiness washed over me.

*I’m sleepy.*

I stopped thinking and surrendered my body to instinct. A familiar sound gradually faded into the distance.

Ding. Ding. Ding.

.

.

.

> **System**
>
> - All internal energy has been depleted.
>
> - You feel extreme fatigue.
>
> - You have completed the achievement **Unity of Self and Object**. A reward will be granted!
>
> - You have realized the connection between martial arts on your own. As a reward, the realms of your martial arts will rise substantially.
>
> - The realm of **Jin Family’s Cultivation Technique**…
>
> - The realm of **Jin Family’s Manoeuvre Technique**…
>
> - The realm of **Jin Family’s Spear Technique**…
>
> - Level up!
>
> - Level up!

* * *

> **System**
>
> - Sleep mode has ended.

I opened my eyes. The cave ceiling, with stalactites hanging from it, came into view.

*The training hall.*

How long had I been unconscious? Half a day? Or a full day?

I didn’t know. What mattered was that I was still in the game and had gotten plenty of rest.

*I feel great, too.*

My physical condition was strangely excellent. Come to think of it, I seemed to have heard System notifications just before I passed out.

“Open Message Window.”

The next moment, unread messages covered my vision. By the time I finished reading them all and sorting through my thoughts, more than ten minutes had passed.

I muttered a brief reaction.

“I really hit the jackpot.”

The Jin Family’s Manoeuvre Technique and Spear Technique had risen all the way to the Third Stage—two whole stages. The Jin Family’s Cultivation Technique had reached the Second Stage.

And on top of that…

“I went up two Levels?”

I was happy, but also bewildered. I hadn’t seriously expected to Level up in the training hall.

“Don’t you usually Level up by completing Quests or killing monsters?”

Apparently, learning martial arts and gaining insight like I had could also lead to a Level Up. Was it because this was a martial-arts game? It was definitely impossible to predict.

“No wonder my body felt so light.”

The Level Up effect must have restored my condition. The bruises and slight pain that had remained before I leveled up had vanished completely.

“Open Status Window.”

The Status Window had changed too. Reaching Level 13 had given me twenty remaining points, and the effects of training had slightly increased my Strength, Stamina, and Agility.

“Level 13…”

The Quest completion requirements were reaching the first-rate realm, Level 30, and 500 Fame.

I wasn’t progressing quickly, but I was steadily leveling up through training alone. That meant I was cruising along.

*Once I leave the training hall, I can spread my sails and surge forward.*

I smiled contentedly and distributed my points.

Now, all that remained was to check the reward I’d received for completing the Unity of Self and Object achievement.

“Open Inventory.”

> **System**
>
> - You have 1 new Item. Would you like to check it?

Yeah. Give it here.
```
## Chapter 12

### Korean source

```text
＃12화



10년 전쯤인가? 내가 고등학생 시절 일반인 수십 명이 정부 승인하에 게이트에 진입한 일이 있었다.

‘중국이었지, 아마.’

헌터들도 한눈팔면 시체가 되는 곳이 게이트인데 일반인들을 들여보내다니, 역시 미라클 대륙이다.

이 미친 짓거리가 벌어진 출정식 당일, 해외 언론과의 인터뷰에서 그들의 정체가 밝혀졌다.

중화 무술 연맹.

한마디로 현대판 무림인들인 셈이다. 완전한 비각성자들로 이루어진 그들은 도포를 펄럭이며 수백 대의 카메라를 향해 엄숙히 선언했다.

‘바로 오늘, 중화의 천년 무맥이 화려하게 부활할 것입니다.’

화려하긴 했다. 불과 반나절 만에 그들의 얼굴이 각종 뉴스 1면을 대문짝만하게 장식했으니까.



- 중화 무술 연맹 소속 25인. F급 게이트에서 몰살. 그중 절반 이상이 고블린 독침에 의해 사망한 것으로 밝혀져…….



천년 무맥이 얼마나 대단한 건지는 모르겠지만 그 사건으로 중국은 개망신을 당했고 중화 무술 연맹은 간판만 남았다.

‘아주 아작 났지.’

대륙에서 손꼽히는 무술인들이 고블린 독침에 맞아 죽고, 태극권의 고수는 이종 격투기 선수한테 얻어터진다.

그게 현실이다. 소설에서, 영화에서 나오는 장면들은 미디어 매체와 신비로움으로 포장한 허구라고 생각했다.

‘그런데…….’

이제는 모르겠다. 혁무진이 보여 준 움직임은 ‘진짜’였다.

직접 무공을 익히면서 의심은 점점 확신으로 변해 갔다. 현실에서처럼 힘없고 흐느적거리는 무공은 어디에도 없다.

이곳의 무공은 체계적이고, 수많은 동작을 포함한다. 현실의 무공이나 권투 따위에 비할 바가 아니었다.

‘어떻게 이런 게 가능하지? 단순히 게임이라서?’

스으읍. 후우우.

호흡과 함께 몸 밖의 기운을 느낀다. 그리고 끌어당긴다.

혈도를 따라 회전하는 10년 공력에 비하면 티끌에 불과한, 작고 약한 기운이었지만 나는 그마저도 아쉬운 처지다.

‘한 바퀴, 두 바퀴…….’

진가심법의 구결을 따라 운기조식을 이어 갔다. 마치 어릴 적부터 수련해 왔던 것처럼 자연스러운 행위였다.

‘견정(肩井), 아문(雅文), 봉안(鳳眼), 입동(入洞)…….’

지난 27년간 듣도 보도 못한 혈도의 명칭들이 머릿속에 떠오르고 사라진다. 그렇게 내 머릿속에 각인된 혈도가 수백 개에 달한다. 시스템의 기능은 어디까지인 걸까.

‘생각해 보면 기이할 정도지.’

인간의 뇌는 컴퓨터가 아니다. 하지만 시스템은 파일을 복사 붙여넣기 한 것처럼 내 머릿속에 입력시켜 놓았다. 다른 무공들도 마찬가지다.

이런 현상이 가능한가? 단지 게임이라는 이유만으로?

‘아니다. 우선 운기조식에만 집중하자.’

다시 호흡을 가다듬고 공력을 이끌었다. 10년 공력을 진가심법의 구결에 따라 꼬박 열두 바퀴를 돌린 후에야 눈을 떴다.

띠링.



- [운기조식]을 마쳤습니다.

- [진가심법]의 숙련도가 미약하게 오릅니다.

- 탁기가 소량 배출되었습니다.



“후우.”

진가심법 삼 성 달성이 코앞이다. 바닥부터 시작해서인지는 몰라도 제법 빠른 속도라고 느껴졌다.

‘아니면 아이템 덕분일 수도 있고.’

나는 오른손 중지에 끼워진 반지를 바라봤다.

앞서 [물아일체] 업적을 달성한 보상으로 받은 아이템이다.



아이템창



[청심환]

종류 : 반지

등급 : 無

제한 : 無

설명 : 매우 단단하고 재질을 알 수 없는 반지. 착용자의 마음을 안정시켜 집중을 돕는다.





청심환. 내가 알고 있는 것과 형태는 다르지만, 효과는 비슷하다. 확실히 이걸 낀 후부터 운기조식에 들어가는 시간은 짧아지고, 얻는 숙련도는 늘었다.

‘좋긴 좋은데…….’

찝찝한 기분이다. 로그아웃은 뭐, 내가 모르는 공돌이들의 기술적인 영역이라 치자. 하지만 무공 구결이나 이 반지, 청심환의 같은 경우는 어딘지 모르게 꺼림칙하다.

‘강제로 주입되는 기분이라고 해야 하나?’

내 생존에 도움이 된다지만 기분 좋은 일이 아닌 것은 분명하다. 여러모로 거지 같은 게임이다.

“성진호 이 인간은 도대체 뭘 하고 자빠진 거야. 고시원 총무라는 양반이.”

일어났으면 해장국이라도 한 그릇 하자고 날 깨웠어야 했다. 그런데도 아직 아무런 변화가 없다는 건…….

‘아냐. 아니야.’

최소한 현실의 나는 아직 살아 있다. 그러니까 아직까지 플레이어로 이 게임에 존재할 수 있는 거다.

현실에서도, 게임에서도 살아 있다. 그리고 반드시 살아 나갈 거다. 이렇게 개죽음당하기에는 내 삶이 너무 아쉽고, 내 짐이 너무 무겁다.

‘여기서 죽을 수는 없지.’

이를 악물고 가부좌를 틀었다. 청심환의 효과일까, 마음이 점차 가라앉고 호흡이 안정된다.

단전의 공력이 움직이는 것을 시작으로, 나는 몇 번째인지 모를 운기조식을 시작했다.



* * *



수련동에 들어온 지 이틀째.

나는 쉬지 않고 수련에 몰두했다. 창법, 보법에 미친 듯이 매달렸고 도중에 공력이 모두 소진되면 곧바로 운기조식을 시작했다.

띠링.



- [진가심법]의 경지가 삼 성으로 올랐습니다.

- 공력이 보다 정순해지고 효율적인 운기조식이 가능합니다.



삼 성의 진가심법. 다른 두 개에 비하면 느린 속도였지만 나쁘지 않다. 아니, 그렇게 생각하려고 노력 중이다.

‘이렇게라도 해야 버티지.’

그나마 무공 수련을 할 때는 나쁜 생각을 떨쳐 버릴 수 있어서 다행이었다.

쉭, 쉬쉭.

진가창법의 초식을 차례대로 풀어냈다. 진가보법과의 연관성을 깨달은 이후로 한층 정교하고 날카로워진 공격이 전방을 휩쓴다.

나는 아무도 없는 그곳에 누군가의 모습을 그려 내고 있었다.

‘혁무진.’

이 게임에서 처음으로 만난, 진짜배기 무림인. 나를 어린애처럼 갖고 놀았던 20레벨의 강자.

‘지금 상태라면 그놈을 이길 수 있을까?’

의문이 떠오른 그 순간이었다.

띠링.



- 새로운 기능, [수련 모드]가 활성화되었습니다.

- 지금까지 대결한 상대의 환영을 불러낼 수 있습니다. 단, 사용자의 레벨과 10레벨 이상 차이 나는 상대는 불가능합니다.

- 현재 소환 가능한 상대 : [Lv.20 혁무진], [Lv.10 천력부]



“엥?”

수련 모드? 지금까지 대결한 상대의 환영을 불러낼 수 있다고? 잠깐 망설이다가 새로운 기능을 시험해 보기로 마음먹었다.

“혁무진 소환.”



- [Lv.20 혁무진]를 소환합니다.



시스템 알림이 뜨기가 무섭게 투명한 형체가 불쑥 솟아올랐다. 태원진가의 남색 무복에 특유의 송충이 눈썹. 선 채로 눈을 감고 있는 형체는 혁무진의 모습 그대로였다.

“헐, 진짜네.”

나는 조심스럽게 다가가 혁무진의 몸을 짚었다. 하지만 환영이라서 그런 걸까, 손은 허무하게 녀석의 몸을 통과했다.

좋아, 이걸로 안전성 테스트는 통과다.



- 소환한 대상의 수준을 일부 변경할 수 있습니다.



“우선은 혁무진의 절반 정도로.”



- [Lv.20 혁무진]의 데이터를 입력합니다. 환영은 본체의 50% 실력을 발휘할 수 있습니다.



동시에 혁무진의 환영이 눈을 떴다. 실력이 아니라 성격도 닮았는지 싸가지 없는 눈빛으로 나를 바라본다.



- 수련을 시작하시겠습니까?



“물론!”

띠링.

시스템 알림이 신호탄이다. 나는 번개처럼 달려들어 창을 찔렀다. 비록 환영과의 싸움이지만 공력을 아끼지 않고 쏟아부었다.

‘일 초식.’

나아감과 동시에 찌르고, 창대를 비트는 걸로 시작한다. 첫 공격을 피하지 못한다면 적은 그것으로 끝이다.

쐐애액-

하지만 혁무진은 미꾸라지 같은 움직임으로 빠져나갔다. 다음 동작이 무의미해지는 순간이다.

‘이것도 피하나 보자.’

나는 계속해서 창법을 펼쳐 냈다. 바람이 찢어지는 소리가 났지만 혁무진은 모두 피해 냈다.

얼핏 그의 불투명한 얼굴에 비웃음이 떠오르는 듯했다.



‘그렇게 무식하게 싸워서야 쓰나. 무인이라면 응당 무공을 써야지.’



지난번 나를 농락하면서 쳤던 대사다. 내가 만들어 낸 허상일 뿐이지만…… 열받네, 이거.

‘자신 있으면 피하지만 말고 덤벼 보든가.’

내 생각을 전달받은 혁무진이 미끄러지듯이 달려들었다. 하지만 창과 주먹의 싸움이다. 이대로 공격을 허용하면 지난 7년 동안 삽질만 한 게 된다.

“어딜!”

후웅-

창대를 휘둘렀다. 만약 허상이 아닌 실제였다면 퍽, 소리가 났을 거다. 설령 피했더라도 거리를 좁히는 데에는 실패했겠지.

‘어디까지 피하나 보자.’

이 초식이 시작됐다. 쏟아지는 공격에 혁무진은 감히 다가올 생각도 못 하고 뒷걸음질 쳤다.

전투도 흐름이다. 나는 그 흐름 위에 올라탔고 혁무진은 휩쓸렸다. 지친 얼굴로 땅을 뒹구는 혁무진을 보며 생각했다.

‘약하다.’

녀석의 움직임이 내게는 보였다. 이 자리에 투영해 낸 혁무진은 권사(拳士)다. 발을 보면 움직임을 알 수 있고, 다음 행동을 예측할 수 있었다. 놈의 주먹은 내게 닿지 못한다.

쉬쉬쉭!

한순간, 세 번을 연달아 찔렀다. F급 헌터 진태경은 할 수 없는 공격. 그러나 공력을 끌어 올린 무림인 진태경이라면 가능하다.

- 크아아악!

가슴을 찔린 혁무진이 그런 비명을 지르는 듯했다.

나는 망설이지 않고 창대를 더욱 깊숙이 밀어 넣고 비틀었다. 창날이 가슴뼈를 부수고 심장을 갈랐다. 쓰러진 혁무진의 모습이 천천히 흐려졌다.

“아. 이건 너무 쉬운데.”

5초도 채 되지 않았는데 벌써 승부가 날 줄이야.

심지어 싸움 내내 우위를 점하다가 싱겁게 끝나 버렸다.

‘절반은 너무 약했나?’

운기조식으로 소진된 공력을 회복하며 생각에 잠겼다.

혁무진은 20레벨이고 최소 몇 년간 무공을 수련한 무인이다. 이렇게 약할 리가 없다.

‘좋아, 다시.’

창을 쥐고 일어났다. 눈을 감고 새로운 혁무진을 떠올렸다.

180센티의 키. 날렵한 근육과 싸가지 없는 눈매. 그때 봤던 움직임을 주입했다. 이윽고 눈을 뜨자 내가 생각한 그대로의 허상이 앞에 서 있었다.

하지만 아직 끝나지 않았다. 혁무진은 더 강해져야 했다.

‘넌 신체 능력이 나보다 우수하다.’

몇 개의 조건을 더 주입시키자 혁무진의 허상 기분 좋은 웃음을 지었다. 그는 훨씬 빠르고 결코 지치지 않는 체력을 갖게 됐다.

“그래, 이 정도는 돼야 할 만하지.”

그 말이 신호탄이었다. 빛살처럼 쇄도하는 혁무진을 향해, 나는 창을 찔러 넣었다.

쉬쉬쉭!



* * *



우우웅. 펑!

창날이 허공을 찢었다. 벌 떼 우는 소리와 함께 터져 나간 공기가 바람을 불러왔다. 진가창법의 최후 절초. 천관일이다.

- 커허…….

혁무진의 허상은 뻥 뚫린 자신의 가슴을 내려다봤다. 믿을 수 없다는 눈빛이다. 이내 무릎이 꺾이고 허상이 흩어진다.

“이게 아닌데.”

진가창법의 숙련도가 올랐다는 메시지를 들으며 머리를 벅벅 긁었다.

‘왜 아직도 내가 이기지?’

시스템이 착각한 건지, 아니면…….

‘그냥 내가 강해진 건가?’

문득 든 생각을 털어 냈다. 그럴 리가. 내가 무슨 불세출의 천재도 아니고. 겨우 무공 두어 개 익혔을 뿐인데.

‘이래서야 효과가 별로 없는데.’

강자를 상대했을 때 어떻게 되는지 실험하는 시뮬레이션에서 내가 이겨 버리면 무슨 의미가 있나 싶다.

적어도 혁무진이 무슨 무공을 익혔는지 알고 있다면 그 위력을 살려 볼 수 있을 텐데…… 아니, 잠깐.

“더 쉬운 방법이 있었네.”

진가보법과 진가창법. 20레벨의 혁무진에게 이 두 개를 접목시키면 어떨까.

제삼자의 시선에서 장단점을 파악할 수도 있을 것이다.

그래, 그게 낫겠다.

“너도 그렇게 생각하지?”

어느새 다시 나타난 혁무진의 허상이 씩 웃으며 고개를 끄덕였다.

“그래, 다시 한번 붙어 보자.”

창을 비스듬히 치켜들고 왼발을 한 발 내딛는다. 허상이 거울처럼 같은 자세를 취했다.

- 후회할걸.

“후회 같은 소리 하고 자빠졌네.”

이제는 허상이랑 대화도 하는구나. 누가 보면 빼도 박도 못하고 미친놈 소리 듣겠다.

- 미친놈.

……내 상상이지만 열받네.

“넌 죽었어.”

나는 망설임 없이 녀석을 향해 창을 겨누었다.

똑같은 무기, 똑같은 무공. 재미있는 싸움이 될 것 같았다.

- 재미? 정말 미친놈이구나. 너.

아, 그러게.

이 상황에서 재미를 느끼다니. 나도 어지간히 미친놈이다.
```

### Current accepted English

```markdown
# Chapter 12

Was it about ten years ago? Back when I was in high school, several dozen ordinary people entered a Gate with government approval.

*China, I think.*

Gates were places where even Hunters became corpses if they let their attention wander, and they were sending ordinary people inside? It really was the Miracle Continent.

On the day of the expedition ceremony when this insane stunt took place, their identities were revealed during an interview with the overseas press.

The Chinese Martial Arts Alliance.

In other words, they were modern-day Murim martial artists. Made up entirely of non-awakened people, they solemnly declared their intentions toward hundreds of cameras, their robes fluttering in the wind.

*Today, the thousand-year martial lineage of China will be reborn in all its glory.*

It certainly was glorious. Their faces had been plastered across the front pages of all kinds of news outlets in less than half a day.

> **Chinese Martial Arts Alliance: Twenty-Five Members Massacred in an F-Rank Gate. More Than Half Confirmed Dead from Goblin Poison Needles…**

I didn’t know how impressive a thousand-year martial lineage was supposed to be, but the incident brought immense disgrace upon China, and the Chinese Martial Arts Alliance was left with nothing but its signboard.

*It got completely wrecked.*

Some of the most renowned martial artists on the continent were killed by goblin poison needles, and a tai chi master was beaten senseless by a mixed martial arts fighter.

That was reality. I had thought the scenes from novels and movies were fiction dressed up in media spectacle and mystery.

*But…*

Now, I wasn’t so sure. The movements Hyuk Mujin had shown me were *real*.

As I learned martial arts myself, my doubts gradually turned into certainty. There was nothing weak or floppy about the martial arts here, unlike in reality.

The martial arts of this world were systematic and involved countless movements. They couldn’t even be compared with real-world martial arts or boxing.

*How is this possible? Is it simply because this is a game?*

Ssshh. Hooouu.

As I breathed, I sensed the energy outside my body and drew it in.

Compared to the ten years of internal energy rotating through my acupoints, it was nothing but a speck of dust—small and weak. But I was in no position to complain about even that.

*One circuit. Two…*

I continued circulating my qi according to the formula of the Jin Family’s Cultivation Technique. It was a natural action, as if I had been practicing it since childhood.

*Gyeonjeong, Amun, Bongan, Ip-dong…*

Names of acupoints I had never heard or seen in my twenty-seven years surfaced and vanished in my mind. Hundreds of acupoints had been engraved into my memory like that. Just how far did the System’s functions go?

*Now that I think about it, it’s downright bizarre.*

The human brain wasn’t a computer. But the System had entered the information into my mind as if it had copied and pasted a file. The other martial arts were the same.

Was a phenomenon like this possible? Simply because this was a game?

*No. For now, focus on circulating qi.*

I steadied my breathing again and guided my internal energy. Only after circulating the ten years of internal energy through twelve complete circuits according to the formula of the Jin Family’s Cultivation Technique did I open my eyes.

Ding.

> **System**
>
> - You have completed **Circulating Qi**.
>
> - **Jin Family’s Cultivation Technique** Mastery has increased slightly.
>
> - A small amount of turbid qi has been expelled.

“Whew.”

The Third Stage of the Jin Family’s Cultivation Technique was within reach. I didn’t know whether it was because I had started from the very bottom, but it felt like a fairly fast pace.

*Or it could be thanks to the Item.*

I looked at the ring on my right middle finger.

It was the Item I had received as a Reward for completing the **Unity of Self and Object** achievement.

> **System**
>
> **Item Window**
>
> **Clear-Heart Pill**
>
> **Type:** Ring
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** A very hard ring made of a material that cannot be identified. It calms the wearer’s mind and helps with concentration.

The Clear-Heart Pill. Its form was different from the one I knew, but its effects were similar. After I put it on, the time it took me to settle into circulating qi had definitely shortened, and the Mastery I gained had increased.

*It’s good, but…*

I still felt uneasy. I could chalk Logout up to the technical territory of engineering nerds beyond my understanding. But the martial arts formulas and this ring, the Clear-Heart Pill, were unsettling in a way I couldn’t quite explain.

*Was I supposed to call it the feeling of something being forcibly injected into me?*

Even if it helped me survive, it clearly wasn’t a pleasant experience. This game was a piece of shit in so many ways.

“What the hell was this Seong Jinho guy doing? That so-called goshiwon manager.[^1]”

If he’d gotten up, he should have woken me so we could at least have a bowl of hangover soup. And yet, the fact that nothing had changed even now meant…

*No. That’s not it.*

At the very least, I was still alive in the real world. That was why I could still exist in this game as a player.

I was alive in reality and in the game. And I would get out alive, no matter what. My life was too precious, and my burdens were too heavy, to die a pointless death like this.

*I can’t die here.*

I clenched my teeth and sat cross-legged. Perhaps it was the effect of the Clear-Heart Pill. My mind gradually settled, and my breathing steadied.

As the internal energy in my dantian began to move, I started yet another session of circulating qi.

* * *

It was the second day since I entered the training hall.

I devoted myself to training without stopping. I trained in the Spear Technique and Manoeuvre Technique like a madman, and whenever my internal energy was completely depleted, I immediately began circulating qi.

Ding.

> **System**
>
> - The realm of **Jin Family’s Cultivation Technique** has risen to the Third Stage.
>
> - Your internal energy has become purer, allowing for more efficient circulation of qi.

The Third Stage of the Jin Family’s Cultivation Technique. It had progressed more slowly than the other two, but it wasn’t bad. No, I was trying to think of it that way.

*I had to think of it that way if I was going to hold on.*

At least martial arts training allowed me to shake off my dark thoughts. For that, I was grateful.

Swish. Ssshk.

I performed the forms of the Jin Family’s Spear Technique in order. Ever since realizing its connection with the Jin Family’s Manoeuvre Technique, my attacks had grown more precise and sharper, sweeping through the empty space ahead of me.

I was projecting someone into that empty space.

*Hyuk Mujin.*

The first genuine martial artist I had met in this game. A Level 20 powerhouse who had toyed with me like a child.

*Could I beat that bastard in my current condition?*

That was the moment the question crossed my mind.

Ding.

> **System**
>
> - A new function, **Training Mode**, has been activated.
>
> - You can summon illusions of opponents you have fought so far. However, opponents whose Level differs from the user’s by ten or more cannot be summoned.
>
> - Currently summonable opponents: **Lv. 20 Hyuk Mujin**, **Lv. 10 Heavenly Axe**

“Huh?”

Training Mode? I could summon illusions of opponents I had fought so far? After a moment’s hesitation, I decided to test the new function.

“Summon Hyuk Mujin.”

> **System**
>
> - Summoning **Lv. 20 Hyuk Mujin**.

The moment the System notification appeared, a transparent figure abruptly sprang into existence. He wore the navy martial uniform of the Jin Family of Taiyuan and had Hyuk Mujin’s distinctive caterpillar eyebrows. The figure stood with his eyes closed, looking exactly like Hyuk Mujin.

“Holy shit, it’s real.”

I carefully approached and touched Hyuk Mujin’s body. But perhaps because it was an illusion, my hand passed straight through him.

*Good. That passes the safety test.*

> **System**
>
> - You can partially alter the summoned target’s abilities.

“For now, make him about half as strong as Hyuk Mujin.”

> **System**
>
> - Entering the data for **Lv. 20 Hyuk Mujin**. The illusion can use 50% of the original’s abilities.

At the same time, Hyuk Mujin’s illusion opened his eyes. Perhaps his personality had been copied along with his abilities, because he looked at me with the same insolent gaze.

> **System**
>
> - Would you like to begin training?

“Of course!”

Ding.

The System notification was the starting signal. I charged forward like lightning and thrust my spear. Even though I was fighting an illusion, I poured out my internal energy without holding anything back.

*First form.*

It began with a thrust as I advanced, followed by a twist of the spear shaft. If the enemy couldn’t evade the first attack, the fight was already over.

Ssshwip—

But Hyuk Mujin slipped away with the movement of a loach. That made the next movement pointless.

*Let’s see if you can dodge this, too.*

I continued unleashing the Spear Technique. The sound of wind splitting filled the air, but Hyuk Mujin dodged every attack.

For an instant, it seemed a sneer crossed his opaque face.

*How can you fight so stupidly? A martial artist ought to use martial arts.*

Those were the words he had used when he toyed with me last time. He was nothing more than an illusion I had created, but…

*God, that’s pissing me off.*

*If you’re so confident, stop dodging and come at me.*

Hyuk Mujin picked up on my thought and rushed at me in a smooth glide. But this was a fight between a spear and a fist. If I let him land that attack, it would mean I had spent the last seven years digging holes for nothing.

“Where do you think you’re going!”

Whoom—

I swung the spear shaft. If the illusion had been real, it would have made a solid *thwack*. Even if he had dodged it, he would have failed to close the distance.

*Let’s see how far you can dodge.*

I launched into the form. Faced with the torrent of attacks, Hyuk Mujin didn’t even dare to approach. He retreated step after step.

Combat had a flow. I had caught that flow, and Hyuk Mujin had been swept along by it. Looking at Hyuk Mujin rolling across the ground with an exhausted expression, I thought,

*He’s weak.*

I could see his movements. The Hyuk Mujin projected here was a fist fighter. I could tell how he would move by watching his feet, and I could predict his next action. His fists couldn’t reach me.

Ssshk-swish-swish!

In a single instant, I thrust three times in succession. It was an attack F-rank Hunter Jin Taekyung couldn’t perform. But Jin Taekyung the Murim martial artist, drawing on internal energy, could.

“Kraaagh!”

Hyuk Mujin seemed to scream as the spear pierced his chest.

Without hesitation, I shoved the spear deeper and twisted it. The spearhead crushed through his breastbone and split his heart. The fallen Hyuk Mujin slowly faded away.

“Ah. This is way too easy.”

The fight had already been decided in less than five seconds.

I had even held the upper hand throughout the entire battle, only for it to end anticlimactically.

*Was half just too weak?*

I fell into thought while recovering the internal energy I had depleted by circulating qi.

Hyuk Mujin was Level 20 and a martial artist who had trained in martial arts for at least several years. There was no way he could be this weak.

*All right. Again.*

I stood up with the spear in my hand and closed my eyes, imagining a new Hyuk Mujin.

A height of 180 centimeters. Lean muscles and insolent eyes. I infused him with the movements I had seen back then. When I opened my eyes, an illusion exactly as I had imagined stood before me.

But it still wasn’t over. Hyuk Mujin had to be stronger.

*Your physical abilities are superior to mine.*

After I fed in a few more conditions, Hyuk Mujin’s illusion smiled pleasantly. He had become much faster and gained stamina that would never run out.

“Yeah. Now this is worth fighting.”

Those words were the starting signal. I thrust my spear at Hyuk Mujin as he charged toward me like a ray of light.

Ssshk-swish!

* * *

Vroooom. Boom!

The spearhead tore through the air. The air burst with the sound of a swarm of bees, bringing a gust of wind with it. It was the final form of the Jin Family’s Spear Technique: Sky-Piercing Strike.

“Kheugh…”

Hyuk Mujin’s illusion looked down at his gaping chest. His eyes held pure disbelief. Then his knees buckled, and the illusion scattered.

“This isn’t right.”

I scratched my head roughly as I heard the message that my Mastery of the Jin Family’s Spear Technique had increased.

*Why am I still winning?*

Had the System made a mistake, or…

*Did I simply become stronger?*

I brushed the thought away as soon as it came to me. That couldn’t be it. I wasn’t some peerless genius. I had only learned a couple of martial arts.

*At this rate, this isn’t very useful.*

This was supposed to be a simulation for testing what happened when I fought a powerful opponent. If I kept winning, what was the point?

If I at least knew which martial arts Hyuk Mujin had learned, I could draw out their power. But wait.

“There’s an easier way.”

The Jin Family’s Manoeuvre Technique and Spear Technique. What if I grafted those two onto the Level 20 Hyuk Mujin?

I might even be able to identify their strengths and weaknesses from a third-party perspective.

Yeah. That would be better.

“You think so too, right?”

Hyuk Mujin’s illusion had reappeared at some point. It grinned and nodded.

“Then let’s fight again.”

I raised the spear diagonally and took one step forward with my left foot. The illusion assumed the same stance as if it were looking in a mirror.

“You’ll regret this.”

“Regret, my ass.”

I was even talking to an illusion now. Anyone who saw me would have no choice but to call me a certifiable lunatic.

“Crazy bastard.”

…It was my imagination, but it still pissed me off.

“You’re dead.”

Without hesitation, I pointed the spear at him.

Same weapon. Same martial arts. It looked like it would be an interesting fight.

“Interesting? You really are a lunatic.”

Yeah. I suppose so.

Finding this fun in a situation like this meant I was pretty damn crazy, too.

[^1]: A goshiwon is cheap boarding made up of tiny private rooms, often rented by exam students.
```
## Chapter 13

### Korean source

```text
＃13화



다섯 마리의 말은 힘차게 달렸다. 산과 들, 강을 지나 마침내 목적지에 도착했을 때는 정오 무렵이었다.

“어디에서 오셨습니까?”

태원진가 수문위사의 긴장 섞인 물음에 선두의 청년이 웃었다. 비뚜름하게 올라간 입술에는 감출 수 없는 적의가 배어 있었다.

“항산(恒山).”

진위경이 가문 중진들을 소집한 것은 일 다경 후였다.



* * *



혁무진은 변화무쌍했다. 나는 그저 머릿속에 녀석의 모습을 그려 넣으면 되었다. 창, 검, 도, 활……. 이길 때도, 질 때도 있었지만 한 가지는 확실했다.

“이제 감 잡았다.”

무공이 몸에 익었다. 처음에는 처음부터 끝까지 차례차례 풀어내는 것에 집중했지만 이제는 다르다.

상황에 따라 초식도 변한다. 꼭 초식 하나하나가 순서대로 이어져야만 무공인 건 아니다. 지금의 나는 초식의 순서를 뛰어넘어 무공을 연계할 수 있을 정도의 수준이 됐다.

‘지금처럼 말이지.’

쐐애애액!

바람 소리가 들렸을 때는 이미 늦었다. 복부를 꿰뚫린 혁무진이 탄식했다.

- 실력이 빨리도 느는군.

“창질만 7년을 했다. 이 새끼야.”

눈을 감았다 뜨니 텅 빈 수련동이 보인다. 내 승리를 축하하듯 시스템 알림이 울렸다.

띠링.



- [진가창법]이 사 성으로 올랐습니다!

- [진가보법]이 사 성으로 올랐습니다!

- 초식이 정교해지고 파괴력이 상승합니다.

- 레벨 업!



“이제 14레벨인가?”

사흘 만에 3레벨을 올렸다.

수련동에서 사흘을 짱박혀 있던 것치고는 가파른 상승세다.

거기에 진가심법은 삼 성, 보법과 창법은 사 성에 도달했다.

“상태창 오픈.”

잔여 포인트를 분배하고 나자 어쩐지 코끝이 찡하다.



상태창



[Lv.14 진태경]

직업 : 이류 무인

명성 : 10

칭호 : 3개 (칭호 효과 적용 중)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 –5, 명성 –50)

- 초보 수련자 (수련 속도 +10%)

근력 : 51체력 : 61

민첩 : 61 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 0





“아름답다. 아름다워.”

이 균형 잡힌 능력치를 보라.

이게 바로 전투의, 전투에 의한, 전투를 위한 능력치다.

‘거기에 무공까지.’

그때의 내가 아니다. 혁무진? 붙어도 이길 자신 있다.

무공의 무자도 모르는 F급 헌터는 죽었다. 지금의 나는 절정 심법에 일류 무공을 두 개나 익힌 무림인이다.

‘오늘부터 시작이야.’

모든 준비는 끝났다. 오늘, 수련동에서 나가게 되면 생각해 둔 물건들을 챙겨 태원진가를 빠져나갈 것이다.

‘진위경의 도움을 받을 수도 있겠지.’

천력부 같은 얼뜨기 산적들만 처리해도 빠른 속도로 목표치에 도달할 수 있을 것이다. 길어 봤자 이틀. 그 후에는 따뜻한 가족의 품으로 돌아갈 수 있다.

‘엄마, 하연아. 보고 싶다.’

눈시울이 붉어지려던 그때였다.

그그긍-

“오, 오오오!”

기다리던 순간이다. 수련동 입구를 막은 철문이 열리고 있었다. 그 거무튀튀하고 무거운 쇳덩어리가, 천국의 문처럼 아름답게 보였다.

“드디어! 나간다!”

나는 환희에 찬 얼굴로 천국 입구를 향해 달려 나갔다.

날 이곳에서 꺼내 줄 천사가 문 뒤에서 모습을 드러냈다.

“삼공자. 사흘 만이군요.”

반가운 얼굴은 아니지만 지금은 마냥 기쁘다.

“저 꺼내 주시려고 오신 거죠? 예? 맞죠?”

사막여우를 닮은 천사, 위팽이 미묘한 말투로 대답했다.

“예. 일단은요.”

“……?”

“나가긴 할 겁니다. 하지만 바로 들러야 할 곳이 있습니다.”

“들러야 할 곳?”

순간 등줄기가 오싹하다. 왠지 모를 생존 본능이 고개를 쳐들었다.

“어딜 가는데요?”

“대회의장입니다. 소가주님께서도 그곳에서 기다리고 계십니다. 그리고…….”

위팽이 덧붙였다.

“본가의 중진들과 항산검문의 사자(使者)도 와 있지요.”

“항산검문이요? 걔네가 여길 왜 와요?”

홍화루에서 월화가 그랬었다. 태원진가와 항산검문은 숙적관계라고. 그런데 그놈들이 왜 여기 있어?

‘일이 잘못 돌아가고 있다.’

불길하다. 불길해. 어떻게든 방법을 찾아야 한다.

“저 그럼 잠깐 처소에서 옷만 갈아입고 가면 안 될까요?”

“안 됩니다.”

“중요한 자리인 것 같은데 냄새나면 안 되니까…….”

“도망칠 생각이십니까?”

생긴 건 사막여운데 눈치는 미어캣 저리 가라다. 내가 뭐라 할 새도 없이 위팽의 손이 어깨를 짓눌렀다.

“삼공자. 지금부터 제가 묻는 말에 사실대로 대답해 주십시오. 아시겠습니까?”

목소리는 건조하고 눈동자는 서늘하다. 그에게서 느껴지는 기세에 입을 뗄 수 없었다. 내가 할 수 있는 것이라곤 고개를 끄덕이는 것뿐이었다.

‘진태경.’

순간 머릿속에 떠오른 세 글자.

확실했다. 분명히 이 새끼다. 나도 모르는 똥을 싸질러 놓은 거다.

그리고…….

“항산검문의 여식을 범하려 한 것이 사실입니까?”

그 똥은 상상 이상으로 거대했다.



* * *



위팽을 따라 대회의장으로 향하는 길, 머릿속이 온통 백지장이었다.

‘성폭행 미수?’

미수에 그쳤다고는 하나, 때려죽여도 시원찮을 성범죄다.

한 사람의 인간으로서, 여동생을 둔 오빠로서 성범죄자는 사형시켜야 한다고 입버릇처럼 말하던 기억이 떠올랐다.

‘이런 미친 새끼.’

손바닥이 식은땀으로 축축하다. 나는 몇 번째인지 모를 말을 내뱉었다.

“저 진짜 아닙니다. 믿어 주세요.”

위팽은 뒤도 돌아보지 않고 대답했다.

“기억이 돌아오셨습니까?”

“아니, 그게 아니고요. 저 진짜 아니라니까요. 제가 그럴 놈으로 보이세요? 그런 쓰레기 짓을 하고 다닐 정도로?”

“예.”

아니, 시발.

숨도 안 쉬고 대답하네.

“저기요. 그럼 저 화장실, 아니 변소 좀 들렀다 갈게요.”

“안 됩니다.”

“아니, 볼일은 보게 해 줘야지!”

“그냥 싸십시오.”

이런 개새끼. 나는 포기하고 곧장 뒤돌아 뛰기 시작했다. 모든 공력을 끌어올려 발에 집중시켰고.

덥석.

“삼공자.”

세 걸음 만에 붙잡혔다. 내 목덜미를 움켜쥔 위팽이 서늘한 눈동자로 나를 내려다봤다.

“계속 이러시면…… 제가 무례해질지도 모릅니다.”

저항은 무의미하다. 위팽은 [기감]으로도 레벨을 파악할 수 없는 고수다.

‘어쩔 수 없다.’

참담한 마음으로 얼마나 걸었을까, 우뚝 선 전각이 눈에 들어왔다.

앞에는 무사 여럿이 경계를 서는 중이었는데, 태원진가 특유의 남색 복장은 눈에 익었지만 몇 명은 처음 보는 붉은 색 옷을 걸치고 있었다.

‘저놈들이 항산검문이구나.’

양 문파의 평소 관계를 생각해 보면 견원지간일 텐데, 지금은 한마음 한뜻으로 나를 노려보는 중이다.

“시발…….”

내 중얼거림을 들은 위팽이 고개를 돌렸다.

“소가주께서는 삼공자를 믿고 계십니다. 그 사실을 잊지 마십시오.”

그래. 진위경이 있다. 내 가장 큰 희망이자 방패.

그 사실을 되새길 때, 위팽이 대회의장의 문을 열어젖혔다.

“삼공자를 데려왔습니다.”

크게 심호흡한 나는 전각으로 발을 디뎠다. 속으로는 끊임없이 되뇌는 중이었다.

‘호랑이한테 물려 가도 정신만 차리면 산다. 호랑이한테 물려 가도 정신만 차리면…….’

내가 회의장 안으로 들어서자 낮게 웅성거리던 목소리가 뚝, 끊겼다. 젊고 늙은 남자 십여 명이 좌우로 도열해 있고 상석에는 진위경이 자리했다.

그리고 중앙의 한 청년.

“오랜만이오. 진 공자.”

그 꺼림칙한 미소와 마주한 순간이었다.

띠링.



- [살기]를 감지했습니다!



……깜빡이 좀 켜고 들어와라.



* * *



살기.

익숙하다. 몬스터들은 말 그대로 악의와 살기로 똘똘 뭉친 녀석들이니까. 수도 없이 느껴 왔고, 이제는 익숙하다고 생각했다. 그런데 이놈은…….

‘달라.’

내가 겪어 온 그것과는 차원이 다르다.

굳이 비교하자면 하급 몬스터와 중급 몬스터의 차이라고 하겠다. 훨씬 다듬어져 있고, 은밀하며 소름 끼친다.

“지난번 저잣거리에서 스치듯이 본 적이 있었는데. 기억할지 모르겠소.”

한 마디, 한 마디. 씹어뱉는 이소군의 머리 위로 시스템창이 둥둥 떠다닌다.



[Lv.30 이소군]



앞서 살기를 감지하자마자 [기감]으로 읽어 낸 녀석의 레벨이었다. 내 레벨의 두 배가 넘어간다.

‘미치겠네.’

더 서글픈 것은 다른 사람들의 눈초리다.

젊은 사람, 늙은 사람 가릴 것 없이 흉험한 눈빛 수십 개가 나를 노려보는 광경에 오금이 저려 온다. 그런 분위기 속에서 이소군이 입을 열었다.

“아쉽구려. 조금만 일찍 왔다면 더 깊은 대화를 나눠 볼 수 있었을 터인데. 방금까지 흥미로운 이야기를 하고 있던 참이어서 말이오.”

“……그래요?”

“무슨 이야기인지 궁금하지 않소?”

“괘, 괜찮습니다.”

목을 자를까, 불알을 자를까에 관한 토론이 아니길 바랄 뿐이다. 그리고 만약 이 불행한 짐작이 사실이라면, 목 대신 불알이 잘렸으면 했다.

‘잘만 하면 레벨 업으로 회복할 수 있…… 내가 이런 것까지 생각해야 하나.’

참담할 뿐이다. 그런 내 표정을 지그시 바라보던 이소군이 말했다.

“며칠 전 가문에 돌아왔다 들었소만. 어디 있었소?”

“홍화루요.”

“그럼 홍화루에 가기 전에는 어디 있었소?”

‘고시원에 있었다. 임마.’

나도 솔직하게 다 털어놓고 싶다. 그날 저는 길드에서 잘리고, 고시원 형이랑 소주 한잔 걸친 다음에 캡슐에 들어가서 잤습니다. 눈 떠 보니까 홍화루였고, 로그아웃을 목표로 열심히 하고 있습니다. 뭐, 이렇게.

‘칼이나 안 뽑으면 다행이지.’

대답을 못 하고 머뭇거릴 때 이소군이 품에서 뭔가를 꺼내 들었다. 정말 칼이라도 뽑나 싶었는데, 웬 종이 뭉치다.

“기억을 못 하는 것 같으니 내 알려 주겠소. 홍화루에 가기 전날 밤, 공자는 명월루에 들렀소. 예약해 두었던 특급 객실로 향했지.”

“명월루요?”

“한때 뻔질나게 드나들던 기루 아니오? 처음 들어 봤다고 변명하진 마시오. 그날 명월루에서 당신을 목격한 사람들의 증언과 수결이 여기 있으니.”

말하자면 증언 목록인 셈이다. 나는 어디 한번 읽어나 보자 하는 심정으로 종이를 읽어 내렸다.

그리고 이상한 점을 발견했다.

“뭐야, 이거?”

“직접 보고도 모르겠나?”

이 자식이 은근슬쩍 말 놓네.

“보니까 하는 소리지. 제대로 된 증언이 없잖아요.”

수십 명의 증언을 빠짐없이 읽어 봤지만 결정적인 증언은 어디에도 없었다.

하는 말도 비슷비슷하다. 진태경이 거나하게 취해서 방을 잘못 찾았고, 그 방의 주인이 항산검문의 여식이었다는 것. 그리고 비명을 지르는 소리가 났다는 것.

“내 누이의 옷을 찢고 범하려 한 놈이 뻔뻔하기 그지없구나. 과연 소문 그대로야.”

“아니, 그게 아니고…….”

“이놈!”

촤르륵!

“아.”

얼굴을 때린 종이 뭉치가 바닥에 흩어졌다. 이소군이 그 위로 가래를 탁 뱉었다.

‘이 새끼 봐라.’

짜증이 아니다. 그저 의심이 들 뿐이다.

뭐라 할까, 이런 일련의 상황들. 특히 증언에 관련해서 굉장히 작위적인 느낌이 든다고나 할까?

하지만 더 이상 찝찝함을 느낄 새도 없었다.

“따라 나와라, 네놈이 저지른 짓의 대가를 치르게 해 주마!”

이소군이 고함을 내지른 그 순간이었다.

띠링.



- [비무] 퀘스트가 생성되었습니다.



이건 또 뭐야.
```

### Current accepted English

```markdown
# Chapter 13

The five horses ran hard. They passed mountains, fields, and rivers, finally reaching their destination around noon.

“Where are you coming from?”

When the Jin Family of Taiyuan’s gate guard asked the tense question, the young man in the lead smiled. Hostility he could not hide seeped from his crooked, lifted lips.

“Mount Heng.”

Jin Wikyung summoned the family’s senior members fifteen minutes later.

* * *

Hyuk Mujin could take on any form. All I had to do was picture him in my mind. Spear, sword, saber, bow… There were times I won and times I lost, but one thing was certain.

“I’ve got the hang of it now.”

The martial arts had become second nature. At first, I had focused on executing them from beginning to end, one form after another. But things were different now.

The forms changed depending on the situation. Martial arts didn’t have to consist of one form flowing into the next in a fixed order. I had reached the point where I could skip the prescribed sequence and link forms together.

*Like this.*

Whoooosh!

By the time I heard the wind, it was already too late. Hyuk Mujin, his abdomen pierced through, let out a rueful sigh.

- You’re improving quickly.

“I trained with a spear for seven years, you bastard.”

When I opened my eyes again, the empty training hall came into view. As if celebrating my victory, the System notification rang out.

Ding.

> **System**
>
> - **Jin Family’s Spear Technique** has risen to the Fourth Stage!
>
> - **Jin Family’s Manoeuvre Technique** has risen to the Fourth Stage!
>
> - The forms have become more refined, and destructive power has increased.
>
> - Level up!

“So I’m Level 14 now?”

I had gained three Levels in three days.

That was a steep rise for someone who had holed up in the training hall for three days.

On top of that, the Jin Family’s Cultivation Technique had reached the Third Stage, while the Manoeuvre Technique and Spear Technique had reached the Fourth Stage.

“Open Status Window.”

After distributing my remaining points, I felt a sting at the tip of my nose for some reason.

> **System**
>
> **Status Window**
>
> **Lv. 14 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
>
> **Fame:** 10
>
> **Titles:** 3 (Title effects active)
>
> - **Child of a Prestigious Family:** All stats +5, Fame +50
>
> - **Shame of the Family:** All stats –5, Fame –50
>
> - **Novice Trainee:** Training speed +10%
>
> **Strength:** 51  
> **Stamina:** 61
>
> **Agility:** 61  
> **Intelligence:** 10
>
> **Charm:** 10  
> **Internal Energy:** 10 years
>
> **Remaining Points:** 0

“Beautiful. Just beautiful.”

Look at those perfectly balanced stats.

These were stats *of* combat, *by* combat, and *for* combat.

*And that’s not even counting the martial arts.*

I wasn’t the same person I had been back then. Hyuk Mujin? I was confident I could beat him now.

The F-rank Hunter Jin Taekyung, who didn’t know the first thing about martial arts, was dead. I was now a Murim martial artist who had learned a Peak cultivation technique and two first-rate martial arts.

*It starts today.*

Everything was ready. Once I left the training hall today, I would gather the things I had in mind and leave the Jin Family of Taiyuan.

*I might even be able to get Jin Wikyung’s help.*

I could reach my target quickly just by dealing with idiot bandits like the Heavenly Axe. Two days at most. After that, I could return to my warm family.

*Mom. Hayeon. I miss you.*

That was when the rims of my eyes started to go red.

Grrrrrr—

“O-oh! Ohhh!”

This was the moment I had been waiting for. The iron door blocking the entrance to the training hall was opening. That ugly, heavy chunk of metal looked as beautiful as the gates of heaven.

“Finally! I’m getting out!”

I ran toward the entrance to heaven with a face full of joy.

The angel who would free me from this place appeared behind the door.

“Third Young Master. It’s been three days.”

He wasn’t exactly a welcome sight, but I was too happy to care.

“You came to let me out, right? Huh? You did, right?”

Wipeng, an angel who resembled a desert fox, answered in a strangely qualified tone.

“Yes. For now.”

“…What?”

“You will be leaving. But there’s somewhere we need to stop by first.”

“Somewhere we need to stop by?”

A chill ran down my spine. Some kind of survival instinct raised its head.

“Where are we going?”

“The main assembly hall. The Lesser Family Head is waiting there as well. And…”

Wipeng added,

“Senior members of our family and an envoy from the Mount Heng Sword Sect have also arrived.”

“The Mount Heng Sword Sect? Why the hell are they here?”

Wolhwa had told me at Honghwaru. The Jin Family of Taiyuan and the Mount Heng Sword Sect were sworn enemies. So why were those bastards here?

*Things are going wrong.*

This was ominous. Very ominous. I had to find some kind of way out of this.

“Then could I stop by my residence and change clothes first?”

“No.”

“It seems like an important occasion, and I can’t show up smelling like this…”

“Are you thinking of running away?”

He looked like a desert fox, but his instincts put a meerkat to shame. Before I could say anything, Wipeng’s hand pressed down hard on my shoulder.

“Third Young Master. From now on, answer my questions truthfully. Understood?”

His voice was dry, and his eyes were cold. The aura coming from him made it impossible for me to open my mouth. All I could do was nod.

*Jin Taekyung.*

The three-syllable name flashed through my mind.

There was no doubt about it. This bastard was responsible. He had dumped a load of shit without me even knowing.

And then…

“Is it true that you tried to rape the daughter of the Mount Heng Sword Sect?”

That shit was far bigger than I could have imagined.

* * *

On the way to the main assembly hall behind Wipeng, my mind was completely blank.

*Attempted rape?*

Even if it had ended at an attempt, it was a sex crime so vile that beating the culprit to death wouldn’t have been enough.

I remembered how I had always said that, as a human being and an older brother with a younger sister, sex offenders should be executed.

*What kind of fucking lunatic was he?*

My palms were damp with cold sweat. I said it again, not knowing how many times I had repeated it already.

“I really wasn’t the one. Please believe me.”

Without turning around, Wipeng replied,

“Has your memory returned?”

“No, that’s not what I mean. I’m telling you, it really wasn’t me. Do I look like the kind of guy who’d do that? The kind of guy who’d go around committing trash like that?”

“Yes.”

No, fuck.

He answered without even taking a breath.

“Look, then let me stop by the bathroom. Or the privy, I mean.”

“No.”

“You have to let me take care of business!”

“Just go here.”

Son of a bitch. I gave up and immediately turned around and ran, drawing up all my internal energy and concentrating it in my feet.

Grab.

“Third Young Master.”

I was caught in three steps. Wipeng had me by the back of the neck, looking down at me with cold eyes.

“If you keep this up… I might have to stop being polite.”

Resistance was pointless. Wipeng was a master whose Level I couldn’t determine even with Qi Sense.

*No choice.*

With a sinking heart, I walked for who knew how long before a tall pavilion came into view.

Several warriors were standing guard outside. I recognized the Jin Family of Taiyuan’s distinctive navy uniforms, but some of the men wore red clothes I had never seen before.

*Those must be members of the Mount Heng Sword Sect.*

Considering the usual relationship between the two sects, they should have been sworn enemies. Yet right now, they were united in glaring at me.

“Fuck…”

Wipeng turned his head at my mutter.

“The Lesser Family Head believes in you. Don’t forget that.”

Right. Jin Wikyung was there. My greatest hope and my shield.

As I reminded myself of that fact, Wipeng threw open the doors to the main assembly hall.

“I’ve brought the Third Young Master.”

I took a deep breath and stepped into the pavilion. Inside my head, I kept repeating the same words.

*Even if a tiger carries you off, you can survive if you keep your wits about you. Even if a tiger carries you off, you can keep your wits—*

The moment I entered the hall, the low murmuring abruptly stopped. A dozen men, young and old, stood arrayed along either side, while Jin Wikyung occupied the seat of honor.

And in the center stood a young man.

“It’s been a while, Young Master Jin.”

The instant I met that unpleasant smile—

Ding.

> **System**
>
> - **Killing intent** detected!

…At least use your blinker before pulling in.

* * *

Killing intent.

I knew it well. Monsters were literally bundles of malice and killing intent. I had felt it countless times and thought I had grown used to it.

But this guy…

*He was different.*

This was on an entirely different level from anything I had experienced.

If I had to compare it to something, it was like the difference between a low-level monster and a mid-level monster. His killing intent was far more refined, more furtive, and more chilling.

“I believe I caught a glimpse of you in the marketplace last time. I don’t know whether you’ll remember me.”

Each word was spat out by Lee Seogeun. Above his head, a System window floated in the air.

> **System**
>
> **Lv. 30 Lee Seogeun**

That was the Level I had seen with Qi Sense the instant I detected his killing intent. It was more than twice my Level.

*This is insane.*

Even worse were the looks from everyone else.

Dozens of sinister gazes, young and old alike, were fixed on me. My knees began to tremble. In that atmosphere, Lee Seogeun opened his mouth.

“What a shame. If you had come a little earlier, we could have had a deeper conversation. We were discussing something interesting until just now.”

“…Were you?”

“Wouldn’t you like to know what we were discussing?”

“N-no, I’m fine.”

I only hoped it wasn’t a discussion about whether to cut off my head or my balls. And if that miserable guess was correct, I preferred them to cut off my balls instead of my head.

*I might be able to recover with a Level Up if they did that… Why am I even thinking about this?*

It was simply miserable. Lee Seogeun studied my expression before speaking again.

“I heard you returned to the family a few days ago. Where have you been?”

“Honghwaru.”

“Then where were you before you went to Honghwaru?”

*I was at a goshiwon, you bastard.*

I wanted to tell him everything honestly.

*I got fired from my Guild that day, had a glass of soju with the hyung from the goshiwon, then went into the capsule and fell asleep. When I woke up, I was at Honghwaru, and now I’m working hard toward Logout. Something like that.*

*It’d be a miracle if he didn’t draw his sword.*

As I hesitated, unable to answer, Lee Seogeun pulled something from inside his robes. I thought he really was drawing a sword, but it turned out to be a bundle of papers.

“Since you don’t seem to remember, I’ll tell you. The night before you went to Honghwaru, you visited Myeongwollu. You went to the top-tier room you had reserved.”

“Myeongwollu?”

“The pleasure house you used to visit all the time? Don’t try to make excuses by saying you’ve never heard of it. These are the testimonies and seals of the people who saw you there that day.”

In other words, it was a list of witness statements. I read through the papers, thinking I might as well take a look.

Then I noticed something strange.

“What is this?”

“You don’t know even after seeing it yourself?”

This bastard was dropping the formal speech now, too.

“I’m saying that because I read it. There isn’t a single proper testimony here.”

I read every one of the dozens of statements, but there wasn’t a decisive testimony anywhere.

They all said roughly the same thing: Jin Taekyung had gotten thoroughly drunk, gone to the wrong room, and found that the room belonged to the daughter of the Mount Heng Sword Sect. Then someone had heard screaming.

“The bastard who tore my sister’s clothes and tried to rape her is shameless beyond belief. You really are exactly as the rumors say.”

“No, that’s not what—”

“You bastard!”

Flutter!

“Ah.”

The bundle of papers smacked me in the face and scattered across the floor. Lee Seogeun spat a wad of phlegm onto them.

*Well, look at this asshole.*

It wasn’t irritation. I was simply suspicious.

How should I put it? This whole chain of events—especially the testimonies—felt incredibly contrived.

But I had no time to dwell on that unease.

“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

The instant Lee Seogeun shouted—

Ding.

> **System**
>
> - The **Duel** Quest has been generated.

What’s this now?
```
